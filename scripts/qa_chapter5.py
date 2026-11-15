#!/usr/bin/env python3
"""Chapter V contracts and 197 campaign, all preference/branch/tactical choices."""
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
ROOT=Path(__file__).resolve().parent.parent
BASELINE='a4d7458:GAME/ALL_UNDER_HEAVEN_v0.4.99.4q_CHAPTER_IV_ROADS_OF_XU.html'
NEW={'m2_197_road_orders','m2_197_road_contact','m2_197_road_aftermath'}
START=r"""()=>{
 state=resolve(fresh('Chapter Five QA',16));activeTab='story';
 for(let i=0;i<250&&SCENES[state.scene].act<9;i++){
  const sc=SCENES[state.scene];state.pageIndex=sc.isPrologue?0:paginateStory(sc.body(state)).length-1;choose(0);
 }
 if(state.scene!=='lc81_196_qin')throw Error('Cannot reach Chapter V');return clone(state);
}"""
WALK=r"""seed=>{
 const queue=[clone(seed)],seen=new Set(),snapshots={},edges=[];
 while(queue.length){
  const before=queue.shift(),sc=SCENES[before.scene];if(sc.act!==9||seen.has(sc.id))continue;
  seen.add(sc.id);snapshots[sc.id]=clone(before);
  for(const [index,option] of sc.choices(before).entries()){
   state=clone(before);activeTab='story';state.pageIndex=paginateStory(sc.body(state)).length-1;choose(index);
   if(state.scene!==option.next||!validSave(state))throw Error('Blocked Chapter V edge: '+sc.id+':'+index+':'+banner);
   const contract=clone(state);delete contract.id;delete contract.pendingFeedback;
   contract.history=contract.history.map(h=>({sceneId:h.sceneId,choice:h.choice,act:h.act,title:h.title}));
   let target=option.next;
   if(sc.id==='ch05_06'){
    target='197-insert-or-original-198';delete contract.age;delete contract.storyClock;delete contract.act;delete contract.scene;
    delete contract.flags.novelYear;delete contract.flags.m2_197_ordered;
   }
   edges.push({scene:sc.id,index,label:option.label,next:target,contract});
   if(!seen.has(state.scene))queue.push(clone(state));
  }
 }
 return {snapshots,edges,ids:Object.keys(SCENES).sort()};
}"""
ROUTES=r"""seed=>{
 const results=[];
 for(let pref=0;pref<3;pref++)for(const branch of ['Infantry','Cavalry'])for(let station=0;station<3;station++)for(let action=0;action<3;action++)for(let report=0;report<2;report++){
  state=clone(seed);activeTab='story';
  if(branch==='Cavalry')state.militaryCareer.combatService={branch,unit:'Recorded cavalry section',commander:'Recorded cavalry officer',year:196,proof:'legacy:lawful-cavalry'};
  const career=clone(state.militaryCareer),circle=JSON.stringify(state.innerCircle),items=JSON.stringify(state.items),coins=state.coins;
  function step(index){const sc=SCENES[state.scene];state.pageIndex=paginateStory(sc.body(state)).length-1;choose(index);if(!validSave(state)||state.scene===sc.id)throw Error('197 route blocked: '+banner);}
  step(pref);
  if(state.scene!=='m2_197_road_orders'||state.storyClock.year!==197||state.age!==23)throw Error('Wrong 197 insertion date');
  if(state.flags.ch05_06!==['field','district','both'][pref])throw Error('Preference lost');
  step(station);
  if(state.militaryCareer.fieldPosition.active!==true||state.militaryCareer.fieldPosition.year!==197)throw Error('Missing 197 active position');
  if(!state.militaryCareer.fieldPosition.formation.startsWith(branch==='Cavalry'?'mounted':'infantry'))throw Error('Branch changed');
  if(state.militaryCareer.fieldPosition.sector!==auh4rSector(state))throw Error('Preference ignored by assignment');
  step(action);
  if(state.militaryCareer.fieldPosition.active!==false)throw Error('Battle stayed active at aftermath');
  const before=JSON.stringify(state);npcMemories('xuwen');militaryPanel();if(JSON.stringify(state)!==before)throw Error('Read-only view changed state');
  if(!npcMemories('xuwen').includes(AUH4R_ACTIONS[state.flags.m2_197_action]))throw Error('Missing chosen memory');
  const saved=clone(state);step(report);
  if(state.scene!=='ch06_01'||state.storyClock.year!==198||state.age!==24)throw Error('Missing original VI transition');
  if(state.militaryCareer.rank!==career.rank||JSON.stringify(state.militaryCareer.combatService)!==JSON.stringify(career.combatService)||JSON.stringify(state.militaryCareer.units)!==JSON.stringify(career.units)||Object.keys(state.militaryCareer.staff).length)throw Error('Unearned military grant');
  if(JSON.stringify(state.innerCircle)!==circle||JSON.stringify(state.items)!==items||state.coins!==coins)throw Error('197 route granted a companion or goods');
  const body=SCENES.ch06_01.body(state);
  if(!body.includes(AUH4R_ACTIONS[state.flags.m2_197_action]))throw Error('No chosen Chapter VI recall');
  if(body.includes('Your district assignment takes the shape of a journey rather than a desk')||body.includes('Working between the district and the moving force has put two sets of figures in your hands.'))throw Error('Rank-and-file reassigned to logistics');
  results.push({pref,branch,station,action,report});
 }
 return results;
}"""

