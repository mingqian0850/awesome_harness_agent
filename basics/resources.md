# 学习资源

> 精选高质量资源，按"入门 → 深入 → 动手"排序。所有链接均已人工验证。

## 📄 必读文章（按顺序）

| 资源 | 说明 |
|------|------|
| [Anthropic: Building Effective Agents](https://www.anthropic.com/research/building-effective-agents) | **入门第一课**。讲清 agent 与 workflow 的区别、三大设计模式，论断"少写框架"影响深远 |
| [OpenAI: A Practical Guide to Building Agents](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/) | OpenAI 官方 34 页指南：模式、工作流、上下文工程、防幻觉、安全 |
| [Anthropic: How We Built Our Multi-Agent Research System](https://www.anthropic.com/engineering/built-multi-agent-research-system) | 多 agent 编排真实案例：主 agent + 子 agent + 并行化 |
| [Anthropic: Claude Code Best Practices](https://www.anthropic.com/engineering/claude-code-best-practices) | 提示工程 + 工作流实践（CLAUDE.md、plan mode、checkpoints） |
| [Anthropic: Effective Context Engineering for AI Agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | 上下文工程专题 |

## 📚 官方文档

| 资源 | 说明 |
|------|------|
| [Model Context Protocol 文档](https://modelcontextprotocol.io/) | MCP 规范、SDK、示例 |
| [OpenAI Agents SDK 文档](https://openai.github.io/openai-agents-python/) | handoffs / guardrails / sessions 详解 |
| [LangGraph 文档](https://langchain-ai.github.io/langgraph/) | 图状态机编排 |
| [Google ADK 文档](https://google.github.io/adk-docs/) | Google 官方 agent 开发套件 |
| [Anthropic Agent SDK 文档](https://docs.claude.com/en/api/agent-sdk/overview) | Claude Agent SDK（TS/Python） |

## 🎓 课程

| 资源 | 说明 |
|------|------|
| [DeepLearning.AI: AI Agents in LangGraph](https://www.deeplearning.ai/short-courses/ai-agents-in-langgraph/) | LangChain 官方免费短课 |
| [anthropics/courses](https://github.com/anthropics/courses) | Anthropic 官方课程仓库（含 agent 主题） |

## 💻 代码仓库

| 资源 | 说明 |
|------|------|
| [anthropics/courses](https://github.com/anthropics/courses) | 官方示例代码 |
| [openai/openai-cookbook](https://github.com/openai/openai-cookbook) | Agents SDK 等官方示例 |
| [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | 官方 MCP 服务器参考实现 |

## 📰 值得关注的信息源

- **GitHub 开源项目精选**：[README 第 2-7 节](../README.md#-开源项目精选)按 6 大类整合了编码 agent、
  框架、协议、评测、沙箱、可观测性项目，第 7 节聚合了 10 个现存 awesome 列表（含中文的 Awesome-MCP-ZH）
- **arXiv**：cs.AI / cs.CL / cs.LG 分类（本仓库每周自动抓取）
- **Hacker News / Reddit r/LocalLLaMA**：harness 工程实践讨论密集
- **各框架官方博客**：LangChain、Anthropic Engineering、OpenAI 等

> 提示：把 [papers/README.md](../papers/README.md) 收藏进浏览器书签，
> 每周日自动更新的论文精选会帮你跟上前沿。
