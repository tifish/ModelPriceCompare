# Model Token Price Comparison

[English](README.md) | [中文](README.zh-CN.md)

Generated: 2026-09-12

All prices are normalized to USD per 1M tokens. Multipliers use the cheapest model in each price category as `1.00x`; in this model set, Xiaomi MiMo-V2.5 is the baseline in all three categories (USD 0.0028 cache hit, 0.14 input, and 0.28 output).

| Model | Provider | Input cache hit | Hit x | Input cache miss | Miss x | Output | Output x | Basis |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Xiaomi MiMo-V2.5 | Xiaomi MiMo | $0.0028 | 1.00x | $0.14 | 1.00x | $0.28 | 1.00x | Overseas API V2.5 reduced price |
| DeepSeek V4.1 Flash (off-peak) | DeepSeek | $0.003 | 1.07x | $0.15 | 1.07x | $0.6 | 2.14x | Standard API off-peak |
| Xiaomi MiMo-V2.5-Pro | Xiaomi MiMo | $0.0036 | 1.29x | $0.435 | 3.11x | $0.87 | 3.11x | Overseas API V2.5 reduced price |
| DeepSeek V4.1 Flash (peak) | DeepSeek | $0.006 | 2.14x | $0.3 | 2.14x | $1.2 | 4.29x | Standard API peak |
| GPT-5.4 Nano | OpenAI | $0.02 | 7.14x | $0.2 | 1.43x | $1.25 | 4.46x | Standard API short context |
| GPT-5.6 Luna (short context) | OpenAI | $0.02 | 7.14x | $0.2 | 1.43x | $1.2 | 4.29x | Standard API <=272K input tokens |
| DeepSeek V4 Pro (off-peak) | DeepSeek | $0.022 | 7.86x | $0.66 | 4.71x | $1.98 | 7.07x | Standard API off-peak |
| Gemini 3.1 Flash-Lite | Google | $0.025 | 8.93x | $0.25 | 1.79x | $1.5 | 5.36x | Standard paid tier text/image/video |
| GLM-5.3-Flash | Z.AI | $0.03 | 10.71x | $0.15 | 1.07x | $0.50 | 1.79x | Standard API list price |
| Gemini 3.5 Flash-Lite | Google | $0.03 | 10.71x | $0.3 | 2.14x | $2.5 | 8.93x | Standard paid tier text/image/video/audio |
| GPT-5.6 Luna (long context) | OpenAI | $0.04 | 14.29x | $0.4 | 2.86x | $1.8 | 6.43x | Standard API >272K input tokens |
| DeepSeek V4 Pro (peak) | DeepSeek | $0.044 | 15.71x | $1.32 | 9.43x | $3.96 | 14.14x | Standard API peak |
| GPT-5.4 Mini | OpenAI | $0.075 | 26.79x | $0.75 | 5.36x | $4.5 | 16.07x | Standard API short context |
| Gemini 3.6 Flash | Google | $0.075 | 26.79x | $0.75 | 5.36x | $3.75 | 13.39x | Standard paid tier promotional price through 2026-12-31 |
| Gemini 3.7 Flash | Google | $0.075 | 26.79x | $0.75 | 5.36x | $3.75 | 13.39x | Standard paid tier promotional price through 2026-12-31 |
| Gemini 3.8 Flash | Google | $0.075 | 26.79x | $0.75 | 5.36x | $3.75 | 13.39x | Standard paid tier introductory price through 2026-12-31 |
| Gemini 3.5 Flash | Google | $0.15 | 53.57x | $1.5 | 10.71x | $9 | 32.14x | Standard paid tier |
| Kimi K2.6 | Moonshot AI / Kimi | $0.16 | 57.14x | $0.95 | 6.79x | $4 | 14.29x | unverified - previous Standard API |
| Kimi K2.7 Code | Moonshot AI / Kimi | $0.19 | 67.86x | $0.95 | 6.79x | $4 | 14.29x | unverified - previous Standard API |
| GLM-5 | Z.AI | $0.2 | 71.43x | $1 | 7.14x | $3.2 | 11.43x | Standard API |
| Claude Sonnet 5 | Anthropic | $0.2 | 71.43x | $2 | 14.29x | $10 | 35.71x | Standard Claude API global routing |
| GPT-5.6 Terra (short context) | OpenAI | $0.2 | 71.43x | $2 | 14.29x | $12 | 42.86x | Standard API <=272K input tokens |
| Gemini 3.1 Pro Preview (<=200K prompts) | Google | $0.2 | 71.43x | $2 | 14.29x | $12 | 42.86x | Standard paid tier <=200K prompts |
| GLM-5-Turbo | Z.AI | $0.24 | 85.71x | $1.2 | 8.57x | $4 | 14.29x | unverified - previous Standard API |
| GPT-5.4 (short context) | OpenAI | $0.25 | 89.29x | $2.5 | 17.86x | $15 | 53.57x | Standard API <=272K input tokens |
| Claude Fable 5.1 | Anthropic | $0.25 | 89.29x | $10 | 71.43x | $50 | 178.57x | Standard Claude API global routing |
| Claude Mythos 5.1 | Anthropic | $0.25 | 89.29x | $10 | 71.43x | $50 | 178.57x | Standard Claude API global routing |
| GLM-5.1 | Z.AI | $0.26 | 92.86x | $1.4 | 10.00x | $4.4 | 15.71x | Standard API |
| GLM-5.2 | Z.AI | $0.26 | 92.86x | $1.4 | 10.00x | $4.4 | 15.71x | Standard API |
| GLM-5.3 | Z.AI | $0.26 | 92.86x | $1.4 | 10.00x | $4.4 | 15.71x | Standard API |
| Kimi K3 | Moonshot AI / Kimi | $0.3 | 107.14x | $3 | 21.43x | $15 | 53.57x | unverified - previous Standard API |
| Kimi K2.7 Code HighSpeed | Moonshot AI / Kimi | $0.38 | 135.71x | $1.9 | 13.57x | $8 | 28.57x | unverified - previous HighSpeed API |
| GPT-5.6 Sol (short context) | OpenAI | $0.4 | 142.86x | $4 | 28.57x | $20 | 71.43x | Standard API promotional price <=272K input tokens |
| GPT-5.6 Terra (long context) | OpenAI | $0.4 | 142.86x | $4 | 28.57x | $18 | 64.29x | Standard API >272K input tokens |
| Gemini 3.1 Pro Preview (>200K prompts) | Google | $0.4 | 142.86x | $4 | 28.57x | $18 | 64.29x | Standard paid tier >200K prompts |
| Claude Opus 4.7 | Anthropic | $0.5 | 178.57x | $5 | 35.71x | $25 | 89.29x | Standard Claude API global routing |
| Claude Opus 4.8 | Anthropic | $0.5 | 178.57x | $5 | 35.71x | $25 | 89.29x | Standard Claude API global routing |
| Claude Opus 5 | Anthropic | $0.5 | 178.57x | $5 | 35.71x | $25 | 89.29x | Standard Claude API global routing |
| GPT-5.4 (long context) | OpenAI | $0.5 | 178.57x | $5 | 35.71x | $22.5 | 80.36x | Standard API >272K input tokens |
| GPT-5.5 (short context) | OpenAI | $0.5 | 178.57x | $5 | 35.71x | $30 | 107.14x | Standard API <=272K input tokens |
| GPT-5.6 Sol (long context) | OpenAI | $0.8 | 285.71x | $8 | 57.14x | $30 | 107.14x | Standard API promotional price >272K input tokens |
| Claude Fable 5 | Anthropic | $1 | 357.14x | $10 | 71.43x | $50 | 178.57x | Standard Claude API global routing |
| Claude Mythos 5 | Anthropic | $1 | 357.14x | $10 | 71.43x | $50 | 178.57x | Standard Claude API global routing limited availability |
| GPT-5.5 (long context) | OpenAI | $1 | 357.14x | $10 | 71.43x | $45 | 160.71x | Standard API >272K input tokens |
| GPT-6 Astra (short context) | OpenAI | $1 | 357.14x | $10 | 71.43x | $50 | 178.57x | Standard API <=272K input tokens |
| GPT-6 Astra (long context) | OpenAI | $2 | 714.29x | $20 | 142.86x | $75 | 267.86x | Standard API >272K input tokens |

