(() => {
  'use strict';
  const base = '/florida-science-standards-review/research/';
  const graphURL = base + 'benchmark-variant-graph.json';
  const addendumURL = base + 'variant-graph-addendum.json';
  const materialsURL = base + 'curriculum-materials.json';
  const labelMap = {
    'doc:fl-science-1996': 'Florida Science Standards (1996)',
    'doc:fl-science-gle-1999': 'Florida Grade-Level Expectations (1998/99)',
    'doc:fl-science-2008': 'Florida Science Standards (2008)',
    'doc:fl-science-2026-draft': 'Florida Draft Science Standards (2026)',
    'doc:ngss-all-topic-standards': 'Next Generation Science Standards',
    'doc:south-carolina-science-2014': 'South Carolina Science Standards (2014)',
    'doc:external:89574ee13dd2c447': 'External comparison source (South Carolina copy)',
    'doc:external:9aab810f0e14c6e9': 'Massachusetts Science and Technology/Engineering Framework (2006)',
    'doc:external:a6ff73f1309c8ec5': 'California Science Framework (2006)',
    'doc:external:8f3e333f4967c18a': 'Florida Citizens for Science proposal (2007)'
  };
  const sourceURLs = {
    'doc:fl-science-1996': [{label:'Florida historical standards archive',url:'https://fcit.usf.edu/sss/sss/'},{label:'Internet Archive scan',url:'https://web.archive.org/web/20040203203325id_/http://www.firn.edu/doe/curric/prek12/pdf/science6.pdf'}],
    'doc:fl-science-gle-1999': [{label:'Florida historical standards archive',url:'https://fcit.usf.edu/sss/sss/'},{label:'Internet Archive GLE scan',url:'https://web.archive.org/web/20041016150428id_/http://www.firn.edu/doe/curric/prek12/pdf/scigle6.pdf'}],
    'doc:fl-science-2008': [{label:'Florida Department of Education standards page',url:'https://www.fldoe.org/academics/standards/subject-areas/math-science/science/'},{label:'Public PDF copy used for comparison',url:'https://science4inquiry.com/documents/Florida%20science_k-12_standards.pdf'}],
    'doc:fl-science-2026-draft': [{label:'Florida Department of Education review portal',url:'https://www.fldoe.org/standardsreview/'}],
    'doc:ngss-all-topic-standards': [{label:'Official NGSS topic-arrangement PDF',url:'https://www.nextgenscience.org/sites/default/files/AllTopic.pdf'}],
    'doc:external:8f3e333f4967c18a': [{label:'Florida Citizens for Science 2007 public proposal',url:'https://www.flascience.org/FCSstandards.pdf'}]
  };
  const reviewLinks = [
    {label:'2026/2008 and external-source omission crosswalk',url:base+'sources/alt-ngss/omission-crosswalk.html'},
    {label:'Alternative-source and wording analysis',url:base+'alternative-source-analysis.html'},
    {label:'Full-draft comparison',url:base+'full-draft-comparison.html'}
  ];
  const byId = new Map(), docs = [], units = [], concepts = [], assertions = [];
  const adj = new Map();
  const materialsByCode = new Map();
  const $ = s => document.querySelector(s);
  const searchInput = $('#graph-search'), versionFilter = $('#version-filter'), gradeFilter = $('#grade-filter'), statusFilter = $('#status-filter');
  const resultsEl = $('#result-list'), countEl = $('#result-count'), moreBtn = $('#more-results'), detailEl = $('#item-detail');
  let results = [], shown = 0, selectedId = null;
  const batch = 50;
  function esc(v='') { return String(v).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c])); }
  function title(id) {
    if (!id) return 'Unspecified source';
    if (labelMap[id]) return labelMap[id];
    const n = byId.get(id);
    if (n?.type === 'Concept') return n.text || n.conceptId || id;
    if (n?.type === 'TextUnit') return n.code || id;
    if (n?.type === 'StandardVersion') return (n.sourceFiles||[])[0]?.file || id;
    return id;
  }
  function textPreview(n) { return n.type === 'Concept' ? n.text : (n.text || ''); }
  function initOptions() {
    const docCounts = new Map();
    units.forEach(n => docCounts.set(n.sourceDocument,(docCounts.get(n.sourceDocument)||0)+1));
    docs.forEach(d => { const o=document.createElement('option'); o.value=d.id; o.textContent=title(d.id); versionFilter.append(o); });
    const grades=[...new Set(units.map(n=>n.gradeSpan).filter(Boolean))].sort((a,b)=>gradeSort(a)-gradeSort(b));
    grades.forEach(g=>{const o=document.createElement('option');o.value=g;o.textContent=/^\d+$/.test(g)?`Grade ${Number(g)}`:g;gradeFilter.append(o);});
    const states=[...new Set(units.map(n=>n.status).filter(Boolean))].sort((a,b)=>a.localeCompare(b));
    states.forEach(s=>{const o=document.createElement('option');o.value=s;o.textContent=s;statusFilter.append(o);});
    const host=$('#source-cards');
    host.innerHTML=docs.map(d=>`<article class="source-card"><h3>${esc(title(d.id))}</h3><p>${esc(d.status||'Source version')}</p><p><strong>${docCounts.get(d.id)||0}</strong> graph items</p><button type="button" data-doc="${esc(d.id)}">Browse these items</button></article>`).join('');
    host.querySelectorAll('button[data-doc]').forEach(b=>b.addEventListener('click',()=>{versionFilter.value=b.dataset.doc;searchInput.value='';gradeFilter.value='';statusFilter.value='';updateResults();showDoc(b.dataset.doc);}));
  }
  function gradeSort(g) { const m=String(g).match(/\d+/); return m?Number(m[0]):100; }
  function addEdge(a,b,assertion) {
    if (!a||!b||a===b||!byId.has(a)||!byId.has(b)) return;
    const e={a,b,assertion};
    if(!adj.has(a))adj.set(a,[]); if(!adj.has(b))adj.set(b,[]);
    adj.get(a).push(e); adj.get(b).push(e);
  }
  function addAssertionEdges(a) {
    const links=[];
    if(a.sourceUnit)links.push(a.sourceUnit);
    if(a.targetUnit)links.push(a.targetUnit);
    if(a.unit)links.push(a.unit);
    if(a.concept)links.push(a.concept);
    if(a.sourceDocument)links.push(a.sourceDocument);
    if(a.targetDocument)links.push(a.targetDocument);
    if(a.document)links.push(a.document);
    const unique=[...new Set(links)];
    for(let i=0;i<unique.length;i++)for(let j=i+1;j<unique.length;j++)addEdge(unique[i],unique[j],a);
  }
  function searchText(n) {
    const d=byId.get(n.sourceDocument);
    return [n.id,n.code,n.gradeSpan,n.text,n.status,n.crosswalkNote,n.provenanceStatus,n.provenanceFollowup,n.conceptId,title(n.sourceDocument),d?.status].join(' ').toLowerCase();
  }
  function updateResults() {
    const q=searchInput.value.trim().toLowerCase(), ver=versionFilter.value, grade=gradeFilter.value, state=statusFilter.value;
    results=[...units,...concepts].filter(n=>(!q||searchText(n).includes(q))&&(!ver||n.sourceDocument===ver)&&(!grade||n.gradeSpan===grade)&&(!state||n.status===state));
    results.sort((a,b)=> (a.type===b.type?0:(a.type==='TextUnit'?-1:1)) || title(a.sourceDocument).localeCompare(title(b.sourceDocument)) || (a.code||a.conceptId||'').localeCompare(b.code||b.conceptId||''));
    shown=0; resultsEl.innerHTML=''; renderMore();
    countEl.textContent=`${results.length.toLocaleString()} matching items${q||ver||grade||state?'':' · search across all represented sources'}`;
  }
  function renderMore() {
    const frag=document.createDocumentFragment(), end=Math.min(shown+batch,results.length);
    for(;shown<end;shown++){
      const n=results[shown], b=document.createElement('button'); b.type='button'; b.className='result-card'; b.setAttribute('role','listitem'); b.dataset.id=n.id;
      b.setAttribute('aria-current',String(n.id===selectedId));
      const meta=n.type==='Concept'?'Concept':`${title(n.sourceDocument)}${n.gradeSpan?` · Grade ${n.gradeSpan}`:''}${n.status?` · ${n.status}`:''}`;
      b.innerHTML=`<strong>${esc(n.code||n.conceptId||title(n.id))}</strong><span class="card-meta">${esc(meta)}</span><span class="card-text">${esc(textPreview(n).slice(0,300))}${textPreview(n).length>300?'…':''}</span>`;
      b.addEventListener('click',()=>showNode(n.id)); frag.append(b);
    }
    resultsEl.append(frag); moreBtn.hidden=shown>=results.length;
  }
  function linkList(urls) { return urls.map(x=>`<a href="${esc(x.url)}" target="_blank" rel="noopener">${esc(x.label)}</a>`).join(' · '); }
  function makeNeighborhood(id) {
    const edges=(adj.get(id)||[]).slice(0,10), ids=[id];
    edges.forEach(e=>{const other=e.a===id?e.b:e.a;if(!ids.includes(other)&&ids.length<11)ids.push(other);});
    if(ids.length<2)return '<p>No explicit graph connection is recorded for this item. That absence should not be read as evidence of no relationship.</p>';
    const cx=400,cy=138,rx=290,ry=96, coords=new Map();
    ids.forEach((nid,i)=>{if(i===0)coords.set(nid,[cx,cy]);else{const a=(2*Math.PI*(i-1)/Math.max(1,ids.length-1))-Math.PI/2;coords.set(nid,[cx+rx*Math.cos(a),cy+ry*Math.sin(a)]);}});
    const lines=edges.filter(e=>coords.has(e.a===id?e.b:e.a)).map(e=>{const other=e.a===id?e.b:e.a,p=coords.get(other);return `<line class="edge" x1="${cx}" y1="${cy}" x2="${p[0]}" y2="${p[1]}"/><text x="${(cx+p[0])/2}" y="${(cy+p[1])/2-4}" text-anchor="middle">${esc(e.assertion.relation||'related')}</text>`;}).join('');
    const circles=ids.map(nid=>{const n=byId.get(nid),p=coords.get(nid),sel=nid===id,label=(n.code||n.conceptId||title(nid));return `<g tabindex="0" role="button" aria-label="Open ${esc(label)}" data-node="${esc(nid)}"><circle class="node ${sel?'selected':''}" cx="${p[0]}" cy="${p[1]}" r="${sel?27:21}"/><text class="node-label ${sel?'selected':''}" x="${p[0]}" y="${p[1]+42}" text-anchor="middle">${esc(label.slice(0,28))}</text></g>`;}).join('');
    return `<svg class="neighborhood" viewBox="0 0 800 280" role="group" aria-label="Selected item and its recorded graph connections">${lines}${circles}</svg>`;
  }
  function addNeighborhoodHandlers() { detailEl.querySelectorAll('[data-node]').forEach(el=>{const go=()=>showNode(el.dataset.node);el.addEventListener('click',go);el.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();go();}});}); }
  function showDocumentLinks(docId) {
    const urls=sourceURLs[docId]||[];
    return `<div class="detail-links">${urls.length?linkList(urls):'<span>Direct source URL not recorded in this graph entry; see source filenames and review links below.</span>'}${linkList(reviewLinks)}</div>`;
  }
  function showDoc(id) {
    const d=byId.get(id); if(!d)return;
    selectedId=id;
    const nodeCount=units.filter(u=>u.sourceDocument===id).length;
    const files=(d.sourceFiles||[]).map(f=>`<li><code>${esc(f.file)}</code>${f.sha256?` · SHA-256 <code>${esc(f.sha256)}</code>`:''}</li>`).join('');
    detailEl.innerHTML=`<p class="item-kicker">Source version</p><h2 id="detail-title">${esc(title(id))}</h2><p>${esc(d.status||'')}</p><p><strong>${nodeCount.toLocaleString()}</strong> text items from this source are represented in the graph.</p><h3>Open source or related review</h3>${showDocumentLinks(id)}<h3>Source files recorded in the graph</h3><ul>${files||'<li>No source file names recorded.</li>'}</ul><p>Source links open the original host. Text reproduced in this graph is the item-level content available in the published research data.</p>`;
    updateSelectionStyle();
  }
  function showNode(id) {
    const n=byId.get(id); if(!n)return;
    if(n.type==='StandardVersion')return showDoc(id);
    selectedId=id; updateSelectionStyle();
    const isUnit=n.type==='TextUnit', doc=byId.get(n.sourceDocument), rels=adj.get(id)||[];
    const direct=rels.map(e=>({e,other:e.a===id?e.b:e.a})).filter(x=>byId.has(x.other)).slice(0,80);
    const materialRecord=materialsByCode.get(n.code), resources=materialRecord?.resources||[];
    const materialStatus=materialRecord?.status||'not_assessed';
    const materialLabel={not_assessed:'Not inventoried',located:'Resource located; fit not fully verified',verified:'Resource fit reviewed',none_found_in_search:'None found in a bounded search'}[materialStatus]||materialStatus;
    const material=resources.length?resources.map(r=>`<li>${r.viewUrl?`<a href="${esc(r.viewUrl)}">${esc(r.title||'Prepared curriculum material')} (view content)</a>`:esc(r.title||'Prepared curriculum material')}${r.url?` · <a href="${esc(r.url)}" target="_blank" rel="noopener">source</a>`:''} · ${esc(r.format||'format not stated')}${r.gradeFit?` · grades: ${esc(r.gradeFit)}`:''}${r.benchmarkFit?` · fit: ${esc(r.benchmarkFit)}`:''}${r.accessibility?` · accessibility: ${esc(r.accessibility)}`:''}${r.redistribution?` · redistribution: ${esc(r.redistribution)}`:''}</li>`).join(''):'<li>No prepared curriculum material is linked in the current inventory. This does not mean none is available.</li>';
    const relationRows=direct.map(({e,other})=>`<li><strong>${esc(e.assertion.relation||'related')}</strong> · <button type="button" data-open-node="${esc(other)}">${esc(title(other))}</button><div class="relation-meta">${esc(e.assertion.evidence||e.assertion.status||'No evidence note recorded.')}${e.assertion.confidence!==undefined?` · confidence recorded as ${esc(e.assertion.confidence)}`:''}${e.assertion.method?` · method: ${esc(e.assertion.method)}`:''}</div></li>`).join('');
    const sourcefiles=n.sourceFiles||[];
    detailEl.innerHTML=`<p class="item-kicker">${isUnit?'Benchmark / source text':'Concept'}</p><h2 id="detail-title">${esc(n.code||n.conceptId||n.id)}</h2><div class="item-content">${esc(textPreview(n)||'This graph node points to a source item, but does not include its complete text. Use the source locator and links below.')}</div><div class="detail-grid"><p><strong>Source:</strong> <button type="button" class="text-link" data-open-node="${esc(n.sourceDocument||'')}">${esc(title(n.sourceDocument))}</button></p><p><strong>Grade/course:</strong> ${esc(n.gradeSpan||'Not specified')}</p><p><strong>Comparison status:</strong> ${esc(n.status||'Not classified in this node')}</p><p><strong>Source locator:</strong> ${esc(n.pageOrAnchor||'Not recorded')}</p></div>${isUnit&&n.sourceDocument==='doc:fl-science-2026-draft'?`<div class="material-flag ${materialStatus==='verified'?'available':''}"><strong>Prepared curriculum material: ${esc(materialLabel)}</strong>${materialRecord?.checkedOn?`<p>Checked: ${esc(materialRecord.checkedOn)}${materialRecord.searchScope?` · Search scope: ${esc(materialRecord.searchScope)}`:''}</p>`:''}<ul>${material}</ul><p>Inventory details and redistribution fields: <a href="curriculum-materials.json">curriculum-materials.json</a>. Content is shown locally only when the recorded rights allow; otherwise, follow the source link.</p></div>`:''}${n.crosswalkNote?`<h3>Comparison note</h3><p>${esc(n.crosswalkNote)}</p>`:''}${n.provenanceStatus?`<h3>Provenance status</h3><p>${esc(n.provenanceStatus)}</p>`:''}${n.provenanceFollowup?`<p><strong>Follow-up:</strong> ${esc(n.provenanceFollowup)}</p>`:''}<h3>Source access</h3>${showDocumentLinks(n.sourceDocument)}${sourcefiles.length?`<p><strong>File references:</strong> ${sourcefiles.map(f=>`<code>${esc(f.file)}</code>${f.sha256?` <span class="relation-meta">(SHA-256 ${esc(f.sha256)})</span>`:''}`).join(' · ')}</p>`:''}<h3>Graph neighborhood</h3>${makeNeighborhood(id)}<h3>Recorded relationships (${direct.length})</h3>${direct.length?`<ul class="relation-list">${relationRows}</ul>`:'<p>No explicit relationship is recorded in the graph for this item. This is not evidence that no relationship exists.</p>'}`;
    detailEl.querySelectorAll('[data-open-node]').forEach(b=>b.addEventListener('click',()=>showNode(b.dataset.openNode)));
    addNeighborhoodHandlers();
  }
  function updateSelectionStyle(){resultsEl.querySelectorAll('.result-card').forEach(b=>b.setAttribute('aria-current',String(b.dataset.id===selectedId)));}
  async function init(){
    try{
      const [a,b,c]=await Promise.all([fetch(graphURL),fetch(addendumURL),fetch(materialsURL)]);
      if(!a.ok)throw new Error(`Graph request returned ${a.status}`);
      const primary=await a.json(), extra=b.ok?await b.json():{'@graph':[]}, materials=c.ok?await c.json():{records:[]};
      (materials.records||[]).forEach(r=>{if(r.benchmarkId)materialsByCode.set(r.benchmarkId,r);});
      const all=[...(primary['@graph']||[]),...(extra['@graph']||[])];
      all.forEach(n=>{if(!byId.has(n.id))byId.set(n.id,n);});
      byId.forEach(n=>{if(n.type==='StandardVersion')docs.push(n);else if(n.type==='TextUnit')units.push(n);else if(n.type==='Concept')concepts.push(n);else if(n.type==='EvidenceAssertion')assertions.push(n);});
      assertions.forEach(addAssertionEdges);
      units.forEach(n=>{if(n.sourceDocument)addEdge(n.id,n.sourceDocument,{relation:'sourceDocumentOf',evidence:'Source-document association recorded on the text item.'});});
      docs.sort((a,b)=>title(a.id).localeCompare(title(b.id)));
      initOptions(); updateResults();
      if(location.hash){const id=decodeURIComponent(location.hash.slice(1));if(byId.has(id))showNode(id);}
    }catch(err){countEl.textContent='The graph could not be loaded.';resultsEl.innerHTML=`<p class="loading-error">${esc(err.message)}. Use the JSON download and source reports linked below.</p>`;}
  }
  [searchInput,versionFilter,gradeFilter,statusFilter].forEach(el=>el.addEventListener(el===searchInput?'input':'change',updateResults));
  moreBtn.addEventListener('click',renderMore);
  init();
})();
