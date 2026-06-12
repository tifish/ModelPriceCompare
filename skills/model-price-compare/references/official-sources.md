# 官方来源映射

比较 API token 价格时，优先使用这些厂商页面。官方文档优先于博客文章、搜索摘要、市场页面或社交媒体内容。

| 厂商 | 官方价格 URL | 模型/规格 URL 示例 | 说明 |
|---|---|---|---|
| OpenAI | https://developers.openai.com/api/docs/pricing | https://developers.openai.com/api/docs/models/gpt-5.4, https://developers.openai.com/api/docs/models/gpt-5.5 | 除非用户要求 Batch、Flex 或 Priority，否则使用 Standard 价格。GPT-5.4/GPT-5.5 的长上下文提示超过 272K input tokens 时，说明完整 session 的长上下文加价。 |
| Anthropic | https://platform.claude.com/docs/en/about-claude/pricing | https://platform.claude.com/docs/en/about-claude/models/overview | 除非用户要求 data residency 或云市场价格，否则使用 Claude API global routing。Cache hit 对应 Cache Hits & Refreshes。新 Claude 家族只要官方 pricing 明确定价就纳入；limited availability 模型保留但必须在备注中说明。 |
| DeepSeek | https://api-docs.deepseek.com/quick_start/pricing | https://api-docs.deepseek.com/news/news260424 | 检查是否存在有效的限时折扣；页面同时显示当前有效价和常规价时，两者都要报告。 |
| Z.AI | https://docs.z.ai/guides/overview/pricing | https://docs.z.ai/guides/llm/glm-5.1 | 使用 USD / 1M tokens。Cached Input Storage 与 Cached Input 分开计费，应写入备注，不要合并进 token 单价。 |
| Google Gemini | https://ai.google.dev/gemini-api/docs/pricing | https://ai.google.dev/gemini-api/docs/models | 除非用户要求 Batch、Flex 或 Priority，否则使用 Standard paid tier。提示长度分层和 cache storage 小时费用要单独说明。 |
| Moonshot AI / Kimi | https://platform.kimi.ai/docs/pricing/chat | https://platform.kimi.ai/docs/models | 有模型专属价格页时，优先使用 `/docs/pricing/chat-k27-code`、`/docs/pricing/chat-k26` 这类页面。cache hit、cache miss 和 output 列按页面原样处理。 |
| 小米 MiMo | https://platform.xiaomimimo.com/docs/en-US/price/pay-as-you-go | https://platform.xiaomimimo.com/llms.txt | 优先使用 pay-as-you-go API 价格页，而不是 token 套餐页。区分中国区和海外价格，并说明生效日期后的价格调整以及限时免费 cache writing。 |
