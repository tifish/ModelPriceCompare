# Model Token Price Comparison

[English](README.md) | [中文](README.zh-CN.md)

Generated: 2026-04-26

All prices are normalized to USD per 1M tokens. Multipliers use the cheapest model in each price category as `1.00x`; in this model set, DeepSeek V4 Flash is the baseline for cache-hit input, cache-miss input, and output.

| Model | Provider | Input cache hit | Hit x | Input cache miss | Miss x | Output | Output x | Basis |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| DeepSeek V4 Flash | DeepSeek | $0.028 | 1.00x | $0.14 | 1.00x | $0.28 | 1.00x | Standard API current |
| DeepSeek V4 Pro | DeepSeek | $0.03625 | 1.29x | $0.435 | 3.11x | $0.87 | 3.11x | Current limited-time discount |
| Kimi K2.6 | Moonshot AI / Kimi | $0.16 | 5.71x | $0.95 | 6.79x | $4.00 | 14.29x | Standard API |
| Xiaomi MiMo-V2.5-Pro | Xiaomi MiMo | $0.20 | 7.14x | $1.00 | 7.14x | $3.00 | 10.71x | Overseas API tier <=256K tokens |
| Gemini 3.1 Pro Preview | Google | $0.20 | 7.14x | $2.00 | 14.29x | $12.00 | 42.86x | Standard paid tier <=200K prompts |
| GLM-5.1 | Z.AI | $0.26 | 9.29x | $1.40 | 10.00x | $4.40 | 15.71x | Standard API |
| GPT-5.4 | OpenAI | $0.25 | 8.93x | $2.50 | 17.86x | $15.00 | 53.57x | Standard short context |
| Claude Opus 4.6 | Anthropic | $0.50 | 17.86x | $5.00 | 35.71x | $25.00 | 89.29x | Standard Claude API global routing |
| Claude Opus 4.7 | Anthropic | $0.50 | 17.86x | $5.00 | 35.71x | $25.00 | 89.29x | Standard Claude API global routing |
| GPT-5.5 | OpenAI | $0.50 | 17.86x | $5.00 | 35.71x | $30.00 | 107.14x | Standard short context |

## Important Notes

- DeepSeek V4 Pro is using the current official limited-time discount: cache hit `$0.03625`, cache miss `$0.435`, output `$0.87`. The same page lists regular prices as cache hit `$0.145`, cache miss `$1.74`, output `$3.48`; the discount is valid until `2026-05-05 15:59 UTC`.
- Xiaomi MiMo-V2.5-Pro prices use the official overseas API tier for requests up to `256K` tokens: cache hit `$0.20`, input `$1.00`, output `$3.00`. For `256K` to `1M` tokens, the same official page lists cache hit `$0.40`, input `$2.00`, output `$6.00`. Cache writing is currently free for a limited time.
- Kimi K2.6 uses official `kimi-k2.6` pricing: cache hit `$0.16`, cache miss `$0.95`, output `$4.00`, with a `256K` context length and automatic context caching.
- Gemini 3.1 Pro uses the official paid Standard tier for `gemini-3.1-pro-preview` at prompts up to `200K` tokens: cache hit `$0.20`, input `$2.00`, output `$12.00`. For prompts over `200K`, Google lists cache hit `$0.40`, input `$4.00`, output `$18.00`; context cache storage is `$4.50 / 1M tokens / hour`.
- OpenAI GPT-5.4 and GPT-5.5 prices above use Standard, short-context pricing. For prompts over `272K` input tokens, OpenAI prices the full session at `2x` input and `1.5x` output for these 1.05M-context models. Regional processing adds a `10%` uplift.
- Anthropic Claude prices above use the standard Claude API with global routing. Cache hits are `0.1x` base input; 5-minute cache writes are `1.25x`, and 1-hour cache writes are `2x`. US-only inference adds `1.1x`. Opus 4.7 may use up to `35%` more tokens than previous tokenizers for the same fixed text.
- Z.AI lists GLM-5.1 cached input storage as limited-time free; only cached input read price is included in the comparison.
- Batch, Flex, Priority, fast mode, data residency, web/tool charges, session runtime, and provider-specific enterprise discounts are excluded unless noted.
- `browser-use` was requested, but the local in-app browser runtime failed to start because the app-server path was missing. Official source pages were still checked through web retrieval and are listed below.

## Price URLs Visited

- OpenAI pricing: https://developers.openai.com/api/docs/pricing
- OpenAI GPT-5.4 model page: https://developers.openai.com/api/docs/models/gpt-5.4
- OpenAI GPT-5.5 model page: https://developers.openai.com/api/docs/models/gpt-5.5
- Anthropic pricing: https://platform.claude.com/docs/en/about-claude/pricing?939688b5_page=1&e45d281a_page=2
- Anthropic Opus 4.7 update: https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-6
- DeepSeek pricing: https://api-docs.deepseek.com/quick_start/pricing
- DeepSeek V4 release note: https://api-docs.deepseek.com/news/news260424
- Z.AI pricing: https://docs.z.ai/guides/overview/pricing
- Z.AI GLM-5.1 model page: https://docs.z.ai/guides/llm/glm-5.1
- Kimi K2.6 pricing: https://platform.kimi.ai/docs/pricing/chat-k26
- Xiaomi MiMo pricing: https://platform.xiaomimimo.com/static/docs/pricing.md
- Xiaomi MiMo-V2.5 release note: https://platform.xiaomimimo.com/static/docs/news/v2.5-news.md
- Gemini API pricing: https://ai.google.dev/gemini-api/docs/pricing
