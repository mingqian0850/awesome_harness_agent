#!/usr/bin/env python3
"""fetch_arxiv.py — 每周 arXiv 论文精选（Agent Harness 生态）

用一组主题查询调用 arXiv API，去重、按滚动时间窗口（默认 7 天）过滤、
按关键词相关性打分排序，输出：

  papers/README.md               最新一期精选（覆盖旧内容）
  papers/archive/YYYY-MM-DD.md   本次运行快照（含完整摘要，便于阅读）
  scripts/seen_ids.json          去重状态（自动清理 180 天前的记录）

仅使用 Python 标准库，无需安装依赖，可在 GitHub Actions 中直接运行。

用法:
  python3 scripts/fetch_arxiv.py [--days 7] [--max-results 30] [--min-score 4]
"""

import argparse
import gzip
import json
import os
import re
import shutil
import subprocess
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import date, datetime, timedelta

ARXIV_API = "https://export.arxiv.org/api/query"
NS = {"atom": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAPERS_DIR = os.path.join(ROOT, "papers")
ARCHIVE_DIR = os.path.join(PAPERS_DIR, "archive")
STATE_FILE = os.path.join(ROOT, "scripts", "seen_ids.json")

# 主题查询（arXiv API 语法，abs: 表示在摘要中检索）
CATS = "(cat:cs.AI OR cat:cs.CL OR cat:cs.LG OR cat:cs.SE OR cat:cs.HC OR cat:cs.CR)"
TOPIC_QUERIES = [
    f'{CATS} AND abs:"agent harness"',
    f'{CATS} AND abs:"model context protocol"',
    f'{CATS} AND abs:"tool use" AND (abs:"language model" OR abs:LLM)',
    f'{CATS} AND abs:"tool calling" AND (abs:"language model" OR abs:LLM)',
    f'{CATS} AND abs:"function calling" AND (abs:"language model" OR abs:LLM)',
    f'{CATS} AND abs:ReAct AND (abs:"language model" OR abs:LLM)',
    f'{CATS} AND (abs:"LLM agent" OR abs:"language model agent" OR abs:"LLM-based agent" OR abs:"LLM-powered agent")',
    f'{CATS} AND abs:agentic',
    f'{CATS} AND abs:"multi-agent" AND (abs:"language model" OR abs:LLM)',
    f'{CATS} AND abs:"computer use" AND (abs:agent OR abs:"language model")',
    f'{CATS} AND abs:agent AND abs:benchmark AND (abs:"language model" OR abs:LLM)',
    f'{CATS} AND (abs:"agent evaluation" OR abs:"agent benchmark")',
]

# 合并成单次查询：arXiv 限流严格，1 次请求远好于 12 次（默认模式）
_TERMS = [q.split(" AND ", 1)[1] for q in TOPIC_QUERIES]
COMBINED_QUERY = f"{CATS} AND (" + " OR ".join(f"({t})" for t in _TERMS) + ")"

# 相关性打分关键词：命中标题权重 x2，命中摘要权重 x1
KEYWORDS = {
    "agent": 2, "harness": 3, "tool use": 3, "tool calling": 3,
    "function calling": 2, "mcp": 3, "model context protocol": 3,
    "react": 3, "agentic": 3, "multi-agent": 2, "multiagent": 2,
    "benchmark": 2, "computer use": 3, "web agent": 2, "orchestrat": 2,
    "sandbox": 2, "scaffold": 2, "workflow": 1, "tool learning": 2,
    "llm agent": 3, "language agent": 3, "autonomous": 1, "planning": 1,
}
# 标题命中即收录的强信号词
STRONG_TITLE = ["harness", "react", "mcp", "model context protocol", "tool use",
                "tool calling", "computer use", "agentic", "swarm", "multi-agent"]

MIN_SCORE = 4
# arXiv 要求客户端标识自己（含联系方式），否则容易被限流
USER_AGENT = "awesome-harness-agent-digest/1.0 (+https://github.com/mingqian0850/awesome_harness_agent)"


def _read_body(resp) -> bytes:
    """读取响应体，必要时解压（arXiv/OpenAlex 均支持 gzip，可显著减少传输量）。"""
    raw = resp.read()
    if (resp.headers.get("Content-Encoding") or "").lower() == "gzip":
        try:
            raw = gzip.decompress(raw)
        except OSError:
            pass
    return raw


def _curl_get(url: str, timeout: int):
    """用 curl 取 JSON（对抖动网络更耐受，支持 HTTP/2 与 gzip），返回 works 列表。"""
    if not shutil.which("curl"):
        raise RuntimeError("curl 不可用")
    proc = subprocess.run(
        ["curl", "-sS", "--compressed", "--max-time", str(timeout), "-A", USER_AGENT,
         "-w", "\n%{http_code}", url],
        capture_output=True, timeout=timeout + 20)
    if proc.returncode != 0:
        raise RuntimeError((proc.stderr.decode(errors="replace") or "curl failed")[:200])
    body, _, code = proc.stdout.rpartition(b"\n")
    if (code or b"").strip() != b"200":
        raise RuntimeError(f"HTTP {(code or b'').decode(errors='replace').strip()}")
    return json.loads(body.decode("utf-8")).get("results", [])


def fetch_topic(query: str, max_results: int = 20, retries: int = 3):
    """执行一次 arXiv API 查询。

    成功返回条目列表（可能为空列表），彻底失败返回 None —— 调用方据此区分
    "本期无相关论文" 与 "抓取失败"，避免把失败当成空结果写坏 digest。
    """
    params = urllib.parse.urlencode({
        "search_query": query,
        "start": 0,
        "max_results": max_results,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    })
    url = f"{ARXIV_API}?{params}"
    for attempt in range(retries + 1):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT,
                                                      "Accept-Encoding": "gzip"})
            with urllib.request.urlopen(req, timeout=25) as resp:
                root = ET.fromstring(_read_body(resp))
            entries = []
            for e in root.findall("atom:entry", NS):
                raw_id = e.find("atom:id", NS).text
                base_id = raw_id.rsplit("/abs/", 1)[-1]
                base_id = re.sub(r"v\d+$", "", base_id)
                cat_el = e.find("arxiv:primary_category", NS)
                cats = [c.get("term") for c in e.findall("atom:category", NS)]
                entries.append({
                    "id": base_id,
                    "url": f"https://arxiv.org/abs/{base_id}",
                    "title": " ".join((e.find("atom:title", NS).text or "").split()),
                    "summary": " ".join((e.find("atom:summary", NS).text or "").split()),
                    "published": (e.find("atom:published", NS).text or "")[:10],
                    "category": (cat_el.get("term") if cat_el is not None else (cats[0] if cats else "cs")),
                    "authors": [a.find("atom:name", NS).text for a in e.findall("atom:author", NS)],
                })
            return entries
        except urllib.error.HTTPError as exc:  # 429/503 = 被限流，需要更长退避
            retry_after = (exc.headers.get("Retry-After") if exc.headers else None) or ""
            wait = int(retry_after) if retry_after.isdigit() else 20 * (attempt + 1)
            if attempt < retries:
                print(f"  [retry] HTTP {exc.code} 限流，等待 {wait}s ...", file=sys.stderr)
                time.sleep(wait)
                continue
            print(f"  [warn] query failed after {retries + 1} attempts: HTTP {exc.code}", file=sys.stderr)
            return None
        except Exception as exc:  # noqa: BLE001 — 网络/解析错误统一重试
            if attempt < retries:
                time.sleep(10 * (attempt + 1))
                continue
            print(f"  [warn] query failed: {exc}", file=sys.stderr)
            return None
    return None


