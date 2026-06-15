# PR-Agent 交互体验说明

这个 PR 用来体验 PR-Agent 的评论区交互能力，不用于验证合并门禁。

建议在 PR Conversation 评论框中依次尝试：

```text
/help
```

```text
/describe
```

```text
/review
```

```text
/improve
```

```text
/ask "请用中文总结这次 PR 改了什么，并指出是否有需要人工重点确认的风险。"
```

也可以在 Files changed 页面选择某一行代码旁边的加号，发起行内评论：

```text
/ask "这一行有没有潜在问题？如果没有，请说明为什么。"
```

观察重点：

- PR-Agent 是否能用中文回答。
- `/describe` 是否能生成 PR 描述。
- `/review` 是否能更新审查摘要。
- `/improve` 是否能给出代码建议。
- `/ask` 是否能回答具体问题。
- 手动命令产生的评论是否会影响合并门禁。
