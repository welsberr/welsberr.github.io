"""Browser regression checks. Requires Playwright + Chromium in the test environment.

Usage: python3 tests/verify_deep_dives.py http://127.0.0.1:8769/presentations/beacon-generative-ai/
"""
import json
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
CONTENT = json.loads((ROOT / 'content.json').read_text())
BASE = sys.argv[1] if len(sys.argv) > 1 else 'http://127.0.0.1:8769/presentations/beacon-generative-ai/'
DIVES = {d['id']: d for d in CONTENT['deep_dives']}
CALLS = [(s['id'], key) for s in CONTENT['scenes'] for key in s.get('deep_dives', [])]

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={'width': 1440, 'height': 900}, reduced_motion='reduce')
    errors = []
    page.on('pageerror', lambda err: errors.append(str(err)))
    page.goto(BASE)

    def selected(scene_id):
        page.wait_for_function('''(id) => {
            const panel = document.querySelector(`[data-for="${id}"]`);
            const rect = document.getElementById(id).getBoundingClientRect();
            return document.querySelector('#scene-select').value === id && (!panel || !panel.hidden) && rect.top <= innerHeight * .43 && rect.bottom > innerHeight * .43;
        }''', arg=scene_id)

    def jump(scene_id):
        page.locator('#scene-select').select_option(scene_id)
        selected(scene_id)

    assert page.locator('.step:not(.dive-step)').count() == 20
    assert page.locator('[data-dive]').count() == 7
    assert page.locator('.dive-step').count() == 19
    assert page.locator('.source-record').count() == 25
    assert page.locator('a[href="comparison/"]').count() >= 3
    ids = page.locator('[id]').evaluate_all('(els)=>els.map(e=>e.id)')
    assert len(ids) == len(set(ids))
    fragments = page.locator('a[href^="#"]').evaluate_all('(els)=>els.map(e=>e.getAttribute("href").slice(1))')
    assert not set(fragments) - set(ids)

    # Every main-section entry must return to that caller, from every step in its dive.
    for caller, key in CALLS:
        jump(caller)
        page.locator(f'#{caller} [data-deep-dive="{key}"]').click()
        first = DIVES[key]['scenes'][0]['id']
        selected(first)
        assert page.evaluate('document.activeElement.id') == first
        for scene in DIVES[key]['scenes']:
            assert page.locator(f'#{scene["id"]} [data-return-for]').get_attribute('href') == '#' + caller
        last = DIVES[key]['scenes'][-1]['id']
        jump(last)
        assert page.locator(f'[data-for="{last}"]').is_visible()
        page.locator(f'#{last} [data-return-for]').click()
        selected(caller)
        assert page.evaluate('document.activeElement.id') == caller

    # Keyboard activation and reload preserve a non-default caller.
    jump('bibliography-outcome')
    entry = page.locator('#bibliography-outcome [data-deep-dive="citegeist"]')
    entry.focus()
    page.keyboard.press('Enter')
    selected('dive-citegeist')
    page.reload()
    selected('dive-citegeist')
    assert page.locator('#dive-citegeist .dive-return').get_attribute('href') == '#bibliography-outcome'
    page.screenshot(path='/tmp/beacon-dive-citegeist.png')

    # History retains the caller associated with the earlier visit to the same dive.
    jump('virtues')
    page.locator('#virtues [data-deep-dive="policy"]').click()
    selected('dive-policy')
    page.locator('#dive-policy .dive-return').click()
    selected('virtues')
    jump('claimwright')
    page.locator('#claimwright [data-deep-dive="policy"]').click()
    selected('dive-policy')
    page.go_back()
    page.go_back()
    page.go_back()
    selected('dive-policy')
    assert page.locator('#dive-policy .dive-return').get_attribute('href') == '#virtues'

    # Directory entry returns to the directory, rather than a stale prior caller.
    jump('deep-dives')
    page.locator('#deep-dives [data-deep-dive="citegeist"]').click()
    selected('dive-citegeist')
    page.locator('#dive-citegeist .dive-return').click()
    selected('deep-dives')

    jump('talkorigins-workflow')
    page.screenshot(path='/tmp/beacon-talkorigins-workflow.png')
    jump('dive-geniehive')
    page.screenshot(path='/tmp/beacon-dive-geniehive.png')
    widths = []
    for width in [1440, 1024, 768, 760, 390, 320]:
        page.set_viewport_size({'width': width, 'height': 900 if width > 760 else 844})
        for scene_id in ['talkorigins-workflow', 'deep-dives', 'dive-citegeist', 'dive-talkorigins-translation', 'dive-geniehive-controls']:
            jump(scene_id)
            assert page.evaluate('document.documentElement.scrollWidth <= innerWidth'), (width, scene_id)
        widths.append(width)
        if width == 390:
            jump('talkorigins-workflow')
            page.screenshot(path='/tmp/beacon-talkorigins-mobile.png', full_page=False)
            page.locator('#talkorigins-workflow [data-deep-dive="geniehive"]').click()
            selected('dive-geniehive')
            page.locator('#dive-geniehive .dive-return').click()
            selected('talkorigins-workflow')

    # Disabled storage must not break navigation.
    isolated = browser.new_context(reduced_motion='reduce')
    isolated.add_init_script('Storage.prototype.getItem = function(){throw new Error("disabled")}; Storage.prototype.setItem = function(){throw new Error("disabled")};')
    fallback = isolated.new_page()
    fallback.goto(BASE + '#virtues')
    fallback.locator('#virtues [data-deep-dive="policy"]').click()
    assert fallback.locator('#dive-policy .dive-return').get_attribute('href') == '#virtues'

    # Without JS, native fragment links still reach every dive and its canonical caller.
    nojs = browser.new_page(java_script_enabled=False)
    nojs.goto(BASE)
    for key, dive in DIVES.items():
        caller = dive['caller']
        nojs.locator(f'#{caller} [data-deep-dive="{key}"]').click()
        assert nojs.url.endswith('#' + dive['scenes'][0]['id'])
        nojs.locator(f'#{dive["scenes"][-1]["id"]} .dive-return').click()
        assert nojs.url.endswith('#' + caller)
    assert not errors, errors
    browser.close()
print(json.dumps({'main_scenes': 20, 'dives': 7, 'dive_scenes': 19, 'caller_round_trips': len(CALLS), 'keyboard_reload_history': 'pass', 'directory_return': 'pass', 'storage_disabled': 'pass', 'native_no_js_links': 'pass', 'widths': widths, 'page_errors': errors}, indent=2))
