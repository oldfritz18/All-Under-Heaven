#!/usr/bin/env python3
"""Chapter VI legacy contracts on identical input states and Xiaopei routes."""
import argparse, hashlib, http.server, json, re, shutil, subprocess, tempfile, threading
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
BASELINE='66e51f0:GAME/ALL_UNDER_HEAVEN_v0.4.99.4r_CHAPTER_V_BETWEEN_ORDERS.html'
NEW={'m2_198_xiaopei_orders','m2_198_xiaopei_pressure','m2_198_xiaopei_retreat','m2_198_xiaopei_after'}
PROJECT=r"""function project(s,source,index,next,label){
 const contract=clone(s);delete contract.id;delete contract.pendingFeedback;delete contract.flags.m2_198_deployed;
 contract.history=contract.history.map(h=>({sceneId:h.sceneId,choice:h.choice,act:h.act,title:h.title}));
 if(source==='ch06_06'&&index===0){next='forward-insert-or-old-continuation';contract.scene=next;}
 return {source,index,next,label,contract};
}"""
START=r"""()=>{
 state=resolve(fresh('Chapter Six QA',16));activeTab='story';
 for(let i=0;i<280&&SCENES[state.scene].act<10;i++){
  const sc=SCENES[state.scene];state.pageIndex=sc.isPrologue?0:paginateStory(sc.body(state)).length-1;choose(0);
 }
 if(state.scene!=='ch06_01')throw Error('Cannot reach Chapter VI');return clone(state);
}"""
WALK='seed=>{'+PROJECT+r"""
 const queue=[clone(seed)],seen=new Set(),snapshots={},edges=[];
 while(queue.length){const before=queue.shift(),sc=SCENES[before.scene];if(sc.act!==10||seen.has(sc.id))continue;
  seen.add(sc.id);snapshots[sc.id]=clone(before);
  for(const [index,option] of sc.choices(before).entries()){
   state=clone(before);activeTab='story';state.pageIndex=paginateStory(sc.body(state)).length-1;choose(index);
   if(state.scene!==option.next||!validSave(state))throw Error('Blocked VI choice');
   edges.push(project(state,sc.id,index,option.next,option.label));if(!seen.has(state.scene))queue.push(clone(state));
  }
 }
 return {snapshots,edges,ids:Object.keys(SCENES).sort()};
}"""
COMPARE='data=>{'+PROJECT+r"""
 const results=[];
 for(const edge of data.edges){
  state=clone(data.snapshots[edge.source]);activeTab='story';const sc=SCENES[state.scene],option=sc.choices(state)[edge.index];
  state.pageIndex=paginateStory(sc.body(state)).length-1;choose(edge.index);
  if(state.scene!==option.next||!validSave(state))throw Error('Blocked legacy VI choice');
  results.push(project(state,sc.id,edge.index,option.next,option.label));
 }
 return results;
}"""
ROUTES=r"""seed=>{
 const rows=[];
 for(const branch of ['Infantry','Cavalry'])for(let station=0;station<3;station++)for(let action=0;action<3;action++)for(let exit=0;exit<3;exit++)for(let report=0;report<2;report++){
  state=clone(seed);activeTab='story';if(branch==='Cavalry')state.militaryCareer.combatService={branch,unit:'Recorded cavalry section',commander:'Recorded cavalry officer',year:198,proof:'legacy:lawful-cavalry'};
  const before=clone(state);
  const step=index=>{const sc=SCENES[state.scene];state.pageIndex=paginateStory(sc.body(state)).length-1;choose(index);if(!validSave(state)||state.scene===sc.id)throw Error('Xiaopei choice blocked');};
  step(0);if(state.scene!=='m2_198_xiaopei_orders')throw Error('No forward deployment');
  for(const [stage,index] of [station,action,exit,report].entries()){
   step(index);
   if(state.age!==24||state.storyClock.year!==198||state.militaryCareer.rank!==before.militaryCareer.rank)throw Error('Date or rank changed');
   if(JSON.stringify(state.militaryCareer.combatService)!==JSON.stringify(before.militaryCareer.combatService)||JSON.stringify(state.militaryCareer.units)!==JSON.stringify(before.militaryCareer.units)||JSON.stringify(state.militaryCareer.staff)!==JSON.stringify(before.militaryCareer.staff))throw Error('New branch, unit or staff');
   if(state.militaryCareer.fieldPosition.active!==(stage<2))throw Error('Wrong withdrawal lifecycle');
   if(!state.militaryCareer.fieldPosition.formation.startsWith(branch==='Cavalry'?'mounted':'infantry'))throw Error('Wrong branch position');
  }
  if(state.scene!=='ch06_07'||!SCENES.ch06_07.body(state).includes(AUH4S_RETREAT[state.flags.m2_198_action]))throw Error('Missing legacy return and chosen aftermath');
  if(JSON.stringify(state.items)!==JSON.stringify(before.items)||state.coins!==before.coins||JSON.stringify(state.innerCircle)!==JSON.stringify(before.innerCircle))throw Error('Automatic grant');
  const frozen=JSON.stringify(state);if(!npcMemories('xuwen').includes(AUH4S_RETREAT[state.flags.m2_198_action]))throw Error('No witnessed memory');militaryPanel();if(JSON.stringify(state)!==frozen)throw Error('View mutated state');
  rows.push({branch,station,action,exit,report});
 }
 return rows;
}"""

