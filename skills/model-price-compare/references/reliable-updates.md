# 可靠更新流程

以下命令从仓库根目录运行。Python 统一使用 `python -X utf8`，文件显式读写 UTF-8；不要依赖 Windows 默认 GBK，也不要把网页全文直接输出到默认编码终端。

## Windows 环境预检

- PowerShell 工具调用使用 `login: false`（外部启动使用 `-NoProfile`），避免用户 profile 被执行策略拦截。读取中文时显式指定 `Get-Content -Encoding utf8`，输出前设置 `$OutputEncoding = [Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()`。不修改机器执行策略。
- 先检查解释器路径和版本。`WindowsApps/python.exe` 可能只是商店占位程序，不能当作可用 Python。优先检查 `py -3`；不可用时定位本机已有 Python，验证版本及标准库后用该解释器的绝对路径运行本文命令（PowerShell 使用 `&`）。不把机器专属路径写入共享脚本，不为此改全局 PATH 或自动安装环境。
- 提交前先用 `git ls-remote origin refs/heads/main` 检查连接。若 SSH 明确报代理程序不存在，检查 `~/.ssh/config` 中 ProxyCommand 的目标路径。仅在确认直接连接可用后，可用仓库局部 `git config --local core.sshCommand 'ssh -o ProxyCommand=none -o BatchMode=yes -o ConnectTimeout=15'` 固化备用路径；不改全局 SSH 配置。保持主机密钥验证。直连仍失败时报告阻塞，不盲目重试 push。
- 提交前检查 `git var GIT_AUTHOR_IDENT`。身份未配置时，核对仓库近期提交；在已有上下文明确支持且身份一致时，仅在仓库局部设置 `user.name` 和 `user.email`，不修改全局配置，不把用户邮箱写进共享脚本。身份有歧义则询问用户，不编造。
- `py`、`gh` 都是可选工具，先用 `Get-Command py,gh -ErrorAction SilentlyContinue` 检测。没有 `py` 时，检测 `Get-Command python,python3 -ErrorAction SilentlyContinue` 的非 WindowsApps 路径并验证标准库。没有 `gh` 时，公开仓库的 Pages 状态可通过 `fetch_official.py` 读取 GitHub 官方 API：`https://api.github.com/repos/tifish/ModelPriceCompare/actions/runs?head_sha=SHA&per_page=10`，从相同 SHA 的 Pages run 获取 jobs URL，再核对 build、deploy 均成功。也可核对 `/pages/builds/latest` 的 `commit` 和 `status`。状态未完成时进行有界查询；API 限流或无权限时明确报告，不能把上一次部署成功当成本次成功。无需为公开只读查询安装 CLI 或索取凭据。

## 官方来源读取

- 多来源抓取使用 `python -X utf8 scripts/fetch_sources.py OUTPUT_DIR name=https://official-url ...`，避免在 PowerShell 的 `python -c` 参数中嵌套字符串或函数定义（Windows 参数传递可能移除引号并导致 SyntaxError）。需要临时解析逻辑时也先写 UTF-8 脚本再执行。批量命令有任一来源失败即返回非零；逐项核对元数据和重试记录后才能使用结果。Windows 下 `rg` 的文件通配符使用 `rg PATTERN DIRECTORY -g '*.txt'`，不将通配符拼进文件路径。

