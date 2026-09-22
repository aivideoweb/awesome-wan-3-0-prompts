# 🎬 Awesome Wan 3.0 Prompts｜万相 3.0 视频提示词中文精选库

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Prompts](https://img.shields.io/badge/Wan_3.0_Prompts-120-blueviolet)](#-场景提示词库)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/aivideoweb/awesome-wan-3-0-prompts/pulls)
[![中文](https://img.shields.io/badge/简体中文-当前-red)](README.zh-CN.md)
[![English](https://img.shields.io/badge/English-Read-blue)](README.md)
[![日本語](https://img.shields.io/badge/日本語-読む-blue)](README.ja.md)
[![Español](https://img.shields.io/badge/Español-Leer-blue)](README.es.md)

> 120 组可直接复制、可继续改写的 **Wan 3.0 / 万相 3.0 AI 视频提示词**，覆盖电影短片、产品广告、电商美妆、人物对白、多语言本地化、自然动物、季节变化、工业制造、教育科学、建筑交通与专业制作控制。每组提示词都包含动作连续性、镜头安排、素材一致性或声音设计等具体要求。

| [浏览 120 条提示词](prompts/README.md) | [提交验证过的 Prompt](https://github.com/aivideoweb/awesome-wan-3-0-prompts/issues/new?template=prompt.yml) | [补充翻译](CONTRIBUTING.zh-CN.md#本地化要求) | [发起 Pull Request](https://github.com/aivideoweb/awesome-wan-3-0-prompts/pulls) |
|---|---|---|---|

![Awesome Wan 3.0 video prompts collection](assets/videoweb-wan-3-hero.png)

**按需阅读：**[120 条基础提示词](prompts/README.md) · [9 个 X 视频案例](guides/x-community-showcase.md) · [6 条补充练习](prompts/community-practice.md) · [JSON 下载](downloads/prompts.json) · [纯文本下载](downloads/prompts.txt)。基础提示词继承自源库，尚未逐条在 VideoWeb 验证。15 种语言提供阅读入口和对照示例，不代表 120 条提示词均有 15 种完整翻译。[内容与图片来源](UPSTREAM.md)。

## 在 VideoWeb AI 开始创作

打开 [VideoWeb AI 的 Wan 3.0 页面](https://videoweb.ai/model/wan-3-0/)，选择文字或图片输入，粘贴提示词，再按界面选择时长、画幅和清晰度。先做一个短镜头，每次只改一项。[操作指南](guides/videoweb-workflow.zh-CN.md) · [X 视频案例](guides/x-community-showcase.md)。

## 为什么值得收藏

- **不是关键词堆砌**：每个提示词包含主体、环境、动作因果、摄影机、光线、节奏、声音和约束。
- **为 Wan 工作流细化**：分别说明文生视频、图生视频、参考生视频、首尾帧和视频编辑的写法。
- **120 个源库实用场景**：从 6 秒单镜头到多镜头广告、教育演示和专业制作素材均可快速改造。
- **15 种语言入口**：提供本地化提示公式和完整对照场景；对白语言与画面描述语言可分开控制。
- **适合 SEO 与二次开发**：稳定的分类、描述性文件名、语义化标题和带来源说明的本地封面便于构建画廊或站点。

## 欢迎分享真实有效的 Prompt

如果你的 Wan 3.0 提示词生成了值得研究的结果，欢迎使用[结构化投稿表单](https://github.com/aivideoweb/awesome-wan-3-0-prompts/issues/new?template=prompt.yml)。每次提交一条完整提示词，并尽量附上工作流、时长、画幅、测试平台、结果链接或截图；只能上传你有权分享的素材。维护者会在审核和测试后，统一重写格式并归入合适专题。

也欢迎通过 Pull Request 提交新场景、成功/失败对照、更自然的翻译或无障碍改进。投稿不要求先写英文：对白和画面文字可以使用任何语言，但需明确说话者、时序与画面指令。发送媒体或参考素材前请阅读[中文贡献指南](CONTRIBUTING.zh-CN.md)。

> [!IMPORTANT]
> Wan 3.0 的具体入口、时长、分辨率、参考素材数量和音频能力可能因地区、产品版本或测试阶段而不同。本仓库以提示工程与创作方法为核心，不虚构固定参数；请以你所使用平台的当前界面和官方文档为准。大多数模板也可向下兼容 Wan 2.6 / 2.7，删去平台不支持的输入项即可。

## 🚀 60 秒上手

一个稳定的 Wan 视频提示词通常按这个顺序写：

```text
[输出] 时长 + 画幅 + 视觉类型
[主体] 固定身份锚点 + 服装/材质 + 不可变化项
[环境] 时间 + 地点 + 天气 + 空间层次
[动作] 起因 → 连续动作 → 明确结果
[镜头] 景别 + 机位 + 运动路径 + 转场
[视觉] 光线 + 色彩 + 质感 + 运动模糊
[声音] 环境音 + 动作音 + 音乐 + 对白语言（平台支持时）
[约束] 保持什么 + 避免什么
```

最小可用示例：

```text
8 秒，16:9，写实电影感。雨后清晨的老街，一名穿深绿色风衣的年轻邮差骑旧式自行车穿过浅水洼；前轮压过水面，水珠先向两侧散开，再落回石板路。摄影机以膝盖高度从侧后方平稳跟拍，前 2 秒中景建立环境，随后缓慢靠近手部和车铃，最后抬升到街道尽头的暖色晨光。自然阴天软光，湿润石材纹理清晰，动作速度真实。声音：轮胎碾水、远处开店卷帘门、一次清脆车铃。保持人物脸、风衣、自行车结构一致；不要字幕、标志、额外肢体、突然跳切或漂浮物体。
```

## 🧭 按输入方式选择写法

| 模式 | 最重要的信息 | 推荐写法 |
|---|---|---|
| 文生视频 T2V | 世界、主体、动作与摄影机 | 先写单一事件，再补风格；不要同时塞入多个无关高潮 |
| 图生视频 I2V | 首帧中已有的内容与“如何动” | 少重复外观，多写动作幅度、物理反馈、镜头路径和禁止形变 |
| 首尾帧 | 两帧之间可解释的变化 | 写清变化的触发、过程和最终状态，避免瞬移式结果 |
| 参考生视频 R2V | 每份素材承担的角色 | 用“图片 1 是人物身份、视频 1 是动作节奏”等方式显式绑定 |
| 视频编辑 | 只修改的维度 | 使用“仅改变天气；保持人物、动作、构图和时长不变” |
| 音频/对白驱动 | 谁在何时发声以及镜头为何响应 | 对白短句化，注明语言、情绪、停顿和非说话者闭嘴 |

完整方法见 [Wan 3.0 提示词写作指南](guides/prompting-guide.md)，能力边界见 [模型与平台兼容说明](guides/model-capabilities.md)，常见失败处理见 [故障排查手册](guides/troubleshooting.md)。

## Wan 3.0 模型介绍：四种生产工作流

Wan 3.0 更适合作为一套覆盖创意到交付的视频生产模型家族来使用，而不是只把它当成“输入一句话生成视频”的工具：没有素材时用文生视频探索创意；构图已经确定时用图生视频控制首帧与运动；已有片段接近目标时用视频编辑只修改一个维度；需要角色、风格、动作或音频连续性时，再选择参考生视频。无论采用哪条路径，本仓库都建议优先写清时间因果、连续动作、镜头路径、身份锚点、物理反馈、声音设计和少量针对性的负面约束。

| Wan 3.0 工作流 | 最适合的起点 | 提示词重点 |
|---|---|---|
| 文生视频 | 创意简报、脚本或分镜想法 | 场景 → 动作 → 镜头 → 视觉与声音 |
| 图生视频 | 产品图、角色定帧、设计好的首帧/尾帧 | 保持构图与身份，明确运动幅度和中间过程 |
| 视频编辑 | 已经基本正确的现有视频 | 只修改一个维度，锁定其余内容 |
| 参考生视频 | 身份、风格、动作、视频或音频参考 | 给每份素材指定唯一且明确的参考职责 |

## 🔥 精选场景

### 1. 雨夜摩托追逐｜动作连续性

![Wan 3.0 cinematic action prompt example](assets/covers/cinematic-action.webp)

```text
10 秒，2.39:1，写实动作电影。暴雨中的未来海滨高架，两名骑手依次压弯进入长弧弯道，轮胎排水在身后形成低矮扇形水雾；前车短暂回头确认距离，后车降低重心但不发生碰撞。摄影机贴近路面从后侧跟随，穿过护栏反光后平滑移动到前车侧面，最后在列车驶过上方时轻微减速。湿地反射符合透视，车轮持续接触路面，速度感由背景拖影而不是车辆形变产生。声音：引擎转速、轮胎排水、雨击头盔、列车低频轰鸣。保持车辆结构和骑手服装一致；无品牌、无事故、无多余车辆突然出现。
```

### 2. 翡翠香氛微距广告｜商品一致性

![Wan 3.0 product commercial prompt example](assets/covers/product-commercial.webp)

```text
8 秒，16:9，高端虚构香氛广告。无文字的深绿色切面玻璃瓶悬停于黑色镜面水面上方，金色瓶盖始终保持几何完整。0-2 秒微距拍摄一滴水沿玻璃棱线下滑；2-5 秒摄影机顺时针环绕 60 度，半透明叶片与液体丝带被气流带起；5-8 秒瓶身轻缓下降，接近水面时形成同心波纹，金色轮廓光勾勒瓶盖。黑、翡翠绿、暖金配色，真实折射与焦散。只有液体和叶片运动，产品比例、标签空白区、瓶盖位置不变；无文字、无商标、无手、无突然爆炸。
```

### 3. 云海纸鹤门｜东方幻想

![Wan 3.0 eastern fantasy prompt example](assets/covers/eastern-fantasy.webp)

```text
12 秒，2.39:1，克制的东方奇幻电影。黎明云海上，一名身穿象牙白与靛蓝长袍的原创女剑客站在狭窄玄武岩桥端，脸、发髻、腰间旧剑全程一致。纸鹤先从近景逆风掠过，再围绕远处太阳形成螺旋门；她没有拔剑，只向前迈一步，衣摆和发丝受同一方向山风影响。摄影机从超广角建立镜头缓慢推近至全身景，最后轻微升高显露纸鹤门后的群峰。云雾体积感、空间遮挡和纸张折光真实，淡墨粒子仅出现在远景边缘。声音：山风、纸翼轻响、远处钟声一次。不要已有影视角色、不要漂浮肢体、不要夸张法术爆炸、不要文字。
```

## 从真实案例学习

下面两条作者原帖有完整提示词。缩略图打开原帖视频；它们不是本仓库在 VideoWeb 生成的结果。涉及参考图或不同模型对比时，请先读案例页的说明。

### Before the Void Swallows You — @0xbisc

[![Before the Void Swallows You](https://pbs.twimg.com/amplify_video_thumb/2093296405674893312/img/KrpfnTtMVpRJboxK.jpg)](https://x.com/0xbisc/status/2093296541834653883/video/1)

[查看作者完整提示词](https://x.com/0xbisc/status/2093296546926539136) · [学习重点与已知限制](guides/x-community-showcase.md#void-escape)

### Five-shot mountain survival story — @chatgptpaglu

[![Five-shot mountain survival story](https://pbs.twimg.com/amplify_video_thumb/2094707623602053120/img/bRfC47Flglx2mSJd.jpg)](https://x.com/chatgptpaglu/status/2094710054675157354/video/1)

[查看作者完整提示词](https://x.com/chatgptpaglu/status/2094710054675157354) · [学习重点与已知限制](guides/x-community-showcase.md#cable-car-story)

[查看全部 9 个视频案例](guides/x-community-showcase.md) · [6 条独立练习](prompts/community-practice.md)

## 📚 场景提示词库

需要一次浏览全部标题？打开 [120 场景总索引](prompts/README.md)。

| 分类 | 数量 | 适用内容 | 文件 |
|---|---:|---|---|
| 🎞️ 电影叙事与镜头语言 | 6 | 情绪短片、悬疑、年代戏、一镜到底 | [查看提示词](prompts/cinematic-storytelling.md) |
| 🛍️ 商品广告与品牌视觉 | 6 | 美妆、食品、科技、家居、时尚、汽车 | [查看提示词](prompts/ads-and-products.md) |
| 📱 UGC、美食与旅行 | 6 | Vlog、探店、开箱、旅行日记、生活方式 | [查看提示词](prompts/ugc-food-travel.md) |
| 🏃 动作、体育与物理特效 | 6 | 追逐、滑雪、球类、跑酷、微缩灾难 | [查看提示词](prompts/action-sports.md) |
| 🐉 动漫、幻想与风格化叙事 | 6 | 2D 动画、3D 动画、仙侠、科幻、童话 | [查看提示词](prompts/anime-fantasy.md) |
| 🎵 音乐、喜剧与社交传播 | 6 | MV、舞蹈、乐队、反转喜剧、萌宠、循环视频 | [查看提示词](prompts/music-comedy-social.md) |
| 💼 专业商业与公共服务 | 11 | SaaS、课程、播客、无障碍、远程医疗、物流 | [查看提示词](prompts/professional-business.md) |
| 🔬 教育、科学与纪录 | 11 | 气候、显微镜、安全、天文、海洋、博物馆 | [查看提示词](prompts/education-science.md) |
| 🏙️ 建筑、酒店与交通 | 11 | 房地产、公共空间、无障碍路线、电助力车、轨道交通 | [查看提示词](prompts/architecture-mobility.md) |
| 🎛️ 专业制作与编辑控制 | 11 | 绿幕、白模预演、商品旋转、局部编辑、多参考、循环 | [查看提示词](prompts/production-control.md) |
| 🛒 电商、美妆与零售 | 10 | 试穿、带货演示、护肤、包装、无障碍零售、批量商品目录 | [查看提示词](prompts/commerce-beauty-retail.md) |
| 🗣️ 人物、对白与本地化 | 10 | 对话轮次、配音、手语、播客、口述史、多语言短剧 | [查看提示词](prompts/people-dialogue-localization.md) |
| 🦊 自然、动物与季节 | 10 | 野生动物、动物照护、天气、微距自然、季节变化、天文台 | [查看提示词](prompts/nature-animals-seasons.md) |
| 🏭 工业与制造 | 10 | 培训、协作机器人、检测、冷链、数字孪生、批量 SKU | [查看提示词](prompts/industrial-manufacturing.md) |

**共计 120 组完整提示词。** 基础场景、人物、商品和对白继承自 MIT 许可的源库；分类插图沿用源库，VideoWeb 主封面重新制作。社区视频保留作者归属，详见[来源说明](UPSTREAM.md)。

## 🆕 四个实用生产专题

[![电商、美妆与零售场景插图](assets/covers/commerce-beauty-retail.webp)](prompts/commerce-beauty-retail.md)

电商与零售专题覆盖服装动态试穿、质地对比、产品功能、包装连续性、柜台咨询和批量商品广告。[查看 10 条提示词 →](prompts/commerce-beauty-retail.md)

[![人物、对白与本地化场景插图](assets/covers/people-dialogue-localization.webp)](prompts/people-dialogue-localization.md)

人物与语言专题覆盖干净的说话轮次、多语言对白、配音编辑、手语取景、播客、纪录片旁白和口述史。[查看 10 条提示词 →](prompts/people-dialogue-localization.md)

[![自然、动物与季节场景插图](assets/covers/nature-animals-seasons.webp)](prompts/nature-animals-seasons.md)

自然专题强调野生动物的非侵入式观察、动物照护、微距物理、天气与季节变化。[查看 10 条提示词 →](prompts/nature-animals-seasons.md)

[![工业与制造场景插图](assets/covers/industrial-manufacturing.webp)](prompts/industrial-manufacturing.md)

工业专题覆盖安全预演、协作机器人、设施解释、质量检测、冷链、数字孪生和多 SKU 批量生产。[查看 10 条提示词 →](prompts/industrial-manufacturing.md)

## 🌍 多语言提示策略

Wan 工作流通常可以理解多语言提示。为了让画面与台词更稳定，建议把“描述语言”和“对白语言”分开：

```text
Visual description: English cinematic production language.
Spoken dialogue: Mandarin Chinese, natural Beijing accent.
Exact line: “今天的风，终于往海边吹了。”
No subtitles. The listener keeps their mouth closed.
```

- **中文**：适合叙事、情绪、动作因果和东方文化语境。
- **英文**：适合镜头、灯光、材质与制作术语。
- **日文/西班牙文等对白**：保留原句，并补充情绪、语速、口音和是否需要字幕。
- 不要逐字堆叠同义翻译；优先使用一种主描述语言，只保留必须精确呈现的其他语言文本。

更多例子见 [多语言章节](guides/prompting-guide.md#多语言与对白)。

查看[15 种语言目录](locales/README.md)：英文、简体中文、繁体中文、日文、韩文、西班牙文、法文、德文、巴西葡萄牙文、意大利文、阿拉伯文、俄文、印度尼西亚文、泰文和越南文。

## ✅ 提升成功率的 10 条规则

1. 一个短片围绕一个主要事件；多镜头也要共享同一因果线。
2. 给角色写 3–5 个可重复的身份锚点，不要每个镜头换一种形容。
3. 动作使用“先—再—最后”，让模型理解物理过程。
4. 每个镜头只指定一个主要摄影机运动。
5. 图生视频少写静态外观，多写谁动、怎么动、动多大。
6. 用环境反馈表现速度：衣摆、雨水、尘土、反射、背景视差。
7. 产品广告明确“不可变项”：比例、材质、标签、瓶盖、按钮位置。
8. 对白保持短句，为停顿、呼吸和镜头反应留出时间。
9. 负面约束只写最可能出现的问题，避免几十个空泛的否定词。
10. 先生成稳定基础版，再一次只增加一个复杂变量。

## 🧩 可替换变量模板

```text
{时长} 秒，{画幅}，{媒介/风格}。
{时间与地点}，{主体身份锚点}正在{主要动作}。
动作过程：先{动作 A 与反馈}，再{动作 B 与反馈}，最后{结果 C}。
摄影机：{起始景别与机位}，{单一运动路径}，结束于{最终构图}。
光线与色彩：{主光}，{色调}，{材质重点}。
声音：{环境音}，{动作音}，{音乐/对白，可选}。
保持：{身份、服装、物体结构、空间方向}。
避免：{最相关的 3–6 个失败模式}。
```

## 🤝 参与贡献

欢迎提交新的 Wan 3.0 视频提示词、失败案例对照和本地化翻译。单条案例可直接使用 [Prompt 投稿表单](https://github.com/aivideoweb/awesome-wan-3-0-prompts/issues/new?template=prompt.yml)，较大的专题或翻译可发起 Pull Request。请确保内容为原创或拥有明确授权，不要提交带有他人水印、未授权名人肖像、在世艺术家风格仿写或受保护角色的素材。详见[中文贡献指南](CONTRIBUTING.zh-CN.md)或[英文贡献指南](CONTRIBUTING.md)。

## 📄 许可与内容说明

代码与仓库原创文本采用 [MIT License](LICENSE)。VideoWeb 主封面由图像工具新建，分类插图继承自源库，均为示意图，不是 Wan 3.0 的实测视频结果。实际使用生成模型时，请同时遵守所用平台的服务条款、内容政策和当地法律。

本项目是独立的社区提示词资源，不代表模型提供方，也不保证名为 “Wan 3.0” 的不同平台具有完全相同的能力。

---

如果这个 Wan 3.0 prompt library 对你的 AI 视频创作有帮助，欢迎 Star、Fork，并提交你验证过的原创工作流。

## VideoWeb AI 联盟计划

[VideoWeb AI 目前提供 Affiliate Program](https://videoweb.ai/affiliate-program/)，面向推荐其 AI 视频、图片与音乐创作工具的开发者、创作者、教育者、评测者和团队。使用普通 VideoWeb AI 账号登录，完善联盟资料并确认协议后，即可生成自己的推荐链接，在教程、评测、社区、产品或网站中进行分享并获得佣金。

- 被推荐用户的首笔有效付费订单可获得 **20%** 佣金。
- 用户注册后的 **60 天归因期**内，后续有效付费订单可获得 **10%** 佣金。
- 佣金可支付前会审核退款、拒付、风控取消订单、归因状态和政策违规情况。

联盟规则可能调整，推广前请查看最新页面和 Affiliate Agreement。上面的链接是官方计划页面，不是本项目的推荐链接。
