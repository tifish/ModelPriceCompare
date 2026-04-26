# Official Source Map

Use these provider pages first when comparing API token prices. Prefer official docs over blog posts, search snippets, marketplace pages, or social posts.

| Provider | Official pricing URL | Model/spec URL examples | Notes |
|---|---|---|---|
| OpenAI | https://developers.openai.com/api/docs/pricing | https://developers.openai.com/api/docs/models/gpt-5.4, https://developers.openai.com/api/docs/models/gpt-5.5 | Use Standard pricing unless the user asks for Batch, Flex, or Priority. For GPT-5.4/GPT-5.5 long-context prompts over 272K input tokens, note the full-session long-context uplift. |
| Anthropic | https://platform.claude.com/docs/en/about-claude/pricing | https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-6 | Use Claude API global routing unless the user asks for data residency or cloud marketplace prices. Cache hit means Cache Hits & Refreshes. |
| DeepSeek | https://api-docs.deepseek.com/quick_start/pricing | https://api-docs.deepseek.com/news/news260424 | Check for active limited-time discounts and report both current effective price and regular price when shown. |
| Z.AI | https://docs.z.ai/guides/overview/pricing | https://docs.z.ai/guides/llm/glm-5.1 | Use USD per 1M tokens. Cached Input Storage is separate from Cached Input and should be noted, not folded into token price. |
| Google Gemini | https://ai.google.dev/gemini-api/docs/pricing | https://ai.google.dev/gemini-api/docs/models | Use Standard paid tier unless the user asks for Batch, Flex, or Priority. Note prompt-length tiers and cache storage hourly fees separately. |
| Moonshot AI / Kimi | https://platform.kimi.ai/docs/pricing/chat | https://platform.kimi.ai/docs/models | Prefer model-specific pricing pages such as `/docs/pricing/chat-k26` when available. Use cache hit, cache miss, and output columns exactly as listed. |
| Xiaomi MiMo | https://platform.xiaomimimo.com/static/docs/pricing.md | https://platform.xiaomimimo.com/llms.txt | Prefer the static Markdown docs over the JS token-plan page. Separate China and Overseas prices, and note 256K vs 1M context tiers plus limited-time free cache writing. |
