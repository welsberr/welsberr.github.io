#!/usr/bin/env python3
"""Render the static presentation; Python standard library only."""
import json
from html import escape as e
from pathlib import Path

ROOT = Path(__file__).resolve().parent
content = json.loads((ROOT / 'content.json').read_text())
sources = {s['id']: s for s in content['sources']}
groups = [('adoption', 'Part one / Adoption & accountability'), ('practice', 'Part two / A responsible workbench'), ('outcomes', 'Applications / What the work made possible'), ('discussion', 'Discussion / Questions for the lab')]
url = 'https://welsberr.github.io/presentations/beacon-generative-ai/'
parts = [f'''<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(content['title'])} | Wesley R. Elsberry</title>
<meta name="description" content="A BEACON discussion of generative AI adoption, evidence, governed memory, and accountable public work.">
<link rel="canonical" href="{url}"><meta property="og:type" content="website">
<meta property="og:title" content="{e(content['title'])}"><meta property="og:description" content="From private-sector adoption to accountable public work. Wesley R. Elsberry · BEACON.">
<meta property="og:url" content="{url}"><meta property="og:image" content="{url}social-card.png"><meta property="og:image:alt" content="Generative AI, with receipts. Wesley R. Elsberry · BEACON.">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{e(content['title'])}"><meta name="twitter:description" content="From private-sector adoption to accountable public work."><meta name="twitter:image" content="{url}social-card.png">
<link rel="stylesheet" href="style.css"><script defer src="presentation.js"></script></head><body>
<a class="skip" href="#story">Skip to presentation</a>
<header><a href="../">WRE / Presentations</a><span>BEACON · Michigan State University</span><a href="#sources">Sources</a></header>
<div id="progress" aria-hidden="true"></div>
<main id="story" tabindex="-1">
<section class="hero" id="opening" data-stop>
<p class="eyebrow">Wesley R. Elsberry · Large-group discussion</p>
<h1>Generative AI,<br>with <em>receipts.</em></h1>
<p class="lede">From private-sector adoption to accountable public work.</p>
<p class="intro">What changes when a system can produce plausible answers faster than we can check them?</p>
<a class="start" href="#delegation">Begin the story <span aria-hidden="true">↓</span></a>
<div class="hero-footer"><span>01 / Adoption &amp; accountability</span><span>02 / Building a responsible workbench</span></div>
<p class="draft-status">{e(content['status'])} · Sources checked {e(content['as_of'])} · About 30 minutes + discussion</p>
</section>
<nav class="contents" aria-label="Talk chapters"><a href="#delegation">Adoption</a><a href="#virtues">The workbench</a><a href="#timeline">Applications</a><a href="#limits">Discussion</a><a href="#sources">Source trail</a></nav>
<noscript><p class="no-script">The full talk and source trail work without JavaScript. Interactive illustrations and presentation controls require JavaScript.</p></noscript>
''']
for gid,glabel in groups:
 scenes=[s for s in content['scenes'] if s['group']==gid]
 parts.append(f'<div class="chapter" id="chapter-{gid}"><aside class="visual" aria-label="{e(glabel)}"><p class="chapter-label">{e(glabel)}</p>')
 for i,s in enumerate(scenes):
  parts.append(f'<div class="visual-panel" data-for="{s["id"]}"{ " hidden" if i else ""}>{s["visual"]}</div>')
 parts.append('</aside><div class="steps">')
 for s in scenes:
  refs=' · '.join(f'<a href="#source-{e(key)}">{e(sources[key]["title"])}</a>' for key in s['refs'])
  parts.append(f'''<section class="step" id="{s['id']}" data-stop aria-labelledby="title-{s['id']}">
<p class="eyebrow">{e(s['kicker'])}</p><h2 id="title-{s['id']}">{e(s['title'])}</h2>
{s['body']}<div class="mobile-visual">{s['visual']}</div>
{f'<p class="source">Source trail: {refs}</p>' if refs else ''}
<details class="speaker-note"><summary>Speaker notes</summary><p>{e(s['notes'])}</p></details></section>''')
 parts.append('</div></div>')
