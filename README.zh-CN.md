# 模型 Token 价格比较（人民币）

[English](README.md) | [中文](README.zh-CN.md)

生成日期：2026-07-13

所有价格统一为人民币约价 / 1M tokens。除提供方直接列出人民币价格的情况外，美元价格按 `1 USD = 6.7886 CNY` 近似换算。倍率按每个价格类别分别计算，以该类别中最便宜的模型作为 `1.00x`；在本次模型列表中，DeepSeek V4 Flash 和 Xiaomi MiMo-V2.5 共同作为缓存命中输入、缓存未命中输入与输出基准。

| 模型 | 提供方 | 输入缓存命中 | 命中倍率 | 输入缓存未命中 | 未命中倍率 | 输出 | 输出倍率 | 价格口径 |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| DeepSeek V4 Flash | DeepSeek | ¥0.019 | 1.00x | ¥0.95 | 1.00x | ¥1.90 | 1.00x | 当前标准 API |
| Xiaomi MiMo-V2.5 | Xiaomi MiMo | ¥0.019 | 1.00x | ¥0.95 | 1.00x | ¥1.90 | 1.00x | 海外 API，V2.5 降价后价格 |
| Xiaomi MiMo-V2.5-Pro | Xiaomi MiMo | ¥0.024 | 1.29x | ¥2.95 | 3.11x | ¥5.91 | 3.11x | 海外 API，V2.5 降价后价格 |
| DeepSeek V4 Pro | DeepSeek | ¥0.025 | 1.29x | ¥2.95 | 3.11x | ¥5.91 | 3.11x | 当前标准 API |
| GPT-5.4 Nano | OpenAI | ¥0.14 | 7.14x | ¥1.36 | 1.43x | ¥8.49 | 4.46x | 标准 API 短上下文 |
| Gemini 3.1 Flash-Lite | Google | ¥0.17 | 8.93x | ¥1.70 | 1.79x | ¥10.18 | 5.36x | 付费 Standard，文本/图像/视频 |
| GPT-5.4 Mini | OpenAI | ¥0.51 | 26.79x | ¥5.09 | 5.36x | ¥30.55 | 16.07x | 标准 API 短上下文 |
| GPT-5.6 Luna （短上下文） | OpenAI | ¥0.68 | 35.71x | ¥6.79 | 7.14x | ¥40.73 | 21.43x | 标准 API，输入 <=272K tokens |
| Gemini 3.5 Flash | Google | ¥1.02 | 53.57x | ¥10.18 | 10.71x | ¥61.10 | 32.14x | 付费 Standard 档 |
| Kimi K2.6 | Moonshot AI / Kimi | ¥1.09 | 57.14x | ¥6.45 | 6.79x | ¥27.15 | 14.29x | 标准 API |
| Kimi K2.7 Code | Moonshot AI / Kimi | ¥1.29 | 67.86x | ¥6.45 | 6.79x | ¥27.15 | 14.29x | 标准 API |
| GPT-5.6 Luna （长上下文） | OpenAI | ¥1.36 | 71.43x | ¥13.58 | 14.29x | ¥61.10 | 32.14x | 标准 API，输入 >272K tokens |
| GLM-5 | Z.AI | ¥1.36 | 71.43x | ¥6.79 | 7.14x | ¥21.72 | 11.43x | 标准 API |
| Claude Sonnet 5 | Anthropic | ¥1.36 | 71.43x | ¥13.58 | 14.29x | ¥67.89 | 35.71x | Claude API 全球路由，2026-08-31 前介绍价 |
| Gemini 3.1 Pro Preview （<=200K prompts） | Google | ¥1.36 | 71.43x | ¥13.58 | 14.29x | ¥81.46 | 42.86x | 付费 Standard，<=200K prompts 档 |
| GLM-5-Turbo | Z.AI | ¥1.63 | 85.71x | ¥8.15 | 8.57x | ¥27.15 | 14.29x | 标准 API |
| GPT-5.4 （短上下文） | OpenAI | ¥1.70 | 89.29x | ¥16.97 | 17.86x | ¥101.83 | 53.57x | 标准 API，输入 <=272K tokens |
| GPT-5.6 Terra （短上下文） | OpenAI | ¥1.70 | 89.29x | ¥16.97 | 17.86x | ¥101.83 | 53.57x | 标准 API，输入 <=272K tokens |
| GLM-5.1 | Z.AI | ¥1.77 | 92.86x | ¥9.50 | 10.00x | ¥29.87 | 15.71x | 标准 API |
| GLM-5.2 | Z.AI | ¥1.77 | 92.86x | ¥9.50 | 10.00x | ¥29.87 | 15.71x | 标准 API |
| Kimi K2.7 Code HighSpeed | Moonshot AI / Kimi | ¥2.58 | 135.71x | ¥12.90 | 13.57x | ¥54.31 | 28.57x | HighSpeed API |
| Gemini 3.1 Pro Preview （>200K prompts） | Google | ¥2.72 | 142.86x | ¥27.15 | 28.57x | ¥122.19 | 64.29x | 付费 Standard，>200K prompts 档 |
| GPT-5.4 （长上下文） | OpenAI | ¥3.39 | 178.57x | ¥33.94 | 35.71x | ¥152.74 | 80.36x | 标准 API，输入 >272K tokens |
| GPT-5.6 Terra （长上下文） | OpenAI | ¥3.39 | 178.57x | ¥33.94 | 35.71x | ¥152.74 | 80.36x | 标准 API，输入 >272K tokens |
| GPT-5.6 Sol （短上下文） | OpenAI | ¥3.39 | 178.57x | ¥33.94 | 35.71x | ¥203.66 | 107.14x | 标准 API，输入 <=272K tokens |
| Claude Opus 4.7 | Anthropic | ¥3.39 | 178.57x | ¥33.94 | 35.71x | ¥169.72 | 89.29x | Claude API 全球路由 |
| Claude Opus 4.8 | Anthropic | ¥3.39 | 178.57x | ¥33.94 | 35.71x | ¥169.72 | 89.29x | Claude API 全球路由 |
| GPT-5.5 （短上下文） | OpenAI | ¥3.39 | 178.57x | ¥33.94 | 35.71x | ¥203.66 | 107.14x | 标准 API，输入 <=272K tokens |
| GPT-5.5 （长上下文） | OpenAI | ¥6.79 | 357.14x | ¥67.89 | 71.43x | ¥305.49 | 160.71x | 标准 API，输入 >272K tokens |
| GPT-5.6 Sol （长上下文） | OpenAI | ¥6.79 | 357.14x | ¥67.89 | 71.43x | ¥305.49 | 160.71x | 标准 API，输入 >272K tokens |
| Claude Fable 5 | Anthropic | ¥6.79 | 357.14x | ¥67.89 | 71.43x | ¥339.43 | 178.57x | Claude API 全球路由 |
| Claude Mythos 5 | Anthropic | ¥6.79 | 357.14x | ¥67.89 | 71.43x | ¥339.43 | 178.57x | Claude API 全球路由，limited availability |
## 重要说明

