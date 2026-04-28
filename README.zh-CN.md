# 模型 Token 价格比较（人民币）

[English](README.md) | [中文](README.zh-CN.md)

生成日期：2026-04-26

所有价格统一为人民币约价 / 1M tokens。除提供方直接列出人民币价格的情况外，美元价格按 `1 USD = 6.95 CNY` 近似换算。倍率按每个价格类别分别计算，以该类别中最便宜的模型作为 `1.00x`；在本次模型列表中，DeepSeek V4 Flash 在缓存未命中输入、缓存命中输入、输出三个类别中都是基准。

| 模型 | 提供方 | 输入缓存未命中 | 未命中倍率 | 输入缓存命中 | 命中倍率 | 输出 | 输出倍率 | 价格口径 |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| DeepSeek V4 Flash | DeepSeek | ¥0.97 | 1.00x | ¥0.19 | 1.00x | ¥1.95 | 1.00x | 当前标准 API |
| DeepSeek V4 Pro | DeepSeek | ¥3.02 | 3.11x | ¥0.25 | 1.29x | ¥6.05 | 3.11x | 当前限时折扣价 |
| Kimi K2.6 | Moonshot AI / Kimi | ¥6.60 | 6.79x | ¥1.11 | 5.71x | ¥27.80 | 14.29x | 标准 API |
| Xiaomi MiMo-V2.5-Pro | Xiaomi MiMo | ¥6.95 | 7.14x | ¥1.39 | 7.14x | ¥20.85 | 10.71x | 海外 API，<=256K tokens 档 |
| GLM-5.1 | Z.AI | ¥9.73 | 10.00x | ¥1.81 | 9.29x | ¥30.58 | 15.71x | 标准 API |
| Gemini 3.1 Pro Preview | Google | ¥13.90 | 14.29x | ¥1.39 | 7.14x | ¥83.40 | 42.86x | 付费 Standard，<=200K prompts 档 |
| GPT-5.4 | OpenAI | ¥17.38 | 17.86x | ¥1.74 | 8.93x | ¥104.25 | 53.57x | 标准短上下文 API |
| Claude Opus 4.6 | Anthropic | ¥34.75 | 35.71x | ¥3.48 | 17.86x | ¥173.75 | 89.29x | Claude API 全球路由 |
| Claude Opus 4.7 | Anthropic | ¥34.75 | 35.71x | ¥3.48 | 17.86x | ¥173.75 | 89.29x | Claude API 全球路由 |
| GPT-5.5 | OpenAI | ¥34.75 | 35.71x | ¥3.48 | 17.86x | ¥208.50 | 107.14x | 标准短上下文 API |

## 重要说明

- 汇率采用近似值 `1 USD = 6.95 CNY`。该汇率取自 2026-04-26 前后可查的 USD/CNY 参考汇率，并四舍五入便于横向比较；实际账单以服务商结算币种和付款时汇率为准。
- DeepSeek V4 Pro 使用当前官方限时折扣价：缓存命中约 `¥0.25`、缓存未命中约 `¥3.02`、输出约 `¥6.05`。同一官方页面还列出常规价格：缓存命中约 `¥1.01`、缓存未命中约 `¥12.09`、输出约 `¥24.19`；折扣有效期至 `2026-05-05 15:59 UTC`。
- Xiaomi MiMo-V2.5-Pro 使用官方海外 API 的 `<=256K` tokens 档并换算为人民币约价：缓存命中约 `¥1.39`、输入约 `¥6.95`、输出约 `¥20.85`。同一官方页面列出 `256K` 到 `1M` tokens 档：缓存命中约 `¥2.78`、输入约 `¥13.90`、输出约 `¥41.70`。缓存写入当前限时免费。小米官方中国区价格表中同档约为缓存命中 `¥1.40`、输入 `¥7.00`、输出 `¥21.00`。
- Kimi K2.6 使用官方 `kimi-k2.6` 价格并换算为人民币约价：缓存命中约 `¥1.11`、缓存未命中约 `¥6.60`、输出约 `¥27.80`；上下文长度为 `256K`，支持自动上下文缓存。
- Gemini 3.1 Pro 使用官方 `gemini-3.1-pro-preview` 付费 Standard 档，且 prompt 不超过 `200K` tokens，换算为人民币约价：缓存命中约 `¥1.39`、输入约 `¥13.90`、输出约 `¥83.40`。超过 `200K` tokens 时，Google 列出的价格约为缓存命中 `¥2.78`、输入 `¥27.80`、输出 `¥125.10`；上下文缓存存储费约为 `¥31.28 / 1M tokens / 小时`。
- OpenAI GPT-5.4 和 GPT-5.5 使用 Standard 短上下文价格。对超过 `272K` 输入 tokens 的请求，OpenAI 会对完整 session 按 `2x` 输入和 `1.5x` 输出计价；区域处理另加 `10%`。
- Anthropic Claude 使用标准 Claude API 全球路由价格。缓存命中为基础输入价格的 `0.1x`；5 分钟缓存写入约 `¥43.44 / 1M tokens`，1 小时缓存写入约 `¥69.50 / 1M tokens`。US-only inference 另加 `1.1x`。Opus 4.7 使用新 tokenizer，同样固定文本可能多消耗最多 `35%` tokens。
- Z.AI 将 GLM-5.1 的 cached input storage 标为限时免费；本比较只纳入 cached input read 价格。
- 除非特别说明，本比较不包含 Batch、Flex、Priority、fast mode、数据驻留、联网/工具调用费用、session runtime、企业折扣等变体。
- 本次曾按请求尝试使用 `browser-use`，但本地 in-app browser runtime 因 app-server 路径缺失未能启动。价格核验仍通过官方网页检索完成，来源列在下方。

## 访问过的价格网址

- OpenAI pricing: https://developers.openai.com/api/docs/pricing
- OpenAI GPT-5.4 model page: https://developers.openai.com/api/docs/models/gpt-5.4
- OpenAI GPT-5.5 model page: https://developers.openai.com/api/docs/models/gpt-5.5
- Anthropic pricing: https://platform.claude.com/docs/en/about-claude/pricing?939688b5_page=1&e45d281a_page=2
- Anthropic Opus 4.7 update: https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-6
- DeepSeek pricing: https://api-docs.deepseek.com/quick_start/pricing
- DeepSeek V4 release note: https://api-docs.deepseek.com/news/news260424
- Z.AI pricing: https://docs.z.ai/guides/overview/pricing
- Z.AI GLM-5.1 model page: https://docs.z.ai/guides/llm/glm-5.1
- Kimi K2.6 pricing: https://platform.kimi.ai/docs/pricing/chat-k26
- Xiaomi MiMo pricing: https://platform.xiaomimimo.com/static/docs/pricing.md
- Xiaomi MiMo-V2.5 release note: https://platform.xiaomimimo.com/static/docs/news/v2.5-news.md
- Gemini API pricing: https://ai.google.dev/gemini-api/docs/pricing
- USD/CNY reference: https://www.exchange-rates.org/exchange-rate-history/usd-cny-2026
