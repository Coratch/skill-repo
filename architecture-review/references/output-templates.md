# Architecture Review Output Templates

## Full Review

````markdown
核心结论：
  <通过 / 有条件通过 / 不建议通过 / 信息不足无法通过>，因为 <one sentence>.

审查对象：
  - 系统/模块：
  - 目标：
  - 输入材料：
  - 关键假设：

审查范围：
  - In scope:
  - NOT in scope:

当前理解：
```text
Input -> Node A -> Node B -> Output
          |          |
          v          v
       Store A    Store B
```

关键对象：
| 阶段 | 输入 | 输出 | 持久化 | 下游消费者 |
|---|---|---|---|---|

已有能力：
| 能力 | 位置/证据 | 当前方案关系 | 判断 |
|---|---|---|---|

主要问题：
| 严重度 | 问题 | 证据 | 影响 | 建议 |
|---|---|---|---|---|

适用边界：
  - ...

失败模式：
  - ...

替代方案：
| 方案 | 适用场景 | 代价 | 风险 |
|---|---|---|---|

推荐路径：
  1. ...
  2. ...
  3. ...

开放问题：
  - ...
````

## Adversarial Review

```markdown
反方结论：
  当前方案在 <boundary> 下不应直接通过。

最弱前提：
  1. ...
  2. ...
  3. ...

失败模式：
| 失败模式 | 触发条件 | 用户影响 | 系统信号 | 防护/修复 |
|---|---|---|---|---|

反方建议：
  - 必须补齐：
  - 可以暂缓：
  - 不建议做：

通过门槛：
  - ...
```

## Incident Architecture Review

```markdown
架构层根因：
  <root cause in one sentence>

事实链：
  1. <evidence>
  2. <evidence>
  3. <evidence>

直接原因：
  - ...

架构缺陷：
  - ...

为什么现有设计没有拦住：
  - contract:
  - observability:
  - timeout/retry:
  - config:

最小恢复方案：
  1. ...

长期修复方案：
  1. ...

需要进入 benchmark 的 case：
  - case name:
  - input:
  - expected contract:
  - deterministic assertion:
```

## Contract Review

```markdown
Contract 结论：
  <stable / unstable / over-specialized / under-specified>

对象边界：
| 对象 | 职责 | 不应承担 | 生产者 | 消费者 |
|---|---|---|---|---|

字段审查：
| 字段 | 当前语义 | 问题 | 建议 |
|---|---|---|---|

结构化保障：
  - schema validation:
  - parser behavior:
  - error classification:
  - backward compatibility:

不建议新增的字段：
  - ...

建议新增或调整：
  - ...
```
