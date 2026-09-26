"""Build the static review report from source.md and provenance.json."""
from pathlib import Path
import html
import json
import re
import markdown

ROOT = Path(__file__).resolve().parent
provenance = json.loads((ROOT / 'provenance.json').read_text())
rows = ['| Repository | First recorded commit | Public main | Local HEAD |',
        '|---|---|---|---|']
for repo in provenance['repositories']:
    public = repo['public_main']
    link = f"https://github.com/welsberr/{repo['name']}/tree/{public}"
    rows.append(f"| {repo['name']} | {repo['first_commit_at'][:10]} | [{public[:8]}]({link}) | `{repo['local_head'][:8]}` |")
rows.append('\nAssessment record: **' + provenance['assessed_at'] + '**. Public-main observations were made during the research session on this date; this is not a continuous branch monitor.')
source = (ROOT / 'source.md').read_text().replace('<!-- SNAPSHOTS -->', '\n'.join(rows))
(ROOT / 'report.md').write_text(source)
rendered = markdown.markdown(source, extensions=['tables', 'attr_list', 'toc'])
def label_table(match):
    table = match.group(0)
    labels = [html.unescape(re.sub('<[^>]+>', '', s)) for s in re.findall(r'<th>(.*?)</th>', table, re.S)]
    def label_row(row):
        index = iter(labels)
        return re.sub(r'<td>', lambda _: '<td data-label="'+html.escape(next(index), quote=True)+'">', row.group(0))
    return re.sub(r'<tr>.*?</tr>', label_row, table, flags=re.S)
rendered = re.sub(r'<table>.*?</table>', label_table, rendered, flags=re.S)
rendered = re.sub(r'<table>(.*?)</table>', r'<div class="table-wrap" role="region" aria-label="Comparison or evidence table" tabindex="0"><table>\1</table></div>', rendered, flags=re.S)
sources = {}
for label, url in re.findall(r'\[([^\]]+)\]\((https://[^\s)]+)\)', source):
    sources.setdefault(url, label)
catalog = '\n'.join(f'<li><a href="{html.escape(url, quote=True)}">{html.escape(label)}</a></li>' for url, label in sources.items())
nav = [('assessment','Assessment'),('comparison','Eight repositories'),('article','Section article'),('adoption','For a course'),('provenance','Evidence'),('sources','Source index')]
navigation = ''.join(f'<a href="#{target}">{label}</a>' for target,label in nav)
page = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="An evidence-based comparison of eight responsible AI workflow repositories, alternatives, implementation history and adoption tradeoffs.">
<title>What this framework contributes — BEACON companion</title><link rel="canonical" href="https://welsberr.github.io/presentations/beacon-generative-ai/comparison/"><link rel="stylesheet" href="style.css"></head>
<body><a class="skip" href="#main">Skip to report</a>
<header><a href="../">BEACON presentation</a><span>Repository comparison · Public report</span></header>
<main id="main"><nav aria-label="Report sections">{navigation}</nav>
{rendered}
<section id="sources"><h2>Source index</h2><p>Primary project documentation, repository snapshots and the confirmed practitioner article. Web sources were consulted on 26 September 2026. Links to moving documentation describe that observation, not a frozen future guarantee.</p><ol class="source-index">{catalog}</ol></section>
<div class="downloads"><a href="report.md">Download Markdown</a> · <a href="provenance.json">Provenance data</a> · <a href="publication-integrity-review.json">Review record</a></div>
</main><footer>Prepared with OpenAI Codex assistance. Reviewed and approved for publication by Wesley R. Elsberry. Personal research report; no institutional endorsement.</footer></body></html>'''
(ROOT / 'index.html').write_text(page)
(ROOT / 'sources.json').write_text(json.dumps({'observed_date':'2026-09-26','sources':[{'url':u,'label':l} for u,l in sources.items()]},indent=2)+'\n')
print(f'Built report with {len(sources)} primary-source and snapshot links.')
