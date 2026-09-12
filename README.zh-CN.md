# 模型 Token 价格比较（人民币）

[English](README.md) | [中文](README.zh-CN.md)

生成日期：2026-09-12

所有价格统一为人民币约价 / 1M tokens。主表统一采用海外 API 美元价格，按 `1 USD = 6.7108 CNY` 近似换算。倍率按每个价格类别分别计算，以该类别中最便宜的模型作为 `1.00x`；在本次模型列表中，Xiaomi MiMo-V2.5 是三个类别的基准（美元缓存命中 0.0028、输入 0.14、输出 0.28）。

| 模型 | 提供方 | 输入缓存命中 | 命中倍率 | 输入缓存未命中 | 未命中倍率 | 输出 | 输出倍率 | 价格口径 |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Xiaomi MiMo-V2.5 | Xiaomi MiMo | ¥0.02 | 1.00x | ¥0.94 | 1.00x | ¥1.88 | 1.00x | Overseas API V2.5 reduced price |
| DeepSeek V4.1 Flash (off-peak) | DeepSeek | ¥0.02 | 1.07x | ¥1.01 | 1.07x | ¥4.03 | 2.14x | Standard API off-peak |
| Xiaomi MiMo-V2.5-Pro | Xiaomi MiMo | ¥0.02 | 1.29x | ¥2.92 | 3.11x | ¥5.84 | 3.11x | Overseas API V2.5 reduced price |
| DeepSeek V4.1 Flash (peak) | DeepSeek | ¥0.04 | 2.14x | ¥2.01 | 2.14x | ¥8.05 | 4.29x | Standard API peak |
| GPT-5.4 Nano | OpenAI | ¥0.13 | 7.14x | ¥1.34 | 1.43x | ¥8.39 | 4.46x | Standard API short context |
| GPT-5.6 Luna（短上下文） | OpenAI | ¥0.13 | 7.14x | ¥1.34 | 1.43x | ¥8.05 | 4.29x | Standard API <=272K input tokens |
| DeepSeek V4 Pro (off-peak) | DeepSeek | ¥0.15 | 7.86x | ¥4.43 | 4.71x | ¥13.29 | 7.07x | Standard API off-peak |
| Gemini 3.1 Flash-Lite | Google | ¥0.17 | 8.93x | ¥1.68 | 1.79x | ¥10.07 | 5.36x | Standard paid tier text/image/video |
| GLM-5.3-Flash | Z.AI | ¥0.20 | 10.71x | ¥1.01 | 1.07x | ¥3.36 | 1.79x | Standard API list price |
| Gemini 3.5 Flash-Lite | Google | ¥0.20 | 10.71x | ¥2.01 | 2.14x | ¥16.78 | 8.93x | Standard paid tier text/image/video/audio |
| GPT-5.6 Luna（长上下文） | OpenAI | ¥0.27 | 14.29x | ¥2.68 | 2.86x | ¥12.08 | 6.43x | Standard API >272K input tokens |
| DeepSeek V4 Pro (peak) | DeepSeek | ¥0.30 | 15.71x | ¥8.86 | 9.43x | ¥26.57 | 14.14x | Standard API peak |
| GPT-5.4 Mini | OpenAI | ¥0.50 | 26.79x | ¥5.03 | 5.36x | ¥30.20 | 16.07x | Standard API short context |
| Gemini 3.6 Flash | Google | ¥0.50 | 26.79x | ¥5.03 | 5.36x | ¥25.17 | 13.39x | Standard paid tier promotional price through 2026-12-31 |
| Gemini 3.7 Flash | Google | ¥0.50 | 26.79x | ¥5.03 | 5.36x | ¥25.17 | 13.39x | Standard paid tier promotional price through 2026-12-31 |
| Gemini 3.8 Flash | Google | ¥0.50 | 26.79x | ¥5.03 | 5.36x | ¥25.17 | 13.39x | Standard paid tier introductory price through 2026-12-31 |
| Gemini 3.5 Flash | Google | ¥1.01 | 53.57x | ¥10.07 | 10.71x | ¥60.40 | 32.14x | Standard paid tier |
| Kimi K2.6 | Moonshot AI / Kimi | ¥1.07 | 57.14x | ¥6.38 | 6.79x | ¥26.84 | 14.29x | unverified - previous Standard API |
| Kimi K2.7 Code | Moonshot AI / Kimi | ¥1.28 | 67.86x | ¥6.38 | 6.79x | ¥26.84 | 14.29x | unverified - previous Standard API |
| GLM-5 | Z.AI | ¥1.34 | 71.43x | ¥6.71 | 7.14x | ¥21.47 | 11.43x | Standard API |
| Claude Sonnet 5 | Anthropic | ¥1.34 | 71.43x | ¥13.42 | 14.29x | ¥67.11 | 35.71x | Standard Claude API global routing |
| GPT-5.6 Terra（短上下文） | OpenAI | ¥1.34 | 71.43x | ¥13.42 | 14.29x | ¥80.53 | 42.86x | Standard API <=272K input tokens |
| Gemini 3.1 Pro Preview (<=200K prompts) | Google | ¥1.34 | 71.43x | ¥13.42 | 14.29x | ¥80.53 | 42.86x | Standard paid tier <=200K prompts |
| GLM-5-Turbo | Z.AI | ¥1.61 | 85.71x | ¥8.05 | 8.57x | ¥26.84 | 14.29x | unverified - previous Standard API |
| GPT-5.4（短上下文） | OpenAI | ¥1.68 | 89.29x | ¥16.78 | 17.86x | ¥100.66 | 53.57x | Standard API <=272K input tokens |
| Claude Fable 5.1 | Anthropic | ¥1.68 | 89.29x | ¥67.11 | 71.43x | ¥335.54 | 178.57x | Standard Claude API global routing |
| Claude Mythos 5.1 | Anthropic | ¥1.68 | 89.29x | ¥67.11 | 71.43x | ¥335.54 | 178.57x | Standard Claude API global routing |
| GLM-5.1 | Z.AI | ¥1.74 | 92.86x | ¥9.40 | 10.00x | ¥29.53 | 15.71x | Standard API |
| GLM-5.2 | Z.AI | ¥1.74 | 92.86x | ¥9.40 | 10.00x | ¥29.53 | 15.71x | Standard API |
| GLM-5.3 | Z.AI | ¥1.74 | 92.86x | ¥9.40 | 10.00x | ¥29.53 | 15.71x | Standard API |
| Kimi K3 | Moonshot AI / Kimi | ¥2.01 | 107.14x | ¥20.13 | 21.43x | ¥100.66 | 53.57x | unverified - previous Standard API |
| Kimi K2.7 Code HighSpeed | Moonshot AI / Kimi | ¥2.55 | 135.71x | ¥12.75 | 13.57x | ¥53.69 | 28.57x | unverified - previous HighSpeed API |
| GPT-5.6 Sol（短上下文） | OpenAI | ¥2.68 | 142.86x | ¥26.84 | 28.57x | ¥134.22 | 71.43x | Standard API promotional price <=272K input tokens |
| GPT-5.6 Terra（长上下文） | OpenAI | ¥2.68 | 142.86x | ¥26.84 | 28.57x | ¥120.79 | 64.29x | Standard API >272K input tokens |
| Gemini 3.1 Pro Preview (>200K prompts) | Google | ¥2.68 | 142.86x | ¥26.84 | 28.57x | ¥120.79 | 64.29x | Standard paid tier >200K prompts |
| Claude Opus 4.7 | Anthropic | ¥3.36 | 178.57x | ¥33.55 | 35.71x | ¥167.77 | 89.29x | Standard Claude API global routing |
| Claude Opus 4.8 | Anthropic | ¥3.36 | 178.57x | ¥33.55 | 35.71x | ¥167.77 | 89.29x | Standard Claude API global routing |
| Claude Opus 5 | Anthropic | ¥3.36 | 178.57x | ¥33.55 | 35.71x | ¥167.77 | 89.29x | Standard Claude API global routing |
| GPT-5.4（长上下文） | OpenAI | ¥3.36 | 178.57x | ¥33.55 | 35.71x | ¥150.99 | 80.36x | Standard API >272K input tokens |
| GPT-5.5（短上下文） | OpenAI | ¥3.36 | 178.57x | ¥33.55 | 35.71x | ¥201.32 | 107.14x | Standard API <=272K input tokens |
| GPT-5.6 Sol（长上下文） | OpenAI | ¥5.37 | 285.71x | ¥53.69 | 57.14x | ¥201.32 | 107.14x | Standard API promotional price >272K input tokens |
| Claude Fable 5 | Anthropic | ¥6.71 | 357.14x | ¥67.11 | 71.43x | ¥335.54 | 178.57x | Standard Claude API global routing |
| Claude Mythos 5 | Anthropic | ¥6.71 | 357.14x | ¥67.11 | 71.43x | ¥335.54 | 178.57x | Standard Claude API global routing limited availability |
| GPT-5.5（长上下文） | OpenAI | ¥6.71 | 357.14x | ¥67.11 | 71.43x | ¥301.99 | 160.71x | Standard API >272K input tokens |
| GPT-6 Astra（短上下文） | OpenAI | ¥6.71 | 357.14x | ¥67.11 | 71.43x | ¥335.54 | 178.57x | Standard API <=272K input tokens |
| GPT-6 Astra（长上下文） | OpenAI | ¥13.42 | 714.29x | ¥134.22 | 142.86x | ¥503.31 | 267.86x | Standard API >272K input tokens |