def relevance_score(entry: dict) -> int:
    title = entry["title"].lower()
    text = (entry["title"] + "\n" + entry["summary"]).lower()
    score = 0
    for kw, w in KEYWORDS.items():
        if kw in title:
            score += 2 * w
        elif kw in text:
            score += w
    if any(k in title for k in STRONG_TITLE):
        score += 4
    return score


# ---- 主题门控：只有真正属于 agent 生态的论文才收录 ----
TITLE_AGENT = re.compile(
    r"\b(agent|agentic|harness|react|mcp|tool|multi[- ]?agent|orchestrat|swarm|"
    r"scaffold|self-play|post-training|computer use|debate|memory)\b", re.I
)
TITLE_LLM = re.compile(r"\b(llm|language model)\b", re.I)
WEAK_WORDS = ["benchmark", "framework", "platform", "eval", "survey", "system", "environment"]
BLOCKED_FILE = os.path.join(ROOT, "scripts", "blocked_ids.json")


def load_blocked() -> set:
    if os.path.exists(BLOCKED_FILE):
        try:
            with open(BLOCKED_FILE, encoding="utf-8") as f:
                return set(json.load(f))
        except (json.JSONDecodeError, OSError):
            pass
    return set()


def is_on_topic(entry: dict) -> bool:
    """收录门控：过滤经典 DRL、纯检索、API 框架等蹭关键词的论文。"""
    title = entry["title"]
    abstract = entry["summary"]
    t = title.lower()

    # 经典 DRL 论文（非 LLM agent）
    if re.search(r"\bdeep reinforcement learning\b", t) and not re.search(r"\b(llm|language model)\b", t):
        return False
    # 纯检索类论文（无 agent/memory/tool 上下文）
    if "retrieval" in t and "memory" not in t and not TITLE_AGENT.search(title):
        return False
    # 标题强信号（agent/harness/tool/mcp/react 等）
    if TITLE_AGENT.search(title):
        return True
    # 标题只有 LLM 信号 → 摘要必须确有其事（出现 agents）
    if TITLE_LLM.search(title):
        return bool(re.search(r"\bagents?\b", abstract, re.I))
    # 标题是 benchmark/framework 等泛词 → 摘要必须出现 agents
    if any(w in t for w in WEAK_WORDS):
        return bool(re.search(r"\bagents?\b", abstract, re.I))
    return False


