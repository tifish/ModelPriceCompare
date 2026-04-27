---
name: model-price-compare
description: Compare current LLM API token prices across providers using official pricing pages. Use when asked to compare model costs, input/cache-hit/cache-miss/output token prices, price multipliers, model price source URLs, or to update a reusable model list/report for OpenAI, Anthropic/Claude, DeepSeek, Z.AI/GLM, Google Gemini, Moonshot AI/Kimi, Xiaomi MiMo, or similar providers.
---

# Model Price Compare

## Overview

Produce a normalized price table for a user-supplied model list, using official pricing pages and current public rates. Record source URLs, caveats, and model-list inputs so the comparison can be repeated and audited.

## Workflow

1. Read the model list from the user prompt or a plain text file such as `models.txt`, one model per line.
2. Browse or fetch current official provider pricing. Use `references/official-sources.md` for preferred URLs and provider-specific caveats.
3. Normalize all token prices to USD per 1M tokens.
4. Capture at least these columns:
   - model
   - provider
   - input cache miss, also called standard/base input
   - input cache hit, also called cached input or cache read
   - output
   - multiplier for each price category
   - source URL
   - notes
5. Compute multipliers per category: divide each price by the cheapest nonzero price in the same column. Do not use one global baseline unless the user explicitly asks for it.
6. Explain exclusions such as Batch, Flex, Priority, regional processing, data residency, cache writes, cache storage, session runtime, tool charges, limited-time discounts, or enterprise pricing.
7. Write reusable artifacts when working in a repo:
   - `models.txt` for the editable input list
   - `README.md` as the default English report when the comparison should be published as the project readme
   - `README.zh-CN.md` as the Simplified Chinese readme when the user wants a bilingual readme; put language-switch links near the top of both readmes
   - `model_price_comparison.md` for the human-readable report
   - `model_price_comparison.zh-CN.md` for the Simplified Chinese report when the user wants bilingual output; localize the currency when requested, state the exchange rate and source, and keep multipliers tied to the underlying normalized prices
   - `model_price_comparison.csv` for spreadsheet-friendly data

## Source Rules

- Prefer official provider docs. Use third-party sources only to discover the official page, and do not cite them as the basis for prices.
- Prices change often; always verify live/current pages instead of relying on previous runs.
- For OpenAI model and pricing questions, use official OpenAI docs only.
- If an official page lists a limited-time, regional, or context-length tiered price, use the current effective price for the main comparison and put regular/alternate prices in notes.
- If a requested model cannot be found on an official page, mark it `unverified` instead of inventing a price.

## Output Style

Keep the main table compact. Put input cache miss before input cache hit in reports and CSV output. Put detailed caveats under `Important Notes`, and source URLs under `Price URLs Visited`.

## Open Source Hygiene

- Do not include local absolute paths, private API keys, account IDs, cookies, browser history, or workspace-specific secrets in generated skill files.
- Keep reusable provider source mappings in `references/official-sources.md`, not in the task report.
- Treat generated comparison files as examples or outputs, not as canonical evergreen pricing data.
