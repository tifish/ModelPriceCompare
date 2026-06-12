# 模型 Token 价格比较（人民币）

[English](README.md) | [中文](README.zh-CN.md)

生成日期：2026-06-13

所有价格统一为人民币约价 / 1M tokens。除提供方直接列出人民币价格的情况外，美元价格按 `1 USD = 6.7760 CNY` 近似换算。倍率按每个价格类别分别计算，以该类别中最便宜的模型作为 `1.00x`；在本次模型列表中，GLM-4.7-FlashX 是缓存未命中输入基准，DeepSeek V4 Flash 和 Xiaomi MiMo-V2.5 共同作为缓存命中输入与输出基准。

| 模型 | 提供方 | 输入缓存未命中 | 未命中倍率 | 输入缓存命中 | 命中倍率 | 输出 | 输出倍率 | 价格口径 |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| GLM-4.7-FlashX | Z.AI | ¥0.47 | 1.00x | ¥0.068 | 3.57x | ¥2.71 | 1.43x | 标准 API |
| DeepSeek V4 Flash | DeepSeek | ¥0.95 | 2.00x | ¥0.019 | 1.00x | ¥1.90 | 1.00x | 当前标准 API |
| Xiaomi MiMo-V2.5 | Xiaomi MiMo | ¥0.95 | 2.00x | ¥0.019 | 1.00x | ¥1.90 | 1.00x | 海外 API，V2.5 降价后价格 |
| GPT-5.4 Nano | OpenAI | ¥1.36 | 2.86x | ¥0.14 | 7.14x | ¥8.47 | 4.46x | 标准 API 短上下文 |
| GLM-4.5-Air | Z.AI | ¥1.36 | 2.86x | ¥0.20 | 10.71x | ¥7.45 | 3.93x | 标准 API |
| Gemini 3.1 Flash-Lite | Google | ¥1.69 | 3.57x | ¥0.17 | 8.93x | ¥10.16 | 5.36x | 付费 Standard，文本/图像/视频 |
| DeepSeek V4 Pro | DeepSeek | ¥2.95 | 6.21x | ¥0.025 | 1.29x | ¥5.90 | 3.11x | 当前标准 API |
| Xiaomi MiMo-V2.5-Pro | Xiaomi MiMo | ¥2.95 | 6.21x | ¥0.024 | 1.29x | ¥5.90 | 3.11x | 海外 API，V2.5 降价后价格 |
| Kimi K2.5 | Moonshot AI / Kimi | ¥4.07 | 8.57x | ¥0.68 | 35.71x | ¥20.33 | 10.71x | 标准 API |
| GLM-4.5 | Z.AI | ¥4.07 | 8.57x | ¥0.75 | 39.29x | ¥14.91 | 7.86x | 标准 API |
| GLM-4.6 | Z.AI | ¥4.07 | 8.57x | ¥0.75 | 39.29x | ¥14.91 | 7.86x | 标准 API |
| GLM-4.7 | Z.AI | ¥4.07 | 8.57x | ¥0.75 | 39.29x | ¥14.91 | 7.86x | 标准 API |
| GPT-5.4 Mini | OpenAI | ¥5.08 | 10.71x | ¥0.51 | 26.79x | ¥30.49 | 16.07x | 标准 API 短上下文 |
| Kimi K2.6 | Moonshot AI / Kimi | ¥6.44 | 13.57x | ¥1.08 | 57.14x | ¥27.10 | 14.29x | 标准 API |
| Kimi K2.7 Code | Moonshot AI / Kimi | ¥6.44 | 13.57x | ¥1.29 | 67.86x | ¥27.10 | 14.29x | 标准 API |
| Claude Haiku 4.5 | Anthropic | ¥6.78 | 14.29x | ¥0.68 | 35.71x | ¥33.88 | 17.86x | Claude API 全球路由 |
| GLM-5 | Z.AI | ¥6.78 | 14.29x | ¥1.36 | 71.43x | ¥21.68 | 11.43x | 标准 API |
| GLM-4.5-AirX | Z.AI | ¥7.45 | 15.71x | ¥1.49 | 78.57x | ¥30.49 | 16.07x | 标准 API |
| GLM-5-Turbo | Z.AI | ¥8.13 | 17.14x | ¥1.63 | 85.71x | ¥27.10 | 14.29x | 标准 API |
| GLM-5.1 | Z.AI | ¥9.49 | 20.00x | ¥1.76 | 92.86x | ¥29.81 | 15.71x | 标准 API |
| Gemini 3.5 Flash | Google | ¥10.16 | 21.43x | ¥1.02 | 53.57x | ¥60.98 | 32.14x | 付费 Standard 档 |
| Gemini 3.1 Pro Preview（<=200K prompts） | Google | ¥13.55 | 28.57x | ¥1.36 | 71.43x | ¥81.31 | 42.86x | 付费 Standard，<=200K prompts 档 |
| GLM-4.5-X | Z.AI | ¥14.91 | 31.43x | ¥3.05 | 160.71x | ¥60.31 | 31.79x | 标准 API |
| GPT-5.4（短上下文） | OpenAI | ¥16.94 | 35.71x | ¥1.69 | 89.29x | ¥101.64 | 53.57x | 标准 API，输入 <=272K tokens |
| Claude Sonnet 4.5 | Anthropic | ¥20.33 | 42.86x | ¥2.03 | 107.14x | ¥101.64 | 53.57x | Claude API 全球路由 |
| Claude Sonnet 4.6 | Anthropic | ¥20.33 | 42.86x | ¥2.03 | 107.14x | ¥101.64 | 53.57x | Claude API 全球路由 |
| Gemini 3.1 Pro Preview（>200K prompts） | Google | ¥27.10 | 57.14x | ¥2.71 | 142.86x | ¥121.97 | 64.29x | 付费 Standard，>200K prompts 档 |
| Claude Opus 4.5 | Anthropic | ¥33.88 | 71.43x | ¥3.39 | 178.57x | ¥169.40 | 89.29x | Claude API 全球路由 |
| Claude Opus 4.6 | Anthropic | ¥33.88 | 71.43x | ¥3.39 | 178.57x | ¥169.40 | 89.29x | Claude API 全球路由 |
| Claude Opus 4.7 | Anthropic | ¥33.88 | 71.43x | ¥3.39 | 178.57x | ¥169.40 | 89.29x | Claude API 全球路由 |
| Claude Opus 4.8 | Anthropic | ¥33.88 | 71.43x | ¥3.39 | 178.57x | ¥169.40 | 89.29x | Claude API 全球路由 |
| GPT-5.4（长上下文） | OpenAI | ¥33.88 | 71.43x | ¥3.39 | 178.57x | ¥152.46 | 80.36x | 标准 API，输入 >272K tokens |
| GPT-5.5（短上下文） | OpenAI | ¥33.88 | 71.43x | ¥3.39 | 178.57x | ¥203.28 | 107.14x | 标准 API，输入 <=272K tokens |
| Claude Fable 5 | Anthropic | ¥67.76 | 142.86x | ¥6.78 | 357.14x | ¥338.80 | 178.57x | Claude API 全球路由 |
| Claude Mythos 5 | Anthropic | ¥67.76 | 142.86x | ¥6.78 | 357.14x | ¥338.80 | 178.57x | Claude API 全球路由，limited availability |
| GPT-5.5（长上下文） | OpenAI | ¥67.76 | 142.86x | ¥6.78 | 357.14x | ¥304.92 | 160.71x | 标准 API，输入 >272K tokens |

