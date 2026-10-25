# 模型 Token 价格比较（人民币）

[English](README.md) | [中文](README.zh-CN.md) | 交互式网页（可排序、按提供方筛选）：[tifish.github.io/ModelPriceCompare](https://tifish.github.io/ModelPriceCompare/)

生成日期：2026-10-26

所有价格统一为人民币约价 / 1M tokens。主表统一采用海外 API 美元价格，按 `1 USD = 6.6861 CNY` 近似换算。倍率按每个价格类别分别计算，以该类别中最便宜的模型作为 `1.00x`：Xiaomi MiMo-V2.6-Flash 为缓存命中和输出基准（美元 0.0028 和 0.28），GPT-6 Luna（短上下文）与 Claude Haiku 5.5（短上下文）并列输入基准（美元 0.10）。

| 提供方 | 模型 | 命中倍率 | 输入缓存命中 | 未命中倍率 | 输入缓存未命中 | 输出倍率 | 输出 | 价格口径 |
|---|---|---:|---:|---:|---:|---:|---:|---|
| OpenAI | GPT-6 Astra（长上下文） | 714.29x | ¥13.37 | 200.00x | ¥133.72 | 267.86x | ¥501.46 | Standard API >272K input tokens |
| xAI | Grok 4.7（长上下文） | 357.14x | ¥6.69 | 40.00x | ¥26.74 | 42.86x | ¥80.23 | Standard global API >=200K input tokens |
| xAI | Grok 4.6（长上下文） | 357.14x | ¥6.69 | 40.00x | ¥26.74 | 42.86x | ¥80.23 | Standard global API >=200K input tokens |
| Anthropic | Claude Fable 5 | 357.14x | ¥6.69 | 100.00x | ¥66.86 | 178.57x | ¥334.30 | Standard Claude API global routing |
| Anthropic | Claude Mythos 5 | 357.14x | ¥6.69 | 100.00x | ¥66.86 | 178.57x | ¥334.30 | Standard Claude API global routing limited availability |
| OpenAI | GPT-5.5（长上下文） | 357.14x | ¥6.69 | 100.00x | ¥66.86 | 160.71x | ¥300.87 | Standard API >272K input tokens |
| OpenAI | GPT-6 Astra（短上下文） | 357.14x | ¥6.69 | 100.00x | ¥66.86 | 178.57x | ¥334.30 | Standard API <=272K input tokens |
| OpenAI | GPT-5.6 Sol（长上下文） | 285.71x | ¥5.35 | 80.00x | ¥53.49 | 107.14x | ¥200.58 | Standard API promotional price >272K input tokens |
| xAI | Grok 4.5（长上下文） | 214.29x | ¥4.01 | 40.00x | ¥26.74 | 42.86x | ¥80.23 | Standard global API >=200K input tokens |
| xAI | Grok 4.7（短上下文） | 178.57x | ¥3.34 | 20.00x | ¥13.37 | 21.43x | ¥40.12 | Standard global API <200K input tokens |
| xAI | Grok 4.6（短上下文） | 178.57x | ¥3.34 | 20.00x | ¥13.37 | 21.43x | ¥40.12 | Standard global API <200K input tokens |
| Anthropic | Claude Opus 4.7 | 178.57x | ¥3.34 | 50.00x | ¥33.43 | 89.29x | ¥167.15 | Standard Claude API global routing |
| Anthropic | Claude Opus 4.8 | 178.57x | ¥3.34 | 50.00x | ¥33.43 | 89.29x | ¥167.15 | Standard Claude API global routing |
| Anthropic | Claude Opus 5 | 178.57x | ¥3.34 | 50.00x | ¥33.43 | 89.29x | ¥167.15 | Standard Claude API global routing |
| OpenAI | GPT-5.4（长上下文） | 178.57x | ¥3.34 | 50.00x | ¥33.43 | 80.36x | ¥150.44 | Standard API >272K input tokens |
| OpenAI | GPT-5.5（短上下文） | 178.57x | ¥3.34 | 50.00x | ¥33.43 | 107.14x | ¥200.58 | Standard API <=272K input tokens |
| OpenAI | GPT-6 Sol（长上下文） | 142.86x | ¥2.67 | 40.00x | ¥26.74 | 53.57x | ¥100.29 | Standard API >272K input tokens |
| OpenAI | GPT-5.6 Sol（短上下文） | 142.86x | ¥2.67 | 40.00x | ¥26.74 | 71.43x | ¥133.72 | Standard API promotional price <=272K input tokens |
| OpenAI | GPT-5.6 Terra（长上下文） | 142.86x | ¥2.67 | 40.00x | ¥26.74 | 64.29x | ¥120.35 | Standard API >272K input tokens |
| xAI | Grok 4.5（短上下文） | 107.14x | ¥2.01 | 20.00x | ¥13.37 | 21.43x | ¥40.12 | Standard global API <200K input tokens |
| Z.AI | GLM-5.3 | 92.86x | ¥1.74 | 14.00x | ¥9.36 | 15.71x | ¥29.42 | Standard API |
| OpenAI | GPT-5.4（短上下文） | 89.29x | ¥1.67 | 25.00x | ¥16.72 | 53.57x | ¥100.29 | Standard API <=272K input tokens |
| Anthropic | Claude Fable 5.1 | 89.29x | ¥1.67 | 100.00x | ¥66.86 | 178.57x | ¥334.30 | Standard Claude API global routing |
| Anthropic | Claude Mythos 5.1 | 89.29x | ¥1.67 | 100.00x | ¥66.86 | 178.57x | ¥334.30 | Standard Claude API global routing |
| Anthropic | Claude Opus 5.5 | 71.43x | ¥1.34 | 40.00x | ¥26.74 | 71.43x | ¥133.72 | Standard Claude API global routing |
| OpenAI | GPT-6 Sol（短上下文） | 71.43x | ¥1.34 | 20.00x | ¥13.37 | 35.71x | ¥66.86 | Standard API <=272K input tokens |
| Anthropic | Claude Sonnet 5 | 71.43x | ¥1.34 | 20.00x | ¥13.37 | 35.71x | ¥66.86 | Standard Claude API global routing |
| OpenAI | GPT-5.6 Terra（短上下文） | 71.43x | ¥1.34 | 20.00x | ¥13.37 | 42.86x | ¥80.23 | Standard API <=272K input tokens |
| OpenAI | GPT-6.1 Sol（长上下文） | 71.43x | ¥1.34 | 40.00x | ¥26.74 | 53.57x | ¥100.29 | Standard API >272K input tokens |
| Moonshot AI / Kimi | Kimi K3.1 Pro | 71.43x | ¥1.34 | 20.00x | ¥13.37 | 35.71x | ¥66.86 | Standard API |
| Moonshot AI / Kimi | Kimi K3.1 Pro Highspeed | 71.43x | ¥1.34 | 40.00x | ¥26.74 | 71.43x | ¥133.72 | Standard API |
| Anthropic | Claude Sonnet 5.5 | 35.71x | ¥0.67 | 20.00x | ¥13.37 | 35.71x | ¥66.86 | Standard Claude API global routing |
| OpenAI | GPT-6.1 Sol（短上下文） | 35.71x | ¥0.67 | 20.00x | ¥13.37 | 35.71x | ¥66.86 | Standard API <=272K input tokens |
| Google | Gemini 4 Argon | 35.71x | ¥0.67 | 20.00x | ¥13.37 | 35.71x | ¥66.86 | Standard paid tier introductory price through 2026-11-30 |
| OpenAI | GPT-5.4 Mini | 26.79x | ¥0.50 | 7.50x | ¥5.01 | 16.07x | ¥30.09 | Standard API short context |
| Z.AI | GLM-5.3-FlashX | 26.79x | ¥0.50 | 3.70x | ¥2.47 | 4.46x | ¥8.36 | Standard API |
| Z.AI | GLM-5.3-FlashX-Legal | 26.79x | ¥0.50 | 3.70x | ¥2.47 | 4.46x | ¥8.36 | Standard API |
| Anthropic | Claude Haiku 5.5（长上下文） | 17.86x | ¥0.33 | 5.00x | ¥3.34 | 8.93x | ¥16.72 | Standard Claude API global routing >100K input tokens |
| OpenAI | GPT-5.6 Luna（长上下文） | 14.29x | ¥0.27 | 4.00x | ¥2.67 | 6.43x | ¥12.03 | Standard API >272K input tokens |
| Xiaomi MiMo | Xiaomi MiMo-V2.6-Pro-UltraSpeed | 12.86x | ¥0.24 | 43.50x | ¥29.08 | 31.07x | ¥58.17 | Overseas real-time API |
| Z.AI | GLM-5.3-Flash | 10.71x | ¥0.20 | 1.50x | ¥1.00 | 1.79x | ¥3.34 | Standard API list price |
| OpenAI | GPT-6 Luna（长上下文） | 7.14x | ¥0.13 | 2.00x | ¥1.34 | 2.68x | ¥5.01 | Standard API >272K input tokens |
| OpenAI | GPT-5.6 Luna（短上下文） | 7.14x | ¥0.13 | 2.00x | ¥1.34 | 4.29x | ¥8.02 | Standard API <=272K input tokens |
| OpenAI | GPT-6 Luna（短上下文） | 3.57x | ¥0.07 | 1.00x | ¥0.67 | 1.79x | ¥3.34 | Standard API <=272K input tokens |
| Anthropic | Claude Haiku 5.5（短上下文） | 3.57x | ¥0.07 | 1.00x | ¥0.67 | 1.79x | ¥3.34 | Standard Claude API global routing <=100K input tokens |
| DeepSeek | DeepSeek V4.1 Flash (peak) | 2.14x | ¥0.04 | 3.00x | ¥2.01 | 4.29x | ¥8.02 | Standard API peak |
| Xiaomi MiMo | Xiaomi MiMo-V2.6-Pro | 1.29x | ¥0.02 | 4.35x | ¥2.91 | 3.11x | ¥5.82 | Overseas real-time API |
| DeepSeek | DeepSeek V4.1 Flash (off-peak) | 1.07x | ¥0.02 | 1.50x | ¥1.00 | 2.14x | ¥4.01 | Standard API off-peak |
| Xiaomi MiMo | Xiaomi MiMo-V2.6-Flash | 1.00x | ¥0.02 | 1.40x | ¥0.94 | 1.00x | ¥1.87 | Overseas real-time API |

## 重要说明

- 当前收录规则（2026-10-24 更新）：OpenAI、Anthropic、xAI 保持既有范围（GPT-5.4+、Claude 4.7+、Grok 4.5+）；其他厂商仅收录最新系列：DeepSeek V4.1、GLM-5.3、Gemini 4、Kimi K3.1、小米 MiMo V2.6，包含系列内符合条件的变体。旧系列即使仍可调用也不再收录。现覆盖 35 个模型、49 条价格记录，保留价格、倍率基准和 USD/CNY 均不变。本规则优先于下方历史更新记录。

- 2026-10-26 重新核查全部八家厂商：未发现符合收录条件的新模型或 token 单价变化，仍覆盖 35 个模型、49 条价格记录。完整加载的 Kimi 价格总览与展开后的 OpenAI Standard 长短上下文表确认保留价格，其余六家官方价格页也与现有记录一致。USD/CNY 仍为 `6.6861`（当前最新可用的美联储 H.10 发布日期为 2026-10-19，数据日期为 2026-10-16）。倍率基准、最新系列范围、已弃用模型排除规则及其他排除项均不变。

- 2026-10-25 重新核查全部八家厂商：未发现符合收录条件的新模型或 token 单价变化，仍覆盖 35 个模型、49 条价格记录。完整加载的 Kimi 价格总览与展开后的 OpenAI Standard 长短上下文表确认保留价格，其余六家官方价格页也与现有记录一致。USD/CNY 仍为 `6.6861`（美联储 H.10，2026-10-19 发布，数据日期为 2026-10-16）。倍率基准、最新系列范围、已弃用模型排除规则及其他排除项均不变。

- 2026-10-24 重新核查全部八家厂商：新增 Kimi K3.1 Pro 和 Kimi K3.1 Pro Highspeed（API ID `kimi-k3.1-pro`、`kimi-k3.1-pro-highspeed`），缓存命中/输入/输出为每 1M tokens USD `0.20/2/10` 和 `0.20/4/20`，已通过完整加载的官方价格总览及模型指南核实。官方明确 K3.1 为新系列，因此按最新系列规则移除 Kimi K3。现覆盖 35 个模型、49 条价格记录。其他保留模型的 token 单价、倍率基准及 USD/CNY `6.6861`（美联储 H.10，2026-10-19 发布）均不变。展开后的 OpenAI 长短上下文表及 Claude 价格表确认保留价格。其他排除项保持不变。

- 2026-10-23 重新核查全部八家厂商：未发现符合收录条件的新模型或 token 单价变化。按排除已弃用模型的规则移除 GPT-5.4 Nano：OpenAI 已于 2026-10-01 宣布弃用，计划于 2027-04-01 停止 API 服务，推荐替代模型为 GPT-6 Luna。现覆盖 34 个模型、48 条价格记录。完整加载的 Kimi 总览及展开后的 OpenAI 长短上下文表确认保留模型的价格。倍率基准和 USD/CNY `6.6861`（美联储 H.10，2026-10-19 发布）均不变。最新系列范围及其他排除项保持不变。

- 2026-10-22 重新核查全部八家厂商：新增 GLM-5.3-FlashX-Legal（API ID `glm-5.3-flashx-legal`），官方价格表及模型文档确认缓存命中/输入/输出为每 1M tokens USD `0.075/0.37/1.25`。移除已于 `2026-10-21 10:00 UTC+8` 正式下线的 Xiaomi MiMo-V2.5 和 MiMo-V2.5-Pro。现覆盖 48 个模型、64 条价格记录。保留模型的 token 单价与倍率基准不变，MiMo-V2.6-Flash 现为唯一缓存命中/输出基准。USD/CNY 仍为 `6.6861`（美联储 H.10，2026-10-19 发布）。完整加载的 Kimi 总览和展开后的 OpenAI 长短上下文表确认原有价格。GLM-5-Turbo 仍未出现在官方价格表中，保留旧值并标记为 `unverified`。其他既有排除项保持不变。

- 2026-10-21（北京时间 10:00 前）重新核查全部八家厂商：未发现符合收录条件的新模型或已核实的 token 单价变化，仍覆盖 49 个模型、65 条价格记录。按美联储 H.10 于 2026-10-19 发布的 2026-10-16 数据，将 USD/CNY 更新为 `6.6861` 并重算人民币约价；美元单价和倍率不变。完整加载的 Kimi 总览及展开后的 OpenAI 长短上下文价格表确认原有价格。MiMo-V2.5 与 MiMo-V2.5-Pro 在 `2026-10-21 10:00 UTC+8` 前仍可用，截止前保留按 V2.6 路由价格计费的两行。GLM-5-Turbo 仍未列入官方价格表，继续标记为 `unverified`。新列出的 gpt-rosalind-discovery 属于专用生命科学模型，不纳入本比较；图像/音频/视频/实时/TTS 及其他既有排除项保持不变。

- 2026-10-20 重新核查全部八家厂商：未发现符合收录条件的新模型或已核实的 token 单价变化。仍覆盖 49 个模型、65 条价格记录；美元单价、倍率与 USD/CNY `6.6920`（美联储 H.10 最新一期，2026-10-13 发布）均不变。Kimi 官方价格总览确认保留的四个价格。DeepSeek `deepseek-flash` 仍由快照 `DeepSeek-V4.1-Flash-1017` 提供服务，V4 Pro 单价不变。Claude、OpenAI、Gemini、xAI 与 Z.AI 价格表均与现有记录一致。小米仍只列出 V2.6 价格；MiMo-V2.5 与 MiMo-V2.5-Pro 请求自动路由至 V2.6，旧 ID 将于 `2026-10-21 10:00 UTC+8` 失效，在此之前保留两行。GLM-5-Turbo 仍未出现在 Z.AI 官方价格表中，沿用此前数值并标记为 `unverified`。图像/音频/视频/实时/TTS 模型及低于 4.5 的 Grok 版本继续排除。

- 2026-10-19 重新核查全部八家厂商：未发现符合收录条件的新模型或已核实的 token 单价变化。仍覆盖 49 个模型、65 条价格记录；美元单价、倍率与 USD/CNY `6.6920`（美联储 H.10 最新一期，2026-10-13 发布）均不变。Kimi 官方价格总览确认保留的四个价格。DeepSeek `deepseek-flash` 仍由快照 `DeepSeek-V4.1-Flash-1017` 提供服务，V4 Pro 单价不变。Claude、OpenAI、Gemini、xAI 与 Z.AI 价格表均与现有记录一致。小米仍只列出 V2.6 价格；MiMo-V2.5 与 MiMo-V2.5-Pro 请求自动路由至 V2.6，旧 ID 将于 `2026-10-21 10:00 UTC+8` 失效，在此之前保留两行。GLM-5-Turbo 仍未出现在 Z.AI 官方价格表中，沿用此前数值并标记为 `unverified`。图像/音频/视频/实时/TTS 模型及低于 4.5 的 Grok 版本继续排除。

- 2026-10-18 重新核查全部八家厂商：未发现符合收录条件的新模型或已核实的 token 单价变化。仍覆盖 49 个模型、65 条价格记录；美元单价、倍率与 USD/CNY `6.6920`（美联储 H.10 最新一期，2026-10-13 发布）均不变。Kimi 官方价格总览确认保留的四个价格。DeepSeek `deepseek-flash` 现由快照 `DeepSeek-V4.1-Flash-1017` 提供服务，单价不变；Search 与 Fetch 工具费用（各为每 1,000 次成功请求 USD `0.75`，不计入本表）经 DeepSeek Harness、Claude Code 和 Codex 调用时暂免，按次计费自北京时间 `2026-11-01 00:00` 开始。小米仍只列出 V2.6 价格；MiMo-V2.5 与 MiMo-V2.5-Pro 请求自动路由至 V2.6，旧 ID 将于 `2026-10-21 10:00 UTC+8` 失效，在此之前保留两行。GLM-5-Turbo 仍未出现在 Z.AI 官方价格表中，沿用此前数值并标记为 `unverified`。图像/音频/视频/实时/TTS 模型及低于 4.5 的 Grok 版本继续排除。

- 2026-10-17 重新核查全部八家厂商：未发现符合收录条件的新模型或已核实的 token 单价变化。仍覆盖 49 个模型、65 条价格记录；美元单价、倍率与 USD/CNY `6.6920`（美联储 H.10 最新一期，2026-10-13 发布）均不变。Kimi 官方价格总览确认保留的四个价格。DeepSeek 价格页新列出 Search 与 Fetch 工具费用（各为每 1,000 次成功请求 USD `0.75`），属于工具费用，不计入本表。小米价格页仍只列 V2.6 价格；MiMo-V2.5 与 MiMo-V2.5-Pro 请求已自动路由至 V2.6，模型 ID 将于 `2026-10-21 10:00 UTC+8` 失效，因此两行保留至该时间。GLM-5-Turbo 仍未出现在 Z.AI 官方价格表中，沿用此前数值并标记为 `unverified`。图像/音频/视频/live/TTS 模型以及低于 4.5 的 Grok 版本继续排除。

- 2026-10-16 重新核查全部八家厂商：未发现符合收录条件的新模型或已核实的 token 单价变化。仍覆盖 49 个模型、65 条价格记录；美元单价、倍率与 USD/CNY `6.6920`（美联储 H.10 最新一期，2026-10-13 发布）均不变。Kimi 官方价格总览确认保留的四个价格。Gemini 价格页新列出的 Gemini Robotics ER 2 Preview（专用具身推理模型）和 Gemini Embedding 2（embeddings）不纳入。小米价格页仍只列 V2.6 价格；MiMo-V2.5 与 MiMo-V2.5-Pro 请求已自动路由至 V2.6，模型 ID 将于 `2026-10-21 10:00 UTC+8` 失效，在此之前保留两行。GLM-5-Turbo 仍未出现在 Z.AI 官方价格表中，保留旧值并标记为 `unverified`。图像/音频/视频/live/TTS 模型及低于 4.5 的 Grok 版本继续排除。

- 2026-10-15 重新核查全部八家厂商：新增 Gemini 4 Argon（API ID `gemini-4-argon`），这是 Google 新发布的稳定版旗舰推理模型。当前 Standard 缓存命中/输入/输出为每 1M tokens USD `0.10/2/10` 的推出价，有效至 `2026-11-30`；自 `2026-12-01` 起为 USD `0.20/4/20`。该模型采用与输出共享的 `1,048,576` tokens 统一上下文窗口（默认输出上限 `65,536`，long decode 最高 `1,048,576`），仅支持隐式缓存。现覆盖 49 个模型、65 条价格记录。未发现其他符合收录条件的新模型或已核实的 token 单价变化；原有美元单价与倍率基准不变。人民币约价按 USD/CNY `6.6920` 重算（美联储 H.10 于 2026-10-13 发布的 2026-10-09 数据）。小米价格页仍只列 V2.6 价格；MiMo-V2.5 与 MiMo-V2.5-Pro 请求已自动路由至 V2.6，模型 ID 将于 `2026-10-21 10:00 UTC+8` 失效，在此之前保留两行。GLM-5-Turbo 仍未出现在 Z.AI 官方价格表中，保留旧值并标记为 `unverified`。图像/音频/视频/live/TTS 模型及低于 4.5 的 Grok 版本继续排除。

- 2026-10-14 重新核查全部八家厂商：未发现符合收录条件的新模型或已核实的 token 单价变化。仍覆盖 48 个模型、64 条价格记录；美元单价、倍率及 USD/CNY 6.7038 均未变化。Kimi 官方价格总览确认了四条保留价格。小米价格页现仅列出 V2.6 价格行，并将 MiMo-V2.5 与 MiMo-V2.5-Pro 标为即将弃用；自北京时间 `2026-10-14 18:00` 起请求自动路由至 V2.6，模型 ID 于 `2026-10-21 10:00` 失效，两行在此之前继续保留。GLM-5-Turbo 仍未出现在 Z.AI 官方价格表中，继续保留旧值并标为 `unverified`（待核验）。图像、音频、视频及受限研究模型继续排除。

- 2026-10-13 重新核查全部八家厂商：未发现符合收录条件的新模型或已核实的 token 单价变化。仍覆盖 48 个模型、64 条价格记录；美元单价、倍率及 USD/CNY 6.7038 均未变化。Kimi 官方价格总览确认了四条保留价格。小米新公告 MiMo-V2.5 与 MiMo-V2.5-Pro 的请求将自北京时间 `2026-10-14 18:00` 起自动路由至 V2.6，模型 ID 仍于 `2026-10-21 10:00` 失效；两行在此之前继续保留。GLM-5-Turbo 仍未出现在 Z.AI 官方价格表中，继续保留旧值并标为 `unverified`（待核验）。图像、音频、视频及受限研究模型继续排除。

- 2026-10-12 重新核查全部八家厂商：未发现符合收录条件的新模型或已核实的 token 单价变化。仍覆盖 48 个模型、64 条价格记录；美元单价、倍率及 USD/CNY 6.7038 均未变化。浏览器完整加载的 Kimi 官方价格总览确认了四条保留价格。GLM-5-Turbo 仍未出现在 Z.AI 官方价格表中，继续保留旧值并标为 `unverified`（待核验）。图像、音频、视频及受限研究模型继续排除。

- 2026-10-11 重新核查全部八家厂商：移除已弃用的 Gemini 3.5 Flash 和 Gemini 3.7 Flash，其请求分别自动路由至 Gemini 3.6 Flash 和 Gemini 3.8 Flash。现覆盖 48 个模型、64 条价格记录。未发现符合收录条件的新模型或已核实的 token 单价变化；保留记录的美元单价、倍率及 USD/CNY 6.7038 均未变化。浏览器完整加载的 Kimi 官方价格总览确认了四条价格。GLM-5-Turbo 仍未出现在 Z.AI 官方价格表中，继续保留旧值并标为 `unverified`（待核验）。

- 2026-10-10 重新核查全部八家厂商：未发现符合收录条件的新模型或已核实的 token 单价变化。仍覆盖 50 个模型、66 条价格记录；美元单价、倍率及 USD/CNY 参考汇率 6.7038 均未变化。浏览器完整加载的 Kimi 官方价格总览确认了保留的四条价格。GLM-5-Turbo 仍未出现在 Z.AI 官方价格表中，继续保留旧值并标为 `unverified`（待核验）。已更新 OpenAI 数据驻留备注：GPT-6 Sol/Luna 的欧盟驻留支持 Fast，GPT-6.1 Sol 的美国及欧盟驻留支持 Fast 和 Ultrafast。图像、音频、视频模型继续排除。

- 2026-10-09 重新核查全部八家厂商：未发现符合收录条件的新模型或已核实的 token 单价变化。仍覆盖 50 个模型、66 条价格记录；美元单价、倍率及 USD/CNY 参考汇率 6.7038 均未变化。浏览器完整加载的 Kimi 和 DeepSeek 官方价格页确认了原有价格。GLM-5-Turbo 仍未出现在 Z.AI 官方价格表中，继续保留此前数值并标为 `unverified`（待核验）。新列出的图像、音频、视频模型继续排除。

- 于 2026-10-08 再次复核全部八家厂商：Claude Sonnet 5.5 缓存读取现为每 1M tokens USD `0.10`，此前记录为 `0.20`；输入/输出仍为 USD `2/10`。已将命中倍率更新为 `35.71x`、人民币约价更新为 `0.67`，并调整表格排序。浏览器完整加载的 Kimi 官方价格总览确认了四条原有价格，已移除其待核验标记并将来源链接更新为总览页。仅 GLM-5-Turbo 仍待核验。未发现符合纳入规则的新模型，仍共 50 个模型、66 条价格记录；倍率基准和美元兑人民币参考汇率 6.7038 未变。新列出的图像、音频、视频模型继续排除。

- 2026-10-08 重新核查全部八家厂商：新增 Claude Haiku 5.5（API ID `claude-haiku-5-5`），按 100K 输入 tokens 阈值拆成两行。短上下文（<=100K）的缓存命中/输入/输出价为 USD `0.01/0.10/0.50`，长上下文（>100K）为 USD `0.05/0.50/2.50` / 1M tokens；与 GPT-6 Luna 短上下文并列输入价格基准。现覆盖 50 个模型、66 条价格记录；已有美元单价、倍率及 USD/CNY 6.7038 均未变化。四条 Kimi 记录和 GLM-5-Turbo 仍标为 unverified，保留此前数值。Haiku 5.5 支持 1M 上下文、128K 最大输出并使用新版 tokenizer；缓存写入、Batch、fast mode 和 US-only inference 加价不纳入主表。

- 2026-10-07 重新核查全部八家厂商：未发现符合纳入条件的新模型或已核实的 token 单价变化。仍覆盖 49 个模型、64 条价格记录；美元单价及倍率不变。人民币约价按 USD/CNY 6.7038 重算（美联储 H.10 于 2026-10-05 发布的 2026-10-02 数据）。四条 Kimi 记录和 GLM-5-Turbo 仍标记为 unverified，保留此前数值。

- 2026-10-06 重新核查全部八家厂商：未发现符合纳入条件的新模型或已核实的 token 单价变化。仍覆盖 49 个模型、64 条价格记录；美元价格、倍率及 USD/CNY 参考汇率 6.7110 均未变化。四条 Kimi 记录和 GLM-5-Turbo 仍标记为 unverified，保留此前数值。

- 2026-10-05 重新核查全部八家厂商：未发现符合纳入条件的新模型或已核实的 token 单价变化。仍覆盖 49 个模型、64 条价格记录；美元价格、倍率及 USD/CNY 参考汇率 6.7110 均未变化。四条 Kimi 记录和 GLM-5-Turbo 仍标记为 unverified，保留此前数值。

- 2026-10-04 重新核查全部八家厂商：未发现符合纳入条件的新模型或已核实的 token 单价变化。仍覆盖 49 个模型、64 条价格记录；美元价格、倍率及 USD/CNY 参考汇率 6.7110 均未变化。四条 Kimi 记录和 GLM-5-Turbo 仍标记为 unverified，保留此前数值。

- 2026-10-03 重新核查全部八家厂商：未发现符合纳入条件的新模型或已核实的 token 单价变化。仍覆盖 49 个模型、64 条价格记录；美元价格、倍率及 USD/CNY 参考汇率 6.7110 均未变化。四条 Kimi 记录和 GLM-5-Turbo 仍标记为 unverified，保留此前数值。

- 于 2026-10-02 复核全部八家厂商：未发现符合收录条件的新模型或已核实的 token 单价变化。仍为 49 个模型、64 条价格记录，美元单价、倍率及美元兑人民币参考汇率 6.7110 均未变。四条 Kimi 记录与 GLM-5-Turbo 继续保留旧值并标为待核验。

- 于 2026-10-01 复核全部八家厂商：未发现符合收录条件的新模型或已核实的 token 单价变化。仍为 49 个模型、64 条价格记录，美元单价、倍率及美元兑人民币参考汇率 6.7110 均未变。四条 Kimi 记录与 GLM-5-Turbo 继续保留旧值并标为待核验。已更新 GPT-6 Sol/Luna 的欧盟数据驻留说明：当前模型文档支持 Standard、Flex 和 Batch。

- 于 2026-09-30 复核全部八家厂商：新增 GPT-6.1 Sol（API ID `gpt-6.1-sol`），短/长上下文缓存命中、输入、输出单价分别为 USD `0.10/2/10` 和 `0.20/4/15` / 1M tokens，现共 49 个模型、64 条价格记录。已有美元单价及倍率基准未变；人民币约价按最新参考汇率 `1 USD = 6.7110 CNY` 重算。四条 Kimi 记录与 GLM-5-Turbo 仍无法核实当前价格，继续保留旧值并标为待核验。GPT-6.1 Sol 的缓存写入、Batch、Flex、Fast/Ultrafast 和区域加价不纳入主表。

- 于 2026-09-29 复核全部八家厂商：新增 Claude Sonnet 5.5（API ID `claude-sonnet-5-5`），每百万 tokens 缓存命中/输入/输出价格为 USD 0.20/2/10，现共 48 个模型、62 条价格记录。已有美元单价、倍率及美元兑人民币参考汇率 6.6975 均未变。四条 Kimi 记录与 GLM-5-Turbo 因当前官方页面未提供对应价格表，继续标为待核验。

- 于 2026-09-23 加入 xAI：新增 Grok 4.5、4.6、4.7，共 6 条上下文分层价格记录，现共 47 个模型、61 条价格记录。本次添加不改变已有模型价格、各列基准或人民币换算汇率。
- 用户指定 xAI 版本下限：只收录 Grok 4.5 及更新版本。排除更早代际的 Grok 4.20 系列、Grok 4.3 及 Grok Build 0.1；模型代际不按小数或字符串排序判断。
- xAI 采用公共 API 全球端点 Standard 价格。官方价格表对已纳入模型均标注输入达到 `200K`（`>=200K`）时，整个请求适用长上下文价；部分模型页面正文则写作“超过”，本表采用价格表明确标注的边界。Batch、Priority、美国区域加价、工具费用、Imagine/Voice 模型、重复别名和非公共 API 的 Grok 4.7 Fast 渠道版本不纳入。

- 于 2026-09-23 复核官方来源：新增 GPT-6 Sol、GPT-6 Luna、Claude Opus 5.5 和 Xiaomi MiMo-V2.6-Flash/Pro/Pro-UltraSpeed，当时共 44 个模型、55 条价格记录，随后另行加入 xAI。原有 47 行美元单价未变。输入倍率按 GPT-6 Luna 短上下文输入价 USD 0.10 重新计算，人民币约价按 `1 USD = 6.6975 CNY` 更新。Kimi 模型专属链接均跳转至不含价格表的总览页，GLM-5-Turbo 未出现在当前 Z.AI 价格表中；这五行保留旧值并标为 `unverified`（待核验）。
- 已排除的发现项：OpenAI chat-latest 与 Daybreak 别名、低于 OpenAI 版本下限的 gpt-5.3-codex、缺少缓存价格的 OpenAI gpt-5.4-pro 和 gpt-5.5-pro、专用网络安全模型 gpt-5.6-cyber 和专用生命科学模型 gpt-rosalind-research/discovery、OpenAI 图像/音频/视频/转录/deep research/工具行、已废弃或退役 Claude 行、没有单独价格表行的邀请制 Claude Mythos Preview、已退役的 DeepSeek V4 Flash Vision Exp 别名、Z.AI 免费或缺少缓存命中价格的文本行、Z.AI 视觉/图像/音频/视频/工具/agent 行、缺少可比缓存命中文本价格的 Gemini Omni Flash 与 Gemini Omni Flash Preview、低于 Gemini 版本下限的 Gemini 3 Flash Preview、专用具身推理模型 Gemini Robotics ER 2 Preview 与 Streaming Preview、Gemini Embedding 2、Gemini live/audio/TTS/图像生成模型、缺少缓存命中价格的 Kimi Moonshot V1 行、Kimi 促销和代金券、已退役的小米 MiMo V2 旧模型名，以及仅图像/音频/视频/工具计费项。
- 汇率采用近似值 `1 USD = 6.6861 CNY`。该汇率取自 Federal Reserve H.10 current release 中 `2026-10-16` 的 CHINA, P.R. YUAN 数据，发布时间为 `2026-10-19`；实际账单以服务商结算币种和付款时汇率为准。
- DeepSeek V4.1 Flash 使用官方 ID `deepseek-flash`。低谷缓存命中/输入/输出为 USD `0.003/0.15/0.60`，高峰为 `0.006/0.30/1.20` / 1M tokens。当前由快照 `DeepSeek-V4.1-Flash-1017` 提供服务。旧 `deepseek-v4-flash` 和 `deepseek-v4-flash-vision-exp` 已退役，其别名请求由 V4.1 Flash 服务并按新价计费。V4 Pro 按最新系列规则排除。官方当前高峰时段为周一至周五 UTC `01:00-04:00`、`06:00-10:00`，中国公共假日除外；其余时间、周末及中国公共假日全天均按低谷价计费。
- Xiaomi MiMo-V2.6-Flash、MiMo-V2.6-Pro 和 MiMo-V2.6-Pro-UltraSpeed 使用官方海外实时 API 价格。MiMo-V2.5 和 MiMo-V2.5-Pro 已于北京时间 `2026-10-21 10:00` 正式下线并从本表移除。国内价格已写入 CSV 备注；缓存写入当前限时免费，Batch 和联网搜索费用未纳入。小米价格页更新时间为 `2026-10-21`。
- Kimi K3.1 Pro 和 Pro Highspeed 价格已于 2026-10-24 通过官方价格总览核实，均支持自动缓存和 `1,048,576` tokens 上下文。5 分钟/1 小时 TTL 缓存写入费用分别为 Pro USD `2/4`、Highspeed USD `4/8` / 1M tokens，不计入主表，促销和代金券亦排除。API 访问需要成功充值（最低 USD 1）。K3 和 K2.x 按最新系列规则排除。
- Gemini 4 Argon 使用官方 `gemini-4-argon` 付费 Standard 价格：缓存命中/输入/输出在 `2026-11-30` 前为 USD `0.10/2/10`，自 `2026-12-01` 起为 USD `0.20/4/20`。该模型仅支持隐式缓存，因此不涉及显式缓存存储费用。
- OpenAI GPT-5.4、GPT-5.5、GPT-5.6 和 GPT-6 使用直接 API Standard 价格。主模型按 `272K` 输入 tokens 阈值拆成短上下文和长上下文行；GPT-5.4 Mini 只列官方短上下文 Standard 价格。GPT-6 Sol 和 Luna 超出该阈值时，整个请求按 2 倍输入/缓存价和 1.5 倍输出价计费。GPT-5.6 Sol 当前 Standard 促销价至少持续至 `2026-11-21`。缓存写入、Batch、Flex、Fast mode 未纳入主表；可用区域处理另加 `10%`，GPT-6 Sol/Luna 的欧盟数据驻留支持 Standard、Fast、Flex 和 Batch；GPT-6.1 Sol 的美国及欧盟数据驻留支持 Fast 和 Ultrafast。
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
- OpenAI gpt-6-sol: https://developers.openai.com/api/docs/models/gpt-6-sol
- OpenAI gpt-6-luna: https://developers.openai.com/api/docs/models/gpt-6-luna
- Claude Haiku 5.5: https://platform.claude.com/docs/en/models/haiku-5-5/overview
- Claude Sonnet 5.5: https://platform.claude.com/docs/en/models/sonnet-5-5/overview
- Claude Opus 5.5: https://platform.claude.com/docs/en/models/opus-5-5/overview
- Anthropic pricing: https://platform.claude.com/docs/en/about-claude/pricing
- DeepSeek pricing: https://api-docs.deepseek.com/quick_start/pricing/
- Z.AI pricing: https://docs.z.ai/guides/overview/pricing
- GLM-5.3-Flash/FlashX/FlashX-Legal model IDs: https://docs.z.ai/guides/vlm/glm-5.3-flash
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

- Kimi K3.1 Pro / Highspeed model guide: https://platform.kimi.ai/docs/guide/kimi-k3-1-pro-quickstart
