# Output Templates

Use these templates as defaults. Adjust length to the user's request.

## Scan Mode

```markdown
**中心论点**
[One sentence]

**这篇文章在解决什么问题**
[2-4 bullets]

**5W2H**
| 维度 | 结论 | 证据位置 |
|---|---|---|

**核心主张**
| 主张 | 证据 | 可信度 |
|---|---|---|

**值得继续深读的点**
[3 bullets]
```

## Deep Mode

```markdown
**中心论点**
[One sentence]

**SCQA**
| 部分 | 内容 |
|---|---|
| Situation | |
| Complication | |
| Question | |
| Answer | |

**主张-证据-假设**
| 主张 | 证据 | 推理桥梁 | 假设/限制 | 证据强度 |
|---|---|---|---|---|

**关键概念**
| 概念 | 通俗解释 | 技术解释 | 例子 |
|---|---|---|---|

**批判性阅读**
- 最强证据：
- 最弱环节：
- 可能反例：
- 适用边界：

**我应该记住什么**
1.
2.
3.

**下一步学习任务**
[3 actionable tasks]
```

## Coach Mode

```markdown
**本轮目标**
[Concept/thesis to explain]

请你先用自己的话解释：
1. 这篇文章的中心论点是什么？
2. 作者为什么认为它成立？
3. 你会如何举一个例子？

我会按这个格式反馈：
- 准确的部分：
- 最大理解缺口：
- 修正解释：
- 请你再试一次：
```

When reviewing the user's answer, do not move to a new topic until the biggest gap is fixed.

## Memory Mode

```markdown
**主动回忆题**
| 问题 | 答案要点 | 难度 |
|---|---|---|

**记忆卡片**
| Front | Back | Type |
|---|---|---|

**迁移练习**
| 场景 | 问题 | 参考答案 |
|---|---|---|

**复习计划**
| 时间 | 任务 |
|---|---|
| 今天 | |
| 明天 | |
| 3天后 | |
| 7天后 | |
| 14天后 | |
```

## Compact Final Answer

When the user asks for a short answer:

```markdown
**一句话**
[Thesis]

**三点**
1.
2.
3.

**一个提醒**
[Weakness, caveat, or application]
```

## Anki CSV Shape

If the user asks for Anki output, use:

```csv
Front,Back,Tags
"Question","Answer","article-learning"
```
