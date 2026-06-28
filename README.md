# Model Token Price Comparison

[English](README.md) | [中文](README.zh-CN.md)

Generated: 2026-06-29

All prices are normalized to USD per 1M tokens. Multipliers use the cheapest model in each price category as `1.00x`; in this model set, DeepSeek V4 Flash and Xiaomi MiMo-V2.5 share the cache-hit input, cache-miss input, and output baselines.

| Model | Provider | Input cache hit | Hit x | Input cache miss | Miss x | Output | Output x | Basis |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| DeepSeek V4 Flash | DeepSeek | $0.0028 | 1.00x | $0.14 | 1.00x | $0.28 | 1.00x | Standard API current |
| Xiaomi MiMo-V2.5 | Xiaomi MiMo | $0.0028 | 1.00x | $0.14 | 1.00x | $0.28 | 1.00x | Overseas API V2.5 reduced price |
| Xiaomi MiMo-V2.5-Pro | Xiaomi MiMo | $0.0036 | 1.29x | $0.435 | 3.11x | $0.87 | 3.11x | Overseas API V2.5 reduced price |
| DeepSeek V4 Pro | DeepSeek | $0.003625 | 1.29x | $0.435 | 3.11x | $0.87 | 3.11x | Standard API current |
| GPT-5.4 Nano | OpenAI | $0.02 | 7.14x | $0.20 | 1.43x | $1.25 | 4.46x | Standard API short context |
| Gemini 3.1 Flash-Lite | Google | $0.025 | 8.93x | $0.25 | 1.79x | $1.50 | 5.36x | Standard paid tier text/image/video |
| GPT-5.4 Mini | OpenAI | $0.075 | 26.79x | $0.75 | 5.36x | $4.50 | 16.07x | Standard API short context |
| Gemini 3.5 Flash | Google | $0.15 | 53.57x | $1.50 | 10.71x | $9.00 | 32.14x | Standard paid tier |
| Kimi K2.6 | Moonshot AI / Kimi | $0.16 | 57.14x | $0.95 | 6.79x | $4.00 | 14.29x | Standard API |
| Kimi K2.7 Code | Moonshot AI / Kimi | $0.19 | 67.86x | $0.95 | 6.79x | $4.00 | 14.29x | Standard API |
| GLM-5 | Z.AI | $0.20 | 71.43x | $1.00 | 7.14x | $3.20 | 11.43x | Standard API |
| Gemini 3.1 Pro Preview (<=200K prompts) | Google | $0.20 | 71.43x | $2.00 | 14.29x | $12.00 | 42.86x | Standard paid tier <=200K prompts |
| GLM-5-Turbo | Z.AI | $0.24 | 85.71x | $1.20 | 8.57x | $4.00 | 14.29x | Standard API |
| GPT-5.4 (short context) | OpenAI | $0.25 | 89.29x | $2.50 | 17.86x | $15.00 | 53.57x | Standard API <=272K input tokens |
| GLM-5.1 | Z.AI | $0.26 | 92.86x | $1.40 | 10.00x | $4.40 | 15.71x | Standard API |
| GLM-5.2 | Z.AI | $0.26 | 92.86x | $1.40 | 10.00x | $4.40 | 15.71x | Standard API |
| Kimi K2.7 Code HighSpeed | Moonshot AI / Kimi | $0.38 | 135.71x | $1.90 | 13.57x | $8.00 | 28.57x | HighSpeed API |
| Gemini 3.1 Pro Preview (>200K prompts) | Google | $0.40 | 142.86x | $4.00 | 28.57x | $18.00 | 64.29x | Standard paid tier >200K prompts |
| Claude Opus 4.7 | Anthropic | $0.50 | 178.57x | $5.00 | 35.71x | $25.00 | 89.29x | Standard Claude API global routing |
| Claude Opus 4.8 | Anthropic | $0.50 | 178.57x | $5.00 | 35.71x | $25.00 | 89.29x | Standard Claude API global routing |
| GPT-5.4 (long context) | OpenAI | $0.50 | 178.57x | $5.00 | 35.71x | $22.50 | 80.36x | Standard API >272K input tokens |
| GPT-5.5 (short context) | OpenAI | $0.50 | 178.57x | $5.00 | 35.71x | $30.00 | 107.14x | Standard API <=272K input tokens |
| Claude Fable 5 | Anthropic | $1.00 | 357.14x | $10.00 | 71.43x | $50.00 | 178.57x | Standard Claude API global routing |
| Claude Mythos 5 | Anthropic | $1.00 | 357.14x | $10.00 | 71.43x | $50.00 | 178.57x | Standard Claude API global routing limited availability |
| GPT-5.5 (long context) | OpenAI | $1.00 | 357.14x | $10.00 | 71.43x | $45.00 | 160.71x | Standard API >272K input tokens |
## Important Notes

