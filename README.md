# Model Token Price Comparison

[English](README.md) | [中文](README.zh-CN.md)

Generated: 2026-08-28

All prices are normalized to USD per 1M tokens. Multipliers use the cheapest model in each price category as `1.00x`; in this model set, Xiaomi MiMo-V2.5 is the cache-hit input baseline, while GLM-5.3-Flash is the cache-miss input and output baseline.

| Model | Provider | Input cache hit | Hit x | Input cache miss | Miss x | Output | Output x | Basis |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Xiaomi MiMo-V2.5 | Xiaomi MiMo | $0.0028 | 1.00x | $0.14 | 1.87x | $0.28 | 1.12x | Overseas API V2.5 reduced price |
| Xiaomi MiMo-V2.5-Pro | Xiaomi MiMo | $0.0036 | 1.29x | $0.435 | 5.80x | $0.87 | 3.48x | Overseas API V2.5 reduced price |
| DeepSeek V4 Flash (off-peak) | DeepSeek | $0.007 | 2.50x | $0.22 | 2.93x | $0.66 | 2.64x | Standard API off-peak |
| DeepSeek V4 Flash (peak) | DeepSeek | $0.014 | 5.00x | $0.44 | 5.87x | $1.32 | 5.28x | Standard API peak |
| GLM-5.3-Flash | Z.AI | $0.015 | 5.36x | $0.075 | 1.00x | $0.25 | 1.00x | Standard API promotional price through 2026-09-09 |
| GPT-5.4 Nano | OpenAI | $0.02 | 7.14x | $0.20 | 2.67x | $1.25 | 5.00x | Standard API short context |
| GPT-5.6 Luna (short context) | OpenAI | $0.02 | 7.14x | $0.20 | 2.67x | $1.20 | 4.80x | Standard API <=272K input tokens |
| DeepSeek V4 Pro (off-peak) | DeepSeek | $0.022 | 7.86x | $0.66 | 8.80x | $1.98 | 7.92x | Standard API off-peak |
| Gemini 3.1 Flash-Lite | Google | $0.025 | 8.93x | $0.25 | 3.33x | $1.50 | 6.00x | Standard paid tier text/image/video |
| Gemini 3.5 Flash-Lite | Google | $0.03 | 10.71x | $0.30 | 4.00x | $2.50 | 10.00x | Standard paid tier text/image/video/audio |
| GPT-5.6 Luna (long context) | OpenAI | $0.04 | 14.29x | $0.40 | 5.33x | $1.80 | 7.20x | Standard API >272K input tokens |
| DeepSeek V4 Pro (peak) | DeepSeek | $0.044 | 15.71x | $1.32 | 17.60x | $3.96 | 15.84x | Standard API peak |
| GPT-5.4 Mini | OpenAI | $0.075 | 26.79x | $0.75 | 10.00x | $4.50 | 18.00x | Standard API short context |
| Gemini 3.6 Flash | Google | $0.075 | 26.79x | $0.75 | 10.00x | $3.75 | 15.00x | Standard paid tier promotional price through 2026-12-31 |
| Gemini 3.7 Flash | Google | $0.075 | 26.79x | $0.75 | 10.00x | $3.75 | 15.00x | Standard paid tier promotional price through 2026-12-31 |
| Gemini 3.5 Flash | Google | $0.15 | 53.57x | $1.50 | 20.00x | $9.00 | 36.00x | Standard paid tier |
| Kimi K2.6 | Moonshot AI / Kimi | $0.16 | 57.14x | $0.95 | 12.67x | $4.00 | 16.00x | Standard API |
| Kimi K2.7 Code | Moonshot AI / Kimi | $0.19 | 67.86x | $0.95 | 12.67x | $4.00 | 16.00x | Standard API |
| GPT-5.6 Terra (short context) | OpenAI | $0.20 | 71.43x | $2.00 | 26.67x | $12.00 | 48.00x | Standard API <=272K input tokens |
| GLM-5 | Z.AI | $0.20 | 71.43x | $1.00 | 13.33x | $3.20 | 12.80x | Standard API |
| Claude Sonnet 5 | Anthropic | $0.20 | 71.43x | $2.00 | 26.67x | $10.00 | 40.00x | Standard Claude API global routing |
| Gemini 3.1 Pro Preview (<=200K prompts) | Google | $0.20 | 71.43x | $2.00 | 26.67x | $12.00 | 48.00x | Standard paid tier <=200K prompts |
| GLM-5-Turbo | Z.AI | $0.24 | 85.71x | $1.20 | 16.00x | $4.00 | 16.00x | Standard API |
| GPT-5.4 (short context) | OpenAI | $0.25 | 89.29x | $2.50 | 33.33x | $15.00 | 60.00x | Standard API <=272K input tokens |
| GLM-5.1 | Z.AI | $0.26 | 92.86x | $1.40 | 18.67x | $4.40 | 17.60x | Standard API |
| GLM-5.2 | Z.AI | $0.26 | 92.86x | $1.40 | 18.67x | $4.40 | 17.60x | Standard API |
| GLM-5.3 | Z.AI | $0.26 | 92.86x | $1.40 | 18.67x | $4.40 | 17.60x | Standard API |
| Kimi K3 | Moonshot AI / Kimi | $0.30 | 107.14x | $3.00 | 40.00x | $15.00 | 60.00x | Standard API |
| Kimi K2.7 Code HighSpeed | Moonshot AI / Kimi | $0.38 | 135.71x | $1.90 | 25.33x | $8.00 | 32.00x | HighSpeed API |
| GPT-5.6 Terra (long context) | OpenAI | $0.40 | 142.86x | $4.00 | 53.33x | $18.00 | 72.00x | Standard API >272K input tokens |
| Gemini 3.1 Pro Preview (>200K prompts) | Google | $0.40 | 142.86x | $4.00 | 53.33x | $18.00 | 72.00x | Standard paid tier >200K prompts |
| GPT-5.6 Sol (short context) | OpenAI | $0.40 | 142.86x | $4.00 | 53.33x | $20.00 | 80.00x | Standard API promotional price <=272K input tokens |
| GPT-5.4 (long context) | OpenAI | $0.50 | 178.57x | $5.00 | 66.67x | $22.50 | 90.00x | Standard API >272K input tokens |
| Claude Opus 4.7 | Anthropic | $0.50 | 178.57x | $5.00 | 66.67x | $25.00 | 100.00x | Standard Claude API global routing |
| Claude Opus 4.8 | Anthropic | $0.50 | 178.57x | $5.00 | 66.67x | $25.00 | 100.00x | Standard Claude API global routing |
| Claude Opus 5 | Anthropic | $0.50 | 178.57x | $5.00 | 66.67x | $25.00 | 100.00x | Standard Claude API global routing |
| GPT-5.5 (short context) | OpenAI | $0.50 | 178.57x | $5.00 | 66.67x | $30.00 | 120.00x | Standard API <=272K input tokens |
| GPT-5.6 Sol (long context) | OpenAI | $0.80 | 285.71x | $8.00 | 106.67x | $30.00 | 120.00x | Standard API promotional price >272K input tokens |
| GPT-5.5 (long context) | OpenAI | $1.00 | 357.14x | $10.00 | 133.33x | $45.00 | 180.00x | Standard API >272K input tokens |
| Claude Fable 5 | Anthropic | $1.00 | 357.14x | $10.00 | 133.33x | $50.00 | 200.00x | Standard Claude API global routing |
| Claude Mythos 5 | Anthropic | $1.00 | 357.14x | $10.00 | 133.33x | $50.00 | 200.00x | Standard Claude API global routing limited availability |
## Important Notes

