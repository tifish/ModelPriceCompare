# 模型价格更新

更新价格列表时，遵循 `skills/model-price-compare/SKILL.md`。

首次读取技能文件前就必须将 PowerShell 工具调用设为 `login: false`，并使用 `Get-Content -Encoding utf8`；不能等读完技能才禁用 profile。调用可选工具 `py`、`gh` 前先用 `Get-Command py,gh -ErrorAction SilentlyContinue` 检测，缺失时走可靠更新流程中的解释器和 GitHub API 备用路径，不直接执行不存在的命令。

中文文本文件优先通过文件编辑工具直接写入 UTF-8，不通过默认编码的 PowerShell 管道传给 Python。必须使用管道时，先在同一次 shell 调用中设置 `$OutputEncoding = [Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()`；`python -X utf8` 本身不会改变 PowerShell 的管道编码。更新命令失败后必须停止依赖步骤，修复并重跑更新成功后才能构建和校验。

## 修复必须固化

- 用户要求：以后本仓库任务中遇到问题，修复后应将可复用的处理固化到脚本、校验或技能规则，避免后续会话重复踩坑；不能只在当前终端临时绕过。
- 先确认根因，再采用适度的持久修复，并用原失败场景或有意义的回归检查验证。网络等外部故障不能保证消除，应采用有界重试、明确的备用路径和失败报告，不得用旧数据冒充核验成功。
- 完成时说明固化位置、验证结果及仍存在的限制。已有处理无法覆盖的新问题，应在同次任务中补充；涉及范围外配置或额外权限时遵循原授权边界。
- 错误恢复和自动 settle 分开判断：以下 settle 条件保持适用，不因重试成功而隐瞒发生过的错误。

## 会话自动 settle

- 用户要求：以后每次更新完成后，如果没有新增模型、没有模型 token 价格变化，而且没有出现错误，自动将当前 T3 会话 settle。
- 判断价格变化时忽略汇率变化及其引起的人民币换算变化；仅更新核验日期或说明不影响自动 settle。
- 必须先完成本次请求及必要校验；若涉及提交和 push，先确认推送和 GitHub Pages 构建部署成功，再 settle。
- 出现新模型、模型 token 价格变化或错误时，不自动 settle，保留会话供用户查看。不得将核验失败当作无变化。
- 使用 T3 的 `t3_thread_organize` 对当前会话执行 settle；工具不可用或调用失败时如实说明，不声称已 settle。
