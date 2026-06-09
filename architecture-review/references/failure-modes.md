# Architecture Failure Modes

Use this taxonomy to avoid shallow reviews.

## Boundary Failures

- 控制层承担业务系统能力，导致通用工作流被特定业务耦合。
- 执行层/Worker 隐式决定编排策略，导致控制层不可预测。
- 公共配置和用户级私有配置混用，导致权限、复现和审计困难。
- 容器内路径、宿主机路径、环境变量语义不一致。

## Contract Failures

- LLM/Agent 自然语言输出被当作稳定结构化输出。
- parsed output 缺少 schema validation，失败时只能靠人工读日志。
- 字段语义不唯一，同一字段在不同 workflow 中代表不同含义。
- 输出对象过度绑定某类业务，无法支持通用工作流。
- 新增字段只是补一次事故，没有形成稳定抽象。

## Runtime Failures

- 超时配置硬编码，无法适配不同任务复杂度。
- 流式输出、工具调用输出、最终输出混合，控制层取错结果。
- session 退出、容器 OOM、工具失败被统一折叠成“Agent失败”。
- 缺少幂等键，重试会重复创建任务、评论、分支或外部记录。
- 长流程没有 checkpoint，失败后无法恢复或跳过已完成阶段。

## Data Failures

- 需求、文档、代码仓库、配置来自不同系统，但没有一致性边界。
- 上游字段缺失时没有明确 fallback 或中断策略。
- 缓存、知识库、本地挂载目录没有版本或更新时间记录。
- 数据库持久化只保存最终状态，不保存关键中间输出。

## Operability Failures

- 缺少 request id/task id/session id 贯穿日志。
- 无法从日志判断失败发生在 intent、context、planning、execution 还是 verification。
- 失败原因没有结构化分类，告警和 benchmark 无法聚合。
- 配置变更是否生效只能靠猜，缺少启动时配置摘要和校验。

## Security Failures

- 密钥进入仓库、镜像、日志、会话记录或 issue。
- 用户级 token 被平台级进程复用，越权读取外部系统。
- MCP/Tool 权限过大，Agent 能访问与任务无关的资源。
- 失败日志把外部系统返回、请求头、token 片段暴露给多人。

## Evolution Failures

- 临时绕过方案没有过期条件，逐渐成为事实架构。
- 新 workflow 必须修改核心数据结构，说明抽象边界不稳。
- 为某个业务字段设计的对象被命名成通用对象。
- 缺少 versioning，旧任务输出无法被新控制层读取。

## Review Heuristic

For each important risk, ask:

```text
What must be true for this design to work?
What breaks first when that assumption is false?
How would the system detect it?
How would an operator recover?
What evidence proves the design already handles it?
```
