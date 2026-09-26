#!/usr/bin/env python3
"""Render the static presentation; Python standard library only."""
import json
from html import escape as e
from pathlib import Path

ROOT = Path(__file__).resolve().parent
content = json.loads((ROOT / 'content.json').read_text())
sources = {s['id']: s for s in content['sources']}
dives = content.get('deep_dives', [])
dive_by_id = {d['id']: d for d in dives}
main_by_id = {s['id']: s for s in content['scenes']}
all_scenes = content['scenes'] + [s for d in dives for s in d['scenes']]
acknowledgements = content['acknowledgements']

def render_acknowledgements():
 result = ['<section class="sources acknowledgements" id="acknowledgements" data-stop tabindex="-1" aria-labelledby="acknowledgements-title"><p class="eyebrow">Credits &amp; development</p><h2 id="acknowledgements-title">Acknowledgements</h2>']
 result += [f'<p>{e(acknowledgements[key])}</p>' for key in ['credit', 'notice']]
 result += ['<h3>Development timeline</h3>', f'<p class="timeline-note">{e(acknowledgements["timeline_note"])}</p>', '<ol class="development-timeline">']
 for milestone in acknowledgements['milestones']:
  links = ' · '.join(f'<a href="https://github.com/welsberr/welsberr.github.io/commit/{sha}" aria-label="View commit {sha}">{sha}</a>' for sha in milestone['commits'])
  result.append(f'<li><span class="milestone-time">{e(milestone["time"])}</span><div><strong>{e(milestone["title"])}</strong><p>{e(milestone["detail"])}</p><p class="commit-links">{links}</p></div></li>')
 result.append('</ol><p><a href="#opening">Return to the beginning ↑</a></p></section>')
 return '\n'.join(result)

# Catch authoring errors before generating navigation or publishing HTML.
scene_ids = [s['id'] for s in all_scenes]
assert len(scene_ids) == len(set(scene_ids)), 'Duplicate scene ID'
for scene in all_scenes:
 for key in scene['refs']:
  assert key in sources, f'Unknown source: {key}'
for scene in content['scenes']:
 for key in scene.get('deep_dives', []):
  assert key in dive_by_id, f'Unknown deep dive: {key}'
for dive in dives:
 assert dive['caller'] in main_by_id, f'Unknown return section: {dive["caller"]}'

def dive_link(dive, caller, label=None):
 return f'<a class="deep-dive-link" href="#{dive["scenes"][0]["id"]}" data-deep-dive="{dive["id"]}" data-return-to="{caller}">{e(label or "Deep Dive: " + dive["title"])}</a>'

def return_link(dive):
 caller = dive['caller']
 return f'<a class="dive-return" href="#{caller}" data-return-for="{dive["id"]}">Return to main talk: {e(main_by_id[caller]["title"])}</a>'
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
<nav class="contents" aria-label="Talk chapters"><a href="#delegation">Adoption</a><a href="#virtues">The workbench</a><a href="#timeline">Applications</a><a href="#limits">Discussion</a><a href="comparison/">Capabilities &amp; alternatives</a><a href="#deep-dives">Deep Dives</a><a href="#sources">Source trail</a><a href="#acknowledgements">Acknowledgements</a></nav>
<noscript><p class="no-script">The full talk and source trail work without JavaScript. Interactive illustrations and presentation controls require JavaScript.</p></noscript>
''']
def render_chapter(gid, glabel, scenes, dive=None):
 dive_attr = f' data-dive="{dive["id"]}"' if dive else ''
 parts.append(f'<div class="chapter" id="chapter-{gid}"{dive_attr}><aside class="visual" aria-label="{e(glabel)}"><p class="chapter-label">{e(glabel)}</p>')
 for i,s in enumerate(scenes):
  parts.append(f'<div class="visual-panel" data-for="{s["id"]}"{ " hidden" if i else ""}>{s["visual"]}</div>')
 parts.append('</aside><div class="steps">')
 for s in scenes:
  refs=' · '.join(f'<a href="#source-{e(key)}">{e(sources[key]["title"])}</a>' for key in s['refs'])
  extras = ''
  if dive:
   extras = '<nav class="dive-links" aria-label="Return to the main talk">' + return_link(dive) + '</nav>'
  elif s.get('deep_dives'):
   extras = '<nav class="dive-links" aria-label="Optional deep dives">' + ''.join(dive_link(dive_by_id[k], s['id']) for k in s['deep_dives']) + '</nav>'
  parts.append(f'''<section class="step{' dive-step' if dive else ''}" id="{s['id']}" data-stop tabindex="-1" aria-labelledby="title-{s['id']}">