## 重要说明

- 本次于 2026-09-12 复核官方来源：未发现已确认的 token 单价变化或符合纳入规则的新模型。DeepSeek 已取消原定 9 月 14 日的 V4 Pro 路由切换，将继续提供 API 服务并维持计费方式。Kimi 页面仍未返回价格表，GLM-5-Turbo 未出现在当前 Z.AI 价格表中；这五行保留旧值并标为 `unverified`（待核验）。
- 用户指定的版本下限：排除 5 以下的 Z.AI/GLM 模型、4.7 以下的 Claude 模型、3.1 以下的 Google Gemini 模型、5.4 以下的 OpenAI 模型，以及 2.6 以下的 Kimi 模型。
- 已排除的发现项：OpenAI chat-latest 与 Daybreak 别名、低于 OpenAI 版本下限的 gpt-5.3-codex、缺少缓存价格的 OpenAI gpt-5.4-pro 和 gpt-5.5-pro、专用网络安全模型 gpt-5.6-cyber、OpenAI 图像/音频/视频/转录/deep research/工具行、已废弃或退役 Claude 行、没有单独价格表行的邀请制 Claude Mythos Preview、已退役的 DeepSeek V4 Flash Vision Exp 别名、Z.AI 免费或缺少缓存命中价格的文本行、Z.AI 视觉/图像/音频/视频/工具/agent 行、缺少可比缓存命中文本价格的 Gemini Omni Flash 与 Gemini Omni Flash Preview、低于 Gemini 版本下限的 Gemini 3 Flash Preview、Gemini live/audio/TTS/图像生成模型、缺少缓存命中价格的 Kimi Moonshot V1 行、Kimi 促销和代金券、已退役的小米 MiMo V2 旧模型名，以及仅图像/音频/视频/工具计费项。
- 汇率采用近似值 `1 USD = 6.7108 CNY`。该汇率取自 Federal Reserve H.10 current release 中 `2026-09-04` 的 CHINA, P.R. YUAN 数据，发布时间为 `2026-09-08`；实际账单以服务商结算币种和付款时汇率为准。
- DeepSeek V4.1 Flash 使用官方 ID `deepseek-flash`。低谷缓存命中/输入/输出为 USD `0.003/0.15/0.60`，高峰为 `0.006/0.30/1.20` / 1M tokens。旧 `deepseek-v4-flash` 和 `deepseek-v4-flash-vision-exp` 已退役，其别名请求由 V4.1 Flash 服务并按新价计费。DeepSeek 已取消此前宣布的 9 月 14 日路由切换：`2026-09-14` 之后仍继续提供 V4 Pro API 服务，计费方式不变；后续变化将另行公告。官方当前高峰时段为周一至周五 UTC `01:00-04:00`、`06:00-10:00`，其余时间均为低谷。
- Xiaomi MiMo-V2.5 和 MiMo-V2.5-Pro 使用官方海外 API V2.5 价格。国内价格已写入 CSV 备注；缓存写入当前限时免费。V2 旧模型名已分批自动路由到 V2.5 价格，并已自 `2026-06-30` 起退役。小米价格页显示更新时间为 `2026-08-06`。
- Kimi K3、K2.6、K2.7 Code 和 K2.7 Code HighSpeed 使用各自官方模型价格页，并支持自动上下文缓存。Kimi K3 的上下文窗口为 `1,048,576` tokens；K2.x 模型为 `262,144` tokens。促销和代金券不折入 token 单价。
- Gemini 3.1 Flash-Lite、Gemini 3.5 Flash-Lite、Gemini 3.5 Flash、Gemini 3.6 Flash、Gemini 3.7 Flash 和 Gemini 3.8 Flash 使用官方付费 Standard 价格。Gemini 3.6 Flash、Gemini 3.7 Flash 与 Gemini 3.8 Flash 当前共享每 1M tokens USD `0.75/0.075/3.75` 的输入/缓存命中/输出价，有效至 `2026-12-31`；自 `2027-01-01` 起恢复为 USD `1.50/0.15/7.50`。Gemini 3.1 Pro 使用官方 `gemini-3.1-pro-preview` 付费 Standard 档，并按 `200K` prompt tokens 阈值拆成两行。Gemini 的缓存存储、Batch、Flex、Priority、Google Search、Maps grounding、live、TTS 与图像生成计费均未折入主表。
- OpenAI GPT-5.4、GPT-5.5 和 GPT-5.6 使用直接 API Standard 价格。GPT-5.4、GPT-5.5、GPT-5.6 Luna、GPT-5.6 Terra 和 GPT-5.6 Sol 主模型按 `272K` 输入 tokens 阈值拆成短上下文和长上下文行；GPT-5.4 Mini 与 Nano 只列官方短上下文 Standard 价格。GPT-5.6 Sol 当前 Standard 促销价至少持续至 `2026-11-21`。Batch、Flex、Fast mode 未纳入主表；区域处理另加 `10%`。
- Anthropic Claude 使用标准 Claude API 全球路由价格。Claude Opus 5 已公开可用，官方 API ID 为 `claude-opus-5`，上下文窗口为 `1M` tokens，最大输出为 `128K` tokens。Claude Sonnet 5 的首发价（每 1M tokens 输入 USD 2、缓存命中 USD 0.20、输出 USD 10）现已成为标准价；Anthropic 已取消原定于 `2026-09-01` 的涨价。Claude Fable 5 和 Fable 5.1 已公开可用；Claude Mythos 5 和 Mythos 5.1 是 Project Glasswing limited availability。缓存写入、US-only inference、云市场价格和 fast mode premium 未折入主表。Opus 4.7 及更新 Opus、Claude Fable 5、Claude Mythos 5 和 Claude Sonnet 5 使用新版 tokenizer。
- GLM-5.3-Flash 的 50% 促销已于 `2026-09-09 24:00 UTC+8` 结束；当前缓存命中/输入/输出常规价为 USD `0.03/0.15/0.50` / 1M tokens。
- Z.AI 将已纳入的 GLM 文本模型 cached input storage 标为限时免费；本比较只纳入 cached input read 价格。
- 除非特别说明，本比较不包含 Batch、Flex、Fast mode、数据驻留、联网/工具调用费用、session runtime、缓存存储、缓存写入、免费档、促销、代金券和企业折扣等变体。