## Important Notes

- Rechecked official sources on 2026-09-12: No confirmed token-price changes or eligible new models were found. DeepSeek canceled the planned September 14 V4 Pro routing change and will continue its API service with unchanged billing. Kimi pages still omit pricing tables and GLM-5-Turbo is absent from Z.AI pricing; these five rows retain previous values marked `unverified`.
- User-requested version floors: exclude Z.AI/GLM models below 5, Claude models below 4.7, Google Gemini models below 3.1, OpenAI models below 5.4, and Kimi models below 2.6.
- Excluded discovered entries: OpenAI chat-latest and Daybreak aliases, gpt-5.3-codex below the OpenAI version floor, OpenAI gpt-5.4-pro and gpt-5.5-pro without cache prices, the specialized OpenAI gpt-5.6-cyber model, OpenAI image/audio/video/transcription/deep-research/tool rows, deprecated or retired Claude rows, Claude Mythos Preview invitation-only row without a separate pricing-table entry, retired DeepSeek V4 Flash Vision Exp alias, Z.AI free/text rows without cached-input prices, Z.AI vision/image/audio/video/tool/agent rows, Gemini Omni Flash and Gemini Omni Flash Preview without a comparable cache-hit text price, Gemini 3 Flash Preview below the Gemini version floor, Gemini live/audio/TTS/image-generation models, Kimi Moonshot V1 rows without cache-hit prices, Kimi promotions and vouchers, deprecated Xiaomi MiMo legacy names, and image/audio/video/tool-only pricing.
- USD/CNY reference rate for the Chinese README is `1 USD = 6.7108 CNY`, from the Federal Reserve H.10 current release for `2026-09-04`, published `2026-09-08`.
- DeepSeek V4.1 Flash uses `deepseek-flash`: cache-hit/input/output USD `0.003/0.15/0.60` off-peak and `0.006/0.30/1.20` peak per 1M tokens. Retired `deepseek-v4-flash` and `deepseek-v4-flash-vision-exp` aliases now use this model and price. DeepSeek has canceled the previously announced September 14 routing change: V4 Pro API service and billing will continue unchanged after `2026-09-14`, with further notice if anything changes. Current peak hours are Monday-Friday `01:00-04:00` and `06:00-10:00 UTC`; all other hours are off-peak.
- Xiaomi MiMo-V2.5 and MiMo-V2.5-Pro use the official overseas API V2.5 prices. Domestic pricing is noted in the CSV; cache writing is currently free for a limited time. Legacy V2 model names were auto-routed to V2.5 pricing on staggered dates and have been deprecated since `2026-06-30`. The Xiaomi pricing page shows update time `2026-08-06`.
- Kimi K3, K2.6, K2.7 Code, and K2.7 Code HighSpeed use their official per-model pricing pages and support automatic context caching. Kimi K3 has a `1,048,576` token context window; the K2.x models have `262,144` tokens. Promotions and vouchers are excluded from token unit prices.
- Gemini 3.1 Flash-Lite, Gemini 3.5 Flash-Lite, Gemini 3.5 Flash, Gemini 3.6 Flash, Gemini 3.7 Flash, and Gemini 3.8 Flash use official Standard paid prices. Gemini 3.6 Flash, Gemini 3.7 Flash, and Gemini 3.8 Flash currently share an input/cache-hit/output price of USD `0.75/0.075/3.75` through `2026-12-31`; the regular USD `1.50/0.15/7.50` price starts `2027-01-01`. Gemini 3.1 Pro uses the official `gemini-3.1-pro-preview` paid Standard tier, split into separate rows for prompts up to `200K` tokens and prompts over `200K` tokens. Gemini cache storage, Batch, Flex, Priority, Google Search, Maps grounding, live, TTS, and image-generation charges are excluded.
- OpenAI GPT-5.4, GPT-5.5, and GPT-5.6 use direct Standard pricing. GPT-5.4, GPT-5.5, GPT-5.6 Luna, GPT-5.6 Terra, and GPT-5.6 Sol base rows are split into short-context and long-context rows at the `272K` input-token threshold; GPT-5.4 Mini and Nano list only short-context Standard pricing. GPT-5.6 Sol's current promotional Standard price is available at least through `2026-11-21`. Batch, Flex, and Fast mode variants are excluded. Regional processing adds a `10%` uplift.
- Anthropic Claude prices above use the standard Claude API with global routing. Claude Opus 5 is generally available with the official API ID `claude-opus-5`, a `1M` token context window, and `128K` max output. Claude Sonnet 5's launch price of USD 2 input, USD 0.20 cache hit, and USD 10 output per 1M tokens is now its standard price; Anthropic canceled the previously scheduled 2026-09-01 increase. Claude Fable 5 and Fable 5.1 are generally available; Claude Mythos 5 and Mythos 5.1 are limited availability through Project Glasswing. Cache writes, US-only inference, cloud marketplace pricing, and fast mode premiums are not folded into the main table. Opus 4.7 and later Opus models, Claude Fable 5, Claude Mythos 5, and Claude Sonnet 5 use newer tokenizers.
- GLM-5.3-Flash promotional pricing ended at `2026-09-09 24:00 UTC+8`; current list prices are USD `0.03/0.15/0.50` per 1M tokens.
- Z.AI lists cached input storage as limited-time free for the included GLM text models; only cached input read price is included in the comparison.
- Unless noted, Batch, Flex, Fast mode, data residency, web/tool charges, session runtime, cache storage, cache writes, free tiers, promotions, vouchers, and provider-specific enterprise discounts are excluded.

## Price URLs Visited

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
