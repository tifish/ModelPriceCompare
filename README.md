# Model Token Price Comparison

[English](README.md) | [中文](README.zh-CN.md) | Interactive web page (sortable, provider filters): [tifish.github.io/ModelPriceCompare](https://tifish.github.io/ModelPriceCompare/)

Generated: 2026-10-29

All prices are normalized to USD per 1M tokens. Multipliers use the cheapest model in each price category as `1.00x`: Xiaomi MiMo-V2.6-Flash sets the cache-hit and output baselines (USD 0.0028 and 0.28), while GPT-6 Luna (short context) and Claude Haiku 5.5 (short context) share the input baseline (USD 0.10).

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
| xAI | Grok 4.5 (short context) | 107.14x | $0.3 | 20.00x | $2 | 21.43x | $6 | Standard global API <200K input tokens |
| Z.AI | GLM-5.3 | 92.86x | $0.26 | 14.00x | $1.4 | 15.71x | $4.4 | Standard API |
| OpenAI | GPT-5.4 (short context) | 89.29x | $0.25 | 25.00x | $2.5 | 53.57x | $15 | Standard API <=272K input tokens |
| Anthropic | Claude Fable 5.1 | 89.29x | $0.25 | 100.00x | $10 | 178.57x | $50 | Standard Claude API global routing |
| Anthropic | Claude Mythos 5.1 | 89.29x | $0.25 | 100.00x | $10 | 178.57x | $50 | Standard Claude API global routing |
| Anthropic | Claude Opus 5.5 | 71.43x | $0.2 | 40.00x | $4 | 71.43x | $20 | Standard Claude API global routing |
| OpenAI | GPT-6 Sol (short context) | 71.43x | $0.2 | 20.00x | $2 | 35.71x | $10 | Standard API <=272K input tokens |
| Anthropic | Claude Sonnet 5 | 71.43x | $0.2 | 20.00x | $2 | 35.71x | $10 | Standard Claude API global routing |
| OpenAI | GPT-5.6 Terra (short context) | 71.43x | $0.2 | 20.00x | $2 | 42.86x | $12 | Standard API <=272K input tokens |
| OpenAI | GPT-6.1 Sol (long context) | 71.43x | $0.2 | 40.00x | $4 | 53.57x | $15 | Standard API >272K input tokens |
| Moonshot AI / Kimi | Kimi K3.1 Pro | 71.43x | $0.2 | 20.00x | $2 | 35.71x | $10 | Standard API |
| Moonshot AI / Kimi | Kimi K3.1 Pro Highspeed | 71.43x | $0.2 | 40.00x | $4 | 71.43x | $20 | Standard API |
| Anthropic | Claude Sonnet 5.5 | 35.71x | $0.1 | 20.00x | $2 | 35.71x | $10 | Standard Claude API global routing |
| OpenAI | GPT-6.1 Sol (short context) | 35.71x | $0.1 | 20.00x | $2 | 35.71x | $10 | Standard API <=272K input tokens |
| Google | Gemini 4 Argon | 35.71x | $0.1 | 20.00x | $2 | 35.71x | $10 | Standard paid tier introductory price through 2026-11-30 |
| OpenAI | GPT-6.1 Terra (long context) | 35.71x | $0.1 | 20.00x | $2 | 26.79x | $7.5 | Standard API >272K input tokens |
| OpenAI | GPT-5.4 Mini | 26.79x | $0.075 | 7.50x | $0.75 | 16.07x | $4.5 | Standard API short context |
| Z.AI | GLM-5.3-FlashX | 26.79x | $0.075 | 3.70x | $0.37 | 4.46x | $1.25 | Standard API |
| Z.AI | GLM-5.3-FlashX-Legal | 26.79x | $0.075 | 3.70x | $0.37 | 4.46x | $1.25 | Standard API |
| Anthropic | Claude Haiku 5.5 (long context) | 17.86x | $0.05 | 5.00x | $0.5 | 8.93x | $2.5 | Standard Claude API global routing >100K input tokens |
| OpenAI | GPT-6.1 Terra (short context) | 17.86x | $0.05 | 10.00x | $1 | 17.86x | $5 | Standard API <=272K input tokens |
| OpenAI | GPT-5.6 Luna (long context) | 14.29x | $0.04 | 4.00x | $0.4 | 6.43x | $1.8 | Standard API >272K input tokens |
| Xiaomi MiMo | Xiaomi MiMo-V2.6-Pro-UltraSpeed | 12.86x | $0.036 | 43.50x | $4.35 | 31.07x | $8.7 | Overseas real-time API |
| Z.AI | GLM-5.3-Flash | 10.71x | $0.03 | 1.50x | $0.15 | 1.79x | $0.5 | Standard API list price |
| OpenAI | GPT-6 Luna (long context) | 7.14x | $0.02 | 2.00x | $0.2 | 2.68x | $0.75 | Standard API >272K input tokens |
| OpenAI | GPT-5.6 Luna (short context) | 7.14x | $0.02 | 2.00x | $0.2 | 4.29x | $1.2 | Standard API <=272K input tokens |
| OpenAI | GPT-6 Luna (short context) | 3.57x | $0.01 | 1.00x | $0.1 | 1.79x | $0.5 | Standard API <=272K input tokens |
| Anthropic | Claude Haiku 5.5 (short context) | 3.57x | $0.01 | 1.00x | $0.1 | 1.79x | $0.5 | Standard Claude API global routing <=100K input tokens |
| DeepSeek | DeepSeek V4.1 Flash (peak) | 2.14x | $0.006 | 3.00x | $0.3 | 4.29x | $1.2 | Standard API peak |
| Xiaomi MiMo | Xiaomi MiMo-V2.6-Pro | 1.29x | $0.0036 | 4.35x | $0.435 | 3.11x | $0.87 | Overseas real-time API |
| DeepSeek | DeepSeek V4.1 Flash (off-peak) | 1.07x | $0.003 | 1.50x | $0.15 | 2.14x | $0.6 | Standard API off-peak |
| Xiaomi MiMo | Xiaomi MiMo-V2.6-Flash | 1.00x | $0.0028 | 1.40x | $0.14 | 1.00x | $0.28 | Overseas real-time API |

## Important Notes

- Rechecked all eight providers on 2026-10-29: no qualifying new models or token-price changes; coverage remains 36 models and 51 price rows. OpenAI Standard short/long-context Markdown tables and Kimi embedded pricing tables confirm existing rates. USD/CNY remains `6.6702` (Federal Reserve H.10 released 2026-10-26, observation dated 2026-10-23). Latest-series scope and exclusions are unchanged; Kimi K2 retirement notices concern an already excluded series. Initial Markdown retrieval, a Kimi HTTP request, and local console encoding encountered errors; alternative retrieval and UTF-8 output completed verification successfully.

- Rechecked all eight providers on 2026-10-28: no qualifying new models or token-price changes; coverage remains 36 models and 51 price rows. OpenAI Standard short/long-context Markdown tables and Kimi embedded pricing tables confirm existing rates. Updated USD/CNY to `6.6702` (Federal Reserve H.10 released 2026-10-26, observation dated 2026-10-23) and recalculated CNY amounts. Latest-series scope and exclusions are unchanged. Initial Markdown retrieval and Kimi HTTP requests encountered errors; alternative direct retrieval completed verification successfully.

- Rechecked all eight providers on 2026-10-27: added GPT-6.1 Terra (API ID `gpt-6.1-terra`), with Standard cache-hit/input/output USD `0.05/1/5` for up to 272K input tokens and `0.10/2/7.5` above that threshold per 1M tokens. Coverage is now 36 models and 51 price rows. Existing token prices and multiplier baselines are unchanged. OpenAI pricing Markdown includes the complete Standard short/long-context tables; Kimi prices were verified from the official page's embedded table data after browser snapshot timeouts. USD/CNY remains `6.6861` (latest available Federal Reserve H.10 release dated 2026-10-19, observation dated 2026-10-16). Latest-series scope and existing exclusions remain unchanged.

- Current inclusion policy (updated 2026-10-24): OpenAI, Anthropic, and xAI retain their existing scope (GPT-5.4+, Claude 4.7+, Grok 4.5+). All other providers include only their latest series: DeepSeek V4.1, GLM-5.3, Gemini 4, Kimi K3.1, and Xiaomi MiMo V2.6, including eligible variants within each series. Older series are excluded even if still available. Coverage is now 36 models and 51 price rows. Retained prices, multiplier baselines, and USD/CNY are unchanged. This policy supersedes the historical coverage notes below.

- Rechecked all eight providers on 2026-10-26: no qualifying new models or token-price changes. Coverage remains 35 models and 49 price rows. The fully loaded Kimi pricing overview and expanded OpenAI Standard short/long-context tables confirm retained prices; the other six official pricing pages also match existing records. USD/CNY remains `6.6861` (latest available Federal Reserve H.10 release dated 2026-10-19, observation dated 2026-10-16). Multiplier baselines, latest-series scope, deprecated-model exclusions, and other exclusions remain unchanged.

- Rechecked all eight providers on 2026-10-25: no qualifying new models or token-price changes. Coverage remains 35 models and 49 price rows. The fully loaded Kimi pricing overview and expanded OpenAI Standard short/long-context tables confirm retained prices; the other six official pricing pages also match existing records. USD/CNY remains `6.6861` (Federal Reserve H.10, released 2026-10-19, observation dated 2026-10-16). Multiplier baselines, latest-series scope, deprecated-model exclusions, and other exclusions remain unchanged.

- Rechecked all eight providers on 2026-10-24: added Kimi K3.1 Pro and Kimi K3.1 Pro Highspeed (API IDs `kimi-k3.1-pro` and `kimi-k3.1-pro-highspeed`) at cache-hit/input/output USD `0.20/2/10` and `0.20/4/20` per 1M tokens, confirmed by the browser-rendered official pricing overview and model guide. Removed Kimi K3 under the latest-series policy: the official guide identifies K3.1 as a new series. Coverage is now 35 models and 49 price rows. Other retained token prices, multiplier baselines, and USD/CNY `6.6861` (Federal Reserve H.10, released 2026-10-19) are unchanged. Expanded OpenAI short/long-context tables and the Claude pricing table confirm retained prices. Other exclusions remain in effect.

- Rechecked all eight providers on 2026-10-23: no qualifying new models or token-price changes. Removed GPT-5.4 Nano under the deprecated-model exclusion rule: OpenAI marked it deprecated on 2026-10-01 and schedules API shutdown for 2027-04-01 (recommended replacement: GPT-6 Luna). Coverage is now 34 models and 48 price rows. Fully loaded Kimi and expanded OpenAI short/long-context tables confirm retained prices. Multiplier baselines and USD/CNY `6.6861` (Federal Reserve H.10, released 2026-10-19) are unchanged. Latest-series scope and other exclusions remain in effect.

- Rechecked all eight providers on 2026-10-22: added GLM-5.3-FlashX-Legal (API ID `glm-5.3-flashx-legal`) at cache-hit/input/output USD `0.075/0.37/1.25` per 1M tokens, confirmed by the official pricing table and model guide. Removed Xiaomi MiMo-V2.5 and MiMo-V2.5-Pro, officially deprecated on `2026-10-21 10:00 UTC+8`. Coverage is now 48 models and 64 price rows. Retained token prices and multiplier baselines are unchanged; MiMo-V2.6-Flash is now the sole cache-hit/output baseline. USD/CNY remains `6.6861` (Federal Reserve H.10, released 2026-10-19). Fully loaded Kimi and expanded OpenAI short/long-context tables confirm existing prices. GLM-5-Turbo remains absent from official pricing and retains previous values marked `unverified`. Existing exclusions remain in effect.

- Rechecked all eight providers on 2026-10-21 before 10:00 UTC+8: no qualifying new models or verified token-price changes; coverage remains 49 models and 65 price rows. Recalculated CNY amounts at USD/CNY `6.6861` using the Federal Reserve H.10 observation for 2026-10-16, published 2026-10-19. USD prices and multipliers are unchanged. The fully loaded Kimi overview and expanded OpenAI short/long-context tables confirm retained prices. MiMo-V2.5 and MiMo-V2.5-Pro remain available until `2026-10-21 10:00 UTC+8` and are retained at the V2.6 routing prices until that cutoff. GLM-5-Turbo still has no official pricing row and remains `unverified`. Newly listed gpt-rosalind-discovery is a specialized life-sciences model outside this comparison; image/audio/video/live/TTS and other existing exclusions remain unchanged.

- Rechecked all eight providers on 2026-10-20: no qualifying new models or verified token-price changes. Coverage remains 49 models and 65 price rows; USD prices, multipliers, and USD/CNY `6.6920` (latest Federal Reserve H.10 release, 2026-10-13) are unchanged. The official Kimi pricing overview confirms all four retained prices. DeepSeek `deepseek-flash` still serves `DeepSeek-V4.1-Flash-1017`, and DeepSeek V4 Pro rates are unchanged. Claude, OpenAI, Gemini, xAI, and Z.AI tables match the retained rows. Xiaomi still lists only V2.6 prices; MiMo-V2.5 and MiMo-V2.5-Pro requests auto-route to V2.6 and the IDs become invalid at `2026-10-21 10:00 UTC+8`, so both rows are retained until then. GLM-5-Turbo remains absent from the official Z.AI pricing table and retains previous values marked `unverified`. Image/audio/video/live/TTS models and Grok versions below 4.5 remain excluded.

- Rechecked all eight providers on 2026-10-19: no qualifying new models or verified token-price changes. Coverage remains 49 models and 65 price rows; USD prices, multipliers, and USD/CNY `6.6920` (latest Federal Reserve H.10 release, 2026-10-13) are unchanged. The official Kimi pricing overview confirms all four retained prices. DeepSeek `deepseek-flash` still serves `DeepSeek-V4.1-Flash-1017`, and DeepSeek V4 Pro rates are unchanged. Claude, OpenAI, Gemini, xAI, and Z.AI tables match the retained rows. Xiaomi still lists only V2.6 prices; MiMo-V2.5 and MiMo-V2.5-Pro requests auto-route to V2.6 and the IDs become invalid at `2026-10-21 10:00 UTC+8`, so both rows are retained until then. GLM-5-Turbo remains absent from the official Z.AI pricing table and retains previous values marked `unverified`. Image/audio/video/live/TTS models and Grok versions below 4.5 remain excluded.

- Rechecked all eight providers on 2026-10-18: no qualifying new models or verified token-price changes. Coverage remains 49 models and 65 price rows; USD prices, multipliers, and USD/CNY `6.6920` (latest Federal Reserve H.10 release, 2026-10-13) are unchanged. The official Kimi pricing overview confirms all four retained prices. DeepSeek's `deepseek-flash` now serves snapshot `DeepSeek-V4.1-Flash-1017` at unchanged prices; Search and Fetch tool calls (USD `0.75` per 1,000 successful requests each, excluded) are free through DeepSeek Harness, Claude Code, and Codex until per-request billing starts at `2026-11-01 00:00` Beijing time. Xiaomi still lists only V2.6 prices; MiMo-V2.5 and MiMo-V2.5-Pro requests auto-route to V2.6 and the IDs become invalid at `2026-10-21 10:00 UTC+8`, so both rows are retained until then. GLM-5-Turbo remains absent from the official Z.AI pricing table and retains previous values marked `unverified`. Image/audio/video/live/TTS models and Grok versions below 4.5 remain excluded.

- Rechecked all eight providers on 2026-10-17: no qualifying new models or verified token-price changes. Coverage remains 49 models and 65 price rows; USD prices, multipliers, and USD/CNY `6.6920` (latest Federal Reserve H.10 release, 2026-10-13) are unchanged. The official Kimi pricing overview confirms all four retained prices. DeepSeek's pricing page now lists Search and Fetch tool charges (USD `0.75` per 1,000 successful requests each), which are excluded as tool charges. Xiaomi still lists only V2.6 prices; MiMo-V2.5 and MiMo-V2.5-Pro requests auto-route to V2.6 and the IDs become invalid at `2026-10-21 10:00 UTC+8`, so both rows are retained until then. GLM-5-Turbo remains absent from the official Z.AI pricing table and retains previous values marked `unverified`. Image/audio/video/live/TTS models and Grok versions below 4.5 remain excluded.

- Rechecked all eight providers on 2026-10-16: no qualifying new models or verified token-price changes. Coverage remains 49 models and 65 price rows; USD prices, multipliers, and USD/CNY `6.6920` (latest Federal Reserve H.10 release, 2026-10-13) are unchanged. The official Kimi pricing overview confirms all four retained prices. Gemini Robotics ER 2 Preview (specialized embodied-reasoning model) and Gemini Embedding 2 (embeddings) are now listed on the Gemini pricing page and are excluded. Xiaomi still lists only V2.6 prices; MiMo-V2.5 and MiMo-V2.5-Pro requests auto-route to V2.6 and the IDs become invalid at `2026-10-21 10:00 UTC+8`, so both rows are retained until then. GLM-5-Turbo remains absent from the official Z.AI pricing table and retains previous values marked `unverified`. Image/audio/video/live/TTS models and Grok versions below 4.5 remain excluded.

- Rechecked all eight providers on 2026-10-15: added Gemini 4 Argon (API ID `gemini-4-argon`), Google's new stable flagship reasoning model, at an introductory Standard cache-hit/input/output price of USD `0.10/2/10` per 1M tokens through `2026-11-30`; USD `0.20/4/20` applies from `2026-12-01`. It has a unified `1,048,576`-token context window shared with output (default output limit `65,536`, up to `1,048,576` with long decode) and supports implicit caching only. Coverage is now 49 models and 65 price rows. No other qualifying new models or verified token-price changes were found; existing USD prices and multiplier baselines are unchanged. Recalculated CNY amounts at USD/CNY `6.6920` (Federal Reserve H.10 observation for 2026-10-09, published 2026-10-13). Xiaomi still lists only V2.6 prices; MiMo-V2.5 and MiMo-V2.5-Pro requests auto-route to V2.6 and the IDs become invalid at `2026-10-21 10:00 UTC+8`, so both rows are retained until then. GLM-5-Turbo remains absent from the official Z.AI pricing table and retains previous values marked `unverified`. Image/audio/video/live/TTS models and Grok versions below 4.5 remain excluded.

- Rechecked all eight providers on 2026-10-14: no qualifying new models or verified token-price changes. Coverage remains 48 models and 64 price rows; USD prices, multipliers, and USD/CNY 6.7038 are unchanged. The official Kimi pricing overview confirms all four retained prices. Xiaomi's pricing page now lists only V2.6 price rows and marks MiMo-V2.5 and MiMo-V2.5-Pro as to be deprecated; requests auto-route to V2.6 from `2026-10-14 18:00 UTC+8` and the IDs become invalid at `2026-10-21 10:00`, so both rows are retained until then. GLM-5-Turbo remains absent from the official Z.AI pricing table and retains previous values marked `unverified`. Image/audio/video and restricted research models remain excluded.

- Rechecked all eight providers on 2026-10-13: no qualifying new models or verified token-price changes. Coverage remains 48 models and 64 price rows; USD prices, multipliers, and USD/CNY 6.7038 are unchanged. The official Kimi pricing overview confirms all four retained prices. Xiaomi now announces that MiMo-V2.5 and MiMo-V2.5-Pro requests auto-route to V2.6 from `2026-10-14 18:00 UTC+8`, ahead of the `2026-10-21 10:00` ID retirement; both rows are retained until then. GLM-5-Turbo remains absent from the official Z.AI pricing table and retains previous values marked `unverified`. Image/audio/video and restricted research models remain excluded.

- Rechecked all eight providers on 2026-10-12: no qualifying new models or verified token-price changes. Coverage remains 48 models and 64 price rows; USD prices, multipliers, and USD/CNY 6.7038 are unchanged. The browser-rendered Kimi overview confirms all four retained prices. GLM-5-Turbo remains absent from the official Z.AI pricing table and retains previous values marked `unverified`. Image/audio/video and restricted research models remain excluded.

- Rechecked all eight providers on 2026-10-11: removed deprecated Gemini 3.5 Flash and Gemini 3.7 Flash, which automatically route to Gemini 3.6 Flash and Gemini 3.8 Flash respectively. Coverage is now 48 models and 64 price rows. No qualifying new models or verified token-price changes were found; retained USD prices, multipliers, and USD/CNY 6.7038 are unchanged. The browser-rendered Kimi overview confirms all four prices. GLM-5-Turbo remains absent from the official Z.AI pricing table; previous values are retained as `unverified`.

- Rechecked all eight providers on 2026-10-10: no qualifying new models or verified token-price changes. Coverage remains 50 models and 66 price rows; USD prices, multipliers, and the USD/CNY reference rate of 6.7038 are unchanged. The browser-rendered Kimi overview confirms all four retained prices. GLM-5-Turbo remains absent from the official Z.AI pricing table and retains previous values marked `unverified`. Updated OpenAI data residency notes: GPT-6 Sol/Luna support Fast processing in the EU, and GPT-6.1 Sol supports US/EU data residency including Fast and Ultrafast modes. Image/audio/video models remain excluded.

- Rechecked all eight providers on 2026-10-09: no qualifying new models or verified token-price changes. Coverage remains 50 models and 66 price rows; USD prices, multipliers, and the USD/CNY reference rate of 6.7038 are unchanged. The browser-rendered Kimi and DeepSeek pricing pages confirm their retained prices. GLM-5-Turbo remains absent from the official Z.AI pricing table and retains its previous values marked `unverified`. Newly listed image/audio/video models remain excluded.

- Follow-up verification of all eight providers on 2026-10-08: Claude Sonnet 5.5 cache reads are now USD `0.10` per 1M tokens, down from the previously recorded `0.20`; input/output remain USD `2/10`. Updated its cache-hit multiplier to `35.71x`, CNY amount to `0.67`, and table position. The browser-rendered Kimi pricing overview confirms all four retained Kimi prices, so their `unverified` labels have been removed and source links point to the overview. Only GLM-5-Turbo remains unverified. No qualifying new models were found; coverage remains 50 models and 66 price rows, with unchanged baselines and USD/CNY 6.7038. Newly listed image/audio/video models remain excluded.

- Rechecked all eight providers on 2026-10-08: added Claude Haiku 5.5 (API ID `claude-haiku-5-5`) as two rows split at 100K input tokens. Cache-hit/input/output prices are USD `0.01/0.10/0.50` for prompts <=100K and `0.05/0.50/2.50` for prompts >100K per 1M tokens. Its short-context input price ties GPT-6 Luna as the input baseline. The report now covers 50 models and 66 price rows; existing USD prices, multipliers, and USD/CNY 6.7038 are unchanged. Four Kimi rows and GLM-5-Turbo remain unverified with previous values retained. Haiku 5.5 supports 1M context and 128K max output and uses the newer tokenizer; cache writes, Batch, fast mode, and US-only inference uplift are excluded.

- Rechecked all eight providers on 2026-10-07: no qualifying new models or verified token-price changes. Coverage remains 49 models and 64 price rows; USD prices and multipliers are unchanged. Recalculated CNY amounts at USD/CNY 6.7038 (Federal Reserve H.10 observation for 2026-10-02, published 2026-10-05). Four Kimi rows and GLM-5-Turbo remain unverified and retain previous values.

- Rechecked all eight providers on 2026-10-06: no qualifying new models or verified token-price changes. Coverage remains 49 models and 64 price rows. USD prices, multipliers, and the USD/CNY reference rate of 6.7110 are unchanged. Four Kimi rows and GLM-5-Turbo remain unverified and retain previous values.

- Rechecked all eight providers on 2026-10-05: no qualifying new models or verified token-price changes. Coverage remains 49 models and 64 price rows. USD prices, multipliers, and the USD/CNY reference rate of 6.7110 are unchanged. Four Kimi rows and GLM-5-Turbo remain unverified and retain previous values.

- Rechecked all eight providers on 2026-10-04: no qualifying new models or verified token-price changes. Coverage remains 49 models and 64 price rows. USD prices, multipliers, and the USD/CNY reference rate of 6.7110 are unchanged. Four Kimi rows and GLM-5-Turbo remain unverified and retain previous values.

- Rechecked all eight providers on 2026-10-03: no qualifying new models or verified token-price changes. Coverage remains 49 models and 64 price rows. USD prices, multipliers, and the USD/CNY reference rate of 6.7110 are unchanged. Four Kimi rows and GLM-5-Turbo remain unverified and retain previous values.

- Rechecked all eight providers on 2026-10-02: no qualifying new models or verified token-price changes. Coverage remains 49 models and 64 price rows. USD prices, multipliers, and the USD/CNY reference rate of 6.7110 are unchanged. Four Kimi rows and GLM-5-Turbo remain unverified and retain previous values.

- Rechecked all eight providers on 2026-10-01: no qualifying new models or verified token-price changes. Coverage remains 49 models and 64 price rows; USD prices, multipliers, and the USD/CNY reference rate of 6.7110 are unchanged. Four Kimi rows and GLM-5-Turbo remain unverified and retain previous values. Updated GPT-6 Sol/Luna EU data residency notes: current model documentation supports Standard, Flex, and Batch processing.

- Rechecked all eight providers on 2026-09-30: added GPT-6.1 Sol (API ID `gpt-6.1-sol`) at cache-hit/input/output USD `0.10/2/10` for short context and `0.20/4/15` above 272K input tokens per 1M tokens. Coverage is now 49 models and 64 price rows. Existing USD prices and multiplier baselines are unchanged; CNY amounts use the latest reference rate, `1 USD = 6.7110 CNY`. Four Kimi rows and GLM-5-Turbo still lack verifiable current pricing and retain previous values marked `unverified`. GPT-6.1 Sol cache writes, Batch, Flex, Fast/Ultrafast modes, and regional premiums are excluded.

- Rechecked all eight providers on 2026-09-29: added Claude Sonnet 5.5 (API ID `claude-sonnet-5-5`) at USD 0.20/2/10 per 1M cache-hit/input/output tokens. Coverage is now 48 models and 62 price rows. Existing USD prices, multipliers, and the USD/CNY reference rate of 6.6975 are unchanged. Four Kimi rows and GLM-5-Turbo remain unverified because current official pages do not expose their price tables.

- Added xAI on 2026-09-23: Grok 4.5, 4.6, and 4.7 with six context-tier rows; total coverage is now 47 models and 61 price rows. Existing prices, baselines, and the CNY exchange rate are unchanged by this addition.
- User-requested xAI version floor: Grok 4.5 and newer only. The earlier Grok 4.20 family, Grok 4.3, and Grok Build 0.1 are excluded; model generations are not compared as decimal numbers or lexicographic strings.
- xAI uses public global-endpoint Standard API prices. The pricing table specifies long-context rates at `>=200K` prompt tokens for all included models, applied to every token in the request; some model-page prose instead says "exceed", so the explicit pricing-table boundary is used here. Batch, Priority, US regional uplift, tools, Imagine/Voice models, aliases, and the non-public-API Grok 4.7 Fast channel variant are excluded.

- Rechecked official sources on 2026-09-23: added GPT-6 Sol, GPT-6 Luna, Claude Opus 5.5, and Xiaomi MiMo-V2.6-Flash/Pro/Pro-UltraSpeed, bringing coverage at that stage to 44 models and 55 price rows before the xAI addition. The previous 47 USD price rows are unchanged. Recalculated input multipliers against GPT-6 Luna's USD 0.10 short-context input price and CNY amounts at `1 USD = 6.6975 CNY`. Kimi per-model links redirect to an overview without price tables, and GLM-5-Turbo is absent from Z.AI pricing; these five rows retain previous values marked `unverified`.
- Excluded discovered entries: OpenAI chat-latest and Daybreak aliases, gpt-5.3-codex below the OpenAI version floor, OpenAI gpt-5.4-pro and gpt-5.5-pro without cache prices, the specialized OpenAI gpt-5.6-cyber and specialized gpt-rosalind-research/discovery models, OpenAI image/audio/video/transcription/deep-research/tool rows, deprecated or retired Claude rows, Claude Mythos Preview invitation-only row without a separate pricing-table entry, retired DeepSeek V4 Flash Vision Exp alias, Z.AI free/text rows without cached-input prices, Z.AI vision/image/audio/video/tool/agent rows, Gemini Omni Flash and Gemini Omni Flash Preview without a comparable cache-hit text price, Gemini 3 Flash Preview below the Gemini version floor, the specialized Gemini Robotics ER 2 Preview and Streaming Preview models, Gemini Embedding 2, Gemini live/audio/TTS/image-generation models, Kimi Moonshot V1 rows without cache-hit prices, Kimi promotions and vouchers, deprecated Xiaomi MiMo legacy names, and image/audio/video/tool-only pricing.
- USD/CNY reference rate for the Chinese README is `1 USD = 6.6702 CNY`, from the Federal Reserve H.10 observation for `2026-10-23`, published `2026-10-26`.
- DeepSeek V4.1 Flash uses `deepseek-flash`: cache-hit/input/output USD `0.003/0.15/0.60` off-peak and `0.006/0.30/1.20` peak per 1M tokens. It currently serves snapshot `DeepSeek-V4.1-Flash-1017`. Retired `deepseek-v4-flash` and `deepseek-v4-flash-vision-exp` aliases now use this model and price. V4 Pro is excluded under the latest-series policy. Current peak hours are Monday-Friday `01:00-04:00` and `06:00-10:00 UTC`, excluding Chinese public holidays; all other hours, including weekends and Chinese public holidays in full, are off-peak.
- Xiaomi MiMo-V2.6-Flash, MiMo-V2.6-Pro, and MiMo-V2.6-Pro-UltraSpeed use official overseas real-time API prices. MiMo-V2.5 and MiMo-V2.5-Pro were deprecated on `2026-10-21 10:00 Beijing time` and have been removed. Domestic pricing is noted in the CSV. Cache writing is limited-time free; Batch and web search charges are excluded. The Xiaomi pricing page was updated `2026-10-21`.
- Kimi K3.1 Pro and Pro Highspeed use the official pricing overview verified on 2026-10-24. Both support automatic caching and a `1,048,576` token context window. Cache writes (5-minute/1-hour TTL) cost USD `2/4` for Pro and `4/8` for Highspeed per 1M tokens and are excluded, as are promotions and vouchers. API access requires a successful top-up (minimum USD 1). K3 and K2.x are excluded under the latest-series policy.
- Gemini 4 Argon uses the official `gemini-4-argon` Standard paid price: USD `0.10/2/10` cache-hit/input/output through `2026-11-30`, then USD `0.20/4/20` from `2026-12-01`. It supports implicit caching only, so no explicit cache storage price applies.
- OpenAI GPT-5.4, GPT-5.5, GPT-5.6, and GPT-6 use direct Standard pricing. Base rows are split into short-context and long-context rows at the `272K` input-token threshold; GPT-5.4 Mini lists only short-context Standard pricing. GPT-6 Sol and Luna charge 2x input/cache and 1.5x output above that threshold for the full request. GPT-5.6 Sol's current promotional Standard price is available at least through `2026-11-21`. Cache writes, Batch, Flex, and Fast mode variants are excluded. Regional processing adds a `10%` uplift where available; GPT-6 Sol/Luna EU data residency supports Standard, Fast, Flex, and Batch processing. GPT-6.1 Sol supports US and EU data residency including Fast and Ultrafast modes.
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

- OpenAI deprecations: https://developers.openai.com/api/docs/deprecations
- OpenAI pricing: https://developers.openai.com/api/docs/pricing
- OpenAI gpt-5.4: https://developers.openai.com/api/docs/models/gpt-5.4
- OpenAI gpt-5.4-mini: https://developers.openai.com/api/docs/models/gpt-5.4-mini
- OpenAI gpt-5.4-nano: https://developers.openai.com/api/docs/models/gpt-5.4-nano
- OpenAI gpt-5.5: https://developers.openai.com/api/docs/models/gpt-5.5
- OpenAI gpt-5.6-luna: https://developers.openai.com/api/docs/models/gpt-5.6-luna
- OpenAI gpt-5.6-terra: https://developers.openai.com/api/docs/models/gpt-5.6-terra
- OpenAI gpt-5.6-sol: https://developers.openai.com/api/docs/models/gpt-5.6-sol
- OpenAI gpt-6.1-sol: https://developers.openai.com/api/docs/models/gpt-6.1-sol
- OpenAI gpt-6.1-terra: https://developers.openai.com/api/docs/models/gpt-6.1-terra
- OpenAI pricing Markdown: https://developers.openai.com/api/docs/pricing.md
- OpenAI gpt-6-sol: https://developers.openai.com/api/docs/models/gpt-6-sol
- OpenAI gpt-6-luna: https://developers.openai.com/api/docs/models/gpt-6-luna
- Claude Haiku 5.5: https://platform.claude.com/docs/en/models/haiku-5-5/overview
- Claude Sonnet 5.5: https://platform.claude.com/docs/en/models/sonnet-5-5/overview
- Claude Opus 5.5: https://platform.claude.com/docs/en/models/opus-5-5/overview
- Anthropic pricing: https://platform.claude.com/docs/en/about-claude/pricing
- DeepSeek pricing: https://api-docs.deepseek.com/quick_start/pricing/
- Z.AI pricing: https://docs.z.ai/guides/overview/pricing
- GLM-5.3-Flash/FlashX/FlashX-Legal model IDs: https://docs.z.ai/guides/vlm/glm-5.3-flash
- Kimi K3.1 Pro / Highspeed model guide: https://platform.kimi.ai/docs/guide/kimi-k3-1-pro-quickstart
- Kimi K3 pricing: https://platform.kimi.ai/docs/pricing/chat-k3
- Kimi K2.6 pricing: https://platform.kimi.ai/docs/pricing/chat-k26
- Kimi K2.7 Code pricing: https://platform.kimi.ai/docs/pricing/chat-k27-code
- Kimi pricing overview: https://platform.kimi.ai/docs/pricing/chat
- Xiaomi MiMo pricing: https://mimo.mi.com/docs/en-US/price/pay-as-you-go
- Gemini API pricing: https://ai.google.dev/gemini-api/docs/pricing
- Gemini models: https://ai.google.dev/gemini-api/docs/models
- Gemini 4 Argon: https://ai.google.dev/gemini-api/docs/models/gemini-4-argon
- Gemini deprecations: https://ai.google.dev/gemini-api/docs/deprecations
- Gemini 3.5 Flash (deprecated): https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash
- Gemini 3.7 Flash (deprecated): https://ai.google.dev/gemini-api/docs/models/gemini-3.7-flash
- Claude models overview: https://platform.claude.com/docs/en/about-claude/models/overview
- USD/CNY reference: https://www.federalreserve.gov/releases/h10/current/
