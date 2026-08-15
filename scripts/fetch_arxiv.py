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
import json
import os
import re
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


def fetch_topic(query: str, max_results: int = 20, retries: int = 2) -> list:
    """执行一次 arXiv API 查询，返回条目字典列表。"""
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
            req = urllib.request.Request(url, headers={"User-Agent": "awesome-harness-agent-digest/1.0"})
            with urllib.request.urlopen(req, timeout=30) as resp:
                root = ET.fromstring(resp.read())
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
        except Exception as exc:  # noqa: BLE001 — 网络/解析错误统一重试
            if attempt < retries:
                time.sleep(5 * (attempt + 1))
            else:
                print(f"  [warn] query failed: {exc}", file=sys.stderr)
    return []


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


def main() -> int:
    ap = argparse.ArgumentParser(description="Agent Harness 每周 arXiv 论文精选")
    ap.add_argument("--days", type=int, default=7, help="时间窗口（天），默认 7")
    ap.add_argument("--max-results", type=int, default=30, help="本期最多收录篇数，默认 30")
    ap.add_argument("--min-score", type=int, default=MIN_SCORE, help="相关性最低分，默认 4")
    args = ap.parse_args()

    today = date.today()
    window_start = (today - timedelta(days=args.days)).isoformat()
    print(f"[1/3] 抓取 arXiv（{len(TOPIC_QUERIES)} 个主题查询，窗口 {window_start} ~ {today}）...")

    state = load_state()
    seen_in_run, collected = set(), []
    for i, q in enumerate(TOPIC_QUERIES, 1):
        for e in fetch_topic(q):
            if e["id"] in seen_in_run or e["published"] < window_start:
                continue
            seen_in_run.add(e["id"])
            e["score"] = relevance_score(e)
            if e["score"] >= args.min_score:
                collected.append(e)
        if i < len(TOPIC_QUERIES):
            time.sleep(3.5)  # arXiv API 建议请求间隔

    collected.sort(key=lambda e: (e["published"], e["score"]), reverse=True)
    picked = collected[: args.max_results]

    print(f"  命中 {len(collected)} 篇，收录 {len(picked)} 篇")

    for e in picked:
        state[e["id"]] = e["published"]

    print("[2/3] 生成 Markdown 文件 ...")
    os.makedirs(ARCHIVE_DIR, exist_ok=True)

    # 先写本期快照，保证归档列表包含本期
    archive_file = os.path.join(ARCHIVE_DIR, f"{today.isoformat()}.md")
    with open(archive_file, "w", encoding="utf-8") as f:
        f.write(f"# arXiv 论文精选快照 · {today.isoformat()}\n\n")
        f.write(f"收录 **{len(picked)}** 篇（窗口: 近 {args.days} 天，按相关性与时间排序）\n\n")
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
        "> 本页由 GitHub Actions 每周自动更新（`scripts/fetch_arxiv.py` 抓取 arXiv API）。",
        "> 覆盖范围：agent harness / LLM agent / tool use / MCP / ReAct / 多智能体 / agent 评测（广义 Agent 生态）。",
        "",
        f"**最近更新**: {today.isoformat()} · 收录 **{len(picked)}** 篇（窗口: 近 {args.days} 天）",
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
