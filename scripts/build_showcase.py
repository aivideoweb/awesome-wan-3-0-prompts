#!/usr/bin/env python3
"""Build the source-linked X gallery from data/x-cases.json."""
from pathlib import Path
import argparse,json
from homepage_showcase import updated_homepage
ROOT=Path(__file__).resolve().parents[1]
LABELS={
 'complete_prompt_at_source':'Complete prompt at author source / 作者原文完整',
 'partial_prompt_in_thread':'Partial prompt only / 仅有部分提示词',
 'external_prompt_link':'External prompt link, unverified / 外链未核验',
 'prompt_not_published_in_retrieved_post':'Demo without retrieved prompt / 未取得提示词的演示',
}
def render():
    cases=json.loads((ROOT/'data/x-cases.json').read_text())
    complete=sum(c['prompt_status']=='complete_prompt_at_source' for c in cases)
    s=f'''# Wan 3.0 videos from X / X 视频案例

[Home](../README.md) · [中文首页](../README.zh-CN.md) · [120 core briefs](../prompts/README.md) · [6 practice briefs](../prompts/community-practice.md)

**{len(cases)} source-linked cases; {complete} complete prompts available at the author source.** The remaining cases link to an unverified external prompt or are demonstrations without a retrieved prompt. Checked 2026-09-22. These are source checks, not our own generation tests.

**{len(cases)} 个案例，其中 {complete} 条可在作者原帖查看完整提示词。** 其余案例指向未核验的外部提示词，或仅提供演示。下面的学习建议由维护者撰写，不代表原作者的提示词，也不代表已在 VideoWeb 复现。

X may require login. Post text and media metadata were retrieved through FxTwitter; three complete-prompt cases were also read on native X. Preview images open the original X video view. Direct media links are secondary: automated HEAD requests returned 403 in our environment, while native X playback was observed for the void-escape, vertical-action and mountain-story cases. Other clips have retrieved media metadata but have not been individually playback-tested. No third-party media is stored or relicensed here. [Rights and provenance](../UPSTREAM.md).

| Case | What to study / 学习重点 | Prompt status |
|---|---|---|
'''
    for c in cases:s+=f'| [{c["title"]}](#{c["id"]}) | {c["lesson_zh"]} | {LABELS[c["prompt_status"]]} |\n'
    for c in cases:
        s+=f'''\n<a id="{c['id']}"></a>

## {c['title']}

Creator: [@{c['author']}](https://x.com/{c['author']}) · [Original post]({c['source_url']}) · [Author prompt / thread]({c['prompt_url']})

Published: {c['published_at']}. Source checked: {c['checked_at']}.

**Prompt status:** {LABELS[c['prompt_status']]}. Model name explicitly stated in the author post: **{c['model_evidence']}**.

**What to study:** {c['lesson']}

**Evidence limit:** {c['limitations']}

**Reproduction inputs:** {c['reference_assets_status']} {c['generation_settings_status']}
'''
        for n,v in enumerate(c['media'],1):
            s+=f'''\n[![{c['title']}, attachment {n}; open video on X]({v['thumbnail_url']})]({v['watch_url']})

[▶ Watch attachment {n} on X]({v['watch_url']}) · [Direct media (may be restricted)]({v['video_url']}) · {v['duration']} seconds · {v['width']} × {v['height']}
'''
        s+=f'''\n**Practice this technique:** [Exercise {c['practice_id']}](../prompts/community-practice.md#prompt-{c['practice_id']}) uses a separate editorial scene. It is untested and is not the prompt behind this video.
'''
    s+='''\n## Contribute a source

Use the [source submission form](https://github.com/aivideoweb/awesome-wan-3-0-prompts/issues/new?template=source.yml). Include the original post, creator, model label, exact prompt location, result and missing settings. A video without a retrieved prompt remains a demonstration. Full prompts stay at their author source unless permission to reproduce is documented.

Maintainers edit [the source catalog](../data/x-cases.json), run `python3 scripts/build_showcase.py`, then run the [content checks](../MAINTAINING.md). Do not relabel another gallery's rewritten text as an author's original prompt.
'''
    return s
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--check',action='store_true');a=parser.parse_args();p=ROOT/'guides/x-community-showcase.md';s=render()
    if a.check:
        if not p.exists() or p.read_text()!=s:raise SystemExit('Stale X gallery; run scripts/build_showcase.py')
    else:p.write_text(s)
    cases=json.loads((ROOT/'data/x-cases.json').read_text())
    for name, language in [('README.md', 'en'), ('README.zh-CN.md', 'zh')]:
        page=ROOT/name
        expected=updated_homepage(page.read_text(), cases, language)
        if a.check:
            if page.read_text()!=expected:raise SystemExit(f'Stale homepage: {name}; run scripts/build_showcase.py')
        else:page.write_text(expected)
    print('PASS: X gallery and both homepages match source catalog')
