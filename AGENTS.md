# 模型价格更新

更新价格列表时，遵循 `skills/model-price-compare/SKILL.md`。

## 会话自动 settle

- 用户要求：以后每次更新完成后，如果没有新增模型、没有模型 token 价格变化，而且没有出现错误，自动将当前 T3 会话 settle。
- 判断价格变化时忽略汇率变化及其引起的人民币换算变化；仅更新核验日期或说明不影响自动 settle。
- 必须先完成本次请求及必要校验；若涉及提交和 push，先确认推送和 GitHub Pages 构建部署成功，再 settle。
- 出现新模型、模型 token 价格变化或错误时，不自动 settle，保留会话供用户查看。不得将核验失败当作无变化。
- 使用 T3 的 `t3_thread_organize` 对当前会话执行 settle；工具不可用或调用失败时如实说明，不声称已 settle。