def snippet(summary: str, limit: int = 150) -> str:
    """取摘要第一句，截断到 limit 字符。"""
    first = re.split(r"(?<=[.!?])\s+", summary)[0]
    first = re.sub(r"\s+", " ", first).strip()
    if len(first) > limit:
        return first[: limit - 1].rstrip() + "…"
    return first


def load_state() -> dict:
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            pass
    return {}


def save_state(state: dict, keep_days: int = 180) -> None:
    cutoff = (date.today() - timedelta(days=keep_days)).isoformat()
    pruned = {k: v for k, v in state.items() if v >= cutoff}
    os.makedirs(os.path.dirname(STATE_FILE), exist_ok=True)
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(pruned, f, ensure_ascii=False, indent=2, sort_keys=True)


def render_table(entries: list) -> str:
    lines = ["| # | 论文 | 日期 | 分类 | 简介 |", "|---|------|------|------|------|"]
    for i, e in enumerate(entries, 1):
        lines.append(
            f"| {i} | [{e['title']}]({e['url']}) | {e['published']} | {e['category']} | {snippet(e['summary'])} |"
        )
    return "\n".join(lines)


# ---- 备用数据源：OpenAlex（索引 arXiv 预印本，限流宽松，arXiv API 不可用时顶上） ----
OPENALEX_API = "https://api.openalex.org/works"
OPENALEX_MAILTO = "mingqian0850@users.noreply.github.com"
OA_TERM_GROUPS = [
    '"agent harness"',
    '"model context protocol"',
    '"tool calling" OR "tool use" OR "function calling"',
    '"LLM agent" OR "language model agent" OR "LLM-based agent"',
    "agentic",
    '"multi-agent"',
    '"computer use" OR orchestrator',
    '"agent benchmark" OR "agent evaluation" OR "harness evolution"',
]