- Rechecked the official pricing and current-model pages. Added the newly eligible Z.AI GLM-5.3-Flash at its current 50% promotional cache hit/input/output prices of USD `0.015/0.075/0.25` per 1M tokens through `2026-09-09 24:00 UTC+8`; its list prices are USD `0.03/0.15/0.50`. OpenAI GPT-5.6 Sol Standard pricing remains promotional at least through `2026-11-21`: short-context cache hit/input/output are USD `0.40/4.00/20.00`, and long-context prices are USD `0.80/8.00/30.00` per 1M tokens.
- User-requested version floors: exclude Z.AI/GLM models below 5, Claude models below 4.7, Google Gemini models below 3.1, OpenAI models below 5.4, and Kimi models below 2.6.
- Excluded discovered entries: OpenAI chat-latest and Daybreak aliases, gpt-5.3-codex below the OpenAI version floor, OpenAI gpt-5.4-pro and gpt-5.5-pro without cache prices, the specialized OpenAI gpt-5.6-cyber model, OpenAI image/audio/video/transcription/deep-research/tool rows, deprecated or retired Claude rows, Claude Mythos Preview invitation-only row without a separate pricing-table entry, DeepSeek V4 Flash Vision Exp, Z.AI free/text rows without cached-input prices, Z.AI vision/image/audio/video/tool/agent rows, Gemini Omni Flash Preview without a comparable cache-hit text price, Gemini 3 Flash Preview below the Gemini version floor, Gemini live/audio/TTS/image-generation models, Kimi Moonshot V1 rows without cache-hit prices, Kimi promotions and vouchers, deprecated Xiaomi MiMo legacy names, and image/audio/video/tool-only pricing.
- USD/CNY reference rate for the Chinese README is `1 USD = 6.7210 CNY`, from the Federal Reserve H.10 current release for `2026-08-21`, published `2026-08-24`.
- DeepSeek V4 Flash and V4 Pro use the current official `deepseek-v4-flash` and `deepseek-v4-pro` prices. They currently route to DeepSeek-V4-Flash-0731 and DeepSeek-V4-Pro-0813, respectively. DeepSeek notes that the `deepseek-chat` and `deepseek-reasoner` compatibility aliases were deprecated on `2026-07-24 15:59 UTC`. Peak/off-peak billing took effect on `2026-08-16 16:00 UTC`: peak hours are `01:00-04:00` and `06:00-10:00 UTC`, with V4 Flash cache hit/input/output at USD `0.014/0.44/1.32` peak and `0.007/0.22/0.66` off-peak, and V4 Pro at USD `0.044/1.32/3.96` peak and `0.022/0.66/1.98` off-peak per 1M tokens. From `2026-08-23 00:00` Beijing time, off-peak pricing applies all day on Saturdays and Sundays (Beijing time). Both current price tiers are listed separately in the main table.
- Xiaomi MiMo-V2.5 and MiMo-V2.5-Pro use the official overseas API V2.5 prices. Domestic pricing is noted in the CSV; cache writing is currently free for a limited time. Legacy V2 model names were auto-routed to V2.5 pricing on staggered dates and have been deprecated since `2026-06-30`. The Xiaomi pricing page shows update time `2026-08-06`.
- Kimi K3, K2.6, K2.7 Code, and K2.7 Code HighSpeed use their official per-model pricing pages and support automatic context caching. Kimi K3 has a `1,048,576` token context window; the K2.x models have `262,144` tokens. Promotions and vouchers are excluded from token unit prices.
- Gemini 3.1 Flash-Lite, Gemini 3.5 Flash-Lite, Gemini 3.5 Flash, Gemini 3.6 Flash, and Gemini 3.7 Flash use official Standard paid prices. Gemini 3.6 Flash and Gemini 3.7 Flash currently share an input/cache-hit/output price of USD `0.75/0.075/3.75` through `2026-12-31`; the regular USD `1.50/0.15/7.50` price starts `2027-01-01`. Gemini 3.1 Pro uses the official `gemini-3.1-pro-preview` paid Standard tier, split into separate rows for prompts up to `200K` tokens and prompts over `200K` tokens. Gemini cache storage, Batch, Flex, Priority, Google Search, Maps grounding, live, TTS, and image-generation charges are excluded.
- OpenAI GPT-5.4, GPT-5.5, and GPT-5.6 use direct Standard pricing. GPT-5.4, GPT-5.5, GPT-5.6 Luna, GPT-5.6 Terra, and GPT-5.6 Sol base rows are split into short-context and long-context rows at the `272K` input-token threshold; GPT-5.4 Mini and Nano list only short-context Standard pricing. GPT-5.6 Sol's current promotional Standard price is available at least through `2026-11-21`. Batch, Flex, and Fast mode variants are excluded. Regional processing adds a `10%` uplift.
- Anthropic Claude prices above use the standard Claude API with global routing. Claude Opus 5 is generally available with the official API ID `claude-opus-5`, a `1M` token context window, and `128K` max output. Claude Sonnet 5's launch price of USD 2 input, USD 0.20 cache hit, and USD 10 output per 1M tokens is now its standard price; Anthropic canceled the previously scheduled 2026-09-01 increase. Claude Fable 5 is generally available; Claude Mythos 5 is limited availability through Project Glasswing. Cache writes, US-only inference, cloud marketplace pricing, and fast mode premiums are not folded into the main table. Opus 4.7 and later Opus models, Claude Fable 5, Claude Mythos 5, and Claude Sonnet 5 use newer tokenizers.
- Z.AI lists cached input storage as limited-time free for the included GLM text models; only cached input read price is included in the comparison.
- Unless noted, Batch, Flex, Fast mode, data residency, web/tool charges, session runtime, cache storage, cache writes, free tiers, promotions, vouchers, and provider-specific enterprise discounts are excluded.

## Price URLs Visited

- OpenAI pricing: https://developers.openai.com/api/docs/pricing
- Anthropic pricing: https://platform.claude.com/docs/en/about-claude/pricing
- DeepSeek pricing: https://api-docs.deepseek.com/quick_start/pricing
- Z.AI pricing: https://docs.z.ai/guides/overview/pricing
- Kimi K3 pricing: https://platform.kimi.ai/docs/pricing/chat-k3
- Kimi K2.6 pricing: https://platform.kimi.ai/docs/pricing/chat-k26
- Kimi K2.7 Code pricing: https://platform.kimi.ai/docs/pricing/chat-k27-code
- Kimi pricing overview: https://platform.kimi.ai/docs/pricing/chat
- Xiaomi MiMo pricing: https://mimo.mi.com/docs/en-US/price/pay-as-you-go
- Gemini API pricing: https://ai.google.dev/gemini-api/docs/pricing
- Claude models overview: https://platform.claude.com/docs/en/about-claude/models/overview
- USD/CNY reference: https://www.federalreserve.gov/releases/h10/current/
