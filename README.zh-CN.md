# 🎬 Awesome Wan 3.0 Prompts｜120 条视频提示词

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE) [![Prompts](https://img.shields.io/badge/Wan_3.0_Prompts-120-blueviolet)](#categories) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/aivideoweb/awesome-wan-3-0-prompts/pulls) [![中文](https://img.shields.io/badge/简体中文-当前-red)](README.zh-CN.md) [![English](https://img.shields.io/badge/English-Read-blue)](README.md) [![日本語](https://img.shields.io/badge/日本語-読む-blue)](README.ja.md) [![Español](https://img.shields.io/badge/Español-Leer-blue)](README.es.md)

**120 条完整提示词模板，覆盖 14 类视频场景，可按平台参数调整**，适合制作商品广告、故事短片、社交视频和知识讲解。选一个场景，按需要修改动作和镜头，再到 [VideoWeb AI 的 Wan 3.0 页面](https://videoweb.ai/model/wan-3-0/)尝试生成。

**[按用途找提示词](#start-here) · [复制入门示例](#quick-start) · [观看视频案例](#community-videos) · [查看全部分类](#categories)**

![VideoWeb AI — Wan 3.0 视频提示词库](assets/videoweb-wan-3-hero.png)

*这是 VideoWeb 维护的社区提示词库。封面为编辑示意图，不是 Wan 3.0 生成结果。*

<a id="start-here"></a>

## 你想制作什么视频？

| 你的目标 | 从这条开始 | 重点练什么 |
|---|---|---|
| 第一次生成短片 | [10 秒杯子开盖](#quick-start) · 中文 | 一个动作、固定镜头，不需要上传图片 |
| 商品广告 | [折叠耳机机械展开](prompts/ads-and-products.md#prompt-02) · 中文 | 铰链动作与商品结构保持一致 |
| 竖屏旅行视频 | [海边民宿入住日记](prompts/ugc-food-travel.md#prompt-02) · 中文 | 在 15 秒内连接四个生活镜头 |
| 双语对白 | [博物馆迎宾](prompts/people-dialogue-localization.md#prompt-01) · 英文 | 一次只让一人说话，听者不动嘴 |
| 动物微距 | [蜂鸟采蜜](prompts/nature-animals-seasons.md#prompt-03) · 英文 | 动作、身体结构与固定观察角度 |
| 后期合成素材 | [绿幕人物表演](prompts/production-control.md#prompt-01) · 英文 | 全身取景、干净边缘；先确认平台支持参考输入 |

[浏览全部 120 个标题](prompts/README.md) · [6 条补充练习](prompts/community-practice.md) · 下载基础模板和补充练习（共 126 条）：[JSON 数据](downloads/prompts.json) / [纯文本](downloads/prompts.txt)。

120 条基础提示词继承自源库，6 条补充练习尚未实测，均未逐条在 VideoWeb 验证。分类文件使用中文或英文；[15 种语言版本](locales/README.md)提供介绍和对照示例，不代表全部提示词都有完整翻译。[内容与图片来源](UPSTREAM.md)。

<a id="quick-start"></a>

## 在 VideoWeb AI 生成第一个视频

1. 打开 [VideoWeb AI 的 Wan 3.0 页面](https://videoweb.ai/model/wan-3-0/)，使用 **Text / Image to Video（文字或图片生成视频）**。下面的例子不需要上传 **Start Frame（首帧）**。
2. 在界面设置 **10 秒、16:9**，选择可用清晰度，粘贴下面的提示词。查看本次费用后再生成。
3. 完整看一遍结果：杯盖是否只开了一次？杯身是否变形？镜头是否突然切换？有问题时先简化一个动作，再比较下一版。

```text
10 秒，16:9。
一个没有文字的陶瓷随行杯放在窗边木质厨房台面上。
摄影机固定在台面高度。
0–2 秒，杯盖关闭，杯子静止；
2–6 秒，一只成年人的手将铰链杯盖打开一次，然后退出画面；
6–10 秒，一缕细蒸汽缓缓上升，杯子继续保持静止。
柔和晨光，真实陶瓷纹理。
支持声音时：一次轻微的开盖声和安静的室内环境音。
保持杯身、杯柄和铰链位置不变。
不要文字、商标、多余手指、跳切或物体融化。
```

这是尚未实测的入门练习，不是社区视频的原始提示词。如果已有商品照片，点击 **Choose Start Frame（选择首帧）**上传图片，再描述需要的动作。详细步骤见[操作指南](guides/videoweb-workflow.zh-CN.md)。

**复制后先核对参数。** 2026-09-22 检查到的表单提供 5、10、15、20、25、30 秒。原模板写 8 秒或 12 秒时，需选可用时长并同步调整各段动作；没有 2.39:1 时，可选现有画幅、给主体留出边缘空间，再后期裁切。提示词不能代替界面设置。声音、尾帧、多参考和视频编辑均需当前模式提供对应功能。

<a id="categories"></a>

## 📚 场景提示词库

需要一次浏览全部标题？打开 [120 场景总索引](prompts/README.md)。

| 分类 | 数量 | 适用内容 | 文件 |
|---|---:|---|---|
| 🎞️ 电影叙事与镜头语言 | 6 | 情绪短片、悬疑、年代戏、一镜到底 | [查看提示词](prompts/cinematic-storytelling.md) |
| 🛍️ 商品广告与品牌视觉 | 6 | 美妆、食品、科技、家居、时尚、汽车 | [查看提示词](prompts/ads-and-products.md) |
| 📱 生活记录、美食与旅行 | 6 | 探店、开箱、旅行日记、生活方式 | [查看提示词](prompts/ugc-food-travel.md) |
| 🏃 动作、体育与物理特效 | 6 | 追逐、滑雪、球类、跑酷、微缩灾难 | [查看提示词](prompts/action-sports.md) |
| 🐉 动漫、幻想与风格化叙事 | 6 | 2D 动画、3D 动画、仙侠、科幻、童话 | [查看提示词](prompts/anime-fantasy.md) |
| 🎵 音乐、喜剧与社交传播 | 6 | 音乐短片、舞蹈、乐队、反转喜剧、萌宠、循环视频 | [查看提示词](prompts/music-comedy-social.md) |
| 💼 专业商业与公共服务 | 11 | 软件服务、课程、播客、无障碍、远程医疗、物流 | [查看提示词](prompts/professional-business.md) |
| 🔬 教育、科学与纪录 | 11 | 气候、显微镜、安全、天文、海洋、博物馆 | [查看提示词](prompts/education-science.md) |
| 🏙️ 建筑、酒店与交通 | 11 | 房地产、公共空间、无障碍路线、电助力车、轨道交通 | [查看提示词](prompts/architecture-mobility.md) |
| 🎛️ 专业制作与编辑控制 | 11 | 绿幕、白模预演、商品旋转、局部编辑、多参考、循环 | [查看提示词](prompts/production-control.md) |
| 🛒 电商、美妆与零售 | 10 | 试穿、带货演示、护肤、包装、无障碍零售、批量商品目录 | [查看提示词](prompts/commerce-beauty-retail.md) |
| 🗣️ 人物、对白与本地化 | 10 | 对话轮次、配音、手语、播客、口述史、多语言短剧 | [查看提示词](prompts/people-dialogue-localization.md) |
| 🦊 自然、动物与季节 | 10 | 野生动物、动物照护、天气、微距自然、季节变化、天文台 | [查看提示词](prompts/nature-animals-seasons.md) |
| 🏭 工业与制造 | 10 | 培训、协作机器人、检测、冷链、数字孪生、批量商品 | [查看提示词](prompts/industrial-manufacturing.md) |

<a id="community-videos"></a>

## 从视频案例学习

**9 个 X 案例，其中 4 个可在作者原帖查看完整提示词。** 先看下面两条。点击缩略图或播放链接进入 X，可能需要登录。这些是第三方作品，并非本仓库在 VideoWeb 上复现的结果。

### 单一角色与追逐方向 — [@0xbisc](https://x.com/0xbisc)

<a href="https://x.com/0xbisc/status/2093296541834653883/video/1"><img src="https://pbs.twimg.com/amplify_video_thumb/2093296405674893312/img/KrpfnTtMVpRJboxK.jpg" alt="Before the Void Swallows You，点击观看 X 原帖视频" width="440"></a>

对照提示词观察：30 秒里如何保持角色一致，让威胁始终位于逃跑方向后方。**复现前注意：**作者提示词需要 Image1 参考图，仓库未提供；原帖标有付费合作。

[▶ 观看视频](https://x.com/0xbisc/status/2093296541834653883/video/1) · [作者完整提示词](https://x.com/0xbisc/status/2093296546926539136) · [另一条追逐练习](prompts/community-practice.md#prompt-03) · [来源与限制](guides/x-community-showcase.md#void-escape)

### 五个镜头连接一个故事 — [@chatgptpaglu](https://x.com/chatgptpaglu)

<a href="https://x.com/chatgptpaglu/status/2094710054675157354/video/1"><img src="https://pbs.twimg.com/amplify_video_thumb/2094707623602053120/img/bRfC47Flglx2mSJd.jpg" alt="五镜头山地故事，点击观看 X 原帖视频" width="440"></a>

作者将 30 秒虚构山地故事拆成五个 6 秒镜头。先读每段动作，再观察人物是否连贯、下一步是否承接上一步。这是故事创作案例，不是逃生指导。原帖注明使用 Lart 上的 Wan 3.0，未提供完整生成参数。

[▶ 观看视频](https://x.com/chatgptpaglu/status/2094710054675157354/video/1) · [作者完整提示词](https://x.com/chatgptpaglu/status/2094710054675157354) · [来源与限制](guides/x-community-showcase.md#cable-car-story)

[查看全部 9 个案例及提示词完整情况](guides/x-community-showcase.md)。[6 条补充练习](prompts/community-practice.md)是独立编写、尚未实测的练习，不是这些视频的原始提示词。

## 精选场景与完整提示词

以下图片沿用源库，仅用于表达场景，不是提示词对应的实测视频。

这些示例保留源库的创作参数。用于 VideoWeb 时，请按上方说明调整时长、画幅与各段动作。

### 1. 雨夜摩托追逐｜动作连续性

![动作追逐场景示意图](assets/covers/cinematic-action.webp)

```text
10 秒，2.39:1，写实动作电影。暴雨中的未来海滨高架，两名骑手依次压弯进入长弧弯道，轮胎排水在身后形成低矮扇形水雾；前车短暂回头确认距离，后车降低重心但不发生碰撞。摄影机贴近路面从后侧跟随，穿过护栏反光后平滑移动到前车侧面，最后在列车驶过上方时轻微减速。湿地反射符合透视，车轮持续接触路面，速度感由背景拖影而不是车辆形变产生。声音：引擎转速、轮胎排水、雨击头盔、列车低频轰鸣。保持车辆结构和骑手服装一致；无品牌、无事故、无多余车辆突然出现。
```

### 2. 翡翠香氛微距广告｜商品一致性

![商品广告场景示意图](assets/covers/product-commercial.webp)

```text
8 秒，16:9，高端虚构香氛广告。无文字的深绿色切面玻璃瓶悬停于黑色镜面水面上方，金色瓶盖始终保持几何完整。0-2 秒微距拍摄一滴水沿玻璃棱线下滑；2-5 秒摄影机顺时针环绕 60 度，半透明叶片与液体丝带被气流带起；5-8 秒瓶身轻缓下降，接近水面时形成同心波纹，金色轮廓光勾勒瓶盖。黑、翡翠绿、暖金配色，真实折射与焦散。只有液体和叶片运动，产品比例、标签空白区、瓶盖位置不变；无文字、无商标、无手、无突然爆炸。
```

### 3. 云海纸鹤门｜东方幻想

![东方幻想场景示意图](assets/covers/eastern-fantasy.webp)

```text
12 秒，2.39:1，克制的东方奇幻电影。黎明云海上，一名身穿象牙白与靛蓝长袍的原创女剑客站在狭窄玄武岩桥端，脸、发髻、腰间旧剑全程一致。纸鹤先从近景逆风掠过，再围绕远处太阳形成螺旋门；她没有拔剑，只向前迈一步，衣摆和发丝受同一方向山风影响。摄影机从超广角建立镜头缓慢推近至全身景，最后轻微升高显露纸鹤门后的群峰。云雾体积感、空间遮挡和纸张折光真实，淡墨粒子仅出现在远景边缘。声音：山风、纸翼轻响、远处钟声一次。不要已有影视角色、不要漂浮肢体、不要夸张法术爆炸、不要文字。
```

## 四个实用专题

以下分类插图沿用源库，用于展示创作方向。

### 电商、美妆与零售

[![电商、美妆与零售场景插图](assets/covers/commerce-beauty-retail.webp)](prompts/commerce-beauty-retail.md)

电商与零售专题覆盖服装动态试穿、质地对比、产品功能、包装连续性、柜台咨询和批量商品广告。[查看 10 条提示词 →](prompts/commerce-beauty-retail.md)

### 人物、对白与本地化

[![人物、对白与本地化场景插图](assets/covers/people-dialogue-localization.webp)](prompts/people-dialogue-localization.md)

人物与语言专题覆盖干净的说话轮次、多语言对白、配音编辑、手语取景、播客、纪录片旁白和口述史。[查看 10 条提示词 →](prompts/people-dialogue-localization.md)

### 自然、动物与季节

[![自然、动物与季节场景插图](assets/covers/nature-animals-seasons.webp)](prompts/nature-animals-seasons.md)

自然专题强调野生动物的非侵入式观察、动物照护、微距物理、天气与季节变化。[查看 10 条提示词 →](prompts/nature-animals-seasons.md)

### 工业与制造

[![工业与制造场景插图](assets/covers/industrial-manufacturing.webp)](prompts/industrial-manufacturing.md)

工业专题覆盖安全预演、协作机器人、设施解释、质量检测、冷链、数字孪生和多款商品批量生产。[查看 10 条提示词 →](prompts/industrial-manufacturing.md)

## 按手里的素材选择写法

| 你有什么素材 | 选择什么方式 | 要写清或先核对什么 |
|---|---|---|
| 只有一个想法 | 文生视频 | 一个主要事件、环境和一条镜头运动路径 |
| 商品图或人物图 | 图生视频 | 上传首帧，写清谁动、怎么动、哪些细节不变 |
| 开始和结束两张图 | 平台支持时使用首尾帧 | 先确认有两个上传位置，再描述中间的变化 |
| 人物、风格或动作参考 | 平台支持时使用参考生视频 | 每份素材只指定一种用途；粘贴网址不等于上传素材 |
| 需要修改的现有片段 | 平台支持时使用视频编辑 | 进入实际编辑模式，只改一个方面，保留其他内容 |
| 对白或音效要求 | 支持声音的模式 | 谁在何时说什么、用哪种语言、哪里停顿；听者保持安静 |

VideoWeb 的具体操作见[入门指南](guides/videoweb-workflow.zh-CN.md)。更详细的方法见[提示词写作指南](guides/prompting-guide.md)、[平台兼容说明](guides/model-capabilities.md)和[故障排查](guides/troubleshooting.md)。库中包含多种写法，不表示 VideoWeb 当前界面支持全部模式。

## 写一条方便修改的提示词

```text
[输出] 时长 + 画幅 + 视觉类型
[主体] 固定外观特征 + 服装/材质 + 不可变化项
[环境] 时间 + 地点 + 天气 + 空间层次
[动作] 起因 → 连续动作 → 明确结果
[镜头] 景别 + 机位 + 运动路径 + 转场
[视觉] 光线 + 色彩 + 质感 + 运动模糊
[声音] 环境音 + 动作音 + 音乐 + 对白语言（平台支持时）
[约束] 保持什么 + 避免什么
```

### 改进结果的 10 条规则

1. 一个短片围绕一个主要事件；多镜头也要共享同一因果线。
2. 给角色写 3–5 个可重复的外观特征，不要每个镜头换一种形容。
3. 动作使用“先—再—最后”，让模型理解物理过程。
4. 每个镜头只指定一个主要摄影机运动。
5. 图生视频少写静态外观，多写谁动、怎么动、动多大。
6. 用环境反馈表现速度：衣摆、雨水、尘土、反射、背景视差。
7. 产品广告明确“不可变项”：比例、材质、标签、瓶盖、按钮位置。
8. 对白保持短句，为停顿、呼吸和镜头反应留出时间。
9. 负面约束只写最可能出现的问题，避免几十个空泛的否定词。
10. 先生成稳定基础版，再一次只增加一个复杂变量。

### 可替换变量模板

```text
{时长} 秒，{画幅}，{媒介/风格}。
{时间与地点}，{主体外观特征}正在{主要动作}。
动作过程：先{动作 A 与反馈}，再{动作 B 与反馈}，最后{结果 C}。
摄影机：{起始景别与机位}，{单一运动路径}，结束于{最终构图}。
光线与色彩：{主光}，{色调}，{材质重点}。
声音：{环境音}，{动作音}，{音乐/对白，可选}。
保持：{身份、服装、物体结构、空间方向}。
避免：{最相关的 3–6 个失败模式}。
```

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

更多例子见 [多语言章节](guides/prompting-guide.md#6-多语言与对白)。

查看[15 种语言目录](locales/README.md)：英文、简体中文、繁体中文、日文、韩文、西班牙文、法文、德文、巴西葡萄牙文、意大利文、阿拉伯文、俄文、印度尼西亚文、泰文和越南文。

## 贡献提示词或推荐案例

- 已生成值得研究的结果？用[提示词投稿表单](https://github.com/aivideoweb/awesome-wan-3-0-prompts/issues/new?template=prompt.yml)提交原文、素材、平台、参数和结果，可先用[生成记录模板](templates/generation-record.md)整理。
- 看到其他作者的好案例？用[外部案例表单](https://github.com/aivideoweb/awesome-wan-3-0-prompts/issues/new?template=source.yml)保留作者和原帖链接。
- 想补充场景或改善翻译？阅读[中文贡献指南](CONTRIBUTING.zh-CN.md)，再[提交修改](https://github.com/aivideoweb/awesome-wan-3-0-prompts/pulls)。后续维护方法见[维护指南](MAINTAINING.md)。

## 来源与许可

120 条基础提示词和 7 张分类插图来自 MIT 许可的源库；VideoWeb 新增品牌封面、网页操作指南、带来源的视频案例及独立练习。[来源说明](UPSTREAM.md)记录源库版本和素材归属，[许可证](LICENSE)保留原版权信息。X 上的第三方媒体仍归原作者所有。本项目是社区资源，不代表模型提供方。

## VideoWeb AI 联盟计划

[VideoWeb AI 支持联盟推广合作](https://videoweb.ai/affiliate-program/)，面向推荐其 AI 视频、图片与音乐创作工具的开发者、创作者、教育者、评测者和团队。使用普通 VideoWeb AI 账号登录，完善联盟资料并确认协议后，即可生成自己的推荐链接，在教程、评测、社区、产品或网站中进行分享并获得佣金。

- 被推荐用户的首笔有效付费订单可获得 **20%** 佣金。
- 用户注册后的 **60 天归因期**内，后续有效付费订单可获得 **10%** 佣金。
- 佣金可支付前会审核退款、拒付、风控取消订单、归因状态和政策违规情况。

联盟规则可能调整，推广前请查看最新页面和联盟协议。上面的链接是官方计划页面，不是本项目的推荐链接。