def _openalex_abstract(inverted: dict) -> str:
    """OpenAlex 用倒排索引存摘要，这里还原成正常文本。"""
    if not inverted:
        return ""
    positions = [(p, w) for w, ps in inverted.items() for p in ps]
    positions.sort()
    return " ".join(w for _, w in positions)


def _openalex_to_entry(w: dict):
    """把 OpenAlex work 转成本脚本统一的 entry 结构；非 arXiv 记录返回 None。"""
    aid = None
    for loc in w.get("locations") or []:
        m = re.search(r"arxiv\.org/abs/([0-9]{4}\.[0-9]{4,5})", (loc or {}).get("landing_page_url") or "")
        if m:
            aid = m.group(1)
            break
    if aid is None:
        m = re.search(r"arxiv\.([0-9]{4}\.[0-9]{4,5})", w.get("doi") or "")
        aid = m.group(1) if m else None
    if aid is None:
        return None
    subfield = (w.get("primary_topic") or {}).get("subfield") or {}
    return {
        "id": aid,
        "url": f"https://arxiv.org/abs/{aid}",
        "title": " ".join((w.get("title") or w.get("display_name") or "").split()),
        "summary": " ".join(_openalex_abstract(w.get("abstract_inverted_index") or {}).split()),
        "published": (w.get("publication_date") or "")[:10],
        "category": subfield.get("display_name") or "arXiv",
        "authors": [a.get("author", {}).get("display_name", "") for a in w.get("authorships") or []],
    }


def fetch_openalex_group(group: str, start: str, per_page: int = 25, retries: int = 3):
    """查询一组 OpenAlex 关键词；成功返回 works 列表，彻底失败返回 None。

    注意：OpenAlex 在 per-page 较大或带 sort 时响应会明显变慢，因此用
    小分页 + select 限定字段 + 默认相关性排序。先试 urllib，失败时改用 curl
    （实测在抖动网络上 curl 成功率明显更高）。
    """
    params = urllib.parse.urlencode({
        "filter": f"from_publication_date:{start},title_and_abstract.search:{group}",
        "per-page": per_page,
        "select": "id,doi,title,publication_date,authorships,primary_topic,locations,abstract_inverted_index",
        "mailto": OPENALEX_MAILTO,
    })
    url = f"{OPENALEX_API}?{params}"
    for attempt in range(retries + 1):
        try:
            if attempt % 2 == 0:      # 先用 curl（实测成功率更高），失败再回退 urllib
                return _curl_get(url, timeout=110)
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT,
                                                      "Accept-Encoding": "gzip"})
            with urllib.request.urlopen(req, timeout=75) as resp:
                return json.loads(_read_body(resp).decode("utf-8")).get("results", [])
        except Exception as exc:  # noqa: BLE001
            if attempt < retries:
                time.sleep(5 * (attempt + 1))
                continue
            print(f"  [warn] openalex query failed: {exc}", file=sys.stderr)
            return None
    return None


def collect_from_arxiv(queries, window_start, blocked, min_score, sleep, retries):
    """从 arXiv API 抓取并筛选，返回 (entries, 失败查询数, 查询总数)。"""
    entries, failed, seen = [], 0, set()
    for i, (q, limit) in enumerate(queries, 1):
        result = fetch_topic(q, max_results=limit, retries=retries)
        if result is None:              # 彻底失败（限流/超时），与"无结果"区分
            failed += 1
        else:
            dates = sorted(e["published"] for e in result if e.get("published"))
            span = f"{dates[0]} ~ {dates[-1]}" if dates else "—"
            print(f"  arxiv 查询 {i}/{len(queries)} 返回 {len(result)} 条（{span}）")
            for e in result:
                if e["id"] in seen or e["id"] in blocked or e["published"] < window_start:
                    continue
                seen.add(e["id"])
                if not is_on_topic(e):
                    continue
                e["score"] = relevance_score(e)
                if e["score"] >= min_score:
                    entries.append(e)
        if i < len(queries):
            time.sleep(sleep)           # 尊重 arXiv 速率限制
    return entries, failed, len(queries)