def main():
 parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--report',type=Path);args=parser.parse_args()
 from playwright.sync_api import sync_playwright
 active=ROOT/'GAME'/(ROOT/'GAME/ACTIVE_BUILD.txt').read_text().strip();current=active.read_bytes()
 baseline=subprocess.run(['git','show',BASELINE],cwd=ROOT,check=True,capture_output=True).stdout
 images=lambda b:re.findall(rb'data:image/[^;"\s]+;base64,[A-Za-z0-9+/=]+',b)
 assert images(current)==images(baseline)
 with tempfile.TemporaryDirectory() as tmp:
  script=Path(tmp)/'game.js';script.write_bytes(b'\n'.join(re.findall(rb'<script[^>]*>(.*?)</script>',current,re.S)))
  subprocess.run(['node','--check',str(script)],check=True,capture_output=True)
 docs={'/baseline.html':baseline,'/active.html':current}
 class Handler(http.server.BaseHTTPRequestHandler):
  def do_GET(self):
   content=docs.get(self.path);self.send_response(200 if content else 404);self.send_header('Content-Type','text/html; charset=utf-8');self.end_headers()
   if content:self.wfile.write(content)
  def log_message(self,*_):pass
 server=http.server.ThreadingHTTPServer(('127.0.0.1',0),Handler);threading.Thread(target=server.serve_forever,daemon=True).start()
 url=f'http://127.0.0.1:{server.server_port}'
 result={'build':active.name,'sha256':hashlib.sha256(current).hexdigest(),'checks':[]}
 try:
  with sync_playwright() as playwright:
   browser=playwright.chromium.launch(executable_path=shutil.which('chromium'),headless=True,args=['--no-sandbox'])
   base=browser.new_page();base.goto(url+'/baseline.html');seed=base.evaluate(START);old=base.evaluate(WALK,seed)
   legacy=base.evaluate('seed=>{state=clone(seed);state.pageIndex=paginateStory(SCENES[state.scene].body(state)).length-1;choose(0);return clone(state);}',old['snapshots']['ch05_06']);base.close()
   for width in (390,1280):
    context=browser.new_context(viewport={'width':width,'height':900});page=context.new_page();errors=[];page.on('pageerror',lambda error:errors.append(str(error)));page.goto(url+'/active.html')
    new=page.evaluate(WALK,seed)
    assert set(old['ids']).issubset(new['ids']) and set(new['ids'])-set(old['ids'])==NEW|{'m2_198_xiaopei_orders','m2_198_xiaopei_pressure','m2_198_xiaopei_retreat','m2_198_xiaopei_after'}
    original=[edge for edge in new['edges'] if edge['scene'] not in NEW]
    assert len(original)==len(old['edges'])
    for previous,successor in zip(old['edges'],original):assert previous==successor,f'Legacy V contract changed: {previous["scene"]}:{previous["index"]}'
    routes=page.evaluate(ROUTES,new['snapshots']['ch05_06']);assert len(routes)==108
    page.evaluate(r"""seed=>{
     const late=clone(seed);late.storyClock.year=198;late.flags.novelYear=198;late.age=24;
     if(SCENES.ch05_06.choices(late).some(o=>o.next!=='ch06_01'))throw Error('Late save rewound');
     state=clone(seed);state.flags.m2_197_action='brace';state.flags.m2_197_report='positions';state.visited=[];state.history=[];
     if(SCENES.ch06_01.body(state).startsWith('<p>'+AUH4R_ACTIONS.brace))throw Error('Flag-only campaign recall');
     if(npcMemories('xuwen').includes(AUH4R_ACTIONS.brace))throw Error('Unplayed campaign memory');
    }""",new['snapshots']['ch05_06'])
    page.evaluate('seed=>{localStorage.setItem(SAVE_KEY,JSON.stringify(seed));handleAction("load-original");}',legacy);page.reload()
    assert page.evaluate('validSave(state)&&state.scene==="ch06_01"&&state.storyClock.year===198&&!state.flags.m2_197_ordered')
    page.evaluate(r"""seed=>{
     const s=clone(seed);delete s.flags.m2_197_action;
     const effect=SCENES.m2_197_road_contact.choices(s)[0].effect;effect(s);const once=JSON.stringify(s);effect(s);if(JSON.stringify(s)!==once)throw Error('197 action replays');
    }""",new['snapshots']['m2_197_road_contact'])
    page.evaluate('seed=>{localStorage.setItem(SAVE_KEY,JSON.stringify(seed));handleAction("load-original");}',new['snapshots']['m2_197_road_aftermath']);page.reload()
    assert page.evaluate('validSave(state)&&state.storyClock.year===197&&state.age===23&&state.militaryCareer.fieldPosition.active===false')
    page.locator('#menuToggle').click();page.locator('#gameMenu [data-nav="military"]').click()
    assert page.evaluate('document.documentElement.scrollWidth<=innerWidth')
    assert not errors,errors
    result['checks'].append({'width':width,'sampled_scenes':len(new['snapshots']),'legacy_edges':len(old['edges']),'new_scene_edges':len(new['edges'])-len(old['edges']),'legacy_parity':'PASS except explicit 197 insertion timing','complete_197_routes':len(routes),'all_preferences_branches_stations_actions_reports':'PASS','no_grants_and_chapter6_recall':'PASS','late_save_and_flag_only':'PASS','idempotence':'PASS','http_reload_197_and_legacy_198':'PASS','military_dom_no_overflow':'PASS','page_errors':errors});context.close()
   browser.close()
 finally:server.shutdown();server.server_close()
 result['limits']='All local 197 decision combinations tested; pre-197 scenes use representative states. Cavalry is a synthetic legacy-assignment fixture. Full novel and physical-device file:// remain unverified.'
 if args.report:args.report.parent.mkdir(parents=True,exist_ok=True);args.report.write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(result,indent=2))
if __name__=='__main__':main()
