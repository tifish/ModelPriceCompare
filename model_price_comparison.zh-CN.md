# 模型 Token 价格比较（人民币）

[English](model_price_comparison.md) | [中文](model_price_comparison.zh-CN.md)

生成日期：2026-06-08

所有价格统一为人民币约价 / 1M tokens。除提供方直接列出人民币价格的情况外，美元价格按 `1 USD = 6.7764 CNY` 近似换算。倍率按每个价格类别分别计算，以该类别中最便宜的模型作为 `1.00x`；在本次模型列表中，DeepSeek V4 Flash 在缓存未命中输入、缓存命中输入、输出三个类别中都是基准。

| 模型 | 提供方 | 输入缓存未命中 | 未命中倍率 | 输入缓存命中 | 命中倍率 | 输出 | 输出倍率 | 价格口径 |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| DeepSeek V4 Flash | DeepSeek | ¥0.95 | 1.00x | ¥0.019 | 1.00x | ¥1.90 | 1.00x | 当前标准 API |
| DeepSeek V4 Pro | DeepSeek | ¥2.95 | 3.11x | ¥0.025 | 1.29x | ¥5.90 | 3.11x | 当前标准 API |
| Xiaomi MiMo-V2.5-Pro | Xiaomi MiMo | ¥2.95 | 3.11x | ¥0.024 | 1.29x | ¥5.90 | 3.11x | 海外 API，V2.5 降价后价格 |
| Kimi K2.6 | Moonshot AI / Kimi | ¥6.44 | 6.79x | ¥1.08 | 57.14x | ¥27.11 | 14.29x | 标准 API |
| GPT-5.4（短上下文） | OpenAI | ¥8.47 | 8.93x | ¥0.88 | 46.43x | ¥50.82 | 26.79x | 标准 API，输入 <=272K tokens |
| GLM-5.1 | Z.AI | ¥9.49 | 10.00x | ¥1.76 | 92.86x | ¥29.82 | 15.71x | 标准 API |
| Gemini 3.1 Pro Preview（<=200K prompts） | Google | ¥13.55 | 14.29x | ¥1.36 | 71.43x | ¥81.32 | 42.86x | 付费 Standard，<=200K prompts 档 |
| GPT-5.4（长上下文） | OpenAI | ¥16.94 | 17.86x | ¥1.69 | 89.29x | ¥76.23 | 40.18x | 标准 API，输入 >272K tokens |
| GPT-5.5（短上下文） | OpenAI | ¥16.94 | 17.86x | ¥1.69 | 89.29x | ¥101.65 | 53.57x | 标准 API，输入 <=272K tokens |
| Claude Sonnet 4.6 | Anthropic | ¥20.33 | 21.43x | ¥2.03 | 107.14x | ¥101.65 | 53.57x | Claude API 全球路由 |
| Gemini 3.1 Pro Preview（>200K prompts） | Google | ¥27.11 | 28.57x | ¥2.71 | 142.86x | ¥121.98 | 64.29x | 付费 Standard，>200K prompts 档 |
| GPT-5.5（长上下文） | OpenAI | ¥33.88 | 35.71x | ¥3.39 | 178.57x | ¥152.47 | 80.36x | 标准 API，输入 >272K tokens |
| Claude Opus 4.8 | Anthropic | ¥33.88 | 35.71x | ¥3.39 | 178.57x | ¥169.41 | 89.29x | Claude API 全球路由 |

## 重要说明

- 汇率采用近似值 `1 USD = 6.7764 CNY`。该汇率取自 Exchange-Rates.org 在 `2026-06-07 18:45 UTC` 给出的 USD/CNY 汇率；实际账单以服务商结算币种和付款时汇率为准。
- DeepSeek V4 Flash 和 V4 Pro 使用当前官方 `deepseek-v4-flash`、`deepseek-v4-pro` 价格。DeepSeek 还标注 `deepseek-chat` 和 `deepseek-reasoner` 作为 `deepseek-v4-flash` 兼容别名，将在 `2026-07-24 15:59 UTC` 后废弃。
- Xiaomi MiMo-V2.5-Pro 使用官方海外 API 在北京时间 `2026-05-27 00:00` 生效的 V2.5 降价后价格：缓存命中 `$0.0036`、缓存未命中 `$0.435`、输出 `$0.87`。国内价格为缓存命中 `¥0.025`、缓存未命中 `¥3.00`、输出 `¥6.00`。缓存写入当前限时免费。
- Kimi K2.6 使用官方 `kimi-k2.6` 价格：缓存命中 `$0.16`、缓存未命中 `$0.95`、输出 `$4.00`；上下文窗口为 `262,144` tokens，支持自动上下文缓存。
- Gemini 3.1 Pro 使用官方 `gemini-3.1-pro-preview` 付费 Standard 档，并按 `200K` prompt tokens 阈值拆成两行。上下文缓存存储费为 `$4.50 / 1M tokens / 小时`，未折入 token 价格。
- OpenAI GPT-5.4 和 GPT-5.5 按 Standard 短上下文价格和超过 `272K` 输入 tokens 的 full-session 长上下文价格拆成独立行。区域处理另加 `10%`。
- Anthropic Claude 使用标准 Claude API 全球路由价格。缓存命中和刷新为基础输入价格的 `0.1x`；5 分钟缓存写入为基础输入价格的 `1.25x`，1 小时缓存写入为 `2x`。US-only inference 另加 `1.1x`。Claude Opus 4.8 和 Claude Sonnet 4.6 的完整 `1M` token 上下文窗口按标准价格计费。Opus 4.8 使用新版 Opus tokenizer，并提供高价 fast mode；二者都未折入主表。
- Z.AI 将 GLM-5.1 的 cached input storage 标为限时免费；本比较只纳入 cached input read 价格。
- 除非特别说明，本比较不包含 Batch、Flex、Priority、fast mode、数据驻留、联网/工具调用费用、session runtime、企业折扣等变体。

## 访问过的价格网址

- OpenAI pricing: https://developers.openai.com/api/docs/pricing
- Anthropic pricing: https://platform.claude.com/docs/en/about-claude/pricing
- DeepSeek pricing: https://api-docs.deepseek.com/quick_start/pricing
- Z.AI pricing: https://docs.z.ai/guides/overview/pricing
- Kimi K2.6 pricing: https://platform.kimi.ai/docs/pricing/chat-k26
- Xiaomi MiMo pricing: https://platform.xiaomimimo.com/docs/en-US/price/pay-as-you-go
- Gemini API pricing: https://ai.google.dev/gemini-api/docs/pricing
- USD/CNY reference: https://www.exchange-rates.org/converter/usd-cny
