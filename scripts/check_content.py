#!/usr/bin/env python3
"""Validate the prompt catalog, local destinations, sources and brand routing."""
from pathlib import Path
import json,re,sys
from urllib.parse import unquote,urlsplit
from html.parser import HTMLParser
from homepage_showcase import updated_homepage
from build_catalog import catalog,outputs,ROOT
from build_showcase import render
class HTMLReferences(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links=[]
    def handle_starttag(self, tag, attrs):
        attrs=dict(attrs)
        if tag=='img' and 'src' in attrs:self.links.append(attrs['src'])
        if tag=='a' and 'href' in attrs:self.links.append(attrs['href'])

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
    prose=re.sub(r'```.*?```','',s,flags=re.S)
    html=HTMLReferences();html.feed(prose)
    links=re.findall(r'\]\(([^\s)]+)(?:\s+"[^"]*")?\)',prose)+html.links
    for link in links:
        if urlsplit(link).scheme:continue
        path=unquote(link.split('#')[0])
        if path:require((p.parent/path).exists(),f'Broken path in {p.relative_to(ROOT)}: {link}')
        destination=p.parent/path if path else p
        anchor=unquote(urlsplit(link).fragment)
        if anchor.startswith(('prompt-','case-')) or anchor=='adapt-settings':
            if destination.is_file():
                require(f'id="{anchor}"' in destination.read_text(),f'Broken explicit anchor in {p.relative_to(ROOT)}: {link}')
    if p.name.startswith('README') and p.parent==ROOT:
        require('https://videoweb.ai/model/wan-3-0/' in s,f'Missing model link: {p.name}')
        require('https://videoweb.ai/affiliate-program/' in s,f'Missing affiliate link: {p.name}')
        require('https://flaq.ai/' not in s,f'Stale promotion: {p.name}')
        require('github.com/flaqai/' not in s,f'Stale contribution routing: {p.name}')
        require('10% OFF' not in s and '$0.045' not in s,f'Upstream pricing leaked into {p.name}')
for page in ROOT.glob('README*.md'):
    if page.name=='README.en.md':continue
    text=page.read_text()
    require(text.count('<!-- comparison-example-status: untested -->')==1,f'Missing comparison example status: {page.name}')
    marker=text.find('<!-- comparison-example-status: untested -->')
    note=text[marker+len('<!-- comparison-example-status: untested -->'):].split('```',1)[0]
    require('VideoWeb' in note and len(note.strip())>30,f'Missing visible comparison status: {page.name}')
for name,content in outputs().items():require((ROOT/'downloads'/name).read_text()==content,f'Stale download: {name}')
cases=json.loads((ROOT/'data/x-cases.json').read_text());gallery=(ROOT/'guides/x-community-showcase.md').read_text()
require(gallery==render(),'Stale gallery; run scripts/build_showcase.py')
for name, language in [('README.md','en'),('README.zh-CN.md','zh')]:
    page=(ROOT/name).read_text()
    try:
        require(page==updated_homepage(page,cases,language),f'Stale homepage: {name}; run scripts/build_showcase.py')
    except (ValueError,KeyError) as exc:
        require(False,f'Invalid homepage catalog: {exc}')
for category in {x['category'] for x in core}:
    page=(ROOT/'prompts'/f'{category}.md').read_text()
    require('<!-- core-template-context -->' in page and '../UPSTREAM.md' in page and '../templates/generation-record.md' in page,f'Missing core context: {category}')
    expected=sum(x['category']==category for x in core)
    require(page.count('#adapt-settings)')==expected+1,f'Missing per-prompt adaptation links: {category}')
    for block in re.split(r'(?=^## )',page,flags=re.M)[1:]:
        prefix=block.split('```',1)[0]
        require(prefix.count('#adapt-settings)')==1,f'Missing nearby settings link: {category} {block.splitlines()[0]}')
    require('尚未逐条在 VideoWeb 生成验证' in page or 'have not each been generated and verified on VideoWeb' in page,f'Missing untested status: {category}')
    intro=page.split('```',1)[0]
    require(not re.search(r'(?:These original prompts|Original prompts for|Original production briefs)',intro),f'Ambiguous authorship: {category}')
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
require('1 new VideoWeb hero + 7 inherited category images' in (ROOT/'prompts/README.md').read_text(),'Artwork counts must separate new and inherited assets')
for name in ['README.md','README.zh-CN.md','prompts/README.md']:
    text=(ROOT/name).read_text()
    for phrase in ['120 original','120 Original','120 个原创实用场景','本地原创封面','Original generated preview images']:
        require(phrase not in text,f'Misleading originality claim in {name}: {phrase}')
require('Copyright (c) 2026 Flaq AI' in (ROOT/'LICENSE').read_text(),'Missing upstream copyright')
if errors:
    print('\n'.join(errors));sys.exit(1)
print(f'PASS: 120 core prompts, 6 practice briefs, 14 categories, local paths, 16 README files and {len(cases)} X cases')
