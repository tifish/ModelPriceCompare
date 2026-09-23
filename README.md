# Model Token Price Comparison

[English](README.md) | [中文](README.zh-CN.md)

Generated: 2026-09-24

All prices are normalized to USD per 1M tokens. Multipliers use the cheapest model in each price category as `1.00x`: Xiaomi MiMo-V2.5 and MiMo-V2.6-Flash share the cache-hit and output baselines (USD 0.0028 and 0.28), while GPT-6 Luna (short context) is the input baseline (USD 0.10).

| Provider | Model | Hit x | Input cache hit | Miss x | Input cache miss | Output x | Output | Basis |
|---|---|---:|---:|---:|---:|---:|---:|---|
| OpenAI | GPT-6 Astra (long context) | 714.29x | $2 | 200.00x | $20 | 267.86x | $75 | Standard API >272K input tokens |
| xAI | Grok 4.7 (long context) | 357.14x | $1 | 40.00x | $4 | 42.86x | $12 | Standard global API >=200K input tokens |
| xAI | Grok 4.6 (long context) | 357.14x | $1 | 40.00x | $4 | 42.86x | $12 | Standard global API >=200K input tokens |
| Anthropic | Claude Fable 5 | 357.14x | $1 | 100.00x | $10 | 178.57x | $50 | Standard Claude API global routing |
| Anthropic | Claude Mythos 5 | 357.14x | $1 | 100.00x | $10 | 178.57x | $50 | Standard Claude API global routing limited availability |
| OpenAI | GPT-5.5 (long context) | 357.14x | $1 | 100.00x | $10 | 160.71x | $45 | Standard API >272K input tokens |
| OpenAI | GPT-6 Astra (short context) | 357.14x | $1 | 100.00x | $10 | 178.57x | $50 | Standard API <=272K input tokens |
| OpenAI | GPT-5.6 Sol (long context) | 285.71x | $0.8 | 80.00x | $8 | 107.14x | $30 | Standard API promotional price >272K input tokens |
| xAI | Grok 4.5 (long context) | 214.29x | $0.6 | 40.00x | $4 | 42.86x | $12 | Standard global API >=200K input tokens |
| xAI | Grok 4.7 (short context) | 178.57x | $0.5 | 20.00x | $2 | 21.43x | $6 | Standard global API <200K input tokens |
| xAI | Grok 4.6 (short context) | 178.57x | $0.5 | 20.00x | $2 | 21.43x | $6 | Standard global API <200K input tokens |
| Anthropic | Claude Opus 4.7 | 178.57x | $0.5 | 50.00x | $5 | 89.29x | $25 | Standard Claude API global routing |
| Anthropic | Claude Opus 4.8 | 178.57x | $0.5 | 50.00x | $5 | 89.29x | $25 | Standard Claude API global routing |
| Anthropic | Claude Opus 5 | 178.57x | $0.5 | 50.00x | $5 | 89.29x | $25 | Standard Claude API global routing |
| OpenAI | GPT-5.4 (long context) | 178.57x | $0.5 | 50.00x | $5 | 80.36x | $22.5 | Standard API >272K input tokens |
| OpenAI | GPT-5.5 (short context) | 178.57x | $0.5 | 50.00x | $5 | 107.14x | $30 | Standard API <=272K input tokens |
| OpenAI | GPT-6 Sol (long context) | 142.86x | $0.4 | 40.00x | $4 | 53.57x | $15 | Standard API >272K input tokens |
| OpenAI | GPT-5.6 Sol (short context) | 142.86x | $0.4 | 40.00x | $4 | 71.43x | $20 | Standard API promotional price <=272K input tokens |
| OpenAI | GPT-5.6 Terra (long context) | 142.86x | $0.4 | 40.00x | $4 | 64.29x | $18 | Standard API >272K input tokens |
| Google | Gemini 3.1 Pro Preview (>200K prompts) | 142.86x | $0.4 | 40.00x | $4 | 64.29x | $18 | Standard paid tier >200K prompts |
| Moonshot AI / Kimi | Kimi K2.7 Code HighSpeed | 135.71x | $0.38 | 19.00x | $1.9 | 28.57x | $8 | unverified - previous HighSpeed API |
| xAI | Grok 4.5 (short context) | 107.14x | $0.3 | 20.00x | $2 | 21.43x | $6 | Standard global API <200K input tokens |
| Moonshot AI / Kimi | Kimi K3 | 107.14x | $0.3 | 30.00x | $3 | 53.57x | $15 | unverified - previous Standard API |
| Z.AI | GLM-5.1 | 92.86x | $0.26 | 14.00x | $1.4 | 15.71x | $4.4 | Standard API |
| Z.AI | GLM-5.2 | 92.86x | $0.26 | 14.00x | $1.4 | 15.71x | $4.4 | Standard API |
| Z.AI | GLM-5.3 | 92.86x | $0.26 | 14.00x | $1.4 | 15.71x | $4.4 | Standard API |
| OpenAI | GPT-5.4 (short context) | 89.29x | $0.25 | 25.00x | $2.5 | 53.57x | $15 | Standard API <=272K input tokens |
| Anthropic | Claude Fable 5.1 | 89.29x | $0.25 | 100.00x | $10 | 178.57x | $50 | Standard Claude API global routing |
| Anthropic | Claude Mythos 5.1 | 89.29x | $0.25 | 100.00x | $10 | 178.57x | $50 | Standard Claude API global routing |
| Z.AI | GLM-5-Turbo | 85.71x | $0.24 | 12.00x | $1.2 | 14.29x | $4 | unverified - previous Standard API |
| Anthropic | Claude Opus 5.5 | 71.43x | $0.2 | 40.00x | $4 | 71.43x | $20 | Standard Claude API global routing |
| OpenAI | GPT-6 Sol (short context) | 71.43x | $0.2 | 20.00x | $2 | 35.71x | $10 | Standard API <=272K input tokens |
| Z.AI | GLM-5 | 71.43x | $0.2 | 10.00x | $1 | 11.43x | $3.2 | Standard API |
| Anthropic | Claude Sonnet 5 | 71.43x | $0.2 | 20.00x | $2 | 35.71x | $10 | Standard Claude API global routing |
| OpenAI | GPT-5.6 Terra (short context) | 71.43x | $0.2 | 20.00x | $2 | 42.86x | $12 | Standard API <=272K input tokens |
| Google | Gemini 3.1 Pro Preview (<=200K prompts) | 71.43x | $0.2 | 20.00x | $2 | 42.86x | $12 | Standard paid tier <=200K prompts |
| Moonshot AI / Kimi | Kimi K2.7 Code | 67.86x | $0.19 | 9.50x | $0.95 | 14.29x | $4 | unverified - previous Standard API |
| Moonshot AI / Kimi | Kimi K2.6 | 57.14x | $0.16 | 9.50x | $0.95 | 14.29x | $4 | unverified - previous Standard API |
| Google | Gemini 3.5 Flash | 53.57x | $0.15 | 15.00x | $1.5 | 32.14x | $9 | Standard paid tier |
| OpenAI | GPT-5.4 Mini | 26.79x | $0.075 | 7.50x | $0.75 | 16.07x | $4.5 | Standard API short context |
| Google | Gemini 3.6 Flash | 26.79x | $0.075 | 7.50x | $0.75 | 13.39x | $3.75 | Standard paid tier promotional price through 2026-12-31 |
| Google | Gemini 3.7 Flash | 26.79x | $0.075 | 7.50x | $0.75 | 13.39x | $3.75 | Standard paid tier promotional price through 2026-12-31 |
| Google | Gemini 3.8 Flash | 26.79x | $0.075 | 7.50x | $0.75 | 13.39x | $3.75 | Standard paid tier introductory price through 2026-12-31 |
| Z.AI | GLM-5.3-FlashX | 26.79x | $0.075 | 3.70x | $0.37 | 4.46x | $1.25 | Standard API |
| DeepSeek | DeepSeek V4 Pro (peak) | 15.71x | $0.044 | 13.20x | $1.32 | 14.14x | $3.96 | Standard API peak |
| OpenAI | GPT-5.6 Luna (long context) | 14.29x | $0.04 | 4.00x | $0.4 | 6.43x | $1.8 | Standard API >272K input tokens |
| Xiaomi MiMo | Xiaomi MiMo-V2.6-Pro-UltraSpeed | 12.86x | $0.036 | 43.50x | $4.35 | 31.07x | $8.7 | Overseas real-time API |
| Z.AI | GLM-5.3-Flash | 10.71x | $0.03 | 1.50x | $0.15 | 1.79x | $0.5 | Standard API list price |
| Google | Gemini 3.5 Flash-Lite | 10.71x | $0.03 | 3.00x | $0.3 | 8.93x | $2.5 | Standard paid tier text/image/video/audio |
| Google | Gemini 3.1 Flash-Lite | 8.93x | $0.025 | 2.50x | $0.25 | 5.36x | $1.5 | Standard paid tier text/image/video |
| DeepSeek | DeepSeek V4 Pro (off-peak) | 7.86x | $0.022 | 6.60x | $0.66 | 7.07x | $1.98 | Standard API off-peak |
| OpenAI | GPT-6 Luna (long context) | 7.14x | $0.02 | 2.00x | $0.2 | 2.68x | $0.75 | Standard API >272K input tokens |
| OpenAI | GPT-5.4 Nano | 7.14x | $0.02 | 2.00x | $0.2 | 4.46x | $1.25 | Standard API short context |
| OpenAI | GPT-5.6 Luna (short context) | 7.14x | $0.02 | 2.00x | $0.2 | 4.29x | $1.2 | Standard API <=272K input tokens |
| OpenAI | GPT-6 Luna (short context) | 3.57x | $0.01 | 1.00x | $0.1 | 1.79x | $0.5 | Standard API <=272K input tokens |
| DeepSeek | DeepSeek V4.1 Flash (peak) | 2.14x | $0.006 | 3.00x | $0.3 | 4.29x | $1.2 | Standard API peak |
| Xiaomi MiMo | Xiaomi MiMo-V2.6-Pro | 1.29x | $0.0036 | 4.35x | $0.435 | 3.11x | $0.87 | Overseas real-time API |
| Xiaomi MiMo | Xiaomi MiMo-V2.5-Pro | 1.29x | $0.0036 | 4.35x | $0.435 | 3.11x | $0.87 | Overseas API V2.5 reduced price |
| DeepSeek | DeepSeek V4.1 Flash (off-peak) | 1.07x | $0.003 | 1.50x | $0.15 | 2.14x | $0.6 | Standard API off-peak |
| Xiaomi MiMo | Xiaomi MiMo-V2.6-Flash | 1.00x | $0.0028 | 1.40x | $0.14 | 1.00x | $0.28 | Overseas real-time API |
| Xiaomi MiMo | Xiaomi MiMo-V2.5 | 1.00x | $0.0028 | 1.40x | $0.14 | 1.00x | $0.28 | Overseas API V2.5 reduced price |