## 访问过的价格网址

- OpenAI pricing: https://developers.openai.com/api/docs/pricing
- OpenAI gpt-5.4: https://developers.openai.com/api/docs/models/gpt-5.4
- OpenAI gpt-5.4-mini: https://developers.openai.com/api/docs/models/gpt-5.4-mini
- OpenAI gpt-5.4-nano: https://developers.openai.com/api/docs/models/gpt-5.4-nano
- OpenAI gpt-5.5: https://developers.openai.com/api/docs/models/gpt-5.5
- Anthropic pricing: https://platform.claude.com/docs/en/about-claude/pricing
- DeepSeek pricing: https://api-docs.deepseek.com/quick_start/pricing/
- Z.AI pricing: https://docs.z.ai/guides/overview/pricing
- Kimi K3 pricing: https://platform.kimi.ai/docs/pricing/chat-k3
- Kimi K2.6 pricing: https://platform.kimi.ai/docs/pricing/chat-k26
- Kimi K2.7 Code pricing: https://platform.kimi.ai/docs/pricing/chat-k27-code
- Kimi pricing overview: https://platform.kimi.ai/docs/pricing/chat
- Xiaomi MiMo pricing: https://mimo.mi.com/docs/en-US/price/pay-as-you-go
- Gemini API pricing: https://ai.google.dev/gemini-api/docs/pricing
- Claude models overview: https://platform.claude.com/docs/en/about-claude/models/overview
- USD/CNY reference: https://www.federalreserve.gov/releases/h10/current/
