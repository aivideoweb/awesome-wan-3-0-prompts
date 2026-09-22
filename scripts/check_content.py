#!/usr/bin/env python3
"""Validate the prompt catalog, local destinations, sources and brand routing."""
from pathlib import Path
import json,re,sys
from urllib.parse import unquote,urlsplit
from build_catalog import catalog,outputs,ROOT
from build_showcase import render
errors=[]
def require(ok,message):
    if not ok:errors.append(message)
rows=catalog();core=[x for x in rows if x['category']!='community-practice']
require(len(core)==120,'Expected 120 core briefs')
require(len(rows)==126,'Expected 6 extra practice briefs')
require(len(set(x['id'] for x in rows))==126,'Duplicate prompt IDs')
require(len(set(x['category'] for x in core))==14,'Expected 14 core categories')
for x in rows:
    require(len(x['prompt'])>100,f'Short prompt {x["id"]}')
    require(bool(x['settings']),f'Missing mode/settings: {x["id"]}')
for p in ROOT.rglob('*.md'):
    if '.git' in p.parts:continue
    s=p.read_text()
    require(s.count('```')%2==0,f'Unbalanced code fences: {p.relative_to(ROOT)}')
    for link in re.findall(r'\]\(([^\s)]+)(?:\s+"[^"]*")?\)',s):
        if urlsplit(link).scheme:continue
        path=unquote(link.split('#')[0])
        if path:require((p.parent/path).exists(),f'Broken path in {p.relative_to(ROOT)}: {link}')
        if '#prompt-' in link and path and (p.parent/path).is_file():
            anchor=link.split('#',1)[1]
            require(f'id="{anchor}"' in (p.parent/path).read_text(),f'Broken prompt anchor: {link}')
    if p.name.startswith('README') and p.parent==ROOT:
        require('https://videoweb.ai/model/wan-3-0/' in s,f'Missing model link: {p.name}')
        require('https://videoweb.ai/affiliate-program/' in s,f'Missing affiliate link: {p.name}')
        require('https://flaq.ai/' not in s,f'Stale promotion: {p.name}')
        require('github.com/flaqai/' not in s,f'Stale contribution routing: {p.name}')
        require('10% OFF' not in s and '$0.045' not in s,f'Upstream pricing leaked into {p.name}')
for name,content in outputs().items():require((ROOT/'downloads'/name).read_text()==content,f'Stale download: {name}')
cases=json.loads((ROOT/'data/x-cases.json').read_text());gallery=(ROOT/'guides/x-community-showcase.md').read_text()
require(gallery==render(),'Stale gallery; run scripts/build_showcase.py')
require(len(cases)>=9,'Expected at least nine sourced cases')
require(len({c['source_url'] for c in cases})==len(cases),'Duplicate X source')
for c in cases:
    require(re.fullmatch(r'https://x.com/[^/]+/status/\d+',c['source_url']) is not None,'Invalid X source')
    for key in ['author','prompt_status','limitations','rights','checked_at','retrieval_url','practice_id']:require(bool(c.get(key)),f'Missing {key}: {c["id"]}')
    require(c['source_url'] in gallery,f'Gallery missing source: {c["id"]}')
    require(bool(c['media']),f'No video: {c["id"]}')
    for v in c['media']:
        require(v['video_url'].startswith('https://video.twimg.com/'),f'Unexpected media host: {c["id"]}')
        require(v['video_url'] in gallery,f'Gallery missing media: {c["id"]}')
        require(f']({v["thumbnail_url"]})]({v["watch_url"]})' in gallery,f'Thumbnail must open X: {c["id"]}')
        require(v['watch_url'].startswith(c['source_url']+'/video/'),f'Wrong video-to-post mapping: {c["id"]}')
require(sum(c['prompt_status']=='complete_prompt_at_source' for c in cases)>=4,'Expected at least four complete author-prompt sources')
require('1 new VideoWeb hero + 7 inherited category images' in (ROOT/'prompts/README.md').read_text(),'Artwork counts must separate new and inherited assets')
for name in ['README.md','README.zh-CN.md','prompts/README.md']:
    text=(ROOT/name).read_text()
    for phrase in ['120 original','120 Original','120 个原创实用场景','本地原创封面','Original generated preview images']:
        require(phrase not in text,f'Misleading originality claim in {name}: {phrase}')
require('Copyright (c) 2026 Flaq AI' in (ROOT/'LICENSE').read_text(),'Missing upstream copyright')
if errors:
    print('\n'.join(errors));sys.exit(1)
print(f'PASS: 120 core prompts, 6 practice briefs, 14 categories, local paths, 16 README files and {len(cases)} X cases')
