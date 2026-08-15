# Awesome Harness Agent

精选 **Agent Harness（智能体脚手架）** 生态的 arXiv 论文、开源框架、协议标准与学习资源。

> **Harness** 指模型之外的"脚手架"：agent 循环、工具调用、上下文管理、沙箱与安全、
> 评测与可观测性等一切把 LLM 变成可用智能体的工程组件。这也是 SWE-bench 等榜单上
> 高分系统（OpenHands、Claude Code 等）与裸模型拉开差距的关键。

- 📚 **论文精选**：`papers/README.md` 每周自动更新（GitHub Actions + arXiv API）
- 📖 **基础知识**：`basics/` 人工维护的概念、术语与学习路径
- 🧰 **开源项目**：下方按类别精选，所有链接均已逐一验证（2026-08 复核）

---

## 📚 每周论文精选（自动更新）

- 最新一期：[papers/README.md](papers/README.md)
- 历史快照：[papers/archive](papers/archive/)
- 更新机制：每周日 00:00 UTC 自动运行 [weekly-digest.yml](.github/workflows/weekly-digest.yml)，
  抓取近 7 天 arXiv 上与 agent harness 生态相关的论文（含完整摘要快照），也可在
  Actions 页面手动触发。

## 🧰 开源项目精选

> ⭐ 数据取自 GitHub API，2026-08-15 复核。

### 1. 编码 Agent（终端 / IDE）