<p class="eyebrow">{e(s['kicker'])}</p><h2 id="title-{s['id']}">{e(s['title'])}</h2>
{s['body']}<div class="mobile-visual">{s['visual']}</div>
{extras}
{f'<p class="source">Source trail: {refs}</p>' if refs else ''}
<details class="speaker-note"><summary>Speaker notes</summary><p>{e(s['notes'])}</p></details></section>''')
 parts.append('</div></div>')
for gid,glabel in groups:
 render_chapter(gid, glabel, [s for s in content['scenes'] if s['group']==gid])
parts.append('''<section class="sources dive-directory" id="deep-dives" data-stop tabindex="-1"><p class="eyebrow">Optional appendix · Deep Dives</p><h2>Follow the question that interests you.</h2><p class="source-intro">The main talk ends above. Each optional scrollytell explores one part of the workbench. Open a dive from a main section to return to that section afterward.</p><div class="dive-grid">''')
for dive in dives:
 parts.append(f'<article class="dive-card"><h3>{dive_link(dive, "deep-dives", dive["title"])}</h3><p>{e(dive["description"])}</p><span>{len(dive["scenes"])} short sections</span></article>')
parts.append('</div><p><a href="#conversation">Return to the discussion</a> · <a href="#sources">Go to the source trail</a></p></section>')
for dive in dives:
 render_chapter('dive-' + dive['id'], 'Deep Dive / ' + dive['title'], dive['scenes'], dive)
parts.append('''<section class="sources" id="sources" data-stop><p class="eyebrow">The source trail</p><h2>Follow the evidence.</h2><p class="source-intro">Published measurements, implemented capabilities, demonstrations, public artifacts, and proposed evaluations are different types of evidence. The notes below preserve those distinctions.</p><p><a href="evidence/bibliography-build.json">Download bibliography counts</a> · <a href="evidence/repository-snapshots.json">Repository snapshots</a> · <a href="speaker-notes.html">Talk outline &amp; speaker notes</a> · <a href="evidence/public-release.json">Revision and archive record</a></p><div class="source-grid">''')
for s in content['sources']:
 parts.append(f'<article class="source-record" id="source-{e(s["id"])}"><p class="eyebrow">{e(s["date"])}</p><h3><a href="{e(s["url"],quote=True)}">{e(s["title"])}</a></h3><p>{e(s["limit"])}</p></article>')
parts.append('''</div><p class="disclosure">Sources, repository documentation, and selected public artifacts were checked during preparation. The speaker supplied the firsthand account of internal adoption at an unnamed company. Productivity and quality are management goals, not measured results reported here. The timeline uses the earliest CiteGeist repository commit rather than claiming a date of first personal use.</p></section>''')
parts.append(render_acknowledgements())
parts.append('''</main>
<nav class="presenter-controls" aria-label="Presentation controls" hidden><button id="previous" aria-label="Previous section">←</button><label class="sr-only" for="scene-select">Jump to section</label><select id="scene-select"><optgroup label="Main talk"><option value="opening">Opening</option>''')
for s in content['scenes']:
 parts.append(f'<option value="{s["id"]}">{e(s["kicker"].split(" · ")[0])} / {e(s["title"])}</option>')
parts.append('</optgroup><optgroup label="Optional Deep Dives"><option value="deep-dives">Deep Dive directory</option>')
for dive in dives:
 for s in dive['scenes']:
  parts.append(f'<option value="{s["id"]}">{e(s["kicker"])} / {e(s["title"])}</option>')
parts.append('''</optgroup><option value="sources">Sources</option><option value="acknowledgements">Acknowledgements</option></select><button id="next" aria-label="Next section">→</button><button id="notes" aria-pressed="false">Notes</button><button id="fullscreen">Full screen</button><button id="print">Print</button></nav><div class="sr-only" id="section-status" aria-live="polite"></div>
<footer class="site-footer">Wesley R. Elsberry · BEACON discussion · <a href="../">All presentations</a><a href="#acknowledgements">Acknowledgements &amp; AI assistance</a><span>Use ← / → to move between sections; Alt+N toggles notes. Normal scrolling always works.</span></footer></body></html>''')
(ROOT/'index.html').write_text('\n'.join(parts)+'\n')
notes=['# Generative AI, with receipts.','', 'Wesley R. Elsberry · Michigan State University BEACON large group','', '**Status:** author-approved public revision, 26 September 2026. Default timing: approximately 30 minutes plus discussion.','', '## Presentation context','', '- Revised after the BEACON discussion for broader public sharing.','- The timeline uses CiteGeist repository history beginning 19 March 2026, not an asserted first-use date.','- Companion report: [Repository capabilities and alternatives](comparison/).','', '## Suggested pacing','', '- Opening, adoption, and firsthand experience: 9 minutes.','- Values and workbench: 9 minutes.','- Applications, including the TalkOrigins update workflow: 8 minutes.','- Limits and discussion setup: 4 minutes.','- For a shorter talk, focus on delegation, personal experience, policy, memory, citations, the Archive workflow, and discussion.','- Deep Dives are optional discussion material, outside the 30-minute core. Links return to the section that opened the dive.','']
for s in all_scenes:
 notes += ['## '+s['kicker']+' — '+s['title'],'',s['notes'],'','Sources: '+', '.join(sources[k]['url'] for k in s['refs']), '']
 if s.get('deep_dives'):
  notes += ['Deep Dives: '+', '.join(dive_by_id[k]['title'] for k in s['deep_dives']), '']
 for dive in dives:
  if s in dive['scenes']:
   notes += ['Default return: #'+dive['caller']+'. When opened from another main section, the return link follows that caller.', '']
notes += ['## Acknowledgements', '', acknowledgements['credit'], '', acknowledgements['notice'], '', '### Development timeline', '', acknowledgements['timeline_note'], '']
for milestone in acknowledgements['milestones']:
 notes += [f'- {milestone["time"]} — {milestone["title"]}: {milestone["detail"]} (' + ', '.join(milestone['commits']) + ')']
(ROOT/'speaker-notes.md').write_text('\n'.join(line.rstrip() for line in notes).rstrip()+'\n')
print(f'Rendered {len(content["scenes"])} main scenes, {len(dives)} deep dives ({len(all_scenes)-len(content["scenes"])} scenes), and {len(sources)} source records.')

notes_html = ['<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Speaker notes | Generative AI, with receipts.</title><link rel="stylesheet" href="style.css"></head><body><header><a href="./">Return to presentation</a><span>Speaker notes</span></header><main class="sources"><h1>Speaker notes</h1><p>Author-approved public revision, 26 September 2026. Suggested pacing: adoption and firsthand experience 9 minutes; workbench 9; applications 8; discussion setup 4.</p><p>The personal account remains anonymous. The timeline uses repository history rather than asserting a first-use date. <a href="comparison/">Repository capabilities and alternatives report</a>.</p>']
for scene in all_scenes:
    notes_html.append(f'<article class="source-record"><h2>{e(scene["kicker"])} — {e(scene["title"])}</h2><p>{e(scene["notes"])}</p><a href="./#{scene["id"]}">Open this section</a></article>')
notes_html.append(render_acknowledgements().replace('href="#opening"', 'href="./#opening"'))
notes_html.append('</main></body></html>')
(ROOT/'speaker-notes.html').write_text('\n'.join(notes_html)+'\n')
