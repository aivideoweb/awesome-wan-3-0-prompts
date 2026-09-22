"""Render expanded homepage cards from the shared X case catalog."""
import html
import re

START = '<!-- BEGIN GENERATED X CASES -->'
END = '<!-- END GENERATED X CASES -->'
STATUS = {
    'complete_prompt_at_source': ('Complete at author source', '作者原文完整'),
    'partial_prompt_in_thread': ('Partial prompt only', '仅有部分提示词'),
    'external_prompt_link': ('External prompt not verified', '提示词外链未核验'),
    'prompt_not_published_in_retrieved_post': ('Demo; prompt not retrieved', '仅演示，未取得提示词'),
}


def render_homepage(cases, language):
    zh = language == 'zh'
    count = len(cases)
    complete = sum(c['prompt_status'] == 'complete_prompt_at_source' for c in cases)
    ordered = sorted(cases, key=lambda c: c['homepage']['order'])
    if len({c['homepage']['order'] for c in cases}) != count:
        raise ValueError('Duplicate homepage case order')
    if zh:
        lines = [f'**{count} 个 X 案例，其中 {complete} 个可在作者原帖查看完整提示词。** 下面直接展示全部 {count} 个案例的预览图。点击图片或播放链接进入 X，可能需要登录。这些是第三方作品，并非本仓库在 VideoWeb 上复现的结果。',
                 f'### 全部 {count} 个案例一览',
                 '| 案例 | 学习重点 | 提示词情况 |\n|---|---|---|']
    else:
        lines = [f'**{count} sourced X cases, including {complete} with complete author prompts.** All {count} cases have expanded previews below. Click a preview or the watch link to open the video on X; login may be required. These are third-party results, not VideoWeb reproductions.',
                 f'### All {count} cases at a glance',
                 '| Case | What to study | Prompt availability |\n|---|---|---|']
    rows = []
    for case in ordered:
        copy = case['homepage'][language]
        status = STATUS[case['prompt_status']][int(zh)]
        rows.append(f'| [{copy["title"]}](#case-{case["id"]}) | {copy["lesson"]} | {status} |')
    lines[-1] += '\n' + '\n'.join(rows)
    lines.append('部分原帖对比多个模型，不能将其中所有附件都当成 Wan 的结果。“原文完整”也不代表参考素材和参数齐全；具体缺项见对应案例。' if zh else 'Some posts compare several models; their attachments are not all confirmed Wan outputs. Complete prompt text does not mean all reference inputs or settings are available. Each case records what is missing.')
    for case in ordered:
        copy = case['homepage'][language]
        media = case['media'][0]
        status = STATUS[case['prompt_status']][int(zh)]
        author = case['author']
        lines.extend([f'<a id="case-{case["id"]}"></a>',
                      f'### {copy["heading"]} — [@{author}](https://x.com/{author})',
                      f'<a href="{html.escape(media["watch_url"], quote=True)}"><img src="{html.escape(media["thumbnail_url"], quote=True)}" alt="{html.escape(copy["title"], quote=True)}" width="100%"></a>',
                      copy['description']])
        links = [f'[{"▶ 观看原帖视频" if zh else "▶ Watch original video"}]({media["watch_url"]})']
        if case['prompt_status'] == 'complete_prompt_at_source':
            links.append(f'[{"作者完整提示词" if zh else "Complete author prompt"}]({case["prompt_url"]})')
        if case['id'] == 'void-escape':
            links.append(f'[{"另一条追逐练习" if zh else "Try a separate chase exercise"}](prompts/community-practice.md#prompt-{case["practice_id"]})')
        links.append(f'[{"来源、全部附件与限制" if zh else "Source, all attachments and limitations"}](guides/x-community-showcase.md#{case["id"]})')
        lines.append(f'**{status}** · ' + ' · '.join(links))
    lines.append(f'[查看全部 {count} 个案例及提示词完整情况](guides/x-community-showcase.md)。[6 条补充练习](prompts/community-practice.md)是独立编写、尚未实测的练习，不是这些视频的原始提示词。' if zh else f'[Browse all {count} cases and their prompt availability](guides/x-community-showcase.md). The [6 practice briefs](prompts/community-practice.md) are separate, untested exercises, not the source prompts for these videos.')
    return '\n\n'.join(lines) + '\n'


def updated_homepage(text, cases, language):
    if text.count(START) != 1 or text.count(END) != 1 or text.index(START) >= text.index(END):
        raise ValueError('Missing or duplicate homepage generation markers')
    before, rest = text.split(START)
    _, after = rest.split(END)
    text = before + START + '\n' + render_homepage(cases, language) + END + after
    # The top navigation count must track the same catalog as the expanded cards.
    return re.sub(r'\[\d+ (个视频案例|video cases)\]\(#community-videos\)',
                  lambda m: f'[{len(cases)} {m[1]}](#community-videos)', text)
