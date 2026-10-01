# 模型 Token 价格比较（人民币）

[English](README.md) | [中文](README.zh-CN.md)

生成日期：2026-10-02

所有价格统一为人民币约价 / 1M tokens。主表统一采用海外 API 美元价格，按 `1 USD = 6.7110 CNY` 近似换算。倍率按每个价格类别分别计算，以该类别中最便宜的模型作为 `1.00x`：Xiaomi MiMo-V2.5 与 MiMo-V2.6-Flash 并列缓存命中和输出基准（美元 0.0028 和 0.28），GPT-6 Luna（短上下文）为输入基准（美元 0.10）。

| 提供方 | 模型 | 命中倍率 | 输入缓存命中 | 未命中倍率 | 输入缓存未命中 | 输出倍率 | 输出 | 价格口径 |
|---|---|---:|---:|---:|---:|---:|---:|---|
| OpenAI | GPT-6 Astra（长上下文） | 714.29x | ¥13.42 | 200.00x | ¥134.22 | 267.86x | ¥503.33 | Standard API >272K input tokens |
| xAI | Grok 4.7（长上下文） | 357.14x | ¥6.71 | 40.00x | ¥26.84 | 42.86x | ¥80.53 | Standard global API >=200K input tokens |
| xAI | Grok 4.6（长上下文） | 357.14x | ¥6.71 | 40.00x | ¥26.84 | 42.86x | ¥80.53 | Standard global API >=200K input tokens |
| Anthropic | Claude Fable 5 | 357.14x | ¥6.71 | 100.00x | ¥67.11 | 178.57x | ¥335.55 | Standard Claude API global routing |
| Anthropic | Claude Mythos 5 | 357.14x | ¥6.71 | 100.00x | ¥67.11 | 178.57x | ¥335.55 | Standard Claude API global routing limited availability |
| OpenAI | GPT-5.5（长上下文） | 357.14x | ¥6.71 | 100.00x | ¥67.11 | 160.71x | ¥302.00 | Standard API >272K input tokens |
| OpenAI | GPT-6 Astra（短上下文） | 357.14x | ¥6.71 | 100.00x | ¥67.11 | 178.57x | ¥335.55 | Standard API <=272K input tokens |
| OpenAI | GPT-5.6 Sol（长上下文） | 285.71x | ¥5.37 | 80.00x | ¥53.69 | 107.14x | ¥201.33 | Standard API promotional price >272K input tokens |
| xAI | Grok 4.5（长上下文） | 214.29x | ¥4.03 | 40.00x | ¥26.84 | 42.86x | ¥80.53 | Standard global API >=200K input tokens |
| xAI | Grok 4.7（短上下文） | 178.57x | ¥3.36 | 20.00x | ¥13.42 | 21.43x | ¥40.27 | Standard global API <200K input tokens |
| xAI | Grok 4.6（短上下文） | 178.57x | ¥3.36 | 20.00x | ¥13.42 | 21.43x | ¥40.27 | Standard global API <200K input tokens |
| Anthropic | Claude Opus 4.7 | 178.57x | ¥3.36 | 50.00x | ¥33.56 | 89.29x | ¥167.78 | Standard Claude API global routing |
| Anthropic | Claude Opus 4.8 | 178.57x | ¥3.36 | 50.00x | ¥33.56 | 89.29x | ¥167.78 | Standard Claude API global routing |
| Anthropic | Claude Opus 5 | 178.57x | ¥3.36 | 50.00x | ¥33.56 | 89.29x | ¥167.78 | Standard Claude API global routing |
| OpenAI | GPT-5.4（长上下文） | 178.57x | ¥3.36 | 50.00x | ¥33.56 | 80.36x | ¥151.00 | Standard API >272K input tokens |
| OpenAI | GPT-5.5（短上下文） | 178.57x | ¥3.36 | 50.00x | ¥33.56 | 107.14x | ¥201.33 | Standard API <=272K input tokens |
| OpenAI | GPT-6 Sol（长上下文） | 142.86x | ¥2.68 | 40.00x | ¥26.84 | 53.57x | ¥100.67 | Standard API >272K input tokens |
| OpenAI | GPT-5.6 Sol（短上下文） | 142.86x | ¥2.68 | 40.00x | ¥26.84 | 71.43x | ¥134.22 | Standard API promotional price <=272K input tokens |
| OpenAI | GPT-5.6 Terra（长上下文） | 142.86x | ¥2.68 | 40.00x | ¥26.84 | 64.29x | ¥120.80 | Standard API >272K input tokens |
| Google | Gemini 3.1 Pro Preview (>200K prompts) | 142.86x | ¥2.68 | 40.00x | ¥26.84 | 64.29x | ¥120.80 | Standard paid tier >200K prompts |
| Moonshot AI / Kimi | Kimi K2.7 Code HighSpeed | 135.71x | ¥2.55 | 19.00x | ¥12.75 | 28.57x | ¥53.69 | unverified - previous HighSpeed API |
| xAI | Grok 4.5（短上下文） | 107.14x | ¥2.01 | 20.00x | ¥13.42 | 21.43x | ¥40.27 | Standard global API <200K input tokens |
| Moonshot AI / Kimi | Kimi K3 | 107.14x | ¥2.01 | 30.00x | ¥20.13 | 53.57x | ¥100.67 | unverified - previous Standard API |
| Z.AI | GLM-5.1 | 92.86x | ¥1.74 | 14.00x | ¥9.40 | 15.71x | ¥29.53 | Standard API |
| Z.AI | GLM-5.2 | 92.86x | ¥1.74 | 14.00x | ¥9.40 | 15.71x | ¥29.53 | Standard API |
| Z.AI | GLM-5.3 | 92.86x | ¥1.74 | 14.00x | ¥9.40 | 15.71x | ¥29.53 | Standard API |
| OpenAI | GPT-5.4（短上下文） | 89.29x | ¥1.68 | 25.00x | ¥16.78 | 53.57x | ¥100.67 | Standard API <=272K input tokens |
| Anthropic | Claude Fable 5.1 | 89.29x | ¥1.68 | 100.00x | ¥67.11 | 178.57x | ¥335.55 | Standard Claude API global routing |
| Anthropic | Claude Mythos 5.1 | 89.29x | ¥1.68 | 100.00x | ¥67.11 | 178.57x | ¥335.55 | Standard Claude API global routing |
| Z.AI | GLM-5-Turbo | 85.71x | ¥1.61 | 12.00x | ¥8.05 | 14.29x | ¥26.84 | unverified - previous Standard API |
| Anthropic | Claude Opus 5.5 | 71.43x | ¥1.34 | 40.00x | ¥26.84 | 71.43x | ¥134.22 | Standard Claude API global routing |
| OpenAI | GPT-6 Sol（短上下文） | 71.43x | ¥1.34 | 20.00x | ¥13.42 | 35.71x | ¥67.11 | Standard API <=272K input tokens |
| Z.AI | GLM-5 | 71.43x | ¥1.34 | 10.00x | ¥6.71 | 11.43x | ¥21.48 | Standard API |
| Anthropic | Claude Sonnet 5 | 71.43x | ¥1.34 | 20.00x | ¥13.42 | 35.71x | ¥67.11 | Standard Claude API global routing |
| OpenAI | GPT-5.6 Terra（短上下文） | 71.43x | ¥1.34 | 20.00x | ¥13.42 | 42.86x | ¥80.53 | Standard API <=272K input tokens |
| Google | Gemini 3.1 Pro Preview (<=200K prompts) | 71.43x | ¥1.34 | 20.00x | ¥13.42 | 42.86x | ¥80.53 | Standard paid tier <=200K prompts |
| Anthropic | Claude Sonnet 5.5 | 71.43x | ¥1.34 | 20.00x | ¥13.42 | 35.71x | ¥67.11 | Standard Claude API global routing |
| OpenAI | GPT-6.1 Sol（长上下文） | 71.43x | ¥1.34 | 40.00x | ¥26.84 | 53.57x | ¥100.67 | Standard API >272K input tokens |
| Moonshot AI / Kimi | Kimi K2.7 Code | 67.86x | ¥1.28 | 9.50x | ¥6.38 | 14.29x | ¥26.84 | unverified - previous Standard API |
| Moonshot AI / Kimi | Kimi K2.6 | 57.14x | ¥1.07 | 9.50x | ¥6.38 | 14.29x | ¥26.84 | unverified - previous Standard API |
| Google | Gemini 3.5 Flash | 53.57x | ¥1.01 | 15.00x | ¥10.07 | 32.14x | ¥60.40 | Standard paid tier |
| OpenAI | GPT-6.1 Sol（短上下文） | 35.71x | ¥0.67 | 20.00x | ¥13.42 | 35.71x | ¥67.11 | Standard API <=272K input tokens |
| OpenAI | GPT-5.4 Mini | 26.79x | ¥0.50 | 7.50x | ¥5.03 | 16.07x | ¥30.20 | Standard API short context |
| Google | Gemini 3.6 Flash | 26.79x | ¥0.50 | 7.50x | ¥5.03 | 13.39x | ¥25.17 | Standard paid tier promotional price through 2026-12-31 |
| Google | Gemini 3.7 Flash | 26.79x | ¥0.50 | 7.50x | ¥5.03 | 13.39x | ¥25.17 | Standard paid tier promotional price through 2026-12-31 |
| Google | Gemini 3.8 Flash | 26.79x | ¥0.50 | 7.50x | ¥5.03 | 13.39x | ¥25.17 | Standard paid tier introductory price through 2026-12-31 |
| Z.AI | GLM-5.3-FlashX | 26.79x | ¥0.50 | 3.70x | ¥2.48 | 4.46x | ¥8.39 | Standard API |
| DeepSeek | DeepSeek V4 Pro (peak) | 15.71x | ¥0.30 | 13.20x | ¥8.86 | 14.14x | ¥26.58 | Standard API peak |
| OpenAI | GPT-5.6 Luna（长上下文） | 14.29x | ¥0.27 | 4.00x | ¥2.68 | 6.43x | ¥12.08 | Standard API >272K input tokens |
| Xiaomi MiMo | Xiaomi MiMo-V2.6-Pro-UltraSpeed | 12.86x | ¥0.24 | 43.50x | ¥29.19 | 31.07x | ¥58.39 | Overseas real-time API |
| Z.AI | GLM-5.3-Flash | 10.71x | ¥0.20 | 1.50x | ¥1.01 | 1.79x | ¥3.36 | Standard API list price |
| Google | Gemini 3.5 Flash-Lite | 10.71x | ¥0.20 | 3.00x | ¥2.01 | 8.93x | ¥16.78 | Standard paid tier text/image/video/audio |
| Google | Gemini 3.1 Flash-Lite | 8.93x | ¥0.17 | 2.50x | ¥1.68 | 5.36x | ¥10.07 | Standard paid tier text/image/video |
| DeepSeek | DeepSeek V4 Pro (off-peak) | 7.86x | ¥0.15 | 6.60x | ¥4.43 | 7.07x | ¥13.29 | Standard API off-peak |
| OpenAI | GPT-6 Luna（长上下文） | 7.14x | ¥0.13 | 2.00x | ¥1.34 | 2.68x | ¥5.03 | Standard API >272K input tokens |
| OpenAI | GPT-5.4 Nano | 7.14x | ¥0.13 | 2.00x | ¥1.34 | 4.46x | ¥8.39 | Standard API short context |
| OpenAI | GPT-5.6 Luna（短上下文） | 7.14x | ¥0.13 | 2.00x | ¥1.34 | 4.29x | ¥8.05 | Standard API <=272K input tokens |
| OpenAI | GPT-6 Luna（短上下文） | 3.57x | ¥0.07 | 1.00x | ¥0.67 | 1.79x | ¥3.36 | Standard API <=272K input tokens |
| DeepSeek | DeepSeek V4.1 Flash (peak) | 2.14x | ¥0.04 | 3.00x | ¥2.01 | 4.29x | ¥8.05 | Standard API peak |
| Xiaomi MiMo | Xiaomi MiMo-V2.6-Pro | 1.29x | ¥0.02 | 4.35x | ¥2.92 | 3.11x | ¥5.84 | Overseas real-time API |
| Xiaomi MiMo | Xiaomi MiMo-V2.5-Pro | 1.29x | ¥0.02 | 4.35x | ¥2.92 | 3.11x | ¥5.84 | Overseas API V2.5 reduced price |
| DeepSeek | DeepSeek V4.1 Flash (off-peak) | 1.07x | ¥0.02 | 1.50x | ¥1.01 | 2.14x | ¥4.03 | Standard API off-peak |
| Xiaomi MiMo | Xiaomi MiMo-V2.6-Flash | 1.00x | ¥0.02 | 1.40x | ¥0.94 | 1.00x | ¥1.88 | Overseas real-time API |
| Xiaomi MiMo | Xiaomi MiMo-V2.5 | 1.00x | ¥0.02 | 1.40x | ¥0.94 | 1.00x | ¥1.88 | Overseas API V2.5 reduced price |

