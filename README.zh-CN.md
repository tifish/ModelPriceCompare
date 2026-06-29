# 模型 Token 价格比较（人民币）

[English](README.md) | [中文](README.zh-CN.md)

生成日期：2026-06-30

所有价格统一为人民币约价 / 1M tokens。除提供方直接列出人民币价格的情况外，美元价格按 `1 USD = 6.7686 CNY` 近似换算。倍率按每个价格类别分别计算，以该类别中最便宜的模型作为 `1.00x`；在本次模型列表中，DeepSeek V4 Flash 和 Xiaomi MiMo-V2.5 共同作为缓存命中输入与输出基准，GPT-5.4 Nano 作为缓存未命中输入基准。

| 模型 | 提供方 | 输入缓存命中 | 命中倍率 | 输入缓存未命中 | 未命中倍率 | 输出 | 输出倍率 | 价格口径 |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| DeepSeek V4 Flash | DeepSeek | ¥0.019 | 1.00x | ¥0.95 | 1.40x | ¥1.90 | 1.00x | 当前标准 API |
| Xiaomi MiMo-V2.5 | Xiaomi MiMo | ¥0.019 | 1.00x | ¥0.95 | 1.40x | ¥1.90 | 1.00x | 海外 API，V2.5 降价后价格 |
| Xiaomi MiMo-V2.5-Pro | Xiaomi MiMo | ¥0.024 | 1.29x | ¥2.94 | 4.35x | ¥5.89 | 3.11x | 海外 API，V2.5 降价后价格 |
| DeepSeek V4 Pro | DeepSeek | ¥0.025 | 1.29x | ¥2.94 | 4.35x | ¥5.89 | 3.11x | 当前标准 API |
| GPT-5.4 Nano | OpenAI | ¥0.068 | 3.57x | ¥0.68 | 1.00x | ¥4.23 | 2.23x | 标准 API 短上下文 |
| Gemini 3.1 Flash-Lite | Google | ¥0.17 | 8.93x | ¥1.69 | 2.50x | ¥10.15 | 5.36x | 付费 Standard，文本/图像/视频 |
| GPT-5.4 Mini | OpenAI | ¥0.25 | 13.39x | ¥2.54 | 3.75x | ¥15.23 | 8.04x | 标准 API 短上下文 |
| GPT-5.4（短上下文） | OpenAI | ¥0.88 | 46.43x | ¥8.46 | 12.50x | ¥50.76 | 26.79x | 标准 API，输入 <=272K tokens |
| Kimi K2.6 | Moonshot AI / Kimi | ¥1.08 | 57.14x | ¥6.43 | 9.50x | ¥27.07 | 14.29x | 标准 API |
| Kimi K2.7 Code | Moonshot AI / Kimi | ¥1.29 | 67.86x | ¥6.43 | 9.50x | ¥27.07 | 14.29x | 标准 API |
| GLM-5 | Z.AI | ¥1.35 | 71.43x | ¥6.77 | 10.00x | ¥21.66 | 11.43x | 标准 API |
| Gemini 3.1 Pro Preview（<=200K prompts） | Google | ¥1.35 | 71.43x | ¥13.54 | 20.00x | ¥81.22 | 42.86x | 付费 Standard，<=200K prompts 档 |
| GLM-5-Turbo | Z.AI | ¥1.62 | 85.71x | ¥8.12 | 12.00x | ¥27.07 | 14.29x | 标准 API |
| GPT-5.4（长上下文） | OpenAI | ¥1.69 | 89.29x | ¥16.92 | 25.00x | ¥76.15 | 40.18x | 标准 API，输入 >272K tokens |
| GPT-5.5（短上下文） | OpenAI | ¥1.69 | 89.29x | ¥16.92 | 25.00x | ¥101.53 | 53.57x | 标准 API，输入 <=272K tokens |
| GLM-5.1 | Z.AI | ¥1.76 | 92.86x | ¥9.48 | 14.00x | ¥29.78 | 15.71x | 标准 API |
| GLM-5.2 | Z.AI | ¥1.76 | 92.86x | ¥9.48 | 14.00x | ¥29.78 | 15.71x | 标准 API |
| Gemini 3.5 Flash | Google | ¥1.83 | 96.43x | ¥18.28 | 27.00x | ¥109.65 | 57.86x | 付费 Standard 档 |
| Kimi K2.7 Code HighSpeed | Moonshot AI / Kimi | ¥2.57 | 135.71x | ¥12.86 | 19.00x | ¥54.15 | 28.57x | HighSpeed API |
| Gemini 3.1 Pro Preview（>200K prompts） | Google | ¥2.71 | 142.86x | ¥27.07 | 40.00x | ¥121.83 | 64.29x | 付费 Standard，>200K prompts 档 |
| Claude Opus 4.7 | Anthropic | ¥3.38 | 178.57x | ¥33.84 | 50.00x | ¥169.22 | 89.29x | Claude API 全球路由 |
| Claude Opus 4.8 | Anthropic | ¥3.38 | 178.57x | ¥33.84 | 50.00x | ¥169.22 | 89.29x | Claude API 全球路由 |
| GPT-5.5（长上下文） | OpenAI | ¥3.38 | 178.57x | ¥33.84 | 50.00x | ¥152.29 | 80.36x | 标准 API，输入 >272K tokens |
| Claude Fable 5 | Anthropic | ¥6.77 | 357.14x | ¥67.69 | 100.00x | ¥338.43 | 178.57x | Claude API 全球路由 |
| Claude Mythos 5 | Anthropic | ¥6.77 | 357.14x | ¥67.69 | 100.00x | ¥338.43 | 178.57x | Claude API 全球路由，limited availability |
## 重要说明

