# 模型 Token 价格比较（人民币）

[English](README.md) | [中文](README.zh-CN.md)

生成日期：2026-05-07

所有价格统一为人民币约价 / 1M tokens。除提供方直接列出人民币价格的情况外，美元价格按 `1 USD = 6.806 CNY` 近似换算。倍率按每个价格类别分别计算，以该类别中最便宜的模型作为 `1.00x`；在本次模型列表中，DeepSeek V4 Flash 在缓存未命中输入、缓存命中输入、输出三个类别中都是基准。

| 模型 | 提供方 | 输入缓存未命中 | 未命中倍率 | 输入缓存命中 | 命中倍率 | 输出 | 输出倍率 | 价格口径 |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| DeepSeek V4 Flash | DeepSeek | ¥0.95 | 1.00x | ¥0.019 | 1.00x | ¥1.91 | 1.00x | 当前标准 API |
| DeepSeek V4 Pro | DeepSeek | ¥2.96 | 3.11x | ¥0.025 | 1.29x | ¥5.92 | 3.11x | 当前限时折扣价 |
| Kimi K2.6 | Moonshot AI / Kimi | ¥6.47 | 6.79x | ¥1.09 | 57.14x | ¥27.22 | 14.29x | 标准 API |
| Xiaomi MiMo-V2.5-Pro | Xiaomi MiMo | ¥6.81 | 7.14x | ¥1.36 | 71.43x | ¥20.42 | 10.71x | 海外 API，<=256K tokens 档 |
| GLM-5.1 | Z.AI | ¥9.53 | 10.00x | ¥1.77 | 92.86x | ¥29.95 | 15.71x | 标准 API |
| Gemini 3.1 Pro Preview | Google | ¥13.61 | 14.29x | ¥1.36 | 71.43x | ¥81.67 | 42.86x | 付费 Standard，<=200K prompts 档 |
| GPT-5.4 | OpenAI | ¥17.02 | 17.86x | ¥1.70 | 89.29x | ¥102.09 | 53.57x | 标准短上下文 API |
| Claude Sonnet 4.6 | Anthropic | ¥20.42 | 21.43x | ¥2.04 | 107.14x | ¥102.09 | 53.57x | Claude API 全球路由 |
| Claude Opus 4.6 | Anthropic | ¥34.03 | 35.71x | ¥3.40 | 178.57x | ¥170.15 | 89.29x | Claude API 全球路由 |
| Claude Opus 4.7 | Anthropic | ¥34.03 | 35.71x | ¥3.40 | 178.57x | ¥170.15 | 89.29x | Claude API 全球路由 |
| GPT-5.5 | OpenAI | ¥34.03 | 35.71x | ¥3.40 | 178.57x | ¥204.18 | 107.14x | 标准短上下文 API |

## 重要说明

- 汇率采用近似值 `1 USD = 6.806 CNY`。该汇率取自 Currency Live 在 `2026-05-07 04:54 GMT` 给出的 USD/CNY 中间价；实际账单以服务商结算币种和付款时汇率为准。
- DeepSeek V4 Flash 的缓存命中输入现为 `$0.0028` / 1M tokens，DeepSeek 标注该价格自 `2026-04-26 12:15 UTC` 起降为发布价的 `1/10`。
- DeepSeek V4 Pro 使用当前官方限时折扣价：缓存命中约 `¥0.025`、缓存未命中约 `¥2.96`、输出约 `¥5.92`。同一官方页面还列出常规价格：缓存命中约 `¥0.099`、缓存未命中约 `¥11.84`、输出约 `¥23.68`；折扣已延长至 `2026-05-31 15:59 UTC`。
- Xiaomi MiMo-V2.5-Pro 使用官方海外 API 的 `<=256K` tokens 档并换算为人民币约价：缓存命中约 `¥1.36`、输入约 `¥6.81`、输出约 `¥20.42`。同一官方页面列出 `256K` 到 `1M` tokens 档：缓存命中约 `¥2.72`、输入 `¥13.61`、输出 `¥40.84`。缓存写入当前限时免费。小米官方中国区价格表中同档为缓存命中 `¥1.40`、输入 `¥7.00`、输出 `¥21.00`。
- Kimi K2.6 使用官方 `kimi-k2.6` 价格并换算为人民币约价：缓存命中约 `¥1.09`、缓存未命中约 `¥6.47`、输出约 `¥27.22`；上下文长度为 `262,144` tokens，支持自动上下文缓存。
- Gemini 3.1 Pro 使用官方 `gemini-3.1-pro-preview` 付费 Standard 档，且 prompt 不超过 `200K` tokens，换算为人民币约价：缓存命中约 `¥1.36`、输入约 `¥13.61`、输出约 `¥81.67`。超过 `200K` tokens 时，Google 列出的价格约为缓存命中 `¥2.72`、输入 `¥27.22`、输出 `¥122.51`；上下文缓存存储费约为 `¥30.63 / 1M tokens / 小时`。
- OpenAI GPT-5.4 和 GPT-5.5 使用 Standard 短上下文价格。长上下文表中，GPT-5.4 为输入 `¥34.03`、缓存输入 `¥3.40`、输出 `¥153.14`；GPT-5.5 为输入 `¥68.06`、缓存输入 `¥6.81`、输出 `¥306.27`。区域处理另加 `10%`。
- Anthropic Claude 使用标准 Claude API 全球路由价格。缓存命中为基础输入价格的 `0.1x`；5 分钟缓存写入为基础输入价格的 `1.25x`，1 小时缓存写入为 `2x`。US-only inference 另加 `1.1x`。Sonnet 4.6、Opus 4.6 和 Opus 4.7 的完整 `1M` token 上下文窗口按标准价格计费。Opus 4.7 使用新 tokenizer，同样固定文本可能多消耗最多 `35%` tokens。
- Z.AI 将 GLM-5.1 的 cached input storage 标为限时免费；本比较只纳入 cached input read 价格。
- 除非特别说明，本比较不包含 Batch、Flex、Priority、fast mode、数据驻留、联网/工具调用费用、session runtime、企业折扣等变体。

## 访问过的价格网址

- OpenAI pricing: https://developers.openai.com/api/docs/pricing
- Anthropic pricing: https://platform.claude.com/docs/en/about-claude/pricing
- DeepSeek pricing: https://api-docs.deepseek.com/quick_start/pricing
- Z.AI pricing: https://docs.z.ai/guides/overview/pricing
- Kimi K2.6 pricing: https://platform.kimi.ai/docs/pricing/chat-k26
- Xiaomi MiMo pricing: https://platform.xiaomimimo.com/static/docs/pricing.md
- Gemini API pricing: https://ai.google.dev/gemini-api/docs/pricing
- USD/CNY reference: https://currencylive.com/exchange-rate/usd-to-cny-exchange-rate-today/
