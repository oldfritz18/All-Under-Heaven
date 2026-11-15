#!/usr/bin/env python3
"""Chapter VII: optional Sergeant commission and lived, bounded unit command."""
import argparse,hashlib,http.server,json,re,shutil,subprocess,threading
from pathlib import Path
import qa_chapter6 as legacy
ROOT=Path(__file__).resolve().parent.parent
BASELINE='2e51ccd:GAME/ALL_UNDER_HEAVEN_v0.4.99.4s_CHAPTER_VI_XIAOPEI.html'
NEW={'m2_201_watch_orders','m2_201_watch_contact','m2_201_watch_after'}
PROJECT=legacy.PROJECT.replace("source==='ch06_06'","source==='ch07_06'")
WALK=legacy.WALK.replace(legacy.PROJECT,PROJECT).replace('sc.act!==10','sc.act!==11')
COMPARE=legacy.COMPARE.replace(legacy.PROJECT,PROJECT)
START=legacy.START.replace('i<280','i<320').replace('act<10','act<11').replace("state.scene!=='ch06_01'","state.scene!=='ch07_01'")
ROUTES=r"""seed=>{
 const rows=[];
 for(let station=0;station<3;station++)for(let action=0;action<3;action++)for(let review=0;review<3;review++){
  state=clone(seed);activeTab='story';
  const step=index=>{const sc=SCENES[state.scene];state.pageIndex=paginateStory(sc.body(state)).length-1;choose(index);if(!validSave(state)||state.scene===sc.id)throw Error('Road-watch choice blocked');};
  if(state.militaryCareer.rank!=='Private')throw Error('Wrong pre-commission fixture');step(0);
  if(state.scene!=='m2_201_watch_orders'||!auh4tWatch(state)||state.militaryCareer.units.length!==1||state.militaryCareer.units[0].infantry!==20)throw Error('Commission did not remain explicit');
  const career=clone(state.militaryCareer),circle=JSON.stringify(state.innerCircle),items=JSON.stringify(state.items),coins=state.coins;
  for(const [stage,index] of [station,action,review].entries()){
   step(index);
   if(state.storyClock.year!==201||state.age!==27||state.militaryCareer.rank!=='Sergeant')throw Error('Runan date/rank');
   if(state.militaryCareer.fieldPosition.active!==(stage===0))throw Error('Wrong 201 position lifecycle');
   if(JSON.stringify(state.militaryCareer.units)!==JSON.stringify(career.units)||JSON.stringify(state.militaryCareer.appointmentHistory)!==JSON.stringify(career.appointmentHistory)||Object.keys(state.militaryCareer.staff).length)throw Error('Extra troop, promotion or assistant');
  }
  if(state.scene!=='ch07_07'||!state.flags.m2_201_completed||!SCENES.ch07_07.body(state).includes(AUH4T_OUTCOMES[state.flags.m2_201_action]))throw Error('No old route/chosen recall');
  const before=JSON.stringify(state);militaryPanel();if(!npcMemories('xuwen').includes(AUH4T_OUTCOMES[state.flags.m2_201_action]))throw Error('No People recall');if(JSON.stringify(state)!==before)throw Error('View mutated state');
  if(JSON.stringify(state.innerCircle)!==circle||JSON.stringify(state.items)!==items||state.coins!==coins)throw Error('Free grant');
  rows.push({station,action,review});
 }
 return rows;
}"""