## 重要说明

- 本次新增的合格明确定价模型：GPT-5.4 Nano、GPT-5.4 Mini、Claude Haiku 4.5、Claude Sonnet 4.5、Claude Opus 4.5、Claude Opus 4.6、Claude Opus 4.7、GLM-5、GLM-5-Turbo、GLM-4.7、GLM-4.7-FlashX、GLM-4.6、GLM-4.5、GLM-4.5-X、GLM-4.5-Air、GLM-4.5-AirX、Gemini 3.5 Flash、Gemini 3.1 Flash-Lite、Kimi K2.5、Xiaomi MiMo-V2.5。
- 已排除的发现项：缺少缓存命中价格的 OpenAI pro 行、已废弃或退役 Claude 行、Z.AI 免费或缺少缓存命中价格的文本行、Gemini live/audio 模型、缺少缓存命中价格的 Kimi Moonshot V1 行、小米 MiMo 旧别名，以及仅图像/音频/视频/工具计费项。
- 汇率采用近似值 `1 USD = 6.7760 CNY`。该汇率取自 Exchange-Rates.org 在 `2026-06-12 17:10 UTC` 给出的 USD/CNY 汇率；实际账单以服务商结算币种和付款时汇率为准。
- DeepSeek V4 Flash 和 V4 Pro 使用当前官方 `deepseek-v4-flash`、`deepseek-v4-pro` 价格。DeepSeek 还标注 `deepseek-chat` 和 `deepseek-reasoner` 作为 `deepseek-v4-flash` 兼容别名，将在 `2026-07-24 15:59 UTC` 后废弃。
- Xiaomi MiMo-V2.5 和 MiMo-V2.5-Pro 使用官方海外 API 在北京时间 `2026-05-27 00:00` 生效的 V2.5 降价后价格。国内价格已写入 CSV 备注；缓存写入当前限时免费。
- Kimi K2.5、K2.6、K2.7 Code 使用各自官方模型价格页；上下文窗口均为 `262,144` tokens，并支持自动上下文缓存。
- Gemini 3.1 Pro 使用官方 `gemini-3.1-pro-preview` 付费 Standard 档，并按 `200K` prompt tokens 阈值拆成两行。Gemini 的缓存存储、Batch、Flex、Priority、Google Search、Maps grounding、live 与音频专属计费均未折入主表。
- OpenAI GPT-5.4 和 GPT-5.5 使用直接 API Standard 价格。GPT-5.4 与 GPT-5.5 主模型按 `272K` 输入 tokens 阈值拆成短上下文和长上下文行；GPT-5.4 Mini 与 Nano 只列官方短上下文 Standard 价格。Batch、Flex、Priority 未纳入主表；区域处理另加 `10%`。
- Anthropic Claude 使用标准 Claude API 全球路由价格。Claude Fable 5 已公开可用；Claude Mythos 5 是 Project Glasswing limited availability。缓存写入、US-only inference、云市场价格和 fast mode premium 未折入主表。Opus 4.7 及更新模型使用新版 Opus tokenizer。
- Z.AI 将已纳入的 GLM 文本模型 cached input storage 标为限时免费；本比较只纳入 cached input read 价格。
- 除非特别说明，本比较不包含 Batch、Flex、Priority、fast mode、数据驻留、联网/工具调用费用、session runtime、缓存存储、缓存写入、免费档和企业折扣等变体。

## 访问过的价格网址

- OpenAI pricing: https://developers.openai.com/api/docs/pricing
- Anthropic pricing: https://platform.claude.com/docs/en/about-claude/pricing
- DeepSeek pricing: https://api-docs.deepseek.com/quick_start/pricing
- Z.AI pricing: https://docs.z.ai/guides/overview/pricing
- Kimi K2.5 pricing: https://platform.kimi.ai/docs/pricing/chat-k25
- Kimi K2.6 pricing: https://platform.kimi.ai/docs/pricing/chat-k26
- Kimi K2.7 Code pricing: https://platform.kimi.ai/docs/pricing/chat-k27-code
- Xiaomi MiMo pricing: https://platform.xiaomimimo.com/docs/en-US/price/pay-as-you-go
- Gemini API pricing: https://ai.google.dev/gemini-api/docs/pricing
- Claude models overview: https://platform.claude.com/docs/en/about-claude/models/overview
- USD/CNY reference: https://www.exchange-rates.org/converter/usd-cny
