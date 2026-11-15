#!/usr/bin/env python3
"""Chapter IV: legacy contracts, both combat branches, event-proven migration."""
import argparse
import hashlib
import http.server
import json
import re
import shutil
import subprocess
import tempfile
import threading
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASELINE = '5ca2665:GAME/ALL_UNDER_HEAVEN_v0.4.99.4p_CHAPTER_III_ROADS_OF_TRUST.html'
START = r"""()=>{
 state=resolve(fresh('Chapter Four QA',16));activeTab='story';
 for(let i=0;i<220&&SCENES[state.scene].act<8;i++){
  const sc=SCENES[state.scene];state.pageIndex=sc.isPrologue?0:paginateStory(sc.body(state)).length-1;choose(0);
 }
 if(state.scene!=='ic80_council_193')throw Error('Cannot reach Chapter IV');return clone(state);
}"""
WALK = r"""seed=>{
 const queue=[clone(seed)],seen=new Set(),snapshots={},edges=[];
 while(queue.length){
  const before=queue.shift(),sc=SCENES[before.scene];
  if(sc.act!==8||seen.has(sc.id))continue;
  seen.add(sc.id);snapshots[sc.id]=clone(before);
  for(const [index,option] of sc.choices(before).entries()){
   state=clone(before);activeTab='story';state.pageIndex=paginateStory(sc.body(state)).length-1;choose(index);
   if(state.scene!==option.next||!validSave(state))throw Error('Blocked Chapter IV choice: '+sc.id+':'+index);
   const contract=clone(state);delete contract.id;delete contract.pendingFeedback;
   contract.history=contract.history.map(h=>({sceneId:h.sceneId,choice:h.choice,act:h.act,title:h.title}));
   for(const key of Object.keys(contract.flags))if(key.startsWith('m2_4q_recorded_'))delete contract.flags[key];
   if(contract.flags.m2_194_muster&&contract.visited.includes('m2_194_beihai_muster'))delete contract.militaryCareer.fieldPosition;
   edges.push({scene:sc.id,index,label:option.label,next:option.next,contract});
   if(!seen.has(state.scene))queue.push(clone(state));
  }
 }
 return {snapshots,edges,ids:Object.keys(SCENES).sort()};
}"""
ROUTES = r"""seed=>{
 const ids=['m2_194_beihai_muster','m2_194_beihai_approach','m2_194_beihai_contact','m2_194_beihai_reckoning','m2_194_xuzhou_messenger','m2_194_xuzhou_defence','m2_194_xuzhou_night','m2_194_xuzhou_debrief'];
 const routes=[];
 for(const branch of ['Infantry','Cavalry'])for(let a=0;a<3;a++)for(let b=0;b<3;b++)for(let c=0;c<3;c++){
  const selections=[a,b,c,(a+b)%3,(a+c)%3,(b+c)%3,(a+2*b)%3,(a+2*c)%3];
  state=clone(seed);activeTab='story';
  if(branch==='Cavalry')state.militaryCareer.combatService={branch,unit:'Recorded cavalry section',commander:'Recorded cavalry officer',year:193,proof:'legacy-cavalry:authorised'};
  const service=JSON.stringify(state.militaryCareer.combatService),rank=state.militaryCareer.rank;
  for(let i=0;i<ids.length;i++){
   const sc=SCENES[state.scene];if(sc.id!==ids[i])throw Error('Wrong Chapter IV stage');
   state.pageIndex=paginateStory(sc.body(state)).length-1;choose(selections[i]);
   if(!validSave(state)||state.scene===sc.id)throw Error('Invalid campaign choice');
   if(JSON.stringify(state.militaryCareer.combatService)!==service||state.militaryCareer.rank!==rank||Object.keys(state.militaryCareer.staff).length)throw Error('Branch, unit or rank rewritten');
   const position=state.militaryCareer.fieldPosition;
   if(!position.proof.startsWith('m2_194:')||position.year!==194||position.commander!=='Assigned section leader')throw Error('Missing actual field position');
   if(position.active!==[true,true,false,false,true,false,false,false][i])throw Error('Wrong field lifecycle');
   if(branch==='Cavalry'&&!/mounted/.test(position.formation))throw Error('Cavalry became infantry');
   if(branch==='Infantry'&&!/infantry|shield/.test(position.formation))throw Error('Infantry became cavalry');
   if(i<7&&(state.age!==20||state.storyClock.year!==194))throw Error('Wrong campaign age/date');
   if(i===7&&(state.age!==22||state.storyClock.year!==196))throw Error('Wrong original chapter transition');
  }
  const before=JSON.stringify(state);militaryPanel();npcMemories('xuwen');if(JSON.stringify(state)!==before)throw Error('Read-only field panel mutated save');
  routes.push({branch,selections});
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
    baseline = subprocess.run(['git', 'show', BASELINE], cwd=ROOT, check=True, capture_output=True).stdout
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
            browser = playwright.chromium.launch(executable_path=shutil.which('chromium'), headless=True, args=['--no-sandbox'])
            base = browser.new_page()
            base.goto(url + '/baseline.html')
            seed = base.evaluate(START)
            previous = base.evaluate(WALK, seed)
            base.close()
            for width in (390, 1280):
                context = browser.new_context(viewport={'width': width, 'height': 900})
                page = context.new_page()
                errors = []
                page.on('pageerror', lambda error: errors.append(str(error)))
                page.goto(url + '/active.html')
                actual = page.evaluate(WALK, seed)
                assert len(previous['ids']) == 632 and set(previous['ids']).issubset(actual['ids'])
                assert set(actual['ids']) - set(previous['ids']) == {
                    'm2_197_road_orders', 'm2_197_road_contact', 'm2_197_road_aftermath',
                    'm2_198_xiaopei_orders', 'm2_198_xiaopei_pressure', 'm2_198_xiaopei_retreat', 'm2_198_xiaopei_after',
                    'm2_201_watch_orders', 'm2_201_watch_contact', 'm2_201_watch_after',
                }
                assert len(actual['edges']) == len(previous['edges'])
                for old, new in zip(previous['edges'], actual['edges']):
                    assert old == new, f'Legacy Chapter IV contract changed: {old["scene"]}:{old["index"]}'
                routes = page.evaluate(ROUTES, actual['snapshots']['m2_194_beihai_muster'])
                for branch in ('Infantry', 'Cavalry'):
                    selected = [row['selections'] for row in routes if row['branch'] == branch]
                    for a in range(8):
                        for b in range(a + 1, 8):
                            assert len({(row[a], row[b]) for row in selected}) == 9
                migration_cases = 0
                for source, target in [('m2_194_beihai_muster','m2_194_beihai_approach'),('m2_194_beihai_approach','m2_194_beihai_contact'),('m2_194_beihai_contact','m2_194_beihai_reckoning'),('m2_194_xuzhou_messenger','m2_194_xuzhou_defence'),('m2_194_xuzhou_defence','m2_194_xuzhou_night')]:
                    for history_only in (False, True):
                        candidate = json.loads(json.dumps(previous['snapshots'][target]))
                        if history_only:
                            candidate['visited'] = []
                        page.evaluate(r"""({seed,source})=>{
                         const after=resolve(clone(seed));
                         if(after.militaryCareer.fieldPosition.proof!==auh4qPosition(seed,source).proof)throw Error('Missing legacy position migration');
                         const original=clone(seed);original.militaryCareer.fieldPosition=after.militaryCareer.fieldPosition;
                         if(JSON.stringify(after)!==JSON.stringify(original))throw Error('Position migration changed unrelated state');
                        }""", {'seed': candidate, 'source': source})
                        migration_cases += 1
                page.evaluate(r"""seed=>{
                 for(const mode of ['flag-only','invalid-selection','unknown-branch','future-position','unrelated-194-position','different-scene']){
                  const s=clone(seed);
                  if(mode==='flag-only'){s.visited=[];s.history=[];}
                  if(mode==='invalid-selection')s.flags.m2_194_xucall='__proto__';
                  if(mode==='unknown-branch')delete s.militaryCareer.combatService;
                  if(mode==='future-position')s.militaryCareer.fieldPosition.year=195;
                  if(mode==='unrelated-194-position'){s.militaryCareer.fieldPosition.year=194;s.militaryCareer.fieldPosition.proof='another-lawful-battle';}
                  if(mode==='different-scene')s.scene='lc81_196_qin';
                  const before=JSON.stringify(s.militaryCareer.fieldPosition);
                  if(JSON.stringify(resolve(s).militaryCareer.fieldPosition)!==before)throw Error('Unsafe migration: '+mode);
                 }
                 if(auh4qPosition(seed,'__proto__')!==null)throw Error('Invalid event source accepted');
                }""", previous['snapshots']['m2_194_xuzhou_defence'])
                # New event guards must not replay a past assignment after a later stage.
                page.evaluate(r"""seed=>{
                 state=clone(seed);const choices=SCENES[state.scene].choices(state);choices[0].effect(state);
                 const once=JSON.stringify(state);choices[0].effect(state);if(JSON.stringify(state)!==once)throw Error('Repeated position event');
                 state.militaryCareer.fieldPosition={...state.militaryCareer.fieldPosition,year:195,proof:'later-battle'};
                 const later=JSON.stringify(state);choices[0].effect(state);if(JSON.stringify(state)!==later)throw Error('Old event replaced later position');
                }""", actual['snapshots']['m2_194_beihai_muster'])
                page.evaluate(r"""seed=>{
                 const body=SCENES.ch04_02.body(seed),tea=SCENES.ch04_linyue_tea.body(seed);
                 if(body.includes('Two years of uncertain')||tea.includes('Two years ago'))throw Error('False 191 first-meeting date');
                 if(body.includes('your soldiers')||body.includes('You have the men measure'))throw Error('Private commands bridge party');
                 const minor=clone(seed);minor.age=17;
                 if(SCENES.ch04_02.choices(minor).some(o=>o.next==='ch04_linyue_tea'))throw Error('Underage romance route');
                }""", actual['snapshots']['ch04_02'])
                for target, active_position in [('m2_194_xuzhou_defence', True), ('m2_194_xuzhou_night', False)]:
                    page.evaluate('seed=>{localStorage.setItem(SAVE_KEY,JSON.stringify(seed));handleAction("load-original");}', actual['snapshots'][target])
                    page.reload()
                    assert page.evaluate('validSave(state)&&state.militaryCareer.fieldPosition.active') is active_position
                    page.locator('#menuToggle').click()
                    page.locator('#gameMenu [data-nav="military"]').click()
                    assert 'Xu Province' in page.locator('#screen').inner_text()
                    assert page.evaluate('document.documentElement.scrollWidth<=innerWidth')
                assert not errors, errors
                result['checks'].append({'width': width, 'sampled_scenes': len(actual['snapshots']), 'legacy_choice_edges': len(actual['edges']), 'legacy_parity': 'PASS except documented field positions and event markers', 'campaign_routes': len(routes), 'both_branches_eight_factors_pairwise': 'PASS', 'migration_positive_cases': migration_cases, 'migration_negative_cases': 6, 'idempotence_and_later_position': 'PASS', 'lin_yue_chronology_and_age_gate': 'PASS', 'http_reload_active_and_retired': 'PASS', 'military_dom_no_overflow': 'PASS', 'page_errors': errors})
                context.close()
            browser.close()
    finally:
        server.shutdown()
        server.server_close()
    result['limits'] = 'Representative states plus pairwise 194 campaign routes. Cavalry uses a documented synthetic legacy assignment fixture. Physical-device file:// and full novel editorial QA remain pending.'
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
