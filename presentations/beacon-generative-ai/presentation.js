'use strict';
(() => {
  document.documentElement.classList.add('js');
  const stops = [...document.querySelectorAll('[data-stop]')];
  const controls = document.querySelector('.presenter-controls');
  const selector = document.querySelector('#scene-select');
  const status = document.querySelector('#section-status');
  const previous = document.querySelector('#previous');
  const next = document.querySelector('#next');
  const notesButton = document.querySelector('#notes');
  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)');
  let current = 0;
  let queued = false;
  const diveChapters = [...document.querySelectorAll('[data-dive]')];
  const validCallers = new Set(stops.filter(stop => !stop.closest('[data-dive]')).map(stop => stop.id));
  const returnTargets = new Map();
  function setReturn(diveId, caller) {
    if (!validCallers.has(caller)) return;
    const chapter = diveChapters.find(item => item.dataset.dive === diveId);
    if (!chapter) return;
    const target = document.getElementById(caller);
    const title = target.querySelector('h1,h2')?.textContent || 'Deep Dive directory';
    returnTargets.set(diveId, caller);
    chapter.querySelectorAll('[data-return-for]').forEach(link => {
      link.href = `#${caller}`;
      link.textContent = caller === 'deep-dives' ? 'Return to Deep Dive directory' : `Return to main talk: ${title}`;
    });
    // A reload within a dive retains its caller; storage is optional.
    try { sessionStorage.setItem(`beacon-dive-${diveId}`, caller); } catch { /* Native default links still work. */ }
  }
  diveChapters.forEach(chapter => {
    const id = chapter.dataset.dive;
    let caller = chapter.querySelector('[data-return-for]').getAttribute('href').slice(1);
    try { caller = sessionStorage.getItem(`beacon-dive-${id}`) || caller; } catch { /* Use the canonical caller. */ }
    setReturn(id, caller);
  });
  controls.hidden = false;
  function update() {
    queued = false;
    const marker = window.innerHeight * 0.43;
    let index = 0;
    stops.forEach((stop, i) => { if (stop.getBoundingClientRect().top <= marker) index = i; });
    current = index;
    selector.value = stops[index].id;
    previous.disabled = index === 0;
    next.disabled = index === stops.length - 1;
    document.querySelectorAll('.chapter').forEach(chapter => {
      const steps = [...chapter.querySelectorAll('.step')];
      let active = steps[0];
      steps.forEach(step => { if (step.getBoundingClientRect().top <= marker) active = step; });
      chapter.querySelectorAll('.visual-panel').forEach(panel => { panel.hidden = panel.dataset.for !== active.id; });
    });
    const chapter = stops[index].closest('[data-dive]');
    const start = chapter ? chapter.getBoundingClientRect().top + window.scrollY : 0;
    const end = chapter ? start + chapter.offsetHeight - window.innerHeight : document.querySelector('#deep-dives').offsetTop - window.innerHeight;
    const progress = end > start ? (window.scrollY - start) / (end - start) * 100 : 100;
    document.querySelector('#progress').style.width = `${Math.min(100, Math.max(0, progress))}%`;
  }
  function schedule() { if (!queued) { queued = true; requestAnimationFrame(update); } }
  function go(index, immediate = false) {
    const target = stops[Math.max(0, Math.min(stops.length - 1, index))];
    const dive = target.closest('[data-dive]')?.dataset.dive;
    history.pushState(dive ? { dive, caller: returnTargets.get(dive) } : null, '', `#${target.id}`);
    target.scrollIntoView({ behavior: immediate || reduced.matches ? 'instant' : 'smooth', block: 'start' });
    if (target.hasAttribute('tabindex')) target.focus({ preventScroll: true });
    status.textContent = target.querySelector('h1,h2')?.textContent || 'Sources';
  }
  document.addEventListener('click', event => {
    if (event.defaultPrevented || event.button !== 0 || event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
    const link = event.target.closest('[data-deep-dive], [data-return-for]');
    if (!link) return;
    const targetId = link.getAttribute('href').slice(1);
    const index = stops.findIndex(stop => stop.id === targetId);
    if (index < 0) return;
    event.preventDefault();
    if (link.dataset.deepDive) setReturn(link.dataset.deepDive, link.dataset.returnTo);
    go(index, true);
  });
  window.addEventListener('popstate', event => {
    if (event.state?.dive) setReturn(event.state.dive, event.state.caller);
    schedule();
  });
  previous.addEventListener('click', () => go(current - 1));
  next.addEventListener('click', () => go(current + 1));
  selector.addEventListener('change', () => go(stops.findIndex(stop => stop.id === selector.value)));
  function toggleNotes() {
    const open = notesButton.getAttribute('aria-pressed') !== 'true';
    document.querySelectorAll('.speaker-note').forEach(note => { note.open = open; });
    notesButton.setAttribute('aria-pressed', String(open));
    schedule();
  }
  notesButton.addEventListener('click', toggleNotes);
  document.addEventListener('keydown', event => {
    if (event.ctrlKey || event.metaKey || event.shiftKey || event.defaultPrevented) return;
    if (event.target.closest('input,select,textarea,button,summary,a,[contenteditable="true"]')) return;
    if (event.altKey && event.key.toLowerCase() === 'n') { event.preventDefault(); toggleNotes(); return; }
    if (event.altKey) return;
    if (event.key === 'ArrowRight') { event.preventDefault(); go(current + 1); }
    if (event.key === 'ArrowLeft') { event.preventDefault(); go(current - 1); }
  });
  const fullscreen = document.querySelector('#fullscreen');
  if (!document.fullscreenEnabled) fullscreen.hidden = true;
  fullscreen.addEventListener('click', async () => {
    try { if (document.fullscreenElement) await document.exitFullscreen(); else await document.documentElement.requestFullscreen(); }
    catch { status.textContent = 'Full screen is unavailable in this browser.'; }
  });
  document.addEventListener('fullscreenchange', () => { fullscreen.textContent = document.fullscreenElement ? 'Exit full screen' : 'Full screen'; });
  document.querySelector('#print').addEventListener('click', () => window.print());
  const demo = document.querySelector('#gate-demo');
  function evaluateGate() {
    const scope = document.querySelector('#visibility').value;
    const evidence = document.querySelector('#evidence').value;
    const review = document.querySelector('#review').value;
    const reasons = [];
    let state = 'hold';
    if (scope === 'private') reasons.push('Private-only material cannot be released publicly.');
    if (evidence === 'missing') reasons.push('Resolve the citation and check claim support.');
    if (evidence === 'metadata') reasons.push('An identifier match does not establish claim support.');
    if (evidence === 'stale') reasons.push('Reassess stale or contradicted evidence before release.');
    if (review !== 'approved') reasons.push('Record human release review.');
    if (scope === 'private' || evidence === 'stale') state = 'block';
    if (!reasons.length) state = 'allow';
    const result = document.querySelector('#gate-result');
    result.dataset.state = state;
    result.textContent = reasons.length ? `${state === 'block' ? 'Block' : 'Hold'}: ${reasons.join(' ')}` : 'Eligible in this simulation: scope, source support, and human review are satisfied. Real release rules may require further checks.';
  }
  demo.addEventListener('change', evaluateGate);
  evaluateGate();
  window.addEventListener('scroll', schedule, { passive: true });
  window.addEventListener('resize', schedule);
  window.addEventListener('hashchange', schedule);
  update();
})();