def collect_from_openalex(window_start, blocked, min_score):
    """从 OpenAlex 备用源抓取，返回 (entries, 失败查询数, 查询总数)。"""
    entries, failed, seen = [], 0, set()
    for group in OA_TERM_GROUPS:
        res = fetch_openalex_group(group, window_start)
        if res is None:
            failed += 1
            continue
        kept = 0
        for w in res:
            e = _openalex_to_entry(w)
            if not e or not e["summary"]:
                continue
            if e["id"] in seen or e["id"] in blocked or e["published"] < window_start:
                continue
            seen.add(e["id"])
            if not is_on_topic(e):
                continue
            e["score"] = relevance_score(e)
            if e["score"] >= min_score:
                entries.append(e)
                kept += 1
        print(f"  openalex: {group[:40]:42s} 返回 {len(res):3d} 条 → 收录 {kept}")
        time.sleep(1)
    return entries, failed, len(OA_TERM_GROUPS)


def main() -> int:
    ap = argparse.ArgumentParser(description="Agent Harness 每周 arXiv 论文精选")
    ap.add_argument("--days", type=int, default=7, help="时间窗口（天），默认 7")
    ap.add_argument("--max-results", type=int, default=30, help="本期最多收录篇数，默认 30")
    ap.add_argument("--min-score", type=int, default=MIN_SCORE, help="相关性最低分，默认 4")
    ap.add_argument("--sleep", type=float, default=6.0, help="查询间隔秒数（arXiv 建议 ≥3s），默认 6")
    ap.add_argument("--per-topic", action="store_true",
                    help="改用 12 个独立主题查询（默认单次合并查询，更不易被 arXiv 限流）")
    ap.add_argument("--fetch-limit", type=int, default=300,
                    help="单次合并查询拉取的最大条目数，默认 300")
    ap.add_argument("--fetch-retries", type=int, default=5,
                    help="每次查询遇到限流时的最大重试次数，默认 5")
    ap.add_argument("--min-papers", type=int, default=3,
                    help="收录数低于该值视为抓取异常，中止且不覆盖已有文件，默认 3")
    ap.add_argument("--max-fail-ratio", type=float, default=0.4,
                    help="查询失败比例上限，超过则中止且不覆盖已有文件，默认 0.4")
    ap.add_argument("--source", choices=["auto", "arxiv", "openalex"], default="auto",
                    help="数据源：auto=先 arXiv，失败时自动切 OpenAlex 备用源（默认）")
    args = ap.parse_args()

    today = date.today()
    window_start = (today - timedelta(days=args.days)).isoformat()

    state = load_state()
    blocked = load_blocked()

    # ---- 抓取阶段：按顺序尝试数据源，任一成功即采用 ----
    order = ["arxiv", "openalex"] if args.source == "auto" else [args.source]
    collected, used_source, diagnostics = [], None, []
    for name in order:
        print(f"[1/3] 数据源 {name}（窗口 {window_start} ~ {today}）...")
        if name == "arxiv":
            # 默认把 12 个主题合并成 1 次查询（arXiv 限流严格，请求数越少越稳）
            queries = ([(q, 20) for q in TOPIC_QUERIES] if args.per_topic
                       else [(COMBINED_QUERY, args.fetch_limit)])
            entries, failed, total = collect_from_arxiv(
                queries, window_start, blocked, args.min_score, args.sleep, args.fetch_retries)
        else:
            entries, failed, total = collect_from_openalex(window_start, blocked, args.min_score)

        ok = total > 0 and failed / total <= args.max_fail_ratio and len(entries) >= args.min_papers
        diagnostics.append(f"{name} 失败 {failed}/{total}、命中 {len(entries)} 篇")
        print(f"  → {name}: {'可用' if ok else '不可用'}（失败 {failed}/{total}，命中 {len(entries)} 篇）")
        if ok:
            collected, used_source = entries, name
            break

    # ---- 安全阀：所有数据源都不可用时中止，绝不覆盖上一期的好内容 ----
    if used_source is None:
        print("[abort] 所有数据源均不可用（" + "；".join(diagnostics)
              + "），本次不更新任何文件，保留上一期内容。", file=sys.stderr)
        return 2

    # 相关性优先、日期次之：避免"最新一天的论文"挤掉整周里更对口的工作
    collected.sort(key=lambda e: (e["score"], e["published"]), reverse=True)
    picked = collected[: args.max_results]
    source_label = "arXiv API" if used_source == "arxiv" else "OpenAlex（arXiv 备用源）"
    print(f"  采用数据源：{source_label}，收录 {len(picked)} 篇")

    for e in picked:
        state[e["id"]] = e["published"]

    print("[2/3] 生成 Markdown 文件 ...")
    os.makedirs(ARCHIVE_DIR, exist_ok=True)

    # 先写本期快照，保证归档列表包含本期
    archive_file = os.path.join(ARCHIVE_DIR, f"{today.isoformat()}.md")
    with open(archive_file, "w", encoding="utf-8") as f:
        f.write(f"# arXiv 论文精选快照 · {today.isoformat()}\n\n")
        f.write(f"收录 **{len(picked)}** 篇（窗口: 近 {args.days} 天 · 数据源: {source_label}，按相关性与时间排序）\n\n")
        f.write(render_table(picked))
        f.write("\n\n---\n\n## 完整摘要\n\n")
        for e in picked:
            f.write(f"### {e['title']}\n\n")
            f.write(f"- **arXiv**: [{e['id']}]({e['url']})  ")
            f.write(f"· **日期**: {e['published']}  ")
            f.write(f"· **分类**: {e['category']}  ")
            f.write(f"· **作者**: {', '.join(e['authors'][:6])}{' 等' if len(e['authors']) > 6 else ''}\n\n")
            f.write(f"{e['summary']}\n\n")

    digest = "\n".join([
        "# 📚 arXiv 论文精选（Agent Harness 生态）",
        "",
        "> 本页由 GitHub Actions 每周自动更新（`scripts/fetch_arxiv.py` 抓取 arXiv API，",
        "> arXiv 限流时自动切换到 OpenAlex 备用源）。",
        "> 覆盖范围：agent harness / LLM agent / tool use / MCP / ReAct / 多智能体 / agent 评测（广义 Agent 生态）。",
        f"> 收录的是**近 {args.days} 天滚动窗口**内的论文，因此与相邻一期可能有重叠；完整历史见下方归档。",
        "",
        f"**最近更新**: {today.isoformat()} · 收录 **{len(picked)}** 篇（窗口: 近 {args.days} 天 · 数据源: {source_label}）",
        "",
        "## 本期新论文",
        "",
        render_table(picked),
        "",
        "## 📂 历史归档",
        "",
    ])
    archives = sorted(
        (f for f in os.listdir(ARCHIVE_DIR) if f.endswith(".md")), reverse=True
    )
    digest += "\n".join(f"- [{f[:-3]}](archive/{f})" for f in archives) + "\n"

    with open(os.path.join(PAPERS_DIR, "README.md"), "w", encoding="utf-8") as f:
        f.write(digest)

    print("[3/3] 保存去重状态 ...")
    save_state(state)
    print(f"完成。最新精选: papers/README.md；快照: {archive_file}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