| 项目 | 说明 | ⭐ |
|------|------|---|
| [Claude Code](https://github.com/anthropics/claude-code) | Anthropic 官方终端编码 agent（commercial harness 标杆） | 141k |
| [OpenHands](https://github.com/All-Hands-AI/OpenHands) | 全自动软件工程 agent，SWE-bench 领先方案之一 | 84k |
| [Cline](https://github.com/cline/cline) | 自主编码 agent：SDK + IDE 插件 + CLI | 66k |
| [Goose](https://github.com/aaif-goose/goose) | 可扩展开源 agent：安装/执行/编辑/测试，支持任意 LLM | 53k |
| [Aider](https://github.com/Aider-AI/aider) | 终端结对编程 agent，git 原生集成、diff 审查工作流 | 48k |
| [Continue](https://github.com/continuedev/continue) | 开源编码 agent，IDE 深度集成 | 35k |
| [SWE-agent](https://github.com/SWE-agent/SWE-agent) | 论文同源实现：agent-计算机接口（ACI），NeurIPS 2024 | 20k |
| [OpenCode](https://github.com/opencode-ai/opencode) | 终端 AI 编码 agent，支持 MCP 与多种模型 | 14k |

### 2. 通用 Agent 框架与 SDK

| 项目 | 说明 | ⭐ |
|------|------|---|
| [MetaGPT](https://github.com/FoundationAgents/MetaGPT) | 多 agent 软件公司范式（角色分工流水线） | 70k |
| [AutoGen](https://github.com/microsoft/autogen) | 微软多 agent 对话/协作框架 | 60k |
| [CrewAI](https://github.com/crewAIInc/crewAI) | 角色化（Role/Goal/Backstory）多 agent 协作框架 | 57k |
| [LangGraph](https://github.com/langchain-ai/langgraph) | 图状态机式 agent 编排，持久化与人工介入支持完善 | 40k |
| [ChatDev](https://github.com/OpenBMB/ChatDev) | LLM 驱动的多 agent 协作软件开发（ChatDev 2.0） | 34k |
| [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | OpenAI 官方 agent 编排 SDK：handoffs、guardrails、tracing | 29k |
| [smolagents](https://github.com/huggingface/smolagents) | Hugging Face 极简 code-first agent 库（代码即行动） | 29k |
| [Mastra](https://github.com/mastra-ai/mastra) | TypeScript agent 框架（Next.js 生态友好） | 27k |
| [Vercel AI SDK](https://github.com/vercel/ai) | TypeScript 全栈 AI/agent 工具包 | 26k |
| [Letta](https://github.com/letta-ai/letta) | 有状态 agent 平台：类 MemGPT 记忆分层，可自我改进 | 24k |
| [Google ADK](https://github.com/google/adk-python) | Google 官方 Agent Development Kit（A2A 协议原生支持） | 21k |
| [PydanticAI](https://github.com/pydantic/pydantic-ai) | 类型安全（Pydantic）的 Python agent 框架 | 19k |
| [ElizaOS](https://github.com/elizaOS/eliza) | 开源 agent 操作系统（AI16Z 团队，多 agent 运行时） | 19k |
| [CAMEL](https://github.com/camel-ai/camel) | 多 agent 协作框架与"Agent 规模定律"研究 | 18k |
| [AG2](https://github.com/ag2ai/ag2) | AutoGen 社区延续版（原 autogen 改名），持续活跃 | 4.9k |

### 3. 协议与标准

| 项目 | 说明 | ⭐ |
|------|------|---|
| [MCP Servers](https://github.com/modelcontextprotocol/servers) | 官方 MCP 服务器参考实现（filesystem/git/slack 等） | 90k |
| [Model Context Protocol (MCP)](https://github.com/modelcontextprotocol/modelcontextprotocol) | 模型上下文协议：工具/资源/提示标准化接入；[规范文档](https://modelcontextprotocol.io/) | 8.9k |
| [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) | MCP 官方 Python SDK（server + client） | 24k |
| [FastMCP](https://github.com/PrefectHQ/fastmcp) | 最快最 Pythonic 的 MCP server/client 构建库 | 27k |
| [Agent2Agent (A2A)](https://github.com/google/A2A) | Google 主导的企业级 agent 互操作协议（与 MCP 互补） | 25k |
| [AGENTS.md](https://github.com/agentsmd/agents.md) | agent 指令文件规范（"agent 界的 .gitignore"）；[agents.md](https://agents.md/) | 24k |
| [Agent Client Protocol (ACP)](https://github.com/agentclientprotocol/agent-client-protocol) | IDE 与编码 agent 的标准化通信协议 | 4.0k |

### 4. 评测 Harness 与基准实现

| 项目 | 说明 | ⭐ |
|------|------|---|
| [OpenAI Evals](https://github.com/openai/evals) | OpenAI 官方评测框架 + 基准注册表 | 19k |
| [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) | LLM 少样本评测事实标准（EleutherAI） | 14k |
| [SWE-bench](https://github.com/SWE-bench/SWE-bench) | 真实 GitHub issue 修复基准（编码 agent 事实标准） | 5.6k |
| [AgentBench](https://github.com/THUDM/AgentBench) | 多环境 LLM-as-Agent 综合评测（ICLR 2024） | 3.7k |
| [OSWorld](https://github.com/xlang-ai/OSWorld) | 真实计算机环境多模态 agent 评测（NeurIPS 2024） | 3.1k |
| [Inspect](https://github.com/UKGovernmentBEIS/inspect_ai) | 英国 AI 安全研究所官方评测框架（agent eval 优先） | 2.6k |
| [MLE-bench](https://github.com/openai/mle-bench) | ML 工程 agent 评测（Kaggle 竞赛环境） | 1.7k |
| [WebArena](https://github.com/web-arena-x/webarena) | 真实网页环境自主 agent 评测环境 | 1.6k |
| [τ-bench](https://github.com/sierra-research/tau-bench) | 工具-用户交互真实场景基准（含用户模拟） | 1.4k |

### 5. 沙箱与执行环境

| 项目 | 说明 | ⭐ |
|------|------|---|
| [Daytona](https://github.com/daytonaio/daytona) | 安全弹性基础设施：运行 AI 生成代码的沙箱/开发环境 | 72k |
| [E2B](https://github.com/e2b-dev/E2B) | 开源安全执行环境：面向企业级 agent 的真实工具沙箱 | 13k |

### 6. 可观测性、评测与安全平台

| 项目 | 说明 | ⭐ |
|------|------|---|
| [Langfuse](https://github.com/langfuse/langfuse) | 开源 AI 工程平台：tracing、LLM evals、prompt 管理（OTel 集成） | 33k |
| [Phoenix](https://github.com/Arize-ai/phoenix) | AI 可观测性与评测（Arize 开源版） | 11k |
| [AgentOps](https://github.com/AgentOps-AI/agentops) | agent 监控 SDK：成本追踪、基准测试、会话回放 | 5.8k |
| [Langtrace](https://github.com/Scale3-Labs/langtrace) | OpenTelemetry 标准的 LLM 端到端可观测性 | 1.2k |

### 7. 更多 Awesome 列表（聚合入口）

> 以下列表更全（其中 Picrew 版 350+ 条），适合查漏；本仓库侧重中文学习路径与论文自动化。

| 列表 | 说明 | ⭐ |
|------|------|---|
| [awesome-agent-harness (Picrew)](https://github.com/Picrew/awesome-agent-harness) | 实现优先的 agent harness 工程清单，350+ 条，9 大分类，含中英双语 | 1.6k |
| [awesome-agent-harness (AutoJunjie)](https://github.com/AutoJunjie/awesome-agent-harness) | harness 工程指南 + 全生命周期平台/编排器/运行时分类 | 512 |
| [Awesome-Agent-Harness (Gloriaameng)](https://github.com/Gloriaameng/Awesome-Agent-Harness) | 论文与系统并重的 harness 清单 | 329 |
| [awesome-agent-harness (RUCAIBox)](https://github.com/RUCAIBox/awesome-agent-harness) | 人大 AI Box：harness 论文/系统集 | 172 |
| [Awesome-Agent-Harness (HKUST-KnowComp)](https://github.com/HKUST-KnowComp/Awesome-Agent-Harness) | 港科大 KnowComp：agent harness 研究资源 | 59 |
| [awesome-ai-agents](https://github.com/e2b-dev/awesome-ai-agents) | 最流行的 AI agent 通用清单 | 29k |
| [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | MCP 服务器大全（900+） | 92k |
| [Awesome-MCP-ZH](https://github.com/yzfly/Awesome-MCP-ZH) | MCP 中文精选（中文社区维护） | 7.6k |
| [awesome-llm-agents](https://github.com/kaushikb11/awesome-llm-agents) | LLM agent 框架/工具清单 | 1.6k |
| [awesome-llm-powered-agent](https://github.com/hyp1231/awesome-llm-powered-agent) | LLM 驱动 agent 的框架/论文/教程清单 | 2.3k |

## 📖 经典论文（入门必读）

| 论文 | 主题 | arXiv |
|------|------|-------|
| [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629) | 推理 + 行动交替循环，agent 范式鼻祖 | 2210.03629 |
| [Toolformer: Language Models Can Teach Themselves to Use Tools](https://arxiv.org/abs/2302.04761) | 自监督工具学习 | 2302.04761 |
| [ToolLLM](https://arxiv.org/abs/2307.16789) | 大规模真实 API 上的工具学习 | 2307.16789 |
| [Language Agent Tree Search](https://arxiv.org/abs/2310.04406) | 树搜索 + ReAct 的统一推理/规划/行动 | 2310.04406 |
| [SWE-bench](https://arxiv.org/abs/2310.06770) | 真实 GitHub issue 上的编码 agent 评测 | 2310.06770 |
| [WebArena](https://arxiv.org/abs/2307.13854) | 真实网页环境中的自主 agent 评测 | 2307.13854 |
| [OSWorld](https://arxiv.org/abs/2404.07972) | 真实计算机环境的多模态 agent 评测 | 2404.07972 |
| [AgentBench](https://arxiv.org/abs/2308.03688) | 多环境 LLM-as-Agent 综合评测 | 2308.03688 |
| [GAIA](https://arxiv.org/abs/2311.12983) | 通用 AI 助手基准（人类级问题） | 2311.12983 |
| [τ-bench](https://arxiv.org/abs/2406.12045) | 工具-用户交互真实场景基准（含"用户模拟"） | 2406.12045 |
| [MLE-bench](https://arxiv.org/abs/2410.07095) | ML 工程 agent 评测（Kaggle 竞赛环境） | 2410.07095 |
| [A Survey on LLM-based Autonomous Agents](https://arxiv.org/abs/2308.11432) | LLM 自主 agent 综述（架构/应用/评估全景） | 2308.11432 |

## 🎓 学习资源

| 资源 | 说明 |
|------|------|
| [Anthropic: Building Effective Agents](https://www.anthropic.com/research/building-effective-agents) | 经典论断："少写框架、多写简单可组合的循环" |
| [Anthropic: Claude Code Best Practices](https://www.anthropic.com/engineering/claude-code-best-practices) | 编码 agent 提示工程实践 |
| [Anthropic: How We Built Our Multi-Agent Research System](https://www.anthropic.com/engineering/built-multi-agent-research-system) | 多 agent 编排真实案例 |
| [Anthropic: Effective Harnesses for Long-Running Agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) | 长任务 agent 的状态/恢复/可靠性 |
| [OpenAI: A Practical Guide to Building Agents](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/) | OpenAI 官方 34 页实战指南（模式/工作流/防幻觉） |
| [OpenAI: Harness Engineering](https://openai.com/index/harness-engineering/) | 用 harness 约束与验证构建可靠 agent 软件 |
| [MCP 官方文档](https://modelcontextprotocol.io/) | 协议规范、SDK 与示例 |
| [DeepLearning.AI: AI Agents in LangGraph](https://www.deeplearning.ai/short-courses/ai-agents-in-langgraph/) | LangChain 官方免费课程 |
| [anthropics/courses](https://github.com/anthropics/courses) | Anthropic 官方课程仓库 |
| [openai/openai-cookbook](https://github.com/openai/openai-cookbook) | OpenAI 官方 cookbook（Agents SDK 示例） |

> 注：openai.com 对非浏览器访问一律返回 403（反爬机制），链接本身有效。

## 📖 基础知识

见 [basics/](basics/)：学习路径、核心概念、术语表、更多资源。

## 🤝 参与贡献

- 想收录某个框架/论文/资源？欢迎提 Issue 或 PR。
- 想手动触发论文更新？仓库 Actions 页面 → **weekly-arxiv-digest** → **Run workflow**。
- 开源项目链接与 ⭐ 数据在每次人工维护时复核（2026-08 复核过一轮）。

## 📄 License

[MIT](LICENSE)
