# 可靠更新流程

以下命令从仓库根目录运行。Python 统一使用 `python -X utf8`，文件显式读写 UTF-8；不要依赖 Windows 默认 GBK，也不要把网页全文直接输出到默认编码终端。

## 官方来源读取

- OpenAI 完整 Standard 长短上下文表优先直接读取 `https://developers.openai.com/api/docs/pricing.md`。网页工具不支持 `text/markdown`，不要先用它打开 `.md` 再等待失败。使用 `python -X utf8 scripts/fetch_official.py URL --output PATH` 保存到临时目录。
- Kimi 价格概览 `https://platform.kimi.ai/docs/pricing/chat` 的正文提取可能漏掉价格表。用同一脚本获取 HTML，检查内嵌 `DocTable` 的 `columns`、`groups` 和 `rows`；逐列辨认 input、output、cached input、cache writes，不能将缓存写入列误当缓存命中列。只读取数据，不执行网页中的 JavaScript。结构变化时重新检查官方模型文档，不盲用旧解析结果。
- DeepSeek 使用带结尾斜杠的 `https://api-docs.deepseek.com/quick_start/pricing/`；无斜杠页面曾返回入门内容。HTTP 成功不代表取得价格表，必须核对页面标题、模型和实际价格字段。
- 读取脚本仅对超时、连接错误和指定临时 HTTP 错误进行最多三次 GET 请求，30 秒超时，间隔 1、2 秒。永久 HTTP 错误立即失败；成功后的元数据保留已发生的重试错误。
- 输出文件在失败时可能仍是旧文件：只有本次命令成功且内容核验通过才可使用。所有请求失败后改用另一个官方入口；仍无法核验则记录 `unverified`，不得声称无变化或自动 settle。工具限制、页面结构变化、外部故障分别处理，不无限重试，不对提交或 push 等写操作盲目重试。
- 此脚本支持网页和 Markdown 内容，但不自动判断厂商真实性、模型资格或价格是否完整；这些仍按技能的来源与收录规则逐项核验。

## 报告更新与验证

1. 完成在线价格核验后，将中英文核验说明各写入一个 UTF-8 临时文本文件（单段），再运行：

   `python -X utf8 scripts/update_verification.py --date YYYY-MM-DD --en-note EN_PATH --zh-note ZH_PATH`

   脚本保留原有文件的混合 LF/CRLF，避免仅改日期却重写整篇报告；同一段说明重复执行不会再次插入。它只记录核验结果，不负责核验价格。
2. 有实际价格变动时同步模型列表、CSV 和双语价格表。随后运行 `python -X utf8 scripts/build_html.py`。
3. 运行 `python -X utf8 scripts/validate_reports.py` 和 `git diff --check`。固定校验覆盖模型清单、非负价格、分类倍率、排序、双语表格所有价格和人民币换算、日期及网页内嵌数据。表头和分隔行按结构剔除，预期数据行数来自 CSV，不硬编码 51、52 或 53。
4. 修改上述脚本后运行 `python -X utf8 -m unittest discover -s scripts -p "test_*.py"`。如需比较 Git 历史文本，先分别解码并统一 CRLF/LF；用字节相等判断文本数据变化会误报。
5. 校验失败必须定位为产物错误还是检查逻辑错误，修正后重跑相关检查。价格一致性检查不能替代实时来源核验。提交前检查 diff 只包含预期改动；push 后核对远端提交及同一 SHA 的 Pages build/deploy 结果。

## 后续故障

对本流程新出现的问题，修复当前运行后更新最接近根因的脚本或规则，补充有意义的回归场景。不要在报告中不断堆积操作技巧而不更新工具。汇报时区分已恢复错误、未解决问题和实际模型价格变化；自动 settle 继续遵循仓库 AGENTS.md。