## 重要说明

- 于 2026-10-02 复核全部八家厂商：未发现符合收录条件的新模型或已核实的 token 单价变化。仍为 49 个模型、64 条价格记录，美元单价、倍率及美元兑人民币参考汇率 6.7110 均未变。四条 Kimi 记录与 GLM-5-Turbo 继续保留旧值并标为待核验。

- 于 2026-10-01 复核全部八家厂商：未发现符合收录条件的新模型或已核实的 token 单价变化。仍为 49 个模型、64 条价格记录，美元单价、倍率及美元兑人民币参考汇率 6.7110 均未变。四条 Kimi 记录与 GLM-5-Turbo 继续保留旧值并标为待核验。已更新 GPT-6 Sol/Luna 的欧盟数据驻留说明：当前模型文档支持 Standard、Flex 和 Batch。

- 于 2026-09-30 复核全部八家厂商：新增 GPT-6.1 Sol（API ID `gpt-6.1-sol`），短/长上下文缓存命中、输入、输出单价分别为 USD `0.10/2/10` 和 `0.20/4/15` / 1M tokens，现共 49 个模型、64 条价格记录。已有美元单价及倍率基准未变；人民币约价按最新参考汇率 `1 USD = 6.7110 CNY` 重算。四条 Kimi 记录与 GLM-5-Turbo 仍无法核实当前价格，继续保留旧值并标为待核验。GPT-6.1 Sol 的缓存写入、Batch、Flex、Fast/Ultrafast 和区域加价不纳入主表。

