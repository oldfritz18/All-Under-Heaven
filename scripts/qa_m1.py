#!/usr/bin/env python3
"""M1 checkpoint: Chapter III parity and real early/declined friendship routes."""
import argparse
import hashlib
import http.server
import json
import shutil
import threading
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
START = r"""()=>{
 state=resolve(fresh('M1 QA',16));activeTab='story';
 for(let i=0;i<200&&SCENES[state.scene].act<7;i++){
  const sc=SCENES[state.scene];state.pageIndex=sc.isPrologue?0:paginateStory(sc.body(state)).length-1;choose(0);
 }
 if(state.scene!=='ic80_relay_191')throw Error('Did not reach original Chapter III entry');
 return clone(state);
}"""
WALK = r"""seed=>{
 const queue=[clone(seed)],seen=new Set(),edges=[],snapshots={};
 while(queue.length){
  const before=queue.shift(),sc=SCENES[before.scene];
  if(sc.act!==7||seen.has(sc.id))continue;
  seen.add(sc.id);snapshots[sc.id]=clone(before);
  for(const [index,option] of sc.choices(before).entries()){
   state=clone(before);activeTab='story';state.pageIndex=paginateStory(sc.body(state)).length-1;choose(index);
   if(state.scene!==option.next||!validSave(state))throw Error('Blocked Chapter III edge: '+sc.id+':'+index+':'+banner);
   if(state.militaryCareer.rank!=='Private'||state.innerCircle.active.length||state.dragonGenerals.active.length||Object.keys(state.militaryCareer.staff).length)throw Error('Automatic rank, membership, or staff');
   const contract=clone(state);delete contract.id;delete contract.pendingFeedback;
   contract.history=contract.history.map(h=>({sceneId:h.sceneId,choice:h.choice,act:h.act,title:h.title}));
   edges.push({scene:sc.id,index,label:option.label,next:option.next,contract});
   if(!seen.has(state.scene))queue.push(clone(state));
  }
 }
 return {edges,snapshots};
}"""
ROUTE = r"""options=>{
 state=resolve(fresh('M1 Route',16));activeTab='story';const trace=[];
 for(let step=0;step<220;step++){
  const sc=SCENES[state.scene],choices=sc.choices(state);
  if(sc.id==='ic80_council_193'){
   const eligible=ic80Eligible(state,'weizhen');
   if(eligible!==options.expectOffer)throw Error('Wrong 193 opportunity: '+JSON.stringify(options));
   if(state.innerCircle.active.length||Object.keys(state.militaryCareer.staff).length||state.militaryCareer.rank!=='Private')throw Error('Premature appointment');
   const checkpoint=clone(state);
   const index=options.recruit?choices.findIndex(o=>o.label.startsWith('Invite Wei Zhen')):choices.findIndex(o=>o.label.startsWith('Thank him'));
   if(index<0)throw Error('Missing explicit accept/refuse choice');
   state.pageIndex=paginateStory(sc.body(state)).length-1;choose(index);
   if((state.innerCircle.grandStrategist==='weizhen')!==options.recruit)throw Error('Recruitment ignored consent');
   if(Object.keys(state.militaryCareer.staff).length||state.militaryCareer.rank!=='Private')throw Error('Personal adviser became military staff or rank');
   return {trace,checkpoint,after:clone(state)};
  }
  let index=0;
  if(sc.id==='ic80_register_190'&&options.skip190)index=2;
  if(sc.id==='ic80_relay_191'&&options.skip191)index=1;
  if(sc.id==='ch03_02'&&options.method!==null)index=choices.findIndex(o=>o.next==='m1p_192_route_table');
  if(sc.id==='m1p_192_route_table')index=options.method;
  if(sc.id==='m1p_192_second_reading')index=options.reply;
  if(index<0||!choices[index])throw Error('Missing route choice: '+sc.id);
  trace.push({scene:sc.id,choice:index,year:state.storyClock.year,age:state.age});
  state.pageIndex=sc.isPrologue?0:paginateStory(sc.body(state)).length-1;choose(index);
  if(!validSave(state)||state.scene===sc.id)throw Error('Invalid route: '+sc.id+':'+banner);
 }
 throw Error('Route did not reach 193 council');
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
    scenarios = [
        dict(name='second_opportunity_verify', skip190=True, skip191=False, method=0, reply=0, expectOffer=True, recruit=True),
        dict(name='second_opportunity_challenge', skip190=True, skip191=False, method=1, reply=0, expectOffer=True, recruit=False),
        dict(name='first_meeting_only_192', skip190=True, skip191=True, method=0, reply=0, expectOffer=False, recruit=False),
        dict(name='explicit_later_refusal', skip190=False, skip191=False, method=1, reply=2, expectOffer=False, recruit=False),
        dict(name='one_afternoon_no_commitment', skip190=True, skip191=False, method=0, reply=1, expectOffer=False, recruit=False),
        dict(name='leave_route_table', skip190=True, skip191=False, method=2, reply=0, expectOffer=False, recruit=False),
        dict(name='original_opportunity_preserved', skip190=False, skip191=False, method=None, reply=0, expectOffer=True, recruit=True),
    ]
    result = {'build': active.name, 'sha256': hashlib.sha256(current).hexdigest(), 'checks': []}
    try:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(executable_path=shutil.which('chromium'), headless=True, args=['--no-sandbox'])
            base = browser.new_page()
            base.goto(url + '/baseline.html')
            seed = base.evaluate(START)
            old = base.evaluate(WALK, seed)
            # The baseline's Cavalry and later-year routes must still bypass Pan.
            bypass = base.evaluate(r"""()=>{
             return ['Cavalry','later-year'].map(mode=>{
              const s=clone(state);s.scene='ch2_35';
              if(mode==='Cavalry')s.militaryCareer.combatService.branch='Cavalry';else{s.storyClock.year=192;s.flags.novelYear=192;}
              return {mode,seed:s,choices:SCENES.ch2_35.choices(s).map(o=>({label:o.label,next:o.next}))};
             });
            }""")
            base.close()
            for width in (390, 1280):
                context = browser.new_context(viewport={'width': width, 'height': 900})
                page = context.new_page()
                errors = []
                page.on('pageerror', lambda error: errors.append(str(error)))
                page.goto(url + '/active.html')
                new = page.evaluate(WALK, seed)
                original_edges = [edge for edge in new['edges'] if not edge['scene'].startswith('m1p_') and not edge['next'].startswith('m1p_')]
                assert len(original_edges) == len(old['edges'])
                for previous, successor in zip(old['edges'], original_edges):
                    assert previous == successor, f'Chapter III legacy contract changed: {previous["scene"]}:{previous["index"]}'
                for case in bypass:
                    choices = page.evaluate('s=>SCENES.ch2_35.choices(s).map(o=>({label:o.label,next:o.next}))', case['seed'])
                    assert choices == case['choices'] and all(choice['next'] != 'pan_01_muster' for choice in choices)
                completed = []
                accepted = None
                for scenario in scenarios:
                    route = page.evaluate(ROUTE, scenario)
                    if scenario['skip190']:
                        assert 'ic80_scholar_190' not in [step['scene'] for step in route['trace']]
                        assert not route['checkpoint']['flags'].get('ic80_wei_190')
                    if scenario['name'] == 'second_opportunity_verify':
                        accepted = route['checkpoint']
                    completed.append({'name': scenario['name'], 'choices': len(route['trace']) + 1, 'result': 'PASS'})
                assert accepted
                page.evaluate(r"""seed=>{
                 for(const historyOnly of [false,true]){
                  state=clone(seed);if(historyOnly)state.visited=[];
                  if(!ic80Eligible(state,'weizhen')||!hasWitnessed('weizhen'))throw Error('Valid 191/192 history lost');
                  const before=JSON.stringify(state);npcObservations('weizhen');npcMemories('weizhen');SCENES.ic80_council_193.body(state);
                  if(JSON.stringify(state)!==before)throw Error('Read-only relationship panel mutated save');
                 }
                 state=clone(seed);state.visited=[];state.history=[];
                 if(ic80Eligible(state,'weizhen'))throw Error('Flag-only strategist opportunity');
                 if(npcObservations('weizhen').some(t=>t.includes('In 192')))throw Error('Unwitnessed 192 observation');
                 if(npcMemories('weizhen').some(t=>t.includes('agreed in 192')))throw Error('Unwitnessed 192 memory');
                }""", accepted)
                # Replaying only the new effects cannot stack trust or rewrite a decision.
                page.evaluate(r"""seed=>{
                 const table=clone(seed);delete table.flags.m1p_192_method;delete table.flags.m1p_192_reply;
                 const first=SCENES.m1p_192_route_table.choices(table)[0];first.effect(table);
                 const once=JSON.stringify(table);first.effect(table);if(JSON.stringify(table)!==once)throw Error('Repeated route effect');
                 const reply=SCENES.m1p_192_second_reading.choices(table)[0];reply.effect(table);
                 const twice=JSON.stringify(table);reply.effect(table);if(JSON.stringify(table)!==twice)throw Error('Repeated relationship effect');
                }""", accepted)
                page.evaluate('seed=>{localStorage.setItem(SAVE_KEY,JSON.stringify(seed));handleAction("load-original");}', accepted)
                page.reload()
                assert page.evaluate('validSave(state)&&ic80Eligible(state,"weizhen")&&state.innerCircle.active.length===0')
                # New optional encounter is usable through real paginated UI choices.
                page.evaluate('seed=>{state=clone(seed);activeTab="story";state.pageIndex=0;render();}', new['snapshots']['ch03_02'])
                while page.locator('[data-action="next-page"]').count():
                    page.locator('[data-action="next-page"]').click()
                page.locator('[data-choice="1"]').click()
                assert page.evaluate('state.scene') == 'm1p_192_route_table'
                assert page.evaluate('document.documentElement.scrollWidth<=innerWidth')
                page.locator('#menuToggle').click()
                page.locator('#gameMenu [data-nav="people"]').click()
                assert page.evaluate('hasWitnessed("weizhen")')
                page.locator('[data-people-gender="male"]').click()
                page.locator('[data-people-category="friends"]').click()
                assert 'Wei Zhen' in page.locator('#screen').inner_text()
                assert not errors, errors
                result['checks'].append({'width': width, 'chapter3_sampled_scenes': len(new['snapshots']), 'original_choice_edges': len(old['edges']), 'new_optional_edges': len(new['edges'])-len(old['edges']), 'legacy_parity': 'PASS', 'full_prologue_to_193_routes': completed, 'new_effect_idempotence': 'PASS', 'history_only_and_flag_only': 'PASS', 'cavalry_and_later_year_pan_bypass': 'PASS', 'http_save_reload': 'PASS', 'dom_optional_encounter_people': 'PASS', 'page_errors': errors})
                context.close()
            browser.close()
    finally:
        server.shutdown()
        server.server_close()
    result['limits'] = 'M1 functional checkpoint and targeted narrative review only; not every combination or final editorial/device release certification.'
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