## Important Notes

- Rechecked all eight providers on 2026-09-24: no confirmed price changes or eligible new models since the September 23 update. Coverage remains 47 models and 61 price rows; CSV prices, multipliers, ordering, and the USD/CNY rate of 6.6975 are unchanged. Four Kimi rows and GLM-5-Turbo remain unverified because current official pages do not expose their price tables.

- Added xAI on 2026-09-23: Grok 4.5, 4.6, and 4.7 with six context-tier rows; total coverage is now 47 models and 61 price rows. Existing prices, baselines, and the CNY exchange rate are unchanged by this addition.
- User-requested xAI version floor: Grok 4.5 and newer only. The earlier Grok 4.20 family, Grok 4.3, and Grok Build 0.1 are excluded; model generations are not compared as decimal numbers or lexicographic strings.
- xAI uses public global-endpoint Standard API prices. The pricing table specifies long-context rates at `>=200K` prompt tokens for all included models, applied to every token in the request; some model-page prose instead says "exceed", so the explicit pricing-table boundary is used here. Batch, Priority, US regional uplift, tools, Imagine/Voice models, aliases, and the non-public-API Grok 4.7 Fast channel variant are excluded.

- Rechecked official sources on 2026-09-23: added GPT-6 Sol, GPT-6 Luna, Claude Opus 5.5, and Xiaomi MiMo-V2.6-Flash/Pro/Pro-UltraSpeed, bringing coverage at that stage to 44 models and 55 price rows before the xAI addition. The previous 47 USD price rows are unchanged. Recalculated input multipliers against GPT-6 Luna's USD 0.10 short-context input price and CNY amounts at `1 USD = 6.6975 CNY`. Kimi per-model links redirect to an overview without price tables, and GLM-5-Turbo is absent from Z.AI pricing; these five rows retain previous values marked `unverified`.
- User-requested version floors: exclude Z.AI/GLM models below 5, Claude models below 4.7, Google Gemini models below 3.1, OpenAI models below 5.4, and Kimi models below 2.6.
- Excluded discovered entries: OpenAI chat-latest and Daybreak aliases, gpt-5.3-codex below the OpenAI version floor, OpenAI gpt-5.4-pro and gpt-5.5-pro without cache prices, the specialized OpenAI gpt-5.6-cyber and restricted gpt-rosalind-research models, OpenAI image/audio/video/transcription/deep-research/tool rows, deprecated or retired Claude rows, Claude Mythos Preview invitation-only row without a separate pricing-table entry, retired DeepSeek V4 Flash Vision Exp alias, Z.AI free/text rows without cached-input prices, Z.AI vision/image/audio/video/tool/agent rows, Gemini Omni Flash and Gemini Omni Flash Preview without a comparable cache-hit text price, Gemini 3 Flash Preview below the Gemini version floor, Gemini live/audio/TTS/image-generation models, Kimi Moonshot V1 rows without cache-hit prices, Kimi promotions and vouchers, deprecated Xiaomi MiMo legacy names, and image/audio/video/tool-only pricing.
- USD/CNY reference rate for the Chinese README is `1 USD = 6.6975 CNY`, from the Federal Reserve H.10 current release for `2026-09-18`, published `2026-09-21`.
- DeepSeek V4.1 Flash uses `deepseek-flash`: cache-hit/input/output USD `0.003/0.15/0.60` off-peak and `0.006/0.30/1.20` peak per 1M tokens. Retired `deepseek-v4-flash` and `deepseek-v4-flash-vision-exp` aliases now use this model and price. The current official pricing table still lists V4 Pro with unchanged rates. Current peak hours are Monday-Friday `01:00-04:00` and `06:00-10:00 UTC`, excluding Chinese public holidays; all other hours, including weekends and Chinese public holidays in full, are off-peak.
- Xiaomi MiMo-V2.6-Flash, MiMo-V2.6-Pro, and MiMo-V2.6-Pro-UltraSpeed use official overseas real-time API prices. MiMo-V2.5 and MiMo-V2.5-Pro remain listed at unchanged prices but are scheduled for deprecation on `2026-10-21 10:00 Beijing time`; they are retained until then. Domestic pricing is noted in the CSV. Cache writing is limited-time free; Batch and web search charges are excluded. The Xiaomi pricing page was updated `2026-09-22`.
- The retained Kimi K3, K2.6, K2.7 Code, and K2.7 Code HighSpeed values came from earlier official per-model pricing pages and support automatic context caching. Kimi K3 has a `1,048,576` token context window; the K2.x models have `262,144` tokens. Promotions and vouchers are excluded from token unit prices.
- Gemini 3.1 Flash-Lite, Gemini 3.5 Flash-Lite, Gemini 3.5 Flash, Gemini 3.6 Flash, Gemini 3.7 Flash, and Gemini 3.8 Flash use official Standard paid prices. Gemini 3.6 Flash, Gemini 3.7 Flash, and Gemini 3.8 Flash currently share an input/cache-hit/output price of USD `0.75/0.075/3.75` through `2026-12-31`; the regular USD `1.50/0.15/7.50` price starts `2027-01-01`. Gemini 3.1 Pro uses the official `gemini-3.1-pro-preview` paid Standard tier, split into separate rows for prompts up to `200K` tokens and prompts over `200K` tokens. Gemini cache storage, Batch, Flex, Priority, Google Search, Maps grounding, live, TTS, and image-generation charges are excluded.
- OpenAI GPT-5.4, GPT-5.5, GPT-5.6, and GPT-6 use direct Standard pricing. Base rows are split into short-context and long-context rows at the `272K` input-token threshold; GPT-5.4 Mini and Nano list only short-context Standard pricing. GPT-6 Sol and Luna charge 2x input/cache and 1.5x output above that threshold for the full request. GPT-5.6 Sol's current promotional Standard price is available at least through `2026-11-21`. Cache writes, Batch, Flex, and Fast mode variants are excluded. Regional processing adds a `10%` uplift where available; GPT-6 Sol/Luna EU data residency requires Standard processing.
- Claude Opus 5.5 was released on `2026-09-22` with API ID `claude-opus-5-5`. Standard cache-hit/input/output prices are USD `0.20/4/20` per 1M tokens, with a `1M` context window and `128K` max output. Cache reads are 0.05x base input; cache writes, Batch, fast mode, and US-only inference uplift are excluded.
- Anthropic Claude prices above use the standard Claude API with global routing. Claude Opus 5 is generally available with the official API ID `claude-opus-5`, a `1M` token context window, and `128K` max output. Claude Sonnet 5's launch price of USD 2 input, USD 0.20 cache hit, and USD 10 output per 1M tokens is now its standard price; Anthropic canceled the previously scheduled 2026-09-01 increase. Claude Fable 5 and Fable 5.1 are generally available; Claude Mythos 5 and Mythos 5.1 are limited availability through Project Glasswing. Cache writes, US-only inference, cloud marketplace pricing, and fast mode premiums are not folded into the main table. Opus 4.7 and later Opus models, Claude Fable 5, Claude Mythos 5, and Claude Sonnet 5 use newer tokenizers.
- GLM-5.3-Flash promotional pricing ended at `2026-09-09 24:00 UTC+8`; current list prices are USD `0.03/0.15/0.50` per 1M tokens.
- Z.AI lists cached input storage as limited-time free for the included GLM text models; only cached input read price is included in the comparison.
- Unless noted, Batch, Flex, Fast mode, data residency, web/tool charges, session runtime, cache storage, cache writes, free tiers, promotions, vouchers, and provider-specific enterprise discounts are excluded.