- 于 2026-09-29 复核全部八家厂商：新增 Claude Sonnet 5.5（API ID `claude-sonnet-5-5`），每百万 tokens 缓存命中/输入/输出价格为 USD 0.20/2/10，现共 48 个模型、62 条价格记录。已有美元单价、倍率及美元兑人民币参考汇率 6.6975 均未变。四条 Kimi 记录与 GLM-5-Turbo 因当前官方页面未提供对应价格表，继续标为待核验。

- 于 2026-09-23 加入 xAI：新增 Grok 4.5、4.6、4.7，共 6 条上下文分层价格记录，现共 47 个模型、61 条价格记录。本次添加不改变已有模型价格、各列基准或人民币换算汇率。
- 用户指定 xAI 版本下限：只收录 Grok 4.5 及更新版本。排除更早代际的 Grok 4.20 系列、Grok 4.3 及 Grok Build 0.1；模型代际不按小数或字符串排序判断。
- xAI 采用公共 API 全球端点 Standard 价格。官方价格表对已纳入模型均标注输入达到 `200K`（`>=200K`）时，整个请求适用长上下文价；部分模型页面正文则写作“超过”，本表采用价格表明确标注的边界。Batch、Priority、美国区域加价、工具费用、Imagine/Voice 模型、重复别名和非公共 API 的 Grok 4.7 Fast 渠道版本不纳入。

