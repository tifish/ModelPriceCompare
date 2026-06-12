---
name: model-price-compare
description: 使用官方价格页面比较当前 LLM API token 价格。适用于比较模型成本、输入/缓存未命中/缓存命中/输出 token 单价、价格倍率、模型价格来源 URL，发现官方价格页新增且已明确定价的模型，或维护 OpenAI、Anthropic/Claude、DeepSeek、Z.AI/GLM、Google Gemini、Moonshot AI/Kimi、小米 MiMo 等厂商的可复用模型列表和报告。
---

# 模型价格比较

## 概览

为用户给定的模型列表生成标准化价格表，价格必须来自官方价格页面和当前公开费率。记录来源 URL、限制说明和模型列表输入，保证比较结果可以复查和重复生成。

## 工作流

1. 从用户提示或 `models.txt` 等纯文本文件读取模型列表，每行一个模型。把条目视为用户提供的别名；它们可能不完整、带本地化名称，或有轻微误写。
2. 浏览或抓取当前官方厂商价格页和模型文档。优先使用 `references/official-sources.md` 中的 URL 和厂商注意事项。
3. 更新可复用报告时，扫描每个已访问的官方价格页面，查找输入列表中尚未出现的新模型。只有同时满足以下条件时才自动加入：属于同一厂商系列的正式或预览 API 模型，主要比较列有明确 token 价格，并且能无歧义映射到官方模型 ID。跳过 embeddings、moderation、仅图像/音频/视频模型、已废弃模型、仅市场渠道 SKU、仅区域变体、企业/私有模型和别名，除非用户明确要求。对看起来相关但被排除的新发现做简短说明。
4. 在定价前，把每个请求模型或新发现别名解析为官方显示名和模型 ID。主表 `model` 列使用修正后的官方名称；写入可复用产物时，把 `models.txt` 更新为规范名称。非显然的更正要在备注中说明原始别名；如果多个官方模型都可能匹配，先向用户澄清，不要猜。
5. 将所有 token 价格标准化为 USD / 1M tokens。
6. 至少记录以下字段；CSV 可继续使用英文列名，中文 Markdown 报告可以翻译表头，但含义必须一致：
   - model
   - provider
   - input cache miss，也就是 standard/base input
   - input cache hit，也就是 cached input 或 cache read
   - output
   - 每个价格类别的 multiplier
   - source URL
   - notes
7. 分类别计算倍率：每个价格除以同一列中最便宜的非零价格。除非用户明确要求，不要使用全局统一基准。
8. 说明排除项，例如 Batch、Flex、Priority、区域处理、数据驻留、cache writes、cache storage、session runtime、tool charges、限时折扣或企业价格。
9. 在仓库中维护可复用产物时，按现有约定同步：
   - `models.txt`：可编辑的输入模型列表
   - `README.md`：需要以项目 readme 发布时的默认英文报告
   - `README.zh-CN.md`：需要双语 readme 时的简体中文版本；在两个 readme 顶部附近放语言切换链接
   - `model_price_comparison.csv`：便于电子表格使用的数据
   - 不再维护独立的 `model_price_comparison*.md`，避免和 README 内容重复；可读报告以双语 README 为准

## 来源规则

- 优先使用官方厂商文档。第三方来源只能用于发现官方页面，不要把第三方页面作为价格依据引用。
- 价格变化频繁；每次都要实时验证当前页面，不要依赖以前的运行结果。
- 对 OpenAI 模型和价格问题，只使用 OpenAI 官方文档。
- 如果官方页面列出限时、区域或上下文长度分层价格，主比较使用当前有效价格，并在备注中写明常规/替代价格。
- 如果更新过程中官方页面出现新的合格模型，要在同一次运行中加入 `models.txt`、CSV 和 Markdown 报告，不要等用户点名。
- 如果在官方页面找不到请求模型，把它标记为 `unverified`，不要编造价格。

## 输出风格

默认使用简体中文与用户沟通，除非用户明确要求英文或双语。主表保持紧凑；README 和 CSV 中把 input cache miss 放在 input cache hit 前，并按 input cache miss 价格升序排序。详细限制写在 `Important Notes` 或中文 README 的 `重要说明` 下，来源 URL 写在 `Price URLs Visited` 或中文 README 的 `已访问价格 URL` 下。

## 开源卫生

- 不要在生成的 skill 文件中包含本地绝对路径、私有 API key、账号 ID、cookie、浏览器历史或工作区专属密钥。
- 可复用厂商来源映射放在 `references/official-sources.md`，不要塞进单次任务报告。
- 把生成的比较文件视为示例或输出，不要当作永久准确的价格数据。
