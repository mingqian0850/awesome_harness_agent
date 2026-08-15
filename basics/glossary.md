# 术语表（中英对照）

> 按主题分组，持续补充。想新增词条欢迎提 PR/Issue。

## 核心概念

| 术语 | 说明 |
|------|------|
| **Agent（智能体）** | 能感知环境、自主决策并采取行动的 AI 系统；本文档语境下指"用 LLM 驱动的任务执行系统" |
| **Agent Harness（脚手架）** | 模型之外的工程组件总和：循环、工具、上下文、沙箱、评测、可观测性 |
| **Agent Loop（智能体循环）** | 思考→行动→观察→再思考 的主循环 |
| **Scaffolding（脚手架）** | 与 harness 近义，强调"支撑结构"，常见于 SWE-bench 语境 |
| **Multi-agent（多智能体）** | 多个 agent 协作/竞争完成任务，如 orchestrator-worker、handoff 模式 |
| **Orchestrator（编排器）** | 负责任务分解与分派的"主管"agent |
| **Handoff（移交）** | 把对话/任务移交给另一个更合适的 agent（OpenAI Agents SDK 核心概念） |
| **Guardrail（护栏）** | 在 agent 输入/输出上运行的校验器，拦截不合规行为 |

## 工具与协议

| 术语 | 说明 |
|------|------|
| **Tool / Function Calling（工具/函数调用）** | 模型输出结构化调用请求，由 harness 执行并返回结果 |
| **MCP（Model Context Protocol）** | 模型上下文协议：工具/资源/提示的标准化接入协议（Anthropic 提出，现为开放标准） |
| **A2A（Agent2Agent）** | Google 主导的 agent 间互操作协议 |
| **AGENTS.md** | 项目内 agent 指令文件规范（类似 .gitignore 之于 git） |
| **JSON Schema** | 描述工具入参的结构化格式，function calling 的载体 |
| **ReAct** | Reasoning + Acting：推理与行动交替的经典范式（论文 2210.03629） |
| **CodeAct** | Code as Action：以写代码/执行代码作为行动方式 |

## 工程组件

| 术语 | 说明 |
|------|------|
| **Context Window（上下文窗口）** | 模型一次能"看到"的 token 上限 |
| **Context Engineering（上下文工程）** | 压缩、检索、注入信息以高效利用上下文窗口 |
| **Memory（记忆）** | 短期（对话内）/长期（向量库、文件、数据库）信息存储 |
| **RAG（检索增强生成）** | 检索外部知识注入上下文再生成 |
| **Sandbox（沙箱）** | agent 的隔离执行环境（容器、受限权限、审批） |
| **Human-in-the-loop（人在回路）** | 关键步骤由人类确认/介入 |
| **Tracing / Observability（追踪/可观测性）** | 记录 agent 的思考与行动过程，用于调试与改进 |

## 评测

| 术语 | 说明 |
|------|------|
| **Benchmark（基准）** | 标准化评测任务集，如 SWE-bench、GAIA、OSWorld、τ-bench |
| **SWE-bench** | 真实 GitHub issue 修复基准，编码 agent 事实标准 |
| **Pass@k** | 生成 k 次中至少一次成功的比例 |
| **Eval Harness（评测脚手架）** | 评测 agent 本身也是一套 harness |
| **Reward Model（奖励模型）** | RL 训练中为模型行为打分的模型 |

## 训练与模型侧（了解即可）

| 术语 | 说明 |
|------|------|
| **RLHF / RL** | 基于人类反馈的强化学习 / 强化学习，agent 行为对齐的主要手段 |
| **Tool-augmented LLM** | 通过工具调用增强的模型（Toolformer、ToolLLM 等） |
| **Reasoning Model（推理模型）** | 显式"思考"后再回答的模型（如 o 系列、DeepSeek-R1），常作为 agent 大脑 |
