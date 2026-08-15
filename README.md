# Awesome Harness Agent

精选 **Agent Harness（智能体脚手架）** 生态的 arXiv 论文、开源框架、协议标准与学习资源。

> **Harness** 指模型之外的"脚手架"：agent 循环、工具调用、上下文管理、沙箱与安全、
> 评测与可观测性等一切把 LLM 变成可用智能体的工程组件。这也是 SWE-bench 等榜单上
> 高分系统（OpenHands、Claude Code 等）与裸模型拉开差距的关键。

- 📚 **论文精选**：`papers/README.md` 每周自动更新（GitHub Actions + arXiv API）
- 📖 **基础知识**：`basics/` 人工维护的概念、术语与学习路径
- 🔧 **框架与协议**：下方精选清单

---

## 📚 每周论文精选（自动更新）

- 最新一期：[papers/README.md](papers/README.md)
- 历史快照：[papers/archive](papers/archive/)
- 更新机制：每周日 00:00 UTC 自动运行 [weekly-digest.yml](.github/workflows/weekly-digest.yml)，
  抓取近 7 天 arXiv 上与 agent harness 生态相关的论文（含完整摘要快照），也可在
  Actions 页面手动触发。

## 🧰 开源 Harness 与框架

| 项目 | 说明 |
|------|------|
| [OpenHands](https://github.com/All-Hands-AI/OpenHands) | 全自动软件工程 agent，SWE-bench 领先方案之一，MIT 协议 |
| [Aider](https://github.com/Aider-AI/aider) | 终端结对编程 agent，git 原生集成、diff 审查工作流 |
| [Claude Code](https://github.com/anthropics/claude-code) | Anthropic 官方终端编码 agent（典型 commercial harness） |
| [Claude Agent SDK](https://github.com/anthropics/claude-agent-sdk) | Anthropic 官方 agent 构建 SDK（TypeScript/Python） |
| [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | OpenAI 官方 agent 编排 SDK：handoffs、guardrails、tracing |
| [Google ADK](https://github.com/google/adk-python) | Google 官方 Agent Development Kit（A2A 协议原生支持） |
| [LangGraph](https://github.com/langchain-ai/langgraph) | 图状态机式 agent 编排框架，支持持久化与人工介入 |
| [AutoGen](https://github.com/microsoft/autogen) | 微软多 agent 对话/协作框架（AG2 社区延续） |
| [CrewAI](https://github.com/crewAIInc/crewAI) | 角色化（Role/Goal/Backstory）多 agent 协作框架 |
| [smolagents](https://github.com/huggingface/smolagents) | Hugging Face 极简 code-first agent 库（写代码而非 JSON 作为行动） |

## 🔌 协议与标准

| 项目 | 说明 |
|------|------|
| [Model Context Protocol (MCP)](https://github.com/modelcontextprotocol/modelcontextprotocol) | 模型上下文协议：工具/资源/提示标准化接入；[规范文档](https://modelcontextprotocol.io/) |
| [Agent2Agent (A2A)](https://github.com/google/A2A) | Google 主导的企业级 agent 互操作协议（与 MCP 互补） |
| [AGENTS.md](https://github.com/agentsmd/agents.md) | agent 指令文件规范（"agent 界的 .gitignore"）；[agents.md](https://agents.md/) |

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
| [OpenAI: A Practical Guide to Building Agents](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/) | OpenAI 官方 34 页实战指南（模式/工作流/防幻觉） |
| [MCP 官方文档](https://modelcontextprotocol.io/) | 协议规范、SDK 与示例 |
| [DeepLearning.AI: AI Agents in LangGraph](https://www.deeplearning.ai/short-courses/ai-agents-in-langgraph/) | LangChain 官方免费课程 |
| [anthropics/courses](https://github.com/anthropics/courses) | Anthropic 官方课程仓库 |
| [openai/openai-cookbook](https://github.com/openai/openai-cookbook) | OpenAI 官方 cookbook（Agents SDK 示例） |

## 📖 基础知识

见 [basics/](basics/)：学习路径、核心概念、术语表、更多资源。

## 🤝 参与贡献

- 想收录某个框架/论文/资源？欢迎提 Issue 或 PR。
- 想手动触发论文更新？仓库 Actions 页面 → **weekly-arxiv-digest** → **Run workflow**。

## 📄 License

[MIT](LICENSE)
