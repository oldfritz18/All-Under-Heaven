#!/usr/bin/env python3
"""Chapter I browser contracts against the original starter (sampled states).

Requires Playwright and Chromium. This is not exhaustive branch or device QA.
"""
import argparse
import hashlib
import http.server
import json
import re
import shutil
import subprocess
import tempfile
import threading
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WALK = r"""() => {
 const queue=[resolve(fresh('Chapter One QA',16))], seen=new Set(), snapshots={}, edges=[];
 while(queue.length){
  const seed=queue.shift(), sc=SCENES[seed.scene];
  if(sc.act>=6||seen.has(sc.id))continue;
  seen.add(sc.id);snapshots[sc.id]=clone(seed);
  for(const [index,option] of sc.choices(seed).entries()){
   if(!SCENES[option.next])throw Error(`Missing destination: ${sc.id} -> ${option.next}`);
   state=clone(seed);activeTab='story';state.pageIndex=sc.isPrologue?0:paginateStory(sc.body(state)).length-1;
   choose(index);
   if(state.scene!==option.next)throw Error(`Choice blocked: ${sc.id}:${index}: ${banner}`);
   if(!validSave(state))throw Error(`Invalid save: ${sc.id}:${index}`);
   const enteringTwo=SCENES[state.scene].act>=6;
   if(state.age!==(enteringTwo?17:16)||state.storyClock.year!==(enteringTwo?191:190))throw Error(`Chapter I date/age: ${sc.id}`);
   if(state.militaryCareer?.rank&&!['Private'].includes(state.militaryCareer.rank))throw Error(`Unearned rank: ${sc.id}`);
   if((state.innerCircle?.active||[]).length||(state.dragonGenerals?.active||[]).length||Object.keys(state.militaryCareer?.staff||{}).length)throw Error(`Unearned appointment: ${sc.id}`);
   const contract=clone(state);delete contract.id;delete contract.pendingFeedback;
   delete contract.flags.ic80_wei_reply_190;
   contract.history=contract.history.map(h=>({sceneId:h.sceneId,choice:h.choice,act:h.act,title:h.title}));
   contract.journal=contract.journal.filter(n=>!['A Copyist with His Own Work','A Disagreement at the Registry'].includes(n.label));
   edges.push({scene:sc.id,index,label:option.label,next:option.next,contract});
   if(!seen.has(state.scene))queue.push(clone(state));
  }
 }
 return {sceneCount:Object.keys(SCENES).length,ids:Object.keys(SCENES).sort(),edges,snapshots,staff:AUH_MC_SPECIAL_STAFF};
}"""


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--report', type=Path)
    args = parser.parse_args()
    from playwright.sync_api import sync_playwright
    active = ROOT / 'GAME' / (ROOT / 'GAME/ACTIVE_BUILD.txt').read_text().strip()
    archive_path = next(ROOT.glob('ALL_UNDER_HEAVEN_CODEX_GOAL_STARTER_*.zip'))
    with zipfile.ZipFile(archive_path) as archive:
        baseline = archive.read('ALL_UNDER_HEAVEN_CODEX_GOAL_READY/GAME/ALL_UNDER_HEAVEN_v0.4.99.4m_CHAPTER_I_HISTORICAL_COHESION.html')
    current = active.read_bytes()
    images = lambda source: [hashlib.sha256(m).hexdigest() for m in re.findall(rb'data:image/[^;"\s]+;base64,[A-Za-z0-9+/=]+', source)]
    assert images(current) == images(baseline), 'Embedded portraits changed'
    with tempfile.TemporaryDirectory() as temporary:
        js = Path(temporary) / 'game.js'
        js.write_bytes(b'\n'.join(re.findall(rb'<script[^>]*>(.*?)</script>', current, re.S)))
        subprocess.run(['node', '--check', str(js)], check=True, capture_output=True)
    documents = {'/baseline.html': baseline, '/active.html': current}

    class Handler(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            content = documents.get(self.path)
            self.send_response(200 if content is not None else 404)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers()
            if content is not None:
                self.wfile.write(content)

        def log_message(self, *_):
            pass

    server = http.server.ThreadingHTTPServer(('127.0.0.1', 0), Handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    url = f'http://127.0.0.1:{server.server_port}'
    results = {'build': active.name, 'html_sha256': hashlib.sha256(current).hexdigest(), 'portrait_data_uris': len(images(current)), 'checks': []}
    try:
        with sync_playwright() as playwright:
            chromium = shutil.which('chromium') or shutil.which('google-chrome')
            options = {'headless': True, 'args': ['--no-sandbox']}
            if chromium:
                options['executable_path'] = chromium
            browser = playwright.chromium.launch(**options)
            baseline_page = browser.new_page()
            baseline_page.goto(url + '/baseline.html')
            old = baseline_page.evaluate(WALK)
            baseline_page.close()
            for width in (390, 1280):
                context = browser.new_context(viewport={'width': width, 'height': 900})
                page = context.new_page()
                errors = []
                page.on('pageerror', lambda error: errors.append(str(error)))
                page.goto(url + '/active.html')
                data = page.evaluate(WALK)
                assert old['sceneCount'] == 630
                assert set(old['ids']).issubset(data['ids'])
                assert set(data['ids']) - set(old['ids']) == {'m1p_192_route_table', 'm1p_192_second_reading'}
                assert data['staff'] == old['staff']
                assert len(data['edges']) == len(old['edges'])
                for previous, successor in zip(old['edges'], data['edges']):
                    assert previous == successor, f'Legacy choice contract changed: {previous["scene"]}:{previous["index"]}'
                for index, reply in enumerate(('exchange', 'courtesy', 'disagree')):
                    seed = data['snapshots']['ic80_scholar_190']
                    result = page.evaluate(r"""({seed,index,reply})=>{
                     state=clone(seed);state.pageIndex=paginateStory(SCENES[state.scene].body(state)).length-1;choose(index);
                     const rendered=SCENES.gate.body(state), memory=npcMemories('weizhen');
                     if(!rendered.includes(AUH4N_WEI_REPLY[reply]))throw Error('Missing chosen registry reply');
                     if(!memory.some(t=>t.includes(reply==='exchange'?'agreed to exchange':reply==='courtesy'?'without promising':'disagreed about')))throw Error('Missing chosen People memory');
                     const before=JSON.stringify(state);SCENES.gate.body(state);npcMemories('weizhen');
                     if(JSON.stringify(state)!==before)throw Error('Read-only callback mutated save');
                     return clone(state);
                    }""", {'seed': seed, 'index': index, 'reply': reply})
                    page.evaluate('seed=>{state=resolve(seed);save();}', result)
                    page.reload()
                    saved = page.evaluate('()=>({scene:state.scene,reply:state.flags.ic80_wei_reply_190,valid:validSave(state)})')
                    assert saved == {'scene': 'gate', 'reply': reply, 'valid': True}
                page.evaluate(r"""() => {
                 for(const historyOnly of [false,true]){
                  state=resolve(fresh('Legacy',16));state.scene='gate';state.flags.ic80_wei_190=true;state.flags.ic80_wei_reply_190='disagree';
                  state.history=historyOnly?[{sceneId:'ic80_scholar_190'}]:[];
                  if(SCENES.gate.body(state).includes(AUH4N_WEI_REPLY.disagree)!==historyOnly)throw Error('Registry visit/history provenance');
                  if(npcMemories('weizhen').some(t=>t.includes('disagreed about'))!==historyOnly)throw Error('Memory visit/history provenance');
                 }
                 state=resolve(fresh('Unwitnessed',16));state.scene='ford_approach';state.flags.ic80_xu_190='share';
                 if(SCENES.ford_approach.body(state).includes('Two ends of the world'))throw Error('Phantom shared-work recall');
                }""")
                # Use actual DOM buttons for both departure branches; test pagination and menu.
                for choice in (0, 2):
                    page.evaluate(r"""({seed})=>{state=clone(seed);activeTab='story';state.pageIndex=0;render();}""", {'seed': data['snapshots']['ic80_register_190']})
                    while page.locator('[data-action="next-page"]').count():
                        page.locator('[data-action="next-page"]').click()
                    page.locator(f'[data-choice="{choice}"]').click()
                    assert page.evaluate('state.scene') == ('ic80_scholar_190' if choice == 0 else 'gate')
                    page.locator('#menuToggle').click()
                    assert page.locator('#gameMenu').is_visible()
                    page.locator('[data-close-menu]').click()
                    assert not page.locator('#gameMenu').is_visible()
                    assert page.evaluate('document.documentElement.scrollWidth<=window.innerWidth'), 'Horizontal overflow'
                # Import and reopen a real baseline HTTP save without adding a reply it never recorded.
                legacy = old['snapshots']['ford_approach']
                # Load through the game's handler so pagehide autosave cannot overwrite
                # the seeded legacy slot with the previously active campaign.
                page.evaluate('seed=>{localStorage.setItem(SAVE_KEY,JSON.stringify(seed));handleAction("load-original");}', legacy)
                page.reload()
                legacy_result = page.evaluate('()=>({valid:validSave(state),scene:state?.scene,reply:state?.flags?.ic80_wei_reply_190,notice:document.querySelector("#storageNotice").textContent})')
                assert legacy_result['valid'] and legacy_result['scene'] == 'ford_approach' and not legacy_result.get('reply'), legacy_result
                assert not errors, errors
                results['checks'].append({'width': width, 'sampled_chapter1_scenes': len(data['snapshots']), 'sampled_choice_edges': len(data['edges']), 'legacy_contracts': 'PASS', 'choice_specific_replies': 3, 'http_save_reload': 'PASS', 'legacy_http_save_migration': 'PASS', 'visit_and_history_guards': 'PASS', 'dom_pagination_choices_menu': 'PASS', 'page_errors': errors})
                context.close()
            browser.close()
    finally:
        server.shutdown()
        server.server_close()
    results['limits'] = 'Representative states per scene, not all path combinations. HTTP Chromium tests do not certify physical-device file:// durability.'
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(results, indent=2) + '\n')
    print(json.dumps(results, indent=2))


if __name__ == '__main__':
    main()