## Price URLs Visited

- xAI pricing: https://docs.x.ai/developers/pricing
- xAI models: https://docs.x.ai/developers/models
- Grok 4.7: https://docs.x.ai/developers/models/grok-4.7
- Grok 4.6: https://docs.x.ai/developers/models/grok-4.6
- Grok Build 0.1: https://docs.x.ai/developers/models/grok-build-0.1
- Grok 4.20 Multi-Agent Beta: https://docs.x.ai/developers/models/grok-4.20-multi-agent-0309

- OpenAI pricing: https://developers.openai.com/api/docs/pricing
- OpenAI gpt-5.4: https://developers.openai.com/api/docs/models/gpt-5.4
- OpenAI gpt-5.4-mini: https://developers.openai.com/api/docs/models/gpt-5.4-mini
- OpenAI gpt-5.4-nano: https://developers.openai.com/api/docs/models/gpt-5.4-nano
- OpenAI gpt-5.5: https://developers.openai.com/api/docs/models/gpt-5.5
- OpenAI gpt-5.6-luna: https://developers.openai.com/api/docs/models/gpt-5.6-luna
- OpenAI gpt-5.6-terra: https://developers.openai.com/api/docs/models/gpt-5.6-terra
- OpenAI gpt-5.6-sol: https://developers.openai.com/api/docs/models/gpt-5.6-sol
- OpenAI gpt-6-sol: https://developers.openai.com/api/docs/models/gpt-6-sol
- OpenAI gpt-6-luna: https://developers.openai.com/api/docs/models/gpt-6-luna
- Claude Opus 5.5: https://platform.claude.com/docs/en/models/opus-5-5/overview
- Anthropic pricing: https://platform.claude.com/docs/en/about-claude/pricing
- DeepSeek pricing: https://api-docs.deepseek.com/quick_start/pricing/
- Z.AI pricing: https://docs.z.ai/guides/overview/pricing
- GLM-5.3-Flash/FlashX model IDs: https://docs.z.ai/guides/llm/glm-5.3-flash
- Kimi K3 pricing: https://platform.kimi.ai/docs/pricing/chat-k3
- Kimi K2.6 pricing: https://platform.kimi.ai/docs/pricing/chat-k26
- Kimi K2.7 Code pricing: https://platform.kimi.ai/docs/pricing/chat-k27-code
- Kimi pricing overview: https://platform.kimi.ai/docs/pricing/chat
- Xiaomi MiMo pricing: https://mimo.mi.com/docs/en-US/price/pay-as-you-go
- Gemini API pricing: https://ai.google.dev/gemini-api/docs/pricing
- Claude models overview: https://platform.claude.com/docs/en/about-claude/models/overview
- USD/CNY reference: https://www.federalreserve.gov/releases/h10/current/
