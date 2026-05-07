# Model Token Price Comparison

[English](README.md) | [中文](README.zh-CN.md)

Generated: 2026-05-07

All prices are normalized to USD per 1M tokens. Multipliers use the cheapest model in each price category as `1.00x`; in this model set, DeepSeek V4 Flash is the baseline for cache-miss input, cache-hit input, and output.

| Model | Provider | Input cache miss | Miss x | Input cache hit | Hit x | Output | Output x | Basis |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| DeepSeek V4 Flash | DeepSeek | $0.14 | 1.00x | $0.0028 | 1.00x | $0.28 | 1.00x | Standard API current |
| DeepSeek V4 Pro | DeepSeek | $0.435 | 3.11x | $0.003625 | 1.29x | $0.87 | 3.11x | Current limited-time discount |
| Kimi K2.6 | Moonshot AI / Kimi | $0.95 | 6.79x | $0.16 | 57.14x | $4.00 | 14.29x | Standard API |
| Xiaomi MiMo-V2.5-Pro | Xiaomi MiMo | $1.00 | 7.14x | $0.20 | 71.43x | $3.00 | 10.71x | Overseas API tier <=256K tokens |
| GLM-5.1 | Z.AI | $1.40 | 10.00x | $0.26 | 92.86x | $4.40 | 15.71x | Standard API |
| Gemini 3.1 Pro Preview | Google | $2.00 | 14.29x | $0.20 | 71.43x | $12.00 | 42.86x | Paid Standard tier <=200K prompts |
| GPT-5.4 | OpenAI | $2.50 | 17.86x | $0.25 | 89.29x | $15.00 | 53.57x | Standard short context |
| Claude Sonnet 4.6 | Anthropic | $3.00 | 21.43x | $0.30 | 107.14x | $15.00 | 53.57x | Claude API global routing |
| Claude Opus 4.6 | Anthropic | $5.00 | 35.71x | $0.50 | 178.57x | $25.00 | 89.29x | Claude API global routing |
| Claude Opus 4.7 | Anthropic | $5.00 | 35.71x | $0.50 | 178.57x | $25.00 | 89.29x | Claude API global routing |
| GPT-5.5 | OpenAI | $5.00 | 35.71x | $0.50 | 178.57x | $30.00 | 107.14x | Standard short context |

## Important Notes

- DeepSeek V4 Flash cache-hit input is now `$0.0028` per 1M tokens, and DeepSeek states that cache-hit input was reduced to `1/10` of launch price effective `2026-04-26 12:15 UTC`.
- DeepSeek V4 Pro uses the current official limited-time discount: cache hit `$0.003625`, cache miss `$0.435`, output `$0.87`. The same page lists regular prices as cache hit `$0.0145`, cache miss `$1.74`, output `$3.48`; the discount is extended until `2026-05-31 15:59 UTC`.
- Xiaomi MiMo-V2.5-Pro prices use the official overseas API tier for requests up to `256K` tokens: cache hit `$0.20`, input `$1.00`, output `$3.00`. For `256K` to `1M` tokens, the same official page lists cache hit `$0.40`, input `$2.00`, output `$6.00`. Cache writing is currently free for a limited time.
- Kimi K2.6 uses official `kimi-k2.6` pricing: cache hit `$0.16`, cache miss `$0.95`, output `$4.00`, with a `262,144` token context length and automatic context caching.
- Gemini 3.1 Pro uses the official `gemini-3.1-pro-preview` paid Standard tier with prompts up to `200K` tokens: cache hit `$0.20`, input `$2.00`, output `$12.00`. For prompts over `200K`, Google lists cache hit `$0.40`, input `$4.00`, output `$18.00`; context cache storage is `$4.50 / 1M tokens / hour`.
- OpenAI GPT-5.4 and GPT-5.5 prices above use Standard, short-context pricing. In the long-context table, GPT-5.4 is `$5.00` input, `$0.50` cached input, `$22.50` output; GPT-5.5 is `$10.00` input, `$1.00` cached input, `$45.00` output. Regional processing adds a `10%` uplift.
- Anthropic Claude prices above use the standard Claude API with global routing. Cache hits are `0.1x` base input; 5-minute cache writes are `1.25x`, and 1-hour cache writes are `2x`. US-only inference adds `1.1x`. Sonnet 4.6, Opus 4.6, and Opus 4.7 include the full `1M` token context window at standard pricing. Opus 4.7 may use up to `35%` more tokens than previous tokenizers for the same fixed text.
- Z.AI lists GLM-5.1 cached input storage as limited-time free; only cached input read price is included in the comparison.
- Batch, Flex, Priority, fast mode, data residency, web/tool charges, session runtime, and provider-specific enterprise discounts are excluded unless noted.

## Price URLs Visited

- OpenAI pricing: https://developers.openai.com/api/docs/pricing
- Anthropic pricing: https://platform.claude.com/docs/en/about-claude/pricing
- DeepSeek pricing: https://api-docs.deepseek.com/quick_start/pricing
- Z.AI pricing: https://docs.z.ai/guides/overview/pricing
- Kimi K2.6 pricing: https://platform.kimi.ai/docs/pricing/chat-k26
- Xiaomi MiMo pricing: https://platform.xiaomimimo.com/static/docs/pricing.md
- Gemini API pricing: https://ai.google.dev/gemini-api/docs/pricing