- 本次没有新增的合格明确定价模型；GPT-5.6 Luna、GPT-5.6 Terra 和 GPT-5.6 Sol 继续保留在维护列表中。
- 用户指定的版本下限：排除 5 以下的 Z.AI/GLM 模型、4.7 以下的 Claude 模型、3.1 以下的 Google Gemini 模型、5.4 以下的 OpenAI 模型，以及 2.6 以下的 Kimi 模型。
- 已排除的发现项：OpenAI chat-latest 别名、低于 OpenAI 版本下限的 gpt-5.3-codex、缺少完整可比缓存价格的 OpenAI pro/cyber 行、OpenAI 图像/音频/视频/转录/deep research/工具行、已废弃或退役 Claude 行、没有单独价格表行的邀请制 Claude Mythos Preview、Z.AI 免费或缺少缓存命中价格的文本行、Z.AI 视觉/图像/音频/视频/工具/agent 行、缺少可比缓存命中文本价格的 Gemini Omni Flash Preview、低于 Gemini 版本下限的 Gemini 3 Flash Preview、Gemini live/audio/TTS/图像生成模型、缺少缓存命中价格的 Kimi Moonshot V1 行、Kimi 促销和代金券、已退役的小米 MiMo V2 旧模型名，以及仅图像/音频/视频/工具计费项。
- 汇率采用近似值 `1 USD = 6.7886 CNY`。该汇率取自 Federal Reserve H.10 current release 中 `2026-07-02` 的 CHINA, P.R. YUAN 数据，发布时间为 `2026-07-06`；实际账单以服务商结算币种和付款时汇率为准。
- DeepSeek V4 Flash 和 V4 Pro 使用当前官方 `deepseek-v4-flash`、`deepseek-v4-pro` 价格。DeepSeek 还标注 `deepseek-chat` 和 `deepseek-reasoner` 作为 `deepseek-v4-flash` 兼容别名，将在 `2026-07-24 15:59 UTC` 后废弃。
- Xiaomi MiMo-V2.5 和 MiMo-V2.5-Pro 使用官方海外 API V2.5 价格。国内价格已写入 CSV 备注；缓存写入当前限时免费。V2 旧模型名已分批自动路由到 V2.5 价格，并已自 `2026-06-30` 起退役。小米价格页显示更新时间为 `2026-06-29`。
- Kimi K2.6、K2.7 Code 和 K2.7 Code HighSpeed 使用各自官方模型价格页；上下文窗口均为 `262,144` tokens，并支持自动上下文缓存。促销和代金券不折入 token 单价。
- Gemini 3.1 Flash-Lite 和 Gemini 3.5 Flash 使用官方付费 Standard 文本/图像/视频价格。Gemini 3.1 Pro 使用官方 `gemini-3.1-pro-preview` 付费 Standard 档，并按 `200K` prompt tokens 阈值拆成两行。Gemini 的缓存存储、Batch、Flex、Priority、Google Search、Maps grounding、live、audio、TTS 与图像生成计费均未折入主表。
- OpenAI GPT-5.4、GPT-5.5 和 GPT-5.6 使用直接 API Standard 价格。GPT-5.4、GPT-5.5、GPT-5.6 Luna、GPT-5.6 Terra 和 GPT-5.6 Sol 主模型按 `272K` 输入 tokens 阈值拆成短上下文和长上下文行；GPT-5.4 Mini 与 Nano 只列官方短上下文 Standard 价格。Batch、Flex、Priority 未纳入主表；区域处理另加 `10%`。
- Anthropic Claude 使用标准 Claude API 全球路由价格。Claude Sonnet 5 使用截至 `2026-08-31` 的介绍价，标准价自 `2026-09-01` 起生效。Claude Fable 5 已公开可用；Claude Mythos 5 是 Project Glasswing limited availability。缓存写入、US-only inference、云市场价格和 fast mode premium 未折入主表。Opus 4.7 及更新 Opus、Claude Fable 5、Claude Mythos 5 和 Claude Sonnet 5 使用新版 tokenizer。
- Z.AI 将已纳入的 GLM 文本模型 cached input storage 标为限时免费；本比较只纳入 cached input read 价格。
- 除非特别说明，本比较不包含 Batch、Flex、Priority、fast mode、数据驻留、联网/工具调用费用、session runtime、缓存存储、缓存写入、免费档、促销、代金券和企业折扣等变体。

## 访问过的价格网址

- OpenAI pricing: https://developers.openai.com/api/docs/pricing
- Anthropic pricing: https://platform.claude.com/docs/en/about-claude/pricing
- DeepSeek pricing: https://api-docs.deepseek.com/quick_start/pricing
- Z.AI pricing: https://docs.z.ai/guides/overview/pricing
- Kimi K2.6 pricing: https://platform.kimi.ai/docs/pricing/chat-k26
- Kimi K2.7 Code pricing: https://platform.kimi.ai/docs/pricing/chat-k27-code
- Kimi pricing overview: https://platform.kimi.ai/docs/pricing/chat
- Xiaomi MiMo pricing: https://mimo.mi.com/docs/en-US/price/pay-as-you-go
- Gemini API pricing: https://ai.google.dev/gemini-api/docs/pricing
- Claude models overview: https://platform.claude.com/docs/en/about-claude/models/overview
- USD/CNY reference: https://www.federalreserve.gov/releases/h10/current/
