# 📚 arXiv 论文精选（Agent Harness 生态）

> 本页由 GitHub Actions 每周自动更新（`scripts/fetch_arxiv.py` 抓取 arXiv API，
> arXiv 限流时自动切换到 OpenAlex 备用源）。
> 覆盖范围：agent harness / LLM agent / tool use / MCP / ReAct / 多智能体 / agent 评测（广义 Agent 生态）。
> 收录的是**近 7 天滚动窗口**内的论文，因此与相邻一期可能有重叠；完整历史见下方归档。

**最近更新**: 2026-10-11 · 收录 **30** 篇（窗口: 近 7 天 · 数据源: arXiv API）

## 本期新论文

| # | 论文 | 日期 | 分类 | 简介 |
|---|------|------|------|------|
| 1 | [A Closer Look at Agentic BBO: Benchmarking LLM Agents for Black-Box Optimization](https://arxiv.org/abs/2610.12183) | 2026-10-08 | cs.LG | Black-box optimization (BBO) arises in many scientific and engineering problems where objective evaluations are expensive and limited. |
| 2 | [DuplexAgent-RSI: Recursive Harness Improvement for Full-Duplex Voice Agent Collaboration](https://arxiv.org/abs/2610.11299) | 2026-10-08 | cs.AI | Voice agents are converging on a collaboration pattern: a full-duplex interaction model stays on the live channel as the entry to the conversation, w… |
| 3 | [The Harness as the Only Mutable Surface: Compliance-Bounded Self-Evolution of LLM Agents in Credit Pipelines, with a Measured Admission Gate](https://arxiv.org/abs/2610.10629) | 2026-10-07 | cs.AI | Self-improving LLM agents can adapt a credit pipeline to a changed rule, but an agent that rewrites itself destroys the artefact a supervisor reviews… |
| 4 | [Agentic AI-Assisted Modeling for Production Scheduling: Assessment in Constraint Programming](https://arxiv.org/abs/2610.10184) | 2026-10-07 | cs.AI | Developing optimization models for production scheduling requires substantial expert effort. |
| 5 | [How Do Agentic LLMs Decide to Call Tools? A Tool-Call Vector Shaped by Suppression](https://arxiv.org/abs/2610.09624) | 2026-10-07 | cs.AI | Tool calling, invoking external tools on demand, is central to agentic LLMs, yet the mechanism that decides whether a model calls a tool or responds… |
| 6 | [SynCo: Data Synthesis Co-Training for Self-Evolving LLMs via Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2610.11345) | 2026-10-08 | cs.AI | Self-evolving LLM agents promise to improve autonomously through continual interaction and learning, reducing their dependence on manually curated su… |
| 7 | [Plan-and-Patch: Diffusion Language Models for Agentic Planning](https://arxiv.org/abs/2610.10786) | 2026-10-07 | cs.AI | Planning is increasingly important for long-horizon agents, where successful execution requires coordinating subgoals, tool use, and intermediate out… |
| 8 | [GeoNatureAgent (GNA): A Framework and Benchmark for Pre-Production Evaluation of Tool-Using Agents on Geospatial and Environmental Tasks](https://arxiv.org/abs/2610.09112) | 2026-10-06 | cs.AI | Before tool-using LLM agents are deployed in environmental and geospatial workflows, teams need evidence that an agent reliably selects the right ope… |
| 9 | [Not Every Call Needs a Frontier Model: Per-Call-Site Evaluation of Small Language Models in a Deployed Agentic Home-Automation System](https://arxiv.org/abs/2610.09021) | 2026-10-06 | cs.AI | An agentic system issues several structurally different kinds of LLM calls. |
| 10 | [RFChipAgent: Multi-Agentic AI Flow for Analog/RF Chip Design](https://arxiv.org/abs/2610.10858) | 2026-10-07 | cs.AR | Analog/RF circuits remain the critical interface between digital computation and the physical world, and emerging standards from Wi-Fi 7 to 6G place… |
| 11 | [Agent4RE: A Self-Refining Multi-agent Framework for End-to-End Software Requirements Engineering and Benchmarking](https://arxiv.org/abs/2610.10628) | 2026-10-07 | cs.SE | Existing LLM-based approaches for software Requirements Engineering (RE) typically rely on basic prompting strategies or rudimentary agent collaborat… |
| 12 | [Goldsmith: Gold-Loss-Guided Definition Optimization with an Agentic Annotation Harness](https://arxiv.org/abs/2610.09489) | 2026-10-07 | cs.CL | Many annotation projects begin before experts have a stable guideline or enough labels to train a task-specific model. |
| 13 | [From Plausible Hierarchies to Useful Taxonomies: Evaluating Agentic Harnesses on Customer Feedback](https://arxiv.org/abs/2610.09377) | 2026-10-07 | cs.AI | Taxonomies are the symbolic representations through which AI systems organize evidence, aggregate patterns, and answer questions over large document… |
| 14 | [Humanize: Judgement Engineering for Agentic Coding](https://arxiv.org/abs/2610.08900) | 2026-10-06 | cs.AI | Agentic coding makes code generation cheap, but reliable completion remains difficult: the agent that writes the code is a weak judge of whether it i… |
| 15 | [TRACE: Diagnosing Verifier Brittleness in Agentic Evaluation](https://arxiv.org/abs/2610.11678) | 2026-10-08 | cs.CL | Verifier scores now serve as both benchmark metrics and training rewards for large language model (LLM) agents, and a change in score is routinely re… |
| 16 | [Safe, Persistent, and Evolving Agent Harness for Understanding Partially Observable Worlds](https://arxiv.org/abs/2610.11552) | 2026-10-08 | cs.AI | Large language model agents can invoke tools fluently, but enterprise workflows demand more than selecting the right tools: actions must strictly com… |
| 17 | [GROB: A Multi-Agent Architecture for Public-Trace Investigation of Candidate Agentic Activity](https://arxiv.org/abs/2610.11467) | 2026-10-08 | cs.CR | We present GROB, a multi-agent architecture for investigating candidate autonomous-agent activity through public Internet traces when privileged tele… |
| 18 | [When Interfaces Speak: Data-Aware Generative UI Harness for Active Interaction](https://arxiv.org/abs/2610.11123) | 2026-10-08 | cs.AI | Most human-agent interaction today remains text-based. |
| 19 | [AgentHorizon: Evaluating Agentic Judges for Long-Horizon Computer-Use Tasks](https://arxiv.org/abs/2610.11050) | 2026-10-08 | cs.AI | Computer-use agents are capable of completing complex tasks, increasing the use of automatic judges to determine success, either for training or for… |
| 20 | [ASPIRE: Agentic Safety & Prompt Injection Red-teaming Engine](https://arxiv.org/abs/2610.08951) | 2026-10-06 | cs.CR | LLM agents retrieve untrusted content and act through tools, creating indirect prompt-injection risks that can cause unauthorized actions or persiste… |
| 21 | [ParanoiaEval: Benchmarking Unnecessary Defensive Work in Agentic Coding](https://arxiv.org/abs/2610.08662) | 2026-10-06 | cs.AI | As coding agents increasingly undertake real-world work autonomously, judging whether their risk treatments are warranted has become important. |
| 22 | [Harness Evolution Hits a Ceiling: When Weight Training Should Begin](https://arxiv.org/abs/2610.11655) | 2026-10-08 | cs.AI | Improving a long-horizon LLM agent means evolving the harness around a frozen model or training its weights. |
| 23 | [Mine Odyssey: Benchmarking Spatial Agentic Intelligence in the Wild](https://arxiv.org/abs/2610.11328) | 2026-10-08 | cs.AI | Advances in foundation models are driving efforts to introduce agents to assist people in the physical world. |
| 24 | [TestJack: Should you trust the results in coding benchmarks? Agentic Coding Benchmarks Auditing via Evaluator Evolution](https://arxiv.org/abs/2610.10619) | 2026-10-07 | cs.SE | Large language model (LLM) agents are rapidly reshaping software engineering, accompanied by an explosion of new code benchmarks. |
| 25 | [ToolRACER: A Robust Agentic Conversation Emulation Resource for Agent Training and Evaluation](https://arxiv.org/abs/2610.09163) | 2026-10-06 | cs.CL | Task-oriented conversational agents remain fragile under real world conversation scenarios as they rarely follow a predictable script, especially whe… |
| 26 | [HarnessSQL: Harness-Native Training for SQL Agents in Realistic Database Environments](https://arxiv.org/abs/2610.12274) | 2026-10-08 | cs.CL | Text-to-SQL models are commonly trained to map questions directly to static queries, whereas real-world database agents operate through stateful, mul… |
| 27 | [Recursive Self-Improvement through Multi-Agent Self-Supervision](https://arxiv.org/abs/2610.12176) | 2026-10-08 | cs.AI | Recursive self-improvement (RSI) of a model on non-verifiable tasks, such as open-ended research, faces a supervision bottleneck when its outputs exc… |
| 28 | [Agentic-TTT: Training test-time policy for test-time training](https://arxiv.org/abs/2610.12002) | 2026-10-08 | cs.LG | Test-time training (TTT) adapts an LLM's parameters using signals derived from test inputs, and can make striking improvements in pre-specified setti… |
| 29 | [Error-Propagation Modeling for Failure Attribution in LLM-Based Multi-Agent Systems](https://arxiv.org/abs/2610.11600) | 2026-10-08 | cs.AI | LLM-based multi-agent systems (MASs) are increasingly used to solve complex tasks through coordinated reasoning, tool use, and interaction with exter… |
| 30 | [Environmental Feedback Modeling Matters: Rethinking Feedback Treatment in Agentic Hindsight Self-Distillation](https://arxiv.org/abs/2610.11384) | 2026-10-08 | cs.AI | Reinforcement learning is commonly used to train language agents in interactive environments, but cannot be directly applied when rewards are unavail… |

## 📂 历史归档
- [2026-10-11](archive/2026-10-11.md)
- [2026-10-04](archive/2026-10-04.md)
- [2026-09-28](archive/2026-09-28.md)
- [2026-09-27](archive/2026-09-27.md)
- [2026-09-21](archive/2026-09-21.md)
- [2026-09-20](archive/2026-09-20.md)
- [2026-09-14](archive/2026-09-14.md)
- [2026-09-13](archive/2026-09-13.md)
- [2026-09-06](archive/2026-09-06.md)
- [2026-08-30](archive/2026-08-30.md)
- [2026-08-23](archive/2026-08-23.md)
- [2026-08-20](archive/2026-08-20.md)
- [2026-08-15](archive/2026-08-15.md)