parts.append('''<section class="sources" id="sources" data-stop><p class="eyebrow">The source trail</p><h2>Follow the evidence.</h2><p class="source-intro">Company statements, implemented capabilities, demonstrations, public artifacts, and proposed evaluations are different types of evidence. The notes below preserve those distinctions.</p><p><a href="evidence/bibliography-build.json">Download bibliography counts</a> · <a href="evidence/repository-snapshots.json">Repository snapshots</a> · <a href="speaker-notes.html">Talk outline &amp; speaker notes</a></p><div class="source-grid">''')
for s in content['sources']:
 parts.append(f'<article class="source-record" id="source-{e(s["id"])}"><p class="eyebrow">{e(s["date"])}</p><h3><a href="{e(s["url"],quote=True)}">{e(s["title"])}</a></h3><p>{e(s["limit"])}</p></article>')
parts.append('''</div><p class="disclosure">Prepared with generative-AI assistance. Sources, repository documentation, and selected public artifacts were checked during preparation. The speaker supplied the firsthand account of internal adoption at an unnamed company. It is separate from RealPage’s public statements. The first-use timeline still needs confirmation. No company, university, or project endorsement is implied. Social-preview artwork was generated with AI.</p><a href="#opening">Return to the beginning ↑</a></section></main>
<nav class="presenter-controls" aria-label="Presentation controls" hidden><button id="previous" aria-label="Previous section">←</button><label class="sr-only" for="scene-select">Jump to section</label><select id="scene-select"><option value="opening">Opening</option>''')
for s in content['scenes']:
 parts.append(f'<option value="{s["id"]}">{e(s["kicker"].split(" · ")[0])} / {e(s["title"])}</option>')
parts.append('''<option value="sources">Sources</option></select><button id="next" aria-label="Next section">→</button><button id="notes" aria-pressed="false">Notes</button><button id="fullscreen">Full screen</button><button id="print">Print</button></nav><div class="sr-only" id="section-status" aria-live="polite"></div>
<footer class="site-footer">Wesley R. Elsberry · BEACON discussion · <a href="../">All presentations</a><span>Use ← / → to move between sections; Alt+N toggles notes. Normal scrolling always works.</span></footer></body></html>''')
(ROOT/'index.html').write_text('\n'.join(parts)+'\n')
notes=['# Generative AI, with receipts.','', 'Wesley R. Elsberry · Michigan State University BEACON large group','', '**Status:** speaker review draft. Default timing: 30-minute core plus discussion.','', '## Speaker input still needed','', '- Confirm meeting date and available time.','- Confirm date and anecdote of first CiteGeist use; repository history begins 19 March 2026.','', '## Suggested pacing','', '- Opening, adoption, and firsthand experience: 9 minutes.','- Values and workbench: 9 minutes.','- Applications: 8 minutes.','- Limits and discussion setup: 4 minutes.','- For a shorter talk, keep sections 1–2, 4–6, 8–10, 12, 14, and 20.','']
for s in content['scenes']:
 notes += ['## '+s['kicker']+' — '+s['title'],'',s['notes'],'','Sources: '+', '.join(sources[k]['url'] for k in s['refs']), '']
(ROOT/'speaker-notes.md').write_text('\n'.join(line.rstrip() for line in notes).rstrip()+'\n')
print(f'Rendered {len(content["scenes"])} scenes and {len(sources)} source records.')

notes_html = ['<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Speaker notes | Generative AI, with receipts.</title><link rel="stylesheet" href="style.css"></head><body><header><a href="./">Return to presentation</a><span>Speaker notes</span></header><main class="sources"><h1>Speaker notes</h1><p>Speaker review draft. Plan: adoption and firsthand experience 9 minutes; workbench 9; applications 8; discussion setup 4.</p><p>Firsthand internal-adoption account incorporated. Awaiting meeting date and duration, and first CiteGeist-use date.</p>']
for scene in content['scenes']:
    notes_html.append(f'<article class="source-record"><h2>{e(scene["kicker"])} — {e(scene["title"])}</h2><p>{e(scene["notes"])}</p><a href="./#{scene["id"]}">Open this section</a></article>')
notes_html.append('</main></body></html>')
(ROOT/'speaker-notes.html').write_text('\n'.join(notes_html)+'\n')
