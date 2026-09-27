# 📚 arXiv 论文精选（Agent Harness 生态）

> 本页由 GitHub Actions 每周自动更新（`scripts/fetch_arxiv.py` 抓取 arXiv API，
> arXiv 限流时自动切换到 OpenAlex 备用源）。
> 覆盖范围：agent harness / LLM agent / tool use / MCP / ReAct / 多智能体 / agent 评测（广义 Agent 生态）。
> 收录的是**近 7 天滚动窗口**内的论文，因此与相邻一期可能有重叠；完整历史见下方归档。

**最近更新**: 2026-09-27 · 收录 **30** 篇（窗口: 近 7 天 · 数据源: OpenAlex（arXiv 备用源））

## 本期新论文

| # | 论文 | 日期 | 分类 | 简介 |
|---|------|------|------|------|
| 1 | [PhysAI-Bench: A Benchmark for LLM-Based Agentic Decision-Making in Autonomous UAV-Centric Physical AI](https://arxiv.org/abs/2609.23695) | 2026-09-20 | Aerospace Engineering | Recent advances in Physical AI have accelerated the use of foundation models in autonomous systems such as unmanned aerial vehicles (UAVs), which mus… |
| 2 | [EVAGE: Autonomous MEV Generation and Adaptation via Multi-Agent Harness](https://arxiv.org/abs/2609.27424) | 2026-09-23 | Information Systems | Maximal Extractable Value (MEV) has evolved into a major economic force in blockchain ecosystems, yet its capture is dominated by experienced teams,… |
| 3 | [Where Does Exactly-Once Live? Model, Harness, and Tool-Contract Effects on Duplicate Side Effects in LLM Agents](https://arxiv.org/abs/2609.29095) | 2026-09-24 | Computer Networks and Communications | When a tool-using agent's write times out or returns a server error, the action may already have taken effect. |
| 4 | [RRSI: Regularized Recursive Self-Improvement of Agent Harnesses](https://arxiv.org/abs/2609.24972) | 2026-09-21 | Artificial Intelligence | An LLM agent's capability is largely magnified by its harness, namely the prompts, control flow, tooling, memory, and context management surrounding… |
| 5 | [Ascent: An Agentic System over the Model Context Protocol for Real-World Clinical Data Analysis](https://arxiv.org/abs/2609.24620) | 2026-09-21 | Artificial Intelligence | Answering epidemiological questions from real-world clinical data requires medical coding, schema-aware SQL, and validation of implicit choices about… |
| 6 | [DUMA-Bench: A Dual-Control Multi-Agent Benchmark for Evaluating LLM Agent Security](https://arxiv.org/abs/2609.24662) | 2026-09-21 | Information Systems | LLM-based agents increasingly operate in environments where they interact with users, tools, and external systems. |
| 7 | [BabelArena: A Large-Scale Multilingual Benchmark for LLM Agents](https://arxiv.org/abs/2609.23490) | 2026-09-20 | Health Informatics | Large language model (LLM) agents increasingly execute multi-step workflows through tool use and interaction with users and environments. |
| 8 | [Who Is Behind the Harness? Fingerprinting LLMs through Agentic Behavior](https://arxiv.org/abs/2609.28559) | 2026-09-23 | Artificial Intelligence | LLMs increasingly operate through coding-agent harnesses that inspect repositories, invoke tools, and modify files. |
| 9 | [World Action Agent: Harnessing VLMs for Robot Manipulation via World Action Rehearsal](https://arxiv.org/abs/2609.29964) | 2026-09-24 | Computer Vision and Pattern Recognition | General-purpose vision-language models (VLMs) bring broad knowledge and spatial reasoning to robot manipulation, yet existing systems either use them… |
| 10 | [Persistent Billable State: Denial-of-Wallet Attacks and Defenses in Tool-Calling LLM Agents](https://arxiv.org/abs/2609.28585) | 2026-09-23 | Artificial Intelligence | Multi-step tool-calling LLM agents rely on host runtimes to preserve state across turns. |
| 11 | [Harness-Zero: Harness Distillation via Agent-as-Harness](https://arxiv.org/abs/2609.24974) | 2026-09-21 | Artificial Intelligence | Agent harnesses, the external systems that mediate model-environment interaction, can substantially improve agent performance, but their gains remain… |
| 12 | [Multi-Agent Orchestration of 3GPP Channel Estimators](https://arxiv.org/abs/2609.29044) | 2026-09-24 | Electrical and Electronic Engineering | Pilot-aided channel estimation is a decisive block in orthogonal frequency-division multiplexing (OFDM) receivers for both 5G New Radio (5G-NR) and L… |
| 13 | [RegenHarness: A Robot Agent Harness with Evidence-Gated Recursive Self-Improvement](https://arxiv.org/abs/2609.27612) | 2026-09-23 | Social Psychology | Long-horizon robot execution requires a clear distinction between a model's proposal, a controller's termination, and verified task completion. |
| 14 | [Shape Your Feed: An LLM-based Agentic System for Conversational Recommendation](https://arxiv.org/abs/2608.06632) | 2026-09-25 | Information Systems | Industrial recommendation systems predominantly adopt a passive ranking paradigm that infers user preferences from implicit behavioral signals (e.g.,… |
| 15 | [Automatic Harness Evolution for Hardware Design Verification: Can LLMs Consolidate Gains Across Discovered Harnesses?](https://arxiv.org/abs/2609.28908) | 2026-09-24 | Cultural Studies | Agent behavior depends on the harness surrounding a language model, but it remains unclear whether language models can reliably improve such harnesse… |
| 16 | [MemCalib: Benchmarking and Optimizing Memory Use in LLM Agents](https://arxiv.org/abs/2609.24259) | 2026-09-21 | Artificial Intelligence | The effectiveness of agent memory ultimately depends on whether the underlying LLM gives each memory in context an appropriate degree of influence ov… |
| 17 | [OSWorld-Pro: Process-based Evaluation for Computer Use Agents](https://arxiv.org/abs/2609.24890) | 2026-09-21 | Artificial Intelligence | Evaluation of Computer-Use Agents (CUAs) is often limited to the final deliverables they create (at the end of hundreds of steps) and assessed with f… |
| 18 | [Agents That Edit Documents: Measuring Agentic PDF Forgery Against a Non-Agentic Control](https://arxiv.org/abs/2609.23953) | 2026-09-20 | Artificial Intelligence | AI agents that carry a multi-step computer task through on their own became ordinary tools in the past year, and the same autonomy is available to an… |
| 19 | [LLM Agents Can Easily Tamper With Their Own Traces](https://arxiv.org/abs/2609.30266) | 2026-09-24 | Computer Networks and Communications | Asynchronous monitoring, incident investigations, and compliance audits primarily rely on agent traces to reconstruct what happened. |
| 20 | [Agent Name Collision Attacks in Multi-Agent Systems](https://arxiv.org/abs/2609.27624) | 2026-09-23 | Computer Networks and Communications | Multi-agent hosts turn remote Agent Cards into local agents, tools, workflow targets, and broker routes. |
| 21 | [Shutdown Sabotage Propensities in Multi-Agent Systems](https://arxiv.org/abs/2609.28274) | 2026-09-23 | Artificial Intelligence | The final safeguard against rogue AI behavior is the human ability to shut systems down. |
| 22 | [REFLEX with Jev for Efficient Selective Control in LLM Agents](https://arxiv.org/abs/2609.26532) | 2026-09-22 | Artificial Intelligence | LLM agents often use generative models for bounded decisions, raising the question of when these decisions can be handled more efficiently without re… |
| 23 | [Fully Byzantine-Resilient Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2609.25701) | 2026-09-22 | Artificial Intelligence | We study distributed Byzantine-resilient actor-critic multi-agent reinforcement learning (AC-MARL), where agents collectively learn policies through… |
| 24 | [Critical-State RL: Diagnosing Trainable States for Multi-Turn Tool Use](https://arxiv.org/abs/2609.24985) | 2026-09-21 | Cognitive Neuroscience | Multi-turn tool-use failures can hinge on a single model call, yet reward variation alone does not reveal which call would benefit from training. |
| 25 | [LeaseGuard: Incumbent-Preserving Admission Control for Privileged LLM Agents](https://arxiv.org/abs/2609.24077) | 2026-09-21 | Computer Networks and Communications | Privileged language-model agents can satisfy a new system task by displacing a healthy incumbent that depends on the same file, process, socket, lock… |
| 26 | [Emergent Collusion in Long-Horizon LLM Agent Interaction](https://arxiv.org/abs/2609.24967) | 2026-09-21 | Artificial Intelligence | LLM agents are increasingly deployed in collaborative settings, yet long-term interaction may give rise to undesirable coordination. |
| 27 | [VideoGen-Agent: Reinforcing Video Generation Agents](https://arxiv.org/abs/2609.24997) | 2026-09-21 | Computer Vision and Pattern Recognition | Recent advances in video generative models have enabled high-fidelity, temporally coherent video generation. |
| 28 | [Proactive Incentive Regulation in Multi-Agent Systems with Environmental Feedback](https://arxiv.org/abs/2609.24506) | 2026-09-21 | Sociology and Political Science | In environmental feedback systems, self-interested behaviors of rational agents often undermine cooperation and environmental sustainability. |
| 29 | [Autonomous Quantum Transport Measurements of 2D Semiconductors by an AI Agent](https://arxiv.org/abs/2609.26661) | 2026-09-22 | Materials Chemistry | Artificial-intelligence (AI) agents are beginning to enter experimental laboratories, automating experiments and accelerating scientific discovery. |
| 30 | [How Strongly Should Task State Influence an LLM Agent?](https://arxiv.org/abs/2609.25686) | 2026-09-22 | Artificial Intelligence | Long-horizon assigned work requires an LLM agent to track the state of a task: which steps are done, blocked, cancelled, or open to repetition. |

## 📂 历史归档
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