- 本次新增的合格明确定价模型：无。
- 用户指定的版本下限：排除 5 以下的 Z.AI/GLM 模型、4.7 以下的 Claude 模型、3.1 以下的 Google Gemini 模型、5.4 以下的 OpenAI 模型，以及 2.6 以下的 Kimi 模型。
- 已排除的发现项：OpenAI chat-latest 别名、缺少完整可比缓存价格的 OpenAI pro/cyber 行、OpenAI 图像/音频/视频/转录/deep research/工具行、已废弃或退役 Claude 行、Z.AI 免费或缺少缓存命中价格的文本行、Z.AI 视觉/图像/音频/视频/工具/agent 行、Gemini live/audio/TTS/图像生成模型、缺少缓存命中价格的 Kimi Moonshot V1 行、Kimi 充值代金券活动、自动路由到 V2.5 价格且即将退役的小米 MiMo V2 旧模型名，以及仅图像/音频/视频/工具计费项。
- 汇率采用近似值 `1 USD = 6.7686 CNY`。该汇率取自 Federal Reserve H.10 current release 中 `2026-06-18` 的 CHINA, P.R. YUAN 数据，发布时间为 `2026-06-22`；实际账单以服务商结算币种和付款时汇率为准。
- DeepSeek V4 Flash 和 V4 Pro 使用当前官方 `deepseek-v4-flash`、`deepseek-v4-pro` 价格。DeepSeek 还标注 `deepseek-chat` 和 `deepseek-reasoner` 作为 `deepseek-v4-flash` 兼容别名，将在 `2026-07-24 15:59 UTC` 后废弃。
- Xiaomi MiMo-V2.5 和 MiMo-V2.5-Pro 使用官方海外 API 在北京时间 `2026-05-27 00:00` 生效的 V2.5 降价后价格。国内价格已写入 CSV 备注；缓存写入当前限时免费。V2 旧模型名会分批自动路由到 V2.5 价格，并计划在 GMT+8 `2026-06-30 00:00` 正式退役。
- Kimi K2.6、K2.7 Code 和 K2.7 Code HighSpeed 使用各自官方模型价格页；上下文窗口均为 `262,144` tokens，并支持自动上下文缓存。当前 Kimi K2.7 Code 发布期充值代金券活动不折入 token 单价。
- Gemini 3.1 Flash-Lite 和 Gemini 3.5 Flash 使用官方付费 Standard 文本/图像/视频价格。Gemini 3.1 Pro 使用官方 `gemini-3.1-pro-preview` 付费 Standard 档，并按 `200K` prompt tokens 阈值拆成两行。本次刷新中 Gemini 3.5 Flash 价格发生变化。Gemini 的缓存存储、Batch、Flex、Priority、Google Search、Maps grounding、live、audio、TTS 与图像生成计费均未折入主表。
- OpenAI GPT-5.4 和 GPT-5.5 使用直接 API Standard 价格；本次刷新中官方列出的 Standard 价格发生变化。GPT-5.4 与 GPT-5.5 主模型按 `272K` 输入 tokens 阈值拆成短上下文和长上下文行；GPT-5.4 Mini 与 Nano 只列官方短上下文 Standard 价格。Batch、Flex、Priority 未纳入主表；区域处理另加 `10%`。
- Anthropic Claude 使用标准 Claude API 全球路由价格。Claude Fable 5 已公开可用；Claude Mythos 5 是 Project Glasswing limited availability。缓存写入、US-only inference、云市场价格和 fast mode premium 未折入主表。Opus 4.7 及更新模型使用新版 Opus tokenizer。
- Z.AI 将已纳入的 GLM 文本模型 cached input storage 标为限时免费；本比较只纳入 cached input read 价格。
- 除非特别说明，本比较不包含 Batch、Flex、Priority、fast mode、数据驻留、联网/工具调用费用、session runtime、缓存存储、缓存写入、免费档、充值代金券和企业折扣等变体。

## 访问过的价格网址

- OpenAI pricing: https://developers.openai.com/api/docs/pricing
- Anthropic pricing: https://platform.claude.com/docs/en/about-claude/pricing
- DeepSeek pricing: https://api-docs.deepseek.com/quick_start/pricing
- Z.AI pricing: https://docs.z.ai/guides/overview/pricing
- Kimi K2.6 pricing: https://platform.kimi.ai/docs/pricing/chat-k26
- Kimi K2.7 Code pricing: https://platform.kimi.ai/docs/pricing/chat-k27-code
- Kimi promotion: https://platform.kimi.ai/docs/pricing/promotion
- Xiaomi MiMo pricing: https://mimo.mi.com/docs/en-US/price/pay-as-you-go
- Gemini API pricing: https://ai.google.dev/gemini-api/docs/pricing
- Claude models overview: https://platform.claude.com/docs/en/about-claude/models/overview
- USD/CNY reference: https://www.federalreserve.gov/releases/h10/current/
