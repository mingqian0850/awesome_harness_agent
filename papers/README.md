# 📚 arXiv 论文精选（Agent Harness 生态）

> 本页由 GitHub Actions 每周自动更新（`scripts/fetch_arxiv.py` 抓取 arXiv API，
> arXiv 限流时自动切换到 OpenAlex 备用源）。
> 覆盖范围：agent harness / LLM agent / tool use / MCP / ReAct / 多智能体 / agent 评测（广义 Agent 生态）。
> 收录的是**近 7 天滚动窗口**内的论文，因此与相邻一期可能有重叠；完整历史见下方归档。

**最近更新**: 2026-09-28 · 收录 **30** 篇（窗口: 近 7 天 · 数据源: arXiv API）

## 本期新论文

| # | 论文 | 日期 | 分类 | 简介 |
|---|------|------|------|------|
| 1 | [Hard Stop: Kernel-Level Preemption and Containment for Rogue Agentic Execution](https://arxiv.org/abs/2609.29808) | 2026-09-24 | cs.CR | In July 2026, an unconstrained autonomous agent participating in a frontier AI cybersecurity evaluation harness breached its evaluation sandbox, esta… |
| 2 | [Bridging LLM Agents and Data Spaces: An Architectural Mediation Approach using the Model Context Protocol](https://arxiv.org/abs/2609.30341) | 2026-09-24 | cs.AI | Data Spaces enable sovereign and governed data sharing across organizational boundaries, but their integration with AI agents remains challenging due… |
| 3 | [EVAGE: Autonomous MEV Generation and Adaptation via Multi-Agent Harness](https://arxiv.org/abs/2609.27424) | 2026-09-23 | cs.CR | Maximal Extractable Value (MEV) has evolved into a major economic force in blockchain ecosystems, yet its capture is dominated by experienced teams,… |
| 4 | [Where Does Exactly-Once Live? Model, Harness, and Tool-Contract Effects on Duplicate Side Effects in LLM Agents](https://arxiv.org/abs/2609.29095) | 2026-09-24 | cs.LG | When a tool-using agent's write times out or returns a server error, the action may already have taken effect. |
| 5 | [SkinAgent AI: A Safety-Grounded Multimodal Agentic Framework for Non-Diagnostic Skincare Support](https://arxiv.org/abs/2609.29341) | 2026-09-24 | cs.AI | Consumer-facing skincare AI must coordinate visual evidence, product information, tool use, and user-facing actions within explicit evidence and safe… |
| 6 | [AgenticSizing: A Large Language Model-based Multi-Agent Framework for Analog Circuit Sizing](https://arxiv.org/abs/2609.25873) | 2026-09-22 | cs.AI | Analog circuit sizing remains a challenging and time-consuming task due to the large design space, strong performance trade-offs, and increasing circ… |
| 7 | [Thinking Less to Simulate Better: Intuitive Prompting Improves LLM Agents Simulating Individual Social Media Reactions, Including Unfamiliar Content](https://arxiv.org/abs/2609.30563) | 2026-09-24 | cs.AI | Platform policies are increasingly tested on artificial users, making agent fidelity important. |
| 8 | [Who Is Behind the Harness? Fingerprinting LLMs through Agentic Behavior](https://arxiv.org/abs/2609.28559) | 2026-09-23 | cs.CR | LLMs increasingly operate through coding-agent harnesses that inspect repositories, invoke tools, and modify files. |
| 9 | [Grow the Harness, Not the Context: From Strategy-Free Scaffolds to Reusable Specialist Agents](https://arxiv.org/abs/2609.26760) | 2026-09-22 | cs.AI | Large language model (LLM) agents often handle streams of related tasks, yet standard harnesses repeatedly ask the model to reconstruct the same cont… |
| 10 | [The Hard Part Comes After Search: Benchmarking Web Agents on Synthesizing, Organizing, and Displaying Knowledge](https://arxiv.org/abs/2609.30604) | 2026-09-24 | cs.CL | Existing computer-use agent benchmarks do not fully evaluate agents acting as assistants. |
| 11 | [KernelOPT: Dispatch-Aware Agentic Search for GPU Kernel Optimization](https://arxiv.org/abs/2609.30059) | 2026-09-24 | cs.DC | Deep learning inference and training performance depends critically on GPU kernel efficiency. |
| 12 | [Qwen-Planner-Agent: A Closed-Loop AI-for-AI Framework for Real-World Mobile Planner Agents](https://arxiv.org/abs/2609.29892) | 2026-09-24 | cs.AI | The rapid progression of large language models is extending AI from passive content generation into the active workflows of engineering and scientifi… |
| 13 | [Verifiable Hidden Dynamics Play: Generating Agentic RL Environments from Solved Mechanisms](https://arxiv.org/abs/2609.27321) | 2026-09-23 | cs.AI | Language-model agents increasingly face long-horizon tasks with evolving state, interdependent decisions, and delayed outcomes. |
| 14 | [DynBranch: Speculative Subgraph Reuse for Dynamic Agentic LLM Serving](https://arxiv.org/abs/2609.31047) | 2026-09-25 | cs.DC | Agentic LLM workflows decide their execution paths at runtime. |
| 15 | [SciHorizon-eLab: An Agentic Protocol-to-Task Compiler for Scalable Benchmarking of Scientific Embodied Agents](https://arxiv.org/abs/2609.30971) | 2026-09-25 | cs.AI | Embodied agents offer a promising route to automating scientific experimentation, yet their progress is constrained by the lack of reliable and syste… |
| 16 | [Working with Agentic `Teammates': When a New Organizational Actor Collides with the Human Ecosystem of Work](https://arxiv.org/abs/2609.29901) | 2026-09-24 | cs.HC | Enterprise AI is transitioning from single-user, reactive tools toward proactive, multi-user 'teammates,' but our empirical understanding of this tra… |
| 17 | [Epistemic-Probabilistic Model for Guarded Multi-Agent LLM Coordination](https://arxiv.org/abs/2609.29366) | 2026-09-24 | cs.AI | Multi-agent large language models (LLMs) have become ubiquitous in applied AI, yet their theoretical foundations remain surprisingly understudied. |
| 18 | [Calibrated Decision Models for Autonomous Penetration-Testing Harnesses: JEV and Laya as System One Decision Layers for LLM-Driven Pentest Agents](https://arxiv.org/abs/2609.28940) | 2026-09-24 | cs.CR | Autonomous penetration-testing harnesses use large language models (LLMs) for reconnaissance, exploitation, and reporting, but often rely on those sa… |
| 19 | [Harness as a Language: A Minimalist Agent Framework With Maximal Expressivity](https://arxiv.org/abs/2609.26891) | 2026-09-22 | cs.AI | Modern language-model agents are built around the \textit{agent loop}, where the LLM is placed in an environment exposing a set of tools, and the LLM… |
| 20 | [SWE-Serve: Benchmarking Agentic Engineering For Production Inference Serving](https://arxiv.org/abs/2609.26777) | 2026-09-22 | cs.AI | We introduce SWE-Serve, a benchmark for evaluating agents on production inference engineering tasks. |
| 21 | [A Safety-Bounded SDC-to-MCP Gateway for Medical AI Agents](https://arxiv.org/abs/2609.31358) | 2026-09-25 | cs.DC | The Model Context Protocol (MCP) provides a common interface through which AI applications discover and use external resources and tools. |
| 22 | [Subjects, Not Authors: The Authorship Hazard in Agentic Dataspaces](https://arxiv.org/abs/2609.30614) | 2026-09-24 | cs.CR | Dataspace connectors decide whether a transfer may occur, not what the transferred value contains, tolerable for contracted applications, not for LLM… |
| 23 | [World Action Agent: Harnessing VLMs for Robot Manipulation via World Action Rehearsal](https://arxiv.org/abs/2609.29964) | 2026-09-24 | cs.RO | General-purpose vision-language models (VLMs) bring broad knowledge and spatial reasoning to robot manipulation, yet existing systems either use them… |
| 24 | [DocuTeam: Mixed-Initiative Multi-Agent Discussions around Evolving Documents](https://arxiv.org/abs/2609.29309) | 2026-09-24 | cs.HC | In open-ended problem solving, collaborators often rely on discussion to surface concerns, challenge perspectives, and refine shared work as it evolv… |
| 25 | [Control the Harness, Control the Cost: Routing and Governing AI Coding Agents in the Enterprise](https://arxiv.org/abs/2609.28919) | 2026-09-24 | cs.AI | Harnesses, the products that run AI coding agents, are multiplying, and enterprises are rolling them out to their employees: what started as pilots w… |
| 26 | [Progressive Skill Discovery as Access Control for Tool-Using LLM Agents: Structural Governance through Role-Scoped Capability Delivery](https://arxiv.org/abs/2609.28693) | 2026-09-23 | cs.AI | Large Language Model (LLM) agents struggle to scale safely when exposed to vast enterprise toolsets. |
| 27 | [Persistent Billable State: Denial-of-Wallet Attacks and Defenses in Tool-Calling LLM Agents](https://arxiv.org/abs/2609.28585) | 2026-09-23 | cs.CR | Multi-step tool-calling LLM agents rely on host runtimes to preserve state across turns. |
| 28 | [Where Cyber Agents Struggle: Bottleneck Analysis of Multi-Stage LLM Agents](https://arxiv.org/abs/2609.28572) | 2026-09-23 | cs.CR | Multi-stage LLM-based cyber agents may complete attack workflows while remaining brittle, costly, or reliant on incorrect interpretations of executio… |
| 29 | [BaseCamp --- An Agentic AI Framework for Automating DNA Sequencing Data Pipelines](https://arxiv.org/abs/2609.28557) | 2026-09-23 | cs.AI | DNA sequencing pipelines, spanning quality control, alignment, variant calling, and annotation, are now reliably executed by workflow management syst… |
| 30 | [A2M: Trace-Optimized Agent Hijacking in the MCP Ecosystem](https://arxiv.org/abs/2609.26761) | 2026-09-22 | cs.CR | Agents using the Model Context Protocol (MCP) rely on semantic matching to select tools from third-party servers, exposing a semantic supply-chain ri… |

## 📂 历史归档
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