- 新发现条目的详情链接必须从官方价格页、模型目录或文档索引中取得，不要按模型 ID 拼接 URL。OpenAI 可从 `https://developers.openai.com/api/docs/llms.txt` 找到模型目录；目录当前为 `https://developers.openai.com/api/docs/models/all.md`。价格页中的 model configuration 不一定有独立模型详情页（例如 `gpt-6-astra-law`）；需区分配置与独立 API 模型。遇到 404 不重复请求同一地址，改查官方索引及价格表；若仍不能确认收录资格，记录排除原因或待核实事项，不将该条目算作已核验的新模型。404 仍属于本次错误，不能自动 settle。
- OpenAI 完整 Standard 长短上下文表优先直接读取 `https://developers.openai.com/api/docs/pricing.md`。网页工具不支持 `text/markdown`，不要先用它打开 `.md` 再等待失败。使用 `python -X utf8 scripts/fetch_official.py URL --output PATH` 保存到临时目录。
- Gemini 价格入口 `https://ai.google.dev/gemini-api/docs/pricing` 也可能返回 Markdown，并重定向到 `https://aistudio.google.com/docs/pricing`；优先用同一抓取脚本读取，核对最终官方域名及 Standard 表。网页工具的 unsupported content-type 不是价格核验成功；直接抓取成功后仍需保留本次错误记录。
- Kimi 价格概览 `https://platform.kimi.ai/docs/pricing/chat` 的正文提取可能漏掉价格表。用同一脚本获取 HTML，检查内嵌 `DocTable` 的 `columns`、`groups` 和 `rows`；逐列辨认 input、output、cached input、cache writes，不能将缓存写入列误当缓存命中列。只读取数据，不执行网页中的 JavaScript。结构变化时重新检查官方模型文档，不盲用旧解析结果。
- DeepSeek 使用带结尾斜杠的 `https://api-docs.deepseek.com/quick_start/pricing/`；无斜杠页面曾返回入门内容。HTTP 成功不代表取得价格表，必须核对页面标题、模型和实际价格字段。
- 读取脚本仅对超时、连接错误和指定临时 HTTP 错误进行最多三次 GET 请求，30 秒超时，间隔 1、2 秒。永久 HTTP 错误立即失败；成功后的元数据保留已发生的重试错误。
- 输出文件在失败时可能仍是旧文件：只有本次命令成功且内容核验通过才可使用。所有请求失败后改用另一个官方入口；仍无法核验则记录 `unverified`，不得声称无变化或自动 settle。工具限制、页面结构变化、外部故障分别处理，不无限重试，不对提交或 push 等写操作盲目重试。
- 此脚本支持网页和 Markdown 内容，但不自动判断厂商真实性、模型资格或价格是否完整；这些仍按技能的来源与收录规则逐项核验。

## 报告更新与验证

抓取后可运行 `python -X utf8 scripts/inspect_sources.py OUTPUT_DIR --previous PREVIOUS_DIR`，生成可读 `.clean` 文本、来源差异和模型详情链接。此前即使是 `python -c` 中的正则引号也曾触发 PowerShell 解析错误；HTML、正则和差异解析统一使用脚本文件，不再把复杂解析嵌入 shell 参数。脚本跳过 script/style 和超长 hydration 文本，不执行网页代码；它只辅助检查，不能替代对原始内嵌价格表（如 Kimi DocTable）的核验，也不能把忽略的内容视为无变化。

1. 完成在线价格核验后，将中英文核验说明各写入一个 UTF-8 临时文本文件（单段），再运行：

   `python -X utf8 scripts/update_verification.py --date YYYY-MM-DD --en-note EN_PATH --zh-note ZH_PATH`

   脚本保留原有文件的混合 LF/CRLF，避免仅改日期却重写整篇报告；同一段说明重复执行不会再次插入。它只记录核验结果，不负责核验价格。
2. 有实际价格变动时同步模型列表、CSV 和双语价格表。随后运行 `python -X utf8 scripts/build_html.py`。
3. 运行 `python -X utf8 scripts/validate_reports.py` 和 `git diff --check`。固定校验覆盖模型清单、非负价格、分类倍率、排序、双语表格所有价格和人民币换算、日期及网页内嵌数据。表头和分隔行按结构剔除，预期数据行数来自 CSV，不硬编码 51、52 或 53。
4. 修改上述脚本后运行 `python -X utf8 -m unittest discover -s scripts -p "test_*.py"`。如需比较 Git 历史文本，先分别解码并统一 CRLF/LF；用字节相等判断文本数据变化会误报。
5. 校验失败必须定位为产物错误还是检查逻辑错误，修正后重跑相关检查。价格一致性检查不能替代实时来源核验。提交前检查 diff 只包含预期改动；push 后核对远端提交及同一 SHA 的 Pages build/deploy 结果。

## 后续故障

README 历史内容混用 LF/CRLF；`.gitattributes` 对 `README*.md` 和 `model_price_comparison.csv` 启用 `cr-at-eol`，让 `git diff --check` 正确识别 CRLF，同时保留真正行尾空格等检查。不要为消除 CR 误报重写全部历史换行。修改此规则时用原有 README 混合换行及 CSV CRLF 的 diff 验证通过，并临时在新增行末插入空格确认检查仍会失败，随后恢复。

对本流程新出现的问题，修复当前运行后更新最接近根因的脚本或规则，补充有意义的回归场景。不要在报告中不断堆积操作技巧而不更新工具。汇报时区分已恢复错误、未解决问题和实际模型价格变化；自动 settle 继续遵循仓库 AGENTS.md。