- Newly added eligible priced models in this run: none.
- User-requested version floors: exclude Z.AI/GLM models below 5, Claude models below 4.7, Google Gemini models below 3.1, OpenAI models below 5.4, and Kimi models below 2.6.
- Excluded discovered entries: OpenAI chat-latest alias, OpenAI pro/cyber rows without complete comparable cache prices, OpenAI image/audio/video/transcription/deep-research/tool rows, deprecated or retired Claude rows, Z.AI free/text rows without cached-input prices, Z.AI vision/image/audio/video/tool/agent rows, Gemini live/audio/TTS/image-generation models, Kimi Moonshot V1 rows without cache-hit prices, Kimi top-up voucher promotion, Xiaomi MiMo legacy names that auto-route to V2.5 pricing before deprecation, and image/audio/video/tool-only pricing.
- DeepSeek V4 Flash and V4 Pro use the current official `deepseek-v4-flash` and `deepseek-v4-pro` prices. DeepSeek also notes that `deepseek-chat` and `deepseek-reasoner` are compatibility aliases for `deepseek-v4-flash` until deprecation on `2026-07-24 15:59 UTC`.
- Xiaomi MiMo-V2.5 and MiMo-V2.5-Pro use the official overseas API V2.5 prices effective `2026-05-27 00:00` Beijing time. Domestic pricing is noted in the CSV; cache writing is currently free for a limited time. Legacy V2 model names are auto-routed to V2.5 pricing on staggered dates and are scheduled for deprecation at `2026-06-30 00:00` GMT+8.
- Kimi K2.6, K2.7 Code, and K2.7 Code HighSpeed use their official per-model pricing pages. Each has a `262,144` token context window and supports automatic context caching. The current Kimi K2.7 Code launch top-up voucher promotion is excluded from token unit prices.
- Gemini 3.1 Flash-Lite and Gemini 3.5 Flash use official Standard paid text/image/video prices. Gemini 3.1 Pro uses the official `gemini-3.1-pro-preview` paid Standard tier, split into separate rows for prompts up to `200K` tokens and prompts over `200K` tokens. Gemini cache storage, Batch, Flex, Priority, Google Search, Maps grounding, live, audio, TTS, and image-generation charges are excluded.
- OpenAI GPT-5.4 and GPT-5.5 use direct Standard pricing. GPT-5.4 and GPT-5.5 base rows are split into short-context and long-context rows at the `272K` input-token threshold; GPT-5.4 Mini and Nano list only short-context Standard pricing. Batch, Flex, and Priority variants are excluded. Regional processing adds a `10%` uplift.
- Anthropic Claude prices above use the standard Claude API with global routing. Claude Fable 5 is generally available; Claude Mythos 5 is limited availability through Project Glasswing. Cache writes, US-only inference, cloud marketplace pricing, and fast mode premiums are not folded into the main table. Opus 4.7 and later use the newer Opus tokenizer.
- Z.AI lists cached input storage as limited-time free for the included GLM text models; only cached input read price is included in the comparison.
- Unless noted, Batch, Flex, Priority, fast mode, data residency, web/tool charges, session runtime, cache storage, cache writes, free tiers, top-up vouchers, and provider-specific enterprise discounts are excluded.

## Price URLs Visited

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
