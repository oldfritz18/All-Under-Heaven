#!/usr/bin/env python3
"""Chapter II legacy contracts, pairwise tactical routes, and position lifecycle.

Requires Playwright and Chromium. HTTP browser QA, not physical-device QA.
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
START = r"""() => {
 state=resolve(fresh('Chapter Two QA',16));activeTab='story';
 for(let i=0;i<160&&SCENES[state.scene].act<6;i++){
  const sc=SCENES[state.scene];state.pageIndex=sc.isPrologue?0:paginateStory(sc.body(state)).length-1;choose(0);
 }
 if(state.scene!=='ch2_01')throw Error('Could not reach Chapter II naturally');
 return clone(state);
}"""
WALK = r"""seed => {
 const queue=[resolve(clone(seed))],seen=new Set(),edges=[],snapshots={};
 while(queue.length){
  const before=queue.shift(),sc=SCENES[before.scene];
  if(sc.act!==6||seen.has(sc.id))continue;
  seen.add(sc.id);snapshots[sc.id]=clone(before);
  for(const [index,option] of sc.choices(before).entries()){
   state=clone(before);activeTab='story';state.pageIndex=paginateStory(sc.body(state)).length-1;choose(index);
   if(state.scene!==option.next||!validSave(state))throw Error('Blocked or invalid choice: '+sc.id+':'+index);
   if(state.age!==17||state.storyClock.year!==191)throw Error('Wrong Chapter II year/age: '+sc.id);
   if(state.militaryCareer.rank!=='Private'||state.militaryCareer.combatService.branch!=='Infantry')throw Error('Unexpected Chapter II rank/branch');
   if(state.innerCircle.active.length||state.dragonGenerals.active.length||Object.keys(state.militaryCareer.staff).length)throw Error('Automatic appointment');
   const contract=clone(state);delete contract.id;delete contract.pendingFeedback;
   contract.history=contract.history.map(h=>({sceneId:h.sceneId,choice:h.choice,act:h.act,title:h.title}));
   contract.journal=contract.journal.filter(n=>n.label!=='Leaving the Pan River Bank');
   // Intentional bug fix: retire the selected position on arrival at the report.
   if(option.next==='pan_06_account')delete contract.militaryCareer.fieldPosition.active;
   edges.push({scene:sc.id,index,label:option.label,next:option.next,contract});
   if(!seen.has(state.scene))queue.push(clone(state));
  }
 }
 return {edges,snapshots,ids:Object.keys(SCENES).sort(),staff:AUH_MC_SPECIAL_STAFF};
}"""
ROUTES = r"""seed => {
 const routes=[];
 for(let a=0;a<3;a++)for(let b=0;b<3;b++)for(let c=0;c<3;c++){
  const selections=[a,b,c,(a+b)%3,(a+c)%3,(b+c)%3];
  state=clone(seed);activeTab='story';
  for(let stage=0;stage<6;stage++){
   const sc=SCENES[state.scene],before=state.scene;
   if(sc.id!==['pan_01_muster','pan_02_contact','pan_03_vanguard','pan_04_bridge','pan_05_rider','pan_06_account'][stage])throw Error('Wrong tactical stage');
   if(stage===4&&selections[3]===2&&sc.body(state).includes('You see him wheel against the pursuit'))throw Error('Rear rank sees hidden mounted fight');
   state.pageIndex=paginateStory(sc.body(state)).length-1;choose(selections[stage]);
   if(state.scene===before||!validSave(state))throw Error('Pan route blocked: '+banner);
   if(state.militaryCareer.fieldPosition.active!==(stage<4))throw Error('Position active after withdrawal or retired too early');
   if(state.age!==17||state.storyClock.year!==191||state.militaryCareer.rank!=='Private')throw Error('Unearned age/rank');
   if(state.flags.historical_meet_zhaoyun)throw Error('Reported rider became a personal encounter');
  }
  const report=SCENES[state.scene];state.pageIndex=paginateStory(report.body(state)).length-1;choose(0);
  if(state.scene!=='ic80_relay_191'||!state.flags.hc06_pan_completed)throw Error('Missing original Chapter III return route');
  const before=JSON.stringify(state),html=militaryPanel(),memories=npcMemories('xuwen');
  if(!html.includes(AUH4O_PAN_WITHDRAWAL[state.flags.hc06_pan_withdraw]))throw Error('Missing Military withdrawal');
  if(!memories.includes(AUH4O_PAN_WITHDRAWAL[state.flags.hc06_pan_withdraw]))throw Error('Missing People withdrawal');
  if(JSON.stringify(state)!==before)throw Error('Panel or memory mutated save');
  if(state.journal.filter(n=>n.label==='Leaving the Pan River Bank').length!==1)throw Error('Missing/duplicate withdrawal note');
  routes.push(selections);
 }
 return routes;
}"""


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--report', type=Path)
    args = parser.parse_args()
    from playwright.sync_api import sync_playwright
    active = ROOT / 'GAME' / (ROOT / 'GAME/ACTIVE_BUILD.txt').read_text().strip()
    current = active.read_bytes()
    with zipfile.ZipFile(next(ROOT.glob('ALL_UNDER_HEAVEN_CODEX_GOAL_STARTER_*.zip'))) as archive:
        baseline = archive.read('ALL_UNDER_HEAVEN_CODEX_GOAL_READY/GAME/ALL_UNDER_HEAVEN_v0.4.99.4m_CHAPTER_I_HISTORICAL_COHESION.html')
    images = lambda content: re.findall(rb'data:image/[^;"\s]+;base64,[A-Za-z0-9+/=]+', content)
    assert images(current) == images(baseline)
    with tempfile.TemporaryDirectory() as temporary:
        js = Path(temporary) / 'game.js'
        js.write_bytes(b'\n'.join(re.findall(rb'<script[^>]*>(.*?)</script>', current, re.S)))
        subprocess.run(['node', '--check', str(js)], check=True, capture_output=True)
    documents = {'/baseline.html': baseline, '/active.html': current}

    class Handler(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            content = documents.get(self.path)
            self.send_response(200 if content else 404)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers()
            if content:
                self.wfile.write(content)

        def log_message(self, *_):
            pass

    server = http.server.ThreadingHTTPServer(('127.0.0.1', 0), Handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    url = f'http://127.0.0.1:{server.server_port}'
    result = {'build': active.name, 'sha256': hashlib.sha256(current).hexdigest(), 'checks': []}
    try:
        with sync_playwright() as playwright:
            executable = shutil.which('chromium') or shutil.which('google-chrome')
            browser = playwright.chromium.launch(headless=True, executable_path=executable, args=['--no-sandbox'])
            baseline_page = browser.new_page()
            baseline_page.goto(url + '/baseline.html')
            seed = baseline_page.evaluate(START)
            previous = baseline_page.evaluate(WALK, seed)
            baseline_page.close()
            for width in (390, 1280):
                context = browser.new_context(viewport={'width': width, 'height': 900})
                page = context.new_page()
                errors = []
                page.on('pageerror', lambda error: errors.append(str(error)))
                page.goto(url + '/active.html')
                actual = page.evaluate(WALK, seed)
                assert len(previous['ids']) == 630
                assert set(previous['ids']).issubset(actual['ids'])
                assert set(actual['ids']) - set(previous['ids']) == {
                    'm1p_192_route_table', 'm1p_192_second_reading',
                    'm2_197_road_orders', 'm2_197_road_contact', 'm2_197_road_aftermath',
                    'm2_198_xiaopei_orders', 'm2_198_xiaopei_pressure', 'm2_198_xiaopei_retreat', 'm2_198_xiaopei_after',
                    'm2_201_watch_orders', 'm2_201_watch_contact', 'm2_201_watch_after',
                }
                assert actual['staff'] == previous['staff']
                assert len(actual['edges']) == len(previous['edges'])
                for old, new in zip(previous['edges'], actual['edges']):
                    assert old == new, f'Legacy choice changed: {old["scene"]}:{old["index"]}'
                routes = page.evaluate(ROUTES, actual['snapshots']['pan_01_muster'])
                # Every pair of the six three-way tactical decisions is represented.
                for a in range(6):
                    for b in range(a + 1, 6):
                        assert len({(route[a], route[b]) for route in routes}) == 9
                legacy = previous['snapshots']['pan_06_account']
                assert legacy['militaryCareer']['fieldPosition']['active'] is True
                for history_only in (False, True):
                    candidate = json.loads(json.dumps(legacy))
                    if history_only:
                        candidate['visited'] = []
                    check = page.evaluate(r"""seed=>{
                     const before=clone(seed),after=resolve(clone(seed));
                     if(after.militaryCareer.fieldPosition.active!==false)throw Error('Legacy position was not retired');
                     before.militaryCareer.fieldPosition.active=false;
                     if(JSON.stringify(after)!==JSON.stringify(before))throw Error('Migration granted or rewrote other state');
                     return validSave(after);
                    }""", candidate)
                    assert check
                page.evaluate(r"""seed=>{
                 for(const mode of ['flag-only','cavalry','different-proof','later-scene']){
                  const candidate=clone(seed);
                  if(mode==='flag-only'){candidate.visited=[];candidate.history=[];}
                  if(mode==='cavalry')candidate.militaryCareer.combatService.branch='Cavalry';
                  if(mode==='different-proof')candidate.militaryCareer.fieldPosition.proof='later-battle:existing';
                  if(mode==='later-scene')candidate.scene='ch03_01';
                  if(resolve(candidate).militaryCareer.fieldPosition.active!==true)throw Error('Migration changed unrelated position: '+mode);
                 }
                }""", legacy)
                # Save an actual post-withdrawal state, then reload using the game handler.
                current_seed = actual['snapshots']['pan_06_account']
                page.evaluate('seed=>{localStorage.setItem(SAVE_KEY,JSON.stringify(seed));handleAction("load-original");}', current_seed)
                page.reload()
                assert page.evaluate('validSave(state)&&state.scene==="pan_06_account"&&state.militaryCareer.fieldPosition.active===false')
                # Real UI navigation and next-page control while inspecting the fixed state.
                page.locator('#menuToggle').click()
                page.locator('#gameMenu [data-nav="military"]').click()
                assert page.locator('[aria-label="Pan River service record"]').is_visible()
                assert page.evaluate('document.documentElement.scrollWidth<=innerWidth')
                page.locator('#menuToggle').click()
                page.locator('#gameMenu [data-nav="story"]').click()
                if page.locator('[data-action="next-page"]').count():
                    page.locator('[data-action="next-page"]').click()
                assert not errors, errors
                result['checks'].append({'width': width, 'sampled_scenes': len(actual['snapshots']), 'sampled_choice_edges': len(actual['edges']), 'legacy_choice_parity': 'PASS except intentional position retirement and its new journal note', 'complete_tactical_routes': len(routes), 'six_factors_pairwise_coverage': 'PASS', 'migration_positive_cases': 2, 'migration_negative_cases': 4, 'save_reload_http': 'PASS', 'military_people_journal': 'PASS', 'dom_military_navigation': 'PASS', 'page_errors': errors})
                context.close()
            browser.close()
    finally:
        server.shutdown()
        server.server_close()
    result['limits'] = 'Representative chapter states plus 27 pairwise tactical routes per viewport, not every full-campaign combination. Physical-device file:// remains untested.'
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
