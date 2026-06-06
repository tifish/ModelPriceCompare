# Model Token Price Comparison

[English](model_price_comparison.md) | [中文](model_price_comparison.zh-CN.md)

Generated: 2026-06-06

All prices are normalized to USD per 1M tokens. Multipliers use the cheapest model in each price category as `1.00x`; in this model set, DeepSeek V4 Flash is the baseline for cache-miss input, cache-hit input, and output.

| Model | Provider | Input cache miss | Miss x | Input cache hit | Hit x | Output | Output x | Basis |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| DeepSeek V4 Flash | DeepSeek | $0.14 | 1.00x | $0.0028 | 1.00x | $0.28 | 1.00x | Standard API current |
| DeepSeek V4 Pro | DeepSeek | $0.435 | 3.11x | $0.003625 | 1.29x | $0.87 | 3.11x | Standard API current |
| Xiaomi MiMo-V2.5-Pro | Xiaomi MiMo | $0.435 | 3.11x | $0.0036 | 1.29x | $0.87 | 3.11x | Overseas API, V2.5 reduced price |
| Kimi K2.6 | Moonshot AI / Kimi | $0.95 | 6.79x | $0.16 | 57.14x | $4.00 | 14.29x | Standard API |
| GPT-5.4 (short context) | OpenAI | $1.25 | 8.93x | $0.13 | 46.43x | $7.50 | 26.79x | Standard API <=272K input tokens |
| GLM-5.1 | Z.AI | $1.40 | 10.00x | $0.26 | 92.86x | $4.40 | 15.71x | Standard API |
| Gemini 3.1 Pro Preview (<=200K prompts) | Google | $2.00 | 14.29x | $0.20 | 71.43x | $12.00 | 42.86x | Paid Standard tier <=200K prompts |
| GPT-5.4 (long context) | OpenAI | $2.50 | 17.86x | $0.25 | 89.29x | $11.25 | 40.18x | Standard API >272K input tokens |
| GPT-5.5 (short context) | OpenAI | $2.50 | 17.86x | $0.25 | 89.29x | $15.00 | 53.57x | Standard API <=272K input tokens |
| Claude Sonnet 4.6 | Anthropic | $3.00 | 21.43x | $0.30 | 107.14x | $15.00 | 53.57x | Claude API global routing |
| Gemini 3.1 Pro Preview (>200K prompts) | Google | $4.00 | 28.57x | $0.40 | 142.86x | $18.00 | 64.29x | Paid Standard tier >200K prompts |
| GPT-5.5 (long context) | OpenAI | $5.00 | 35.71x | $0.50 | 178.57x | $22.50 | 80.36x | Standard API >272K input tokens |
| Claude Opus 4.8 | Anthropic | $5.00 | 35.71x | $0.50 | 178.57x | $25.00 | 89.29x | Claude API global routing |

## Important Notes

- DeepSeek V4 Flash and V4 Pro use the current official `deepseek-v4-flash` and `deepseek-v4-pro` prices. DeepSeek also notes that `deepseek-chat` and `deepseek-reasoner` are compatibility aliases for `deepseek-v4-flash` until deprecation on `2026-07-24 15:59 UTC`.
- Xiaomi MiMo-V2.5-Pro uses the official overseas API V2.5 price effective `2026-05-27 00:00` Beijing time: cache hit `$0.0036`, cache miss `$0.435`, output `$0.87`. Domestic pricing is cache hit `¥0.025`, cache miss `¥3.00`, output `¥6.00`; cache writing is currently free for a limited time.
- Kimi K2.6 uses official `kimi-k2.6` pricing: cache hit `$0.16`, cache miss `$0.95`, output `$4.00`, with a `262,144` token context window and automatic context caching.
- Gemini 3.1 Pro uses the official `gemini-3.1-pro-preview` paid Standard tier, split into separate rows for prompts up to `200K` tokens and prompts over `200K` tokens. Context cache storage is `$4.50 / 1M tokens / hour` and is not folded into token prices.
- OpenAI GPT-5.4 and GPT-5.5 use separate rows for Standard short-context pricing and full-session long-context pricing over `272K` input tokens. Regional processing adds a `10%` uplift.
- Anthropic Claude prices above use the standard Claude API with global routing. Cache hits and refreshes are `0.1x` base input; 5-minute cache writes are `1.25x`, and 1-hour cache writes are `2x`. US-only inference adds `1.1x`. Claude Opus 4.8 and Claude Sonnet 4.6 include the full `1M` token context window at standard pricing. Opus 4.8 uses the newer Opus tokenizer and has fast mode available at premium pricing; neither tokenization effects nor fast mode are folded into the main table.
- Z.AI lists GLM-5.1 cached input storage as limited-time free; only cached input read price is included in the comparison.
- Batch, Flex, Priority, fast mode, data residency, web/tool charges, session runtime, and provider-specific enterprise discounts are excluded unless noted.

## Price URLs Visited

- OpenAI pricing: https://developers.openai.com/api/docs/pricing
- Anthropic pricing: https://platform.claude.com/docs/en/about-claude/pricing
- DeepSeek pricing: https://api-docs.deepseek.com/quick_start/pricing
- Z.AI pricing: https://docs.z.ai/guides/overview/pricing
- Kimi K2.6 pricing: https://platform.kimi.ai/docs/pricing/chat-k26
- Xiaomi MiMo pricing: https://platform.xiaomimimo.com/docs/en-US/price/pay-as-you-go
- Gemini API pricing: https://ai.google.dev/gemini-api/docs/pricing
