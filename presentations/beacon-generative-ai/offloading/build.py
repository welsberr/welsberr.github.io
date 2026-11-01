#!/usr/bin/env python3
"""Build the essay, bibliography and readable provenance appendix from content.json."""
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
D = json.loads((ROOT / 'content.json').read_text())
E = html.escape

def inline(text):
    text = E(text)
    return re.sub(r'\[([^\]]+)\]\(([^)]+)\)', lambda m: f'<a href="{m[2]}">{m[1]}</a>', text)

def p(text):
    return '<p>' + inline(text) + '</p>'

def heading(level, ident, text):
    return f'<h{level} id="{ident}">{E(text)}</h{level}>'

figure = '''<figure id="figure-1" aria-labelledby="figure-caption">
<div class="flow"><div><strong>Complete a task</strong><span>Request an answer → inspect and use it</span><em>Measure the quality of the assisted output.</em></div>
<div><strong>Learn a skill</strong><span>Attempt → request a hint → explain → check and revise</span><em>Then close the tool, solve a new problem, and test recall later.</em></div></div>
<figcaption id="figure-caption">Figure 1. Two goals require different evidence. This original schematic proposes a study workflow; it does not plot experimental results or guarantee learning. <a href="#F1">Figure provenance F1</a>.</figcaption></figure>'''
figure_md = '''**Figure 1. Two goals require different evidence.**

- Complete a task: request an answer → inspect and use it. Measure assisted output quality.
- Learn a skill: attempt → request a hint → explain → check and revise. Then close the tool, solve a new problem, and test recall later.

Original conceptual schematic, not experimental data or a guarantee of learning. [Figure provenance F1](#F1).'''

body = [heading(1, 'top', D['title']), p(D['subtitle']), p(D['status'])]
md = [f"# {D['title']}", D['subtitle'], D['status']]
body += ['<nav aria-label="Essay contents"><a href="#essay">Essay</a><a href="#bibliography">Bibliography</a><a href="#provenance">Provenance appendix</a><a href="#methods">Review scope</a><a href="#acknowledgements">Acknowledgements</a></nav>']
body += [heading(2,'essay','Essay')]
md += ['## Essay']
for section in D['sections']:
    body += [heading(3,section['id'],section['title'])]
    md += [f"### {section['title']}"]
    for para in section['paragraphs']:
        body += [p(para)]
        md += [para]
    if section.get('figure'):
        body += [figure]
        md += [figure_md]

body += [heading(2,'bibliography','Annotated bibliography'),p(D['bibliography_intro'])]
md += ['## Annotated bibliography',D['bibliography_intro']]
bib=[]
for s in D['sources']:
    body += [f'<article class="reference" id="{s["id"]}">',heading(3,s['id']+'-title',s['id']+' · '+s['short']),p(s['citation']),p(s['annotation']),p('Access and version: '+s['access']),p('Status check: '+s['status_check']),'</article>']
    md += [f'<a id="{s["id"]}"></a>',f"### {s['id']} · {s['short']}",s['citation'],s['annotation'],'Access and version: '+s['access'],'Status check: '+s['status_check']]
    fields = s['bib']['fields'].copy()
    fields['urldate'] = D['as_of']
    esc=lambda x:str(x).replace('&',r'\&').replace('%',r'\%').replace('_',r'\_')
    bib += ['@'+s['bib']['entry_type']+'{'+s['bib']['citation_key']+',\n'+',\n'.join('  '+k+' = {'+esc(v)+'}' for k,v in fields.items())+'\n}']

body += [heading(2,'provenance','Appendix: claim and figure provenance')]
md += ['## Appendix: claim and figure provenance']
for para in D['provenance_intro']:
    body += [p(para)]; md += [para]
for c in D['claims']:
    body += [f'<article class="claim" id="{c["id"]}">',heading(3,c['id']+'-title',c['id']+' · '+c['title'])]
    md += [f'<a id="{c["id"]}"></a>',f"### {c['id']} · {c['title']}"]
    for label,key in [('Statement','statement'),('Type','type'),('Evidence and locator','evidence'),('Limits','limits'),('Confidence','confidence'),('Stewardship','stewardship'),('Recorded / checked','recorded_at'),('Review status','review_status')]:
        body += [p(label+': '+c[key])]; md += [f'**{label}:** '+c[key]]
    body += ['</article>']
body += [heading(2,'methods','Review scope and update policy')]
md += ['## Review scope and update policy']
for para in D['methods']:
    body += [p(para)]; md += [para]
body += [heading(2,'acknowledgements','Acknowledgements and stewardship')]
md += ['## Acknowledgements and stewardship']
for para in D['acknowledgements']:
    body += [p(para)]; md += [para]
body += ['<p class="downloads"><a href="essay.md" download>Download Markdown</a> · <a href="bibliography.bib" download>Download BibTeX</a> · <a href="provenance.json" download>Download provenance JSON</a></p>','<p><a href="../">Return to the BEACON presentation</a> · <a href="#top">Back to top</a></p>']

doc='''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="A short evidence-based essay on cognitive offloading, generative AI study practices, and unaided recall, with an annotated bibliography and claim provenance.">
<title>'''+E(D['title'])+'''</title><link rel="stylesheet" href="style.css"></head>
<body><a class="skip" href="#main">Skip to essay</a><header><a href="../">BEACON discussion companion</a><span>Wesley R. Elsberry · Personal research notes</span></header>
<main id="main" tabindex="-1">'''+ '\n'.join(body)+'''</main><footer>Prepared 25 September 2026. Personal scholarship; no MSU or employer endorsement is implied.</footer></body></html>'''
(ROOT/'index.html').write_text(doc)
(ROOT/'essay.md').write_text('\n\n'.join(md)+'\n')
(ROOT/'bibliography.bib').write_text('% Selected and source-checked bibliography; human-reviewed and approved for public release.\n\n'+'\n\n'.join(bib)+'\n')
(ROOT/'provenance.json').write_text(json.dumps({'schema_version':'offloading.provenance.v1','title':D['title'],'as_of':D['as_of'],'recorded_at':D['recorded_at'],'stewardship':D['stewardship'],'confidence_policy':D['provenance_intro'],'sources':D['sources'],'claims':D['claims']},ensure_ascii=False,indent=2)+'\n')
print(f"Built HTML, Markdown, BibTeX and provenance: {len(D['sources'])} references, {len(D['claims'])} provenance records.")