def main():
 parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--report',type=Path);args=parser.parse_args()
 from playwright.sync_api import sync_playwright
 active=ROOT/'GAME'/(ROOT/'GAME/ACTIVE_BUILD.txt').read_text().strip();current=active.read_bytes();baseline=subprocess.run(['git','show',BASELINE],cwd=ROOT,check=True,capture_output=True).stdout
 images=lambda b:re.findall(rb'data:image/[^;"\s]+;base64,[A-Za-z0-9+/=]+',b);assert images(current)==images(baseline)
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
    for a,b in zip(old['edges'],compared):assert a==b,f'VII legacy contract changed: {a["source"]}:{a["index"]}'
    new=page.evaluate(WALK,seed);routes=page.evaluate(ROUTES,old['snapshots']['ch07_06']);assert len(routes)==27
    page.evaluate(r"""seed=>{
     for(const index of [1,2]){
      state=clone(seed);activeTab='story';state.pageIndex=paginateStory(SCENES[state.scene].body(state)).length-1;choose(index);
      if(state.scene!=='ch07_07'||state.militaryCareer.rank!=='Private'||state.militaryCareer.units.length||Object.keys(state.militaryCareer.staff).length)throw Error('Declined/requested commission became grant');
     }
     for(const mode of ['cavalry','late','unrelated-rank','inconsistent-record']){
      const s=clone(seed);
      if(mode==='cavalry')s.militaryCareer.combatService.branch='Cavalry';
      if(mode==='late'){s.storyClock.year=202;s.age=28;s.flags.novelYear=202;}
      if(mode==='unrelated-rank')s.militaryCareer.rank='General';
      if(mode==='inconsistent-record')s.militaryCareer.appointmentHistory=[{proof:'auh3e:ch07_06:military',rank:'Sergeant'}];
      if(SCENES.ch07_06.choices(s)[0].next!=='ch07_07')throw Error('Unjustified twenty-person watch route: '+mode);
     }
     state=clone(seed);state.flags.m2_201_completed=true;state.flags.m2_201_action='interval';state.visited=[];state.history=[];
     if(SCENES.ch07_07.body(state).includes('Your next duty begins with the same warrant'))throw Error('Phantom watch recall');
     if(npcMemories('xuwen').includes(AUH4T_OUTCOMES.interval))throw Error('Phantom People recall');
    }""",old['snapshots']['ch07_06'])
    page.evaluate(r"""seed=>{
     const s=clone(seed);const before=JSON.stringify(s.militaryCareer.units);auhStoryUIChoice(s,clone(s),'ch07_06',0);auhStoryUIChoice(s,clone(s),'ch07_06',0);if(JSON.stringify(s.militaryCareer.units)!==before)throw Error('Duplicate commissioned troops');
     delete s.flags.m2_201_completed;const effect=SCENES.m2_201_watch_after.choices(s)[0].effect;effect(s);const once=JSON.stringify(s);effect(s);if(JSON.stringify(s)!==once)throw Error('Repeated review effect');
    }""",new['snapshots']['m2_201_watch_after'])
    for value in (old['snapshots']['ch07_07'],new['snapshots']['m2_201_watch_after']):
     page.evaluate('seed=>{localStorage.setItem(SAVE_KEY,JSON.stringify(seed));handleAction("load-original");}',value);page.reload();assert page.evaluate('state.scene')==value['scene'];assert page.evaluate('validSave(state)&&state.militaryCareer.units.filter(u=>u.id==="road-watch-201").length===1')
    page.locator('#menuToggle').click();page.locator('#gameMenu [data-nav="military"]').click();assert 'Sergeant' in page.locator('#screen').inner_text();assert page.evaluate('document.documentElement.scrollWidth<=innerWidth')
    assert not errors,errors
    result['checks'].append({'width':width,'legacy_scene_samples':len(old['snapshots']),'current_scene_samples':len(new['snapshots']),'legacy_edges':len(old['edges']),'new_scene_edges':len(new['edges'])-len(old['edges']),'same_input_legacy_parity':'PASS except accepted-infantry watch route','complete_local_routes':len(routes),'decline_and_independent_request_no_grants':'PASS','four_negative_entry_cases':'PASS','commission_units_not_duplicated':'PASS','no_staff_or_other_grants':'PASS','read_only_and_flag_only':'PASS','http_reload_legacy_and_after_watch':'PASS','military_dom_no_overflow':'PASS','page_errors':errors});context.close()
   browser.close()
 finally:server.shutdown();server.server_close()
 result['limits']='All 27 local road-watch combinations tested. Earlier chapter states representative. W07/W08/W10 remain partial/reported coverage requiring later audit; full novel/device release not certified.'
 if args.report:args.report.parent.mkdir(parents=True,exist_ok=True);args.report.write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(result,indent=2))
if __name__=='__main__':main()
