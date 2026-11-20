#!/usr/bin/env python3
"""Render a reviewable static viewer directly from the Didactopus YAML pack."""
import argparse
import hashlib
import json
from html import escape
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / 'pack'
OUT = ROOT / 'evidence/rehearsal/didactopus-pack.html'
VALIDATION = ROOT / 'evidence/rehearsal/didactopus-validation.json'
NAMES = ['pack.yaml', 'concepts.yaml', 'roadmap.yaml', 'projects.yaml', 'rubrics.yaml']
e = lambda value: escape(str(value), quote=True)
raw = {name: (PACK / name).read_text(encoding='utf-8') for name in NAMES}
docs = {name: yaml.safe_load(content) for name, content in raw.items()}
record = json.loads(VALIDATION.read_text(encoding='utf-8'))
hashes = {name: hashlib.sha256((PACK / name).read_bytes()).hexdigest() for name in NAMES}
matched = hashes == record['file_sha256']
metadata = docs['pack.yaml']
concepts = docs['concepts.yaml']['concepts']
stages = docs['roadmap.yaml']['stages']
projects = docs['projects.yaml']['projects']
rubrics = docs['rubrics.yaml']['rubrics']
titles = {item['id']: item['title'] for item in concepts}
def concept_names(ids):
    return ', '.join(e(titles.get(item, item + ' (unresolved)')) for item in ids) or 'None listed'
def items(values):
    return ''.join('<li>' + e(item) + '</li>' for item in values) or '<li>None listed</li>'
status = ('<strong>Structural validation passed.</strong> The displayed files match the recorded validation.' if matched and record['ok'] else
          '<strong>Validation needs review.</strong> The displayed files do not match a passing recorded validation.')
parts = [f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Didactopus draft pack viewer</title><link rel="stylesheet" href="../../style.css"></head>
<body><main class="activity pack-viewer"><p class="eyebrow">Didactopus · draft pack</p><h1>{e(metadata['display_name'])}</h1>
<p class="lead">{e(metadata['description'])}</p>
<p class="pack-status">{status}<br><span>Recorded {e(record['recorded_date_utc'])} UTC · {len(concepts)} concepts · {len(stages)} learning stage · {len(projects)} project · {len(rubrics)} rubric</span></p>
<p>Structural validation checks the pack’s format. Scientific accuracy, instructional effectiveness, and reuse terms still require review.</p>
<nav class="pack-nav" aria-label="Pack sections"><a href="#concepts">Concepts</a><a href="#sequence">Learning sequence</a><a href="#project">Project</a><a href="#rubric">Rubric</a><a href="#source">Source files</a></nav>
<section id="concepts"><p class="eyebrow">1 · Concepts</p><h2>What the learner should understand</h2><div class="pack-grid">''']
for n, c in enumerate(concepts, 1):
    parts.append(f'''<article class="pack-card"><p class="pack-number">{n:02d}</p><h3>{e(c['title'])}</h3><p>{e(c['description'])}</p><p><strong>Prerequisite:</strong> {concept_names(c.get('prerequisites', []))}</p><p><strong>Evidence of understanding:</strong></p><ul>{items(c.get('mastery_signals', []))}</ul></article>''')
parts.append('</div></section><section id="sequence"><p class="eyebrow">2 · Learning sequence</p><h2>How the activity is organized</h2>')
for stage in stages:
    parts.append(f'<article class="pack-card"><h3>{e(stage["title"])}</h3><p><strong>Concepts:</strong> {concept_names(stage.get("concepts", []))}</p><p><strong>Checkpoint prompts:</strong></p><ul>{items(stage.get("checkpoint", []))}</ul></article>')
parts.append('</section><section id="project"><p class="eyebrow">3 · Project</p><h2>What the learner produces</h2>')
for project in projects:
    parts.append(f'<article class="pack-card"><h3>{e(project["title"])}</h3><p><strong>Prerequisites:</strong> {concept_names(project.get("prerequisites", []))}</p><p><strong>Difficulty:</strong> {e(project.get("difficulty", "Not specified"))}</p><p><strong>Deliverables:</strong></p><ul>{items(project.get("deliverables", []))}</ul></article>')
parts.append('</section><section id="rubric"><p class="eyebrow">4 · Draft rubric</p><h2>What to consider in review</h2>')
for rubric in rubrics:
    parts.append(f'<article class="pack-card"><h3>{e(rubric["title"])}</h3><ul>{items(rubric.get("criteria", []))}</ul><p>This pack lists criteria only; it does not yet define scoring levels.</p></article>')
parts.append(f'''</section><section id="source"><p class="eyebrow">5 · Inspect the sources</p><h2>The YAML behind the viewer</h2>
<p>Version {e(metadata['version'])} · Author: {e(metadata['author'])} · License: {e(metadata['license'])}. This is a rendered snapshot. Rebuild it after editing a source file.</p>
<p><a href="didactopus-validation.json" target="beacon_pack_file">Open the recorded validation and file hashes</a></p>''')
for name in NAMES:
    parts.append(f'<details class="pack-source"><summary>{e(name)}</summary><p><a href="../../pack/{e(name)}" target="beacon_pack_file">Open {e(name)} separately</a></p><pre><code>{e(raw[name])}</code></pre></details>')
parts.append('''</section><p><a href="../../index.html#build" target="beacon_talk">Return to section 04</a> · <a href="../../preview/" target="beacon_activity">Open the activity</a></p></main></body></html>''')
output = '\n'.join(parts) + '\n'
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--check', action='store_true', help='Fail if the viewer is out of date or validation hashes do not match.')
args = parser.parse_args()
if args.check:
    if not matched:
        raise SystemExit('Pack changed since the recorded Didactopus validation.')
    if not OUT.exists() or OUT.read_text(encoding='utf-8') != output:
        raise SystemExit('Pack viewer is out of date; rebuild it.')
    print('Viewer matches its YAML sources and validation snapshot.')
else:
    OUT.write_text(output, encoding='utf-8')
    print('Built', OUT, '(validation matches)' if matched else '(validation is stale)')
