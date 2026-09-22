#!/usr/bin/env python3
"""Build deterministic downloads from the Markdown source, without network access."""
from pathlib import Path
import re,json,argparse
ROOT=Path(__file__).resolve().parents[1]
def catalog():
    out=[]
    for p in sorted((ROOT/'prompts').glob('*.md')):
        if p.name=='README.md':continue
        for block in re.split(r'(?=^## )',p.read_text(),flags=re.M)[1:]:
            title=block.splitlines()[0][3:]
            prompts=re.findall(r'```text\n(.*?)\n```',block,re.S)
            if len(prompts)!=1:raise ValueError(f'{p.name}: expected one prompt for {title}')
            setup=re.search(r'^\*\*(?:模式|Mode|Setup).*$',block,re.M)
            out.append(dict(id=p.stem+'-'+re.match(r'\d+',title)[0],category=p.stem,title=title,source=str(p.relative_to(ROOT)),settings=setup[0] if setup else '',prompt=prompts[0],status='untested_editorial_practice' if p.stem=='community-practice' else 'upstream_template_not_videoweb_tested'))
    return out

def outputs():
    rows=catalog()
    return {'prompts.json':json.dumps(rows,ensure_ascii=False,indent=2)+'\n','prompts.txt':'Wan 3.0 — VideoWeb AI\n120 upstream templates + 6 untested practice briefs.\nSource and rights: ../UPSTREAM.md\n\n'+'\n\n'.join(x['id']+' | '+x['title']+'\n'+x['settings']+'\n'+x['prompt'] for x in rows)+'\n'}
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--check',action='store_true');args=parser.parse_args()
    dest=ROOT/'downloads';dest.mkdir(exist_ok=True)
    for name,content in outputs().items():
        p=dest/name
        if args.check:
            if not p.exists() or p.read_text()!=content:raise SystemExit(f'Stale download: {name}; run scripts/build_catalog.py')
        else:p.write_text(content)
    print('PASS: downloads match 126 catalog entries' if args.check else 'Built 126 entries')
