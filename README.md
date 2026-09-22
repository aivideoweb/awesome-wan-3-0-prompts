# 🎬 Awesome Wan 3.0 Prompts — 120 AI Video Directing Briefs | VideoWeb AI

[![English](https://img.shields.io/badge/English-Current-brightgreen)](README.md)
[![简体中文](https://img.shields.io/badge/简体中文-阅读-red)](README.zh-CN.md)
[![日本語](https://img.shields.io/badge/日本語-読む-blue)](README.ja.md)
[![Español](https://img.shields.io/badge/Español-Leer-blue)](README.es.md)
[![Prompts](https://img.shields.io/badge/Wan_3.0_Prompts-120-blueviolet)](prompts/README.md)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/aivideoweb/awesome-wan-3-0-prompts/pulls)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

[繁體中文](README.zh-TW.md) · [한국어](README.ko.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português](README.pt-BR.md) · [Italiano](README.it.md) · [العربية](README.ar.md) · [Русский](README.ru.md) · [Bahasa Indonesia](README.id.md) · [ไทย](README.th.md) · [Tiếng Việt](README.vi.md) · [All 15 languages](locales/README.md)

> A practical collection of **120 upstream-derived Wan 3.0 AI video prompts** for cinematic storytelling, product commercials, shoppable retail, beauty, UGC, dialogue, localization, wildlife, seasonal processes, industry, manufacturing, education, architecture, mobility, and professional production control.

| [Browse 120 prompts](prompts/README.md) | [Submit a tested prompt](https://github.com/aivideoweb/awesome-wan-3-0-prompts/issues/new?template=prompt.yml) | [Add a translation](CONTRIBUTING.md#translations) | [Open a pull request](https://github.com/aivideoweb/awesome-wan-3-0-prompts/pulls) |
|---|---|---|---|

![Awesome Wan 3.0 AI video prompt collection](assets/videoweb-wan-3-hero.png)

**Read this collection:** [120 core briefs](prompts/README.md) · [9 X video cases](guides/x-community-showcase.md) · [6 extra practice briefs](prompts/community-practice.md) · [JSON download](downloads/prompts.json) · [Text download](downloads/prompts.txt). The core briefs are inherited writing templates, not verified VideoWeb outputs. Category files are Chinese and English; localized READMEs provide an introduction and a comparison example, not 15 full translations of all 120 briefs. [Source and media provenance](UPSTREAM.md).

## Create with VideoWeb AI

Open [Wan 3.0 on VideoWeb AI](https://videoweb.ai/model/wan-3-0/), choose text or image input, paste a brief, then select the settings available in the form. Start with one short shot and change one variable at a time. [Step-by-step guide](guides/videoweb-workflow.md) · [X video examples](guides/x-community-showcase.md).

## What makes these prompts useful

- Built around visible action and cause-and-effect, not keyword piles.
- Designed for text-to-video, image-to-video, start/end frames, reference-to-video, and video editing.
- Includes camera paths, timing, lighting, sound, identity locks, and relevant negative constraints.
- Works with multilingual visual descriptions and spoken dialogue.
- Organized with descriptive filenames and semantic headings for search and downstream gallery projects.

## Share a prompt that worked

Useful outside submissions are actively welcome. If a Wan 3.0 prompt produced a result worth studying, use the [guided prompt submission form](https://github.com/aivideoweb/awesome-wan-3-0-prompts/issues/new?template=prompt.yml). One submission should contain one complete prompt, its workflow and settings, a result link or screenshot where possible, and only assets you are allowed to share. Maintainers can then review, test, rewrite for consistency, and place it in the right production category.

You can also submit a pull request for a new scenario, a failure/success comparison, a more natural localization, or an accessibility improvement. Contributions do not need to be English-first: dialogue and on-screen language may use any language when the visual direction and speaker timing remain clear. Read the [contribution guide](CONTRIBUTING.md) before sending media or reference files.

> [!IMPORTANT]
> Wan 3.0 availability, duration, resolution, reference limits, and audio features may vary by region, product, or preview program. This repository does not invent fixed specifications. Use the controls shown by your current platform. Most templates can also be simplified for Wan 2.6 or 2.7.

## Quick prompt formula

```text
[Output] duration + aspect ratio + visual medium
[Subject] reusable identity anchors + immutable details
[World] time + place + weather + spatial layers
[Action] trigger → continuous motion → visible result
[Camera] shot size + angle + one movement path + ending frame
[Look] light + palette + material + motion treatment
[Sound] ambience + action sound + music + dialogue, if supported
[Constraints] what must remain + the most likely failure modes
```

Minimal example:

```text
8 seconds, 16:9, naturalistic cinematic footage. At dawn on a rain-washed old street, a young postal worker in a dark green coat rides a vintage bicycle through a shallow puddle. The front wheel parts the water into two low sprays; droplets fall back onto the stone instead of floating. The camera tracks from knee height at the rear-left, starts as a medium environmental shot, moves closer to the hand and bell, then rises toward warm light at the end of the street. Realistic speed and soft overcast light. Sound: tire through water, a distant shop shutter, one clear bicycle bell. Keep the face, coat, bicycle geometry, and travel direction consistent. No text, logos, extra limbs, jump cuts, or floating objects.
```

## Choose a workflow

| Mode | Prioritize | Reliable instruction pattern |
|---|---|---|
| T2V | World, subject, action, camera | Describe one event before adding style |
| I2V | Motion and amplitude | Keep the input composition; specify exactly what moves and by how much |
| Start/end frames | Explainable transition | Describe the trigger, intermediate physics, and final state |
| R2V | Clear reference roles | “Image 1 = identity; Video 1 = motion rhythm only” |
| Video edit | One changed dimension | “Change only the weather; preserve action, timing, subject, and camera” |
| Audio/dialogue | Speaker timing | Use short lines; identify language, emotion, pause, and silent listener |

Read the detailed [prompt engineering guide](guides/prompting-guide.md), [model and platform compatibility notes](guides/model-capabilities.md), and [troubleshooting handbook](guides/troubleshooting.md). These core guides are maintained in Simplified Chinese and include language-independent templates; the VideoWeb getting-started guide is available in English and Chinese.

## Wan 3.0 overview: one family, four production paths

Wan 3.0 is most useful when treated as a production family rather than a single text box. Start from text when the idea is still open, animate a designed keyframe when composition matters, edit an existing clip when only one dimension should change, and use reference-driven generation when identity or motion continuity is the priority. Across all four paths, the prompts in this repository emphasize temporal cause and effect, deliberate camera movement, stable subject anchors, physical motion cues, sound direction, and a short list of shot-specific constraints.

| Wan 3.0 path | Best starting material | Best use case | Prompting priority |
|---|---|---|---|
| Text to video | A written creative brief | Concept exploration, cinematic scenes, ad ideation | World → action → camera → look |
| Image to video | A strong first frame, plus an end frame where supported | Product shots, character shots, art direction | Preserve composition; define motion amplitude |
| Video edit | Existing footage | Weather, wardrobe, material, background, or mood changes | Change one dimension; lock everything else |
| Reference to video | Identity, style, audio, or motion references | Recurring characters and campaign consistency | Assign one explicit role to each reference |

## Learn from community videos

These two author threads include complete prompts. Click a preview to watch on X. They are not VideoWeb-generated results; reference inputs and comparison-model labels still matter.

### Before the Void Swallows You — @0xbisc

[![Before the Void Swallows You](https://pbs.twimg.com/amplify_video_thumb/2093296405674893312/img/KrpfnTtMVpRJboxK.jpg)](https://x.com/0xbisc/status/2093296541834653883/video/1)

[Read the author’s complete prompt](https://x.com/0xbisc/status/2093296546926539136) · [Technique and evidence limits](guides/x-community-showcase.md#void-escape)

### Five-shot mountain survival story — @chatgptpaglu

[![Five-shot mountain survival story](https://pbs.twimg.com/amplify_video_thumb/2094707623602053120/img/bRfC47Flglx2mSJd.jpg)](https://x.com/chatgptpaglu/status/2094710054675157354/video/1)

[Read the author’s complete prompt](https://x.com/chatgptpaglu/status/2094710054675157354) · [Technique and evidence limits](guides/x-community-showcase.md#cable-car-story)

[Browse all 9 source-linked cases](guides/x-community-showcase.md) · [Try 6 separate practice briefs](prompts/community-practice.md)

## Prompt categories

Need one place to scan every title? Open the [120-scene master index](prompts/README.md).

| Category | Prompts | Includes | Open |
|---|---:|---|---|
| Cinematic storytelling | 6 | drama, suspense, period scenes, one-take shots | [Browse](prompts/cinematic-storytelling.md) |
| Ads and products | 6 | beauty, food, technology, home, automotive | [Browse](prompts/ads-and-products.md) |
| UGC, food and travel | 6 | vlogs, street food, stays, workshops, ASMR | [Browse](prompts/ugc-food-travel.md) |
| Action and sports | 6 | pursuit, snowboarding, volleyball, parkour, VFX | [Browse](prompts/action-sports.md) |
| Animation and fantasy | 6 | 2D, 3D, stop motion, East Asian fantasy, sci-fi | [Browse](prompts/anime-fantasy.md) |
| Music, comedy and social | 6 | live music, dance, rap, pets, office comedy, loops | [Browse](prompts/music-comedy-social.md) |
| Professional business and public service | 11 | SaaS, creator courses, podcasts, accessibility, telehealth, logistics | [Browse](prompts/professional-business.md) |
| Education and science | 11 | climate, microscopy, safety, astronomy, marine science, museums | [Browse](prompts/education-science.md) |
| Architecture, hospitality and mobility | 11 | real estate, public space, accessible routes, e-bikes, transit, hotels | [Browse](prompts/architecture-mobility.md) |
| Production control and editing | 11 | green screen, previs, product rotation, local edits, reference roles, loops | [Browse](prompts/production-control.md) |
| Commerce, beauty, and retail | 10 | fit demos, shoppable video, skincare, packaging, accessible retail, catalog batches | [Browse](prompts/commerce-beauty-retail.md) |
| People, dialogue, and localization | 10 | speaker turns, dubbing, sign language, podcasts, oral history, micro-drama | [Browse](prompts/people-dialogue-localization.md) |
| Nature, animals, and seasons | 10 | wildlife, animal care, weather, macro nature, seasonal change, observatories | [Browse](prompts/nature-animals-seasons.md) |
| Industrial and manufacturing | 10 | training, cobots, inspection, cold chain, digital twins, multi-SKU production | [Browse](prompts/industrial-manufacturing.md) |

The 120 core scenarios, characters, fictional products and dialogue are adapted from the MIT-licensed upstream collection. Category artwork is inherited illustrative artwork; the VideoWeb hero is newly generated. Community video links retain their original creators. See [provenance](UPSTREAM.md).

## Four new practical production packs

### Commerce, beauty, and retail

[![Inherited commerce, beauty, and retail prompt cover](assets/covers/commerce-beauty-retail.webp)](prompts/commerce-beauty-retail.md)

Shoppable demonstrations, fit and texture comparisons, accessible product use, packaging continuity, consultations, and repeatable catalog campaigns. [Open 10 prompts →](prompts/commerce-beauty-retail.md)

### People, dialogue, and localization

[![Inherited people, dialogue, and localization prompt cover](assets/covers/people-dialogue-localization.webp)](prompts/people-dialogue-localization.md)

Clean speaking turns, multilingual dialogue, localized dubbing, sign-language framing, podcasts, documentary voiceover, and oral history. [Open 10 prompts →](prompts/people-dialogue-localization.md)

### Nature, animals, and seasons

[![Inherited nature, animals, and seasons prompt cover](assets/covers/nature-animals-seasons.webp)](prompts/nature-animals-seasons.md)

Patient wildlife observation, animal-care routines, macro physics, weather transitions, seasonal change, and non-invasive documentary direction. [Open 10 prompts →](prompts/nature-animals-seasons.md)

### Industrial and manufacturing

[![Inherited industrial and manufacturing prompt cover](assets/covers/industrial-manufacturing.webp)](prompts/industrial-manufacturing.md)

Safety rehearsals, cobot handoffs, facility explainers, inspection, cold-chain continuity, digital-twin overlays, and multi-SKU generation. [Open 10 prompts →](prompts/industrial-manufacturing.md)

## Multilingual prompting

Use one main language for the visual description and isolate exact dialogue:

```text
Visual description: English cinematic production language.
Spoken dialogue: Mandarin Chinese, relaxed natural delivery.
Exact line: “今天的风，终于往海边吹了。”
No subtitles. The listener keeps their mouth closed and reacts with one small nod.
```

Avoid duplicating the entire prompt in multiple languages. Keep camera and material terminology in the main language; preserve only exact spoken or on-screen text in its target language.

The [15-language directory](locales/README.md) provides a localized prompt formula and the same complete comparison scene in every supported language: English, Simplified Chinese, Traditional Chinese, Japanese, Korean, Spanish, French, German, Brazilian Portuguese, Italian, Arabic, Russian, Indonesian, Thai, and Vietnamese.

## Ten practical rules

1. Build each short around one primary event.
2. Reuse three to five identity anchors without paraphrasing them.
3. Write motion as “first, then, finally.”
4. Assign one main camera movement per shot.
5. For I2V, describe motion more than static appearance.
6. Show speed through water, dust, clothing, parallax, and sound.
7. Lock product geometry, material, label, cap, and button positions.
8. Keep dialogue short enough for natural pauses.
9. Use three to six scene-specific negative constraints.
10. Add one complex variable per iteration.

## Contributing and license

Original prompts, tested comparisons, and natural localizations are welcome. Use the [prompt submission form](https://github.com/aivideoweb/awesome-wan-3-0-prompts/issues/new?template=prompt.yml) for one tested recipe, or open a pull request for a larger category or translation. Do not submit copied prompt libraries, watermarked media, unauthorized celebrity likenesses, protected characters, or imitation of a living artist’s style. See [CONTRIBUTING.md](CONTRIBUTING.md).

Repository code and original text are provided under the [MIT License](LICENSE). Artwork includes one new VideoWeb hero and seven inherited category illustrations; none is evidence of a Wan video generation. This independent community resource is not an official model-provider publication.

## VideoWeb AI Affiliate Program

[VideoWeb AI currently offers an affiliate program](https://videoweb.ai/affiliate-program/) for developers, creators, educators, reviewers, and teams that recommend its AI video, image and music creation tools. Sign in with a regular VideoWeb AI account, complete the affiliate profile and agreement, generate your own referral link, and share that link in tutorials, reviews, communities, products, or websites.

- Earn **20%** on a referred user's first valid paid order.
- Earn **10%** on following valid paid orders made within the **60-day attribution window** after registration.
- Refunds, chargebacks, risk-cancelled orders, attribution status, and policy abuse are reviewed before commission becomes payable.

Program rules may change. Review the current affiliate page and agreement before promoting VideoWeb AI. The link above is the official program page, not this project's referral link.