- 于 2026-09-23 复核官方来源：新增 GPT-6 Sol、GPT-6 Luna、Claude Opus 5.5 和 Xiaomi MiMo-V2.6-Flash/Pro/Pro-UltraSpeed，当时共 44 个模型、55 条价格记录，随后另行加入 xAI。原有 47 行美元单价未变。输入倍率按 GPT-6 Luna 短上下文输入价 USD 0.10 重新计算，人民币约价按 `1 USD = 6.6975 CNY` 更新。Kimi 模型专属链接均跳转至不含价格表的总览页，GLM-5-Turbo 未出现在当前 Z.AI 价格表中；这五行保留旧值并标为 `unverified`（待核验）。
- 用户指定的版本下限：排除 5 以下的 Z.AI/GLM 模型、4.7 以下的 Claude 模型、3.1 以下的 Google Gemini 模型、5.4 以下的 OpenAI 模型，以及 2.6 以下的 Kimi 模型。
- 已排除的发现项：OpenAI chat-latest 与 Daybreak 别名、低于 OpenAI 版本下限的 gpt-5.3-codex、缺少缓存价格的 OpenAI gpt-5.4-pro 和 gpt-5.5-pro、专用网络安全模型 gpt-5.6-cyber 和限受信研究机构使用的 gpt-rosalind-research、OpenAI 图像/音频/视频/转录/deep research/工具行、已废弃或退役 Claude 行、没有单独价格表行的邀请制 Claude Mythos Preview、已退役的 DeepSeek V4 Flash Vision Exp 别名、Z.AI 免费或缺少缓存命中价格的文本行、Z.AI 视觉/图像/音频/视频/工具/agent 行、缺少可比缓存命中文本价格的 Gemini Omni Flash 与 Gemini Omni Flash Preview、低于 Gemini 版本下限的 Gemini 3 Flash Preview、Gemini live/audio/TTS/图像生成模型、缺少缓存命中价格的 Kimi Moonshot V1 行、Kimi 促销和代金券、已退役的小米 MiMo V2 旧模型名，以及仅图像/音频/视频/工具计费项。
- 汇率采用近似值 `1 USD = 6.7110 CNY`。该汇率取自 Federal Reserve H.10 current release 中 `2026-09-25` 的 CHINA, P.R. YUAN 数据，发布时间为 `2026-09-28`；实际账单以服务商结算币种和付款时汇率为准。
- DeepSeek V4.1 Flash 使用官方 ID `deepseek-flash`。低谷缓存命中/输入/输出为 USD `0.003/0.15/0.60`，高峰为 `0.006/0.30/1.20` / 1M tokens。旧 `deepseek-v4-flash` 和 `deepseek-v4-flash-vision-exp` 已退役，其别名请求由 V4.1 Flash 服务并按新价计费。当前官方价格表仍列有 V4 Pro，单价保持不变。官方当前高峰时段为周一至周五 UTC `01:00-04:00`、`06:00-10:00`，中国公共假日除外；其余时间、周末及中国公共假日全天均按低谷价计费。
- Xiaomi MiMo-V2.6-Flash、MiMo-V2.6-Pro 和 MiMo-V2.6-Pro-UltraSpeed 使用官方海外实时 API 价格。MiMo-V2.5 和 MiMo-V2.5-Pro 仍列于官方价格表且价格未变，但已公告将于北京时间 `2026-10-21 10:00` 退役，本次仍保留。国内价格已写入 CSV 备注；缓存写入当前限时免费，Batch 和联网搜索费用未纳入。小米价格页更新时间为 `2026-09-22`。
- 保留的 Kimi K3、K2.6、K2.7 Code 和 K2.7 Code HighSpeed 数据来自此前的官方模型价格页，并支持自动上下文缓存。Kimi K3 的上下文窗口为 `1,048,576` tokens；K2.x 模型为 `262,144` tokens。当前 Kimi 总览说明 K3 缓存写入按 5 分钟和 1 小时 TTL 分别计费；这部分费用不计入本表。促销和代金券不折入 token 单价。
- Gemini 3.1 Flash-Lite、Gemini 3.5 Flash-Lite、Gemini 3.5 Flash、Gemini 3.6 Flash、Gemini 3.7 Flash 和 Gemini 3.8 Flash 使用官方付费 Standard 价格。Gemini 3.6 Flash、Gemini 3.7 Flash 与 Gemini 3.8 Flash 当前共享每 1M tokens USD `0.75/0.075/3.75` 的输入/缓存命中/输出价，有效至 `2026-12-31`；自 `2027-01-01` 起恢复为 USD `1.50/0.15/7.50`。Gemini 3.1 Pro 使用官方 `gemini-3.1-pro-preview` 付费 Standard 档，并按 `200K` prompt tokens 阈值拆成两行。Gemini 的缓存存储、Batch、Flex、Priority、Google Search、Maps grounding、live、TTS 与图像生成计费均未折入主表。
- OpenAI GPT-5.4、GPT-5.5、GPT-5.6 和 GPT-6 使用直接 API Standard 价格。主模型按 `272K` 输入 tokens 阈值拆成短上下文和长上下文行；GPT-5.4 Mini 与 Nano 只列官方短上下文 Standard 价格。GPT-6 Sol 和 Luna 超出该阈值时，整个请求按 2 倍输入/缓存价和 1.5 倍输出价计费。GPT-5.6 Sol 当前 Standard 促销价至少持续至 `2026-11-21`。缓存写入、Batch、Flex、Fast mode 未纳入主表；可用区域处理另加 `10%`，GPT-6 Sol/Luna 的欧盟数据驻留支持 Standard、Flex 和 Batch。
- Claude Opus 5.5 于 `2026-09-22` 发布，官方 API ID 为 `claude-opus-5-5`。标准缓存命中/输入/输出价为每 1M tokens USD `0.20/4/20`，上下文窗口为 `1M` tokens，最大输出为 `128K` tokens。缓存读取为基础输入价的 0.05 倍；缓存写入、Batch、fast mode 和 US-only inference 加价未纳入。
- Anthropic Claude 使用标准 Claude API 全球路由价格。Claude Opus 5 已公开可用，官方 API ID 为 `claude-opus-5`，上下文窗口为 `1M` tokens，最大输出为 `128K` tokens。Claude Sonnet 5 的首发价（每 1M tokens 输入 USD 2、缓存命中 USD 0.20、输出 USD 10）现已成为标准价；Anthropic 已取消原定于 `2026-09-01` 的涨价。Claude Fable 5 和 Fable 5.1 已公开可用；Claude Mythos 5 和 Mythos 5.1 是 Project Glasswing limited availability。缓存写入、US-only inference、云市场价格和 fast mode premium 未折入主表。Opus 4.7 及更新 Opus、Claude Fable 5、Claude Mythos 5 和 Claude Sonnet 5 使用新版 tokenizer。
- GLM-5.3-Flash 的 50% 促销已于 `2026-09-09 24:00 UTC+8` 结束；当前缓存命中/输入/输出常规价为 USD `0.03/0.15/0.50` / 1M tokens。
- Z.AI 将已纳入的 GLM 文本模型 cached input storage 标为限时免费；本比较只纳入 cached input read 价格。
- 除非特别说明，本比较不包含 Batch、Flex、Fast mode、数据驻留、联网/工具调用费用、session runtime、缓存存储、缓存写入、免费档、促销、代金券和企业折扣等变体。

## 访问过的价格网址

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
- OpenAI gpt-6.1-sol: https://developers.openai.com/api/docs/models/gpt-6.1-sol
- OpenAI gpt-6-sol: https://developers.openai.com/api/docs/models/gpt-6-sol
- OpenAI gpt-6-luna: https://developers.openai.com/api/docs/models/gpt-6-luna
- Claude Sonnet 5.5: https://platform.claude.com/docs/en/models/sonnet-5-5/overview
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
