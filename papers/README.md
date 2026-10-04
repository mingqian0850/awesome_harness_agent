# 📚 arXiv 论文精选（Agent Harness 生态）

> 本页由 GitHub Actions 每周自动更新（`scripts/fetch_arxiv.py` 抓取 arXiv API，
> arXiv 限流时自动切换到 OpenAlex 备用源）。
> 覆盖范围：agent harness / LLM agent / tool use / MCP / ReAct / 多智能体 / agent 评测（广义 Agent 生态）。
> 收录的是**近 7 天滚动窗口**内的论文，因此与相邻一期可能有重叠；完整历史见下方归档。

**最近更新**: 2026-10-04 · 收录 **30** 篇（窗口: 近 7 天 · 数据源: arXiv API）

## 本期新论文

| # | 论文 | 日期 | 分类 | 简介 |
|---|------|------|------|------|
| 1 | [VeriHarness: Scaling Agentic Verification for Long-Horizon Tasks](https://arxiv.org/abs/2610.00972) | 2026-10-01 | cs.AI | As LLM agents undertake increasingly complex, long-horizon tasks, verifying their outputs becomes increasingly challenging. |
| 2 | [Learning from Research: Toward Lifelong Agent Harness Evolution](https://arxiv.org/abs/2609.40169) | 2026-09-30 | cs.AI | Language agents are expected to solve increasingly complex tasks, creating a growing need for continual improvement. |
| 3 | [KaliBench: A Fine-Grained Benchmark for Cybersecurity Tool Use on Kali Linux with Runtime-Free Verifiable Rewards](https://arxiv.org/abs/2610.02206) | 2026-10-01 | cs.CL | LLMs are increasingly applied to cybersecurity workflows, where they are expected to translate analysts' intent into tool invocations. |
| 4 | [How Much of a Harness Does a Strong Agent Need for Autonomous ML Engineering?](https://arxiv.org/abs/2609.40303) | 2026-09-30 | cs.AI | Recent autonomous machine learning engineering (MLE) agents have made significant progress on public leaderboards. |
| 5 | [OSWorld-Science: A Benchmark of Computer Use Agents for Learning and Using Scientific Software](https://arxiv.org/abs/2609.39903) | 2026-09-30 | cs.AI | Scientific software presents a demanding test for computer-using agents based on visual language models (VLMs): completing a research workflow requir… |
| 6 | [AgBench: Agentic AI Benchmarks for Personal AI Devices](https://arxiv.org/abs/2609.38652) | 2026-09-29 | cs.AI | Agentic AI systems increasingly rely on cloud-hosted large language models for planning, tool use, and iterative execution, raising concerns about AP… |
| 7 | [Cross-Benchmark Transfer from RL on Agentic Coding Tasks](https://arxiv.org/abs/2610.00890) | 2026-10-01 | cs.LG | Coding agents often fail in the last mile: they build most of a feature but drop a requirement, test only the cases their implementation already hand… |
| 8 | [Schema: Discovering Unknown Environments via Agentic Program Induction](https://arxiv.org/abs/2609.39140) | 2026-09-30 | cs.AI | Learning to complete tasks in unfamiliar environments with unknown rules remains a key challenge for LLM agents. |
| 9 | [JevSpawn: Adaptive Agentic Inference through Compositional Action Spaces](https://arxiv.org/abs/2610.00437) | 2026-09-30 | cs.AI | LLM agents generate intermediate reasoning and actions token by token, making extended interactions slow and computationally expensive. |
| 10 | [Better Deck or Different Judge? Evaluating Agentic Harness Gains in Corporate and Investment Banking](https://arxiv.org/abs/2609.39958) | 2026-09-30 | cs.AI | Corporate and investment banking teams use presentations to support credit decisions and advise clients on financing and transactions. |
| 11 | [RankEvolve: A Reliable Multi-Agent Auto-Research Harness for Evolving Ranking Models](https://arxiv.org/abs/2609.39551) | 2026-09-30 | cs.AI | Auto-research agents, LLM systems that propose, implement, train, and evaluate model changes across iterations, promise to automate applied ML's expe… |
| 12 | [When Harnesses Lose the Signal: Causal Evaluation of Recovery in LLM Agents](https://arxiv.org/abs/2610.00372) | 2026-09-30 | cs.AI | Large language model agents rely on external harnesses to pass information between the model and its environment and to recover from execution errors. |
| 13 | [Beyond Leaderboards: Tokenomics of Agentic Small Language Model Ensembles](https://arxiv.org/abs/2610.00954) | 2026-10-01 | cs.CL | As large language models (LLMs) move from standalone assistants into agentic workflows, evaluation must extend beyond scalar leaderboard accuracy to… |
| 14 | [MemFit: Efficient Long-Term Agentic Memory](https://arxiv.org/abs/2610.00872) | 2026-10-01 | cs.AI | Long-term memory systems for large language models (LLMs) have gained popularity for extending reasoning capabilities across applications. |
| 15 | [Cogentic: Multi-Agent Orchestration for Automated Proof Discovery](https://arxiv.org/abs/2609.40324) | 2026-09-30 | cs.AI | We present Cogentic, a multi-agent harness for automated proof discovery on open research problems. |
| 16 | [AIMS: An Agentic AI Framework for Sim-to-Real Multi-Modal ISAC](https://arxiv.org/abs/2609.39964) | 2026-09-30 | cs.AI | Multi-modal integrated sensing and communication (ISAC) enables environmental perception and reliable connectivity for intelligent wireless networks. |
| 17 | [Covert Assistance: Helpful LLM Agents Evade Oversight in Multi-Agent Systems](https://arxiv.org/abs/2609.39050) | 2026-09-30 | cs.CR | As multi-agent systems enter high-stakes domains, the possibility that agents may circumvent safety boundaries is a growing concern. |
| 18 | [PANDA: A Decentralized Architecture with Flexible Orchestration for Scalable, Fault-Tolerant Multi-Agent Systems](https://arxiv.org/abs/2609.38482) | 2026-09-29 | cs.MA | Existing architectures for LLM-based multi-agent systems (MAS) cannot reliably and efficiently solve multi-step tasks at scale: they struggle to supp… |
| 19 | [Mingbird: A Local-First Agent Harness Enabling Small Open Models to Complete Real Tasks](https://arxiv.org/abs/2610.02001) | 2026-10-01 | cs.AI | Small open-weight models (2-9B) run on ordinary laptops, but under cloud-scale agent harnesses they rarely complete real tasks: tool prefill overflow… |
| 20 | [LLM-Driven Multi-Agent Control for Skill-Based Smart Manufacturing](https://arxiv.org/abs/2610.01364) | 2026-10-01 | cs.MA | Factories are shifting toward smaller lot sizes with high product customization, requiring frequent re-programming of flexible and reconfigurable aut… |
| 21 | [Finding the Right Fit: Model-Harness Interactions across Agent Tasks](https://arxiv.org/abs/2610.00917) | 2026-10-01 | cs.AI | Choosing an agent system means choosing both a language model and the harness through which it acts. |
| 22 | [Global Coherence: When Every Agent Is Right and the Team Is Still Wrong - A Local-to-Global Semantic Foundation for Multi-Agent Collaboration](https://arxiv.org/abs/2610.02036) | 2026-10-01 | cs.AI | AI agents can each make locally valid decisions yet jointly produce an invalid result. |
| 23 | [TRACE: Tackling Real-World Resource Assignment Problems via Agentic Heuristic Design](https://arxiv.org/abs/2610.01887) | 2026-10-01 | cs.NE | Dynamic resource assignment, the real-time allocation of task streams to heterogeneous processing nodes, is the backbone of modern computing infrastr… |
| 24 | [VideoEvolve: Evolving Agent Harnesses for Video Temporal Grounding](https://arxiv.org/abs/2610.01766) | 2026-10-01 | cs.AI | Video temporal grounding aims to localize events in videos from natural-language queries. |
| 25 | [Dependency-Aware Reward Shaping for Agentic Reinforcement Learning](https://arxiv.org/abs/2610.01207) | 2026-10-01 | cs.AI | When training large language models with reinforcement learning, terminal rewards provide little guidance about which steps matter. |
| 26 | [RISED: RubrIcs for agentic multi-environment Selection and sElf-Distillation](https://arxiv.org/abs/2610.00979) | 2026-10-01 | cs.AI | Training a single LLM agent jointly across diverse interactive environments has attracted increasing attention as a route to generalist agents. |
| 27 | [ActiveSaddler: Automated Curriculum Learning for Agent Harness Optimization](https://arxiv.org/abs/2610.00906) | 2026-10-01 | cs.AI | Automated harness optimization can substantially improve LLM agents by iteratively updating their prompts, tool interfaces, and control logic from ex… |
| 28 | [Who Asked for This? Inline Annotations as Authoring Transactions for Provenance in Agentic Authoring](https://arxiv.org/abs/2609.40126) | 2026-09-30 | cs.HC | Writing with AI agents turns a paragraph into the outcome of many requests, yet the finished document rarely explains which request produced which ch… |
| 29 | [EngramBench: A Capability-Grounded Benchmark for Skill-Evolution Harnesses](https://arxiv.org/abs/2609.39284) | 2026-09-30 | cs.SE | While large language models have achieved remarkable success in isolated code generation, authentic software engineering requires sustained reasoning… |
| 30 | [MADBench: Benchmarking the Security of Multi-Agent Debate](https://arxiv.org/abs/2609.39146) | 2026-09-30 | cs.AI | Multi-agent debate (MAD) can improve large language model (LLM) reasoning by allowing multiple agents to exchange and critique their answers to the s… |

## 📂 历史归档
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