def main():
 parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--report',type=Path);args=parser.parse_args()
 from playwright.sync_api import sync_playwright
 active=ROOT/'GAME'/(ROOT/'GAME/ACTIVE_BUILD.txt').read_text().strip();current=active.read_bytes();baseline=subprocess.run(['git','show',BASELINE],cwd=ROOT,check=True,capture_output=True).stdout
 images=lambda b:re.findall(rb'data:image/[^;"\s]+;base64,[A-Za-z0-9+/=]+',b)
 assert images(current)==images(baseline)
 with tempfile.TemporaryDirectory() as tmp:
  p=Path(tmp)/'game.js';p.write_bytes(b'\n'.join(re.findall(rb'<script[^>]*>(.*?)</script>',current,re.S)));subprocess.run(['node','--check',str(p)],check=True,capture_output=True)
 docs={'/baseline.html':baseline,'/active.html':current}
 class Handler(http.server.BaseHTTPRequestHandler):
  def do_GET(self):
   b=docs.get(self.path);self.send_response(200 if b else 404);self.send_header('Content-Type','text/html; charset=utf-8');self.end_headers()
   if b:self.wfile.write(b)
  def log_message(self,*_):pass
 server=http.server.ThreadingHTTPServer(('127.0.0.1',0),Handler);threading.Thread(target=server.serve_forever,daemon=True).start();url=f'http://127.0.0.1:{server.server_port}'
 result={'build':active.name,'sha256':hashlib.sha256(current).hexdigest(),'checks':[]}
 try:
  with sync_playwright() as playwright:
   browser=playwright.chromium.launch(executable_path=shutil.which('chromium'),headless=True,args=['--no-sandbox']);base=browser.new_page();base.goto(url+'/baseline.html');seed=base.evaluate(START);old=base.evaluate(WALK,seed);base.close()
   for width in (390,1280):
    context=browser.new_context(viewport={'width':width,'height':900});page=context.new_page();errors=[];page.on('pageerror',lambda error:errors.append(str(error)));page.goto(url+'/active.html')
    ids=page.evaluate('Object.keys(SCENES)');assert set(old['ids']).issubset(ids) and set(ids)-set(old['ids'])==NEW
    compared=page.evaluate(COMPARE,old)
    for a,b in zip(old['edges'],compared):assert a==b,f'VI contract changed on identical input: {a["source"]}:{a["index"]}'
    new=page.evaluate(WALK,seed);routes=page.evaluate(ROUTES,old['snapshots']['ch06_06']);assert len(routes)==108
    page.evaluate(r"""seed=>{
     for(const index of [1,2])if(SCENES.ch06_06.choices(seed)[index].next!=='ch06_07')throw Error('Non-forward preference overridden');
     const late=clone(seed);late.storyClock.year=199;late.flags.novelYear=199;late.age=25;
     if(SCENES.ch06_06.choices(late)[0].next!=='ch06_07')throw Error('Late save rewound');
     state=clone(seed);state.flags.m2_198_action='signal';state.flags.m2_198_report='people';state.visited=[];state.history=[];
     if(SCENES.ch06_07.body(state).includes('The later reports cannot erase that witnessed cost'))throw Error('Flag-only aftermath');
     if(npcMemories('xuwen').includes(AUH4S_RETREAT.signal))throw Error('Flag-only memory');
    }""",old['snapshots']['ch06_06'])
    page.evaluate(r"""seed=>{
     const s=clone(seed);delete s.flags.m2_198_exit;const effect=SCENES.m2_198_xiaopei_retreat.choices(s)[0].effect;effect(s);const once=JSON.stringify(s);effect(s);if(JSON.stringify(s)!==once)throw Error('Repeated exit effect');
    }""",new['snapshots']['m2_198_xiaopei_retreat'])
    for value,expected in [(old['snapshots']['ch06_07'],'ch06_07'),(new['snapshots']['m2_198_xiaopei_after'],'m2_198_xiaopei_after')]:
     page.evaluate('seed=>{localStorage.setItem(SAVE_KEY,JSON.stringify(seed));handleAction("load-original");}',value);page.reload();assert page.evaluate('state.scene')==expected
    page.locator('#menuToggle').click();page.locator('#gameMenu [data-nav="military"]').click();assert 'Xiaopei' in page.locator('#screen').inner_text();assert page.evaluate('document.documentElement.scrollWidth<=innerWidth')
    assert not errors,errors
    result['checks'].append({'width':width,'legacy_sampled_scenes':len(old['snapshots']),'current_sampled_scenes':len(new['snapshots']),'legacy_choice_edges':len(old['edges']),'new_scene_edges':len(new['edges'])-len(old['edges']),'same_input_legacy_parity':'PASS except selected forward-route insert','complete_local_routes':len(routes),'branch_rank_no_grants_lifecycle':'PASS','nonforward_and_late_bypass':'PASS','flag_only_negative':'PASS','idempotence':'PASS','http_reload_legacy_and_after_battle':'PASS','military_dom_no_overflow':'PASS','page_errors':errors});context.close()
   browser.close()
 finally:server.shutdown();server.server_close()
 result['limits']='All local Xiaopei decisions tested; legacy chapter scenes use representative states. Cavalry uses a synthetic lawful-assignment fixture. Full campaign, all historical sources and physical-device file:// remain pending.'
 if args.report:args.report.parent.mkdir(parents=True,exist_ok=True);args.report.write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(result,indent=2))
if __name__=='__main__':main()
