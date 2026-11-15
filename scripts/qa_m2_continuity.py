#!/usr/bin/env python3
"""W08/W10 local routes, optional Xu Shu meeting, and dated advice in 208."""
import argparse
from pathlib import Path
from qa_support import fixture, write_report
BASELINE='4c1d04d:GAME/ALL_UNDER_HEAVEN_v0.4.99.4t_CHAPTER_VII_TWENTY_NAMES.html'
NEW={'m2_200_xu_orders','m2_200_xu_pressure','m2_200_xu_departure','m2_200_xu_after','m2_207_fan_orders','m2_207_fan_contact','m2_207_fan_report','m2_207_xushu_debrief'}
START=r"""decline=>{
 state=resolve(fresh('M2 continuity',16));activeTab='story';const snapshots={};
 for(let step=0;step<420;step++){
  const sc=SCENES[state.scene];
  if(['ch06_10','ch07_13','ch08_pb55_xushu'].includes(sc.id))snapshots[sc.id]=clone(state);
  if(sc.id==='ch08_pb55_xushu')return {snapshots,ids:Object.keys(SCENES)};
  const index=decline&&sc.id==='ch07_06'?1:0;
  state.pageIndex=sc.isPrologue?0:paginateStory(sc.body(state)).length-1;choose(index);
  if(state.scene===sc.id)throw Error('Organic baseline path blocked: '+sc.id+':'+banner);
 }
 throw Error('Did not reach 208');
}"""
XU=r"""seed=>{
 const rows=[];
 for(const branch of ['Infantry','Cavalry'])for(let a=0;a<3;a++)for(let b=0;b<3;b++)for(let c=0;c<3;c++)for(let report=0;report<2;report++){
  state=clone(seed);activeTab='story';if(branch==='Cavalry')state.militaryCareer.combatService={branch,unit:'Legacy cavalry section',commander:'Recorded officer',year:199,proof:'legacy:lawful-cavalry'};
  const before=clone(state),moves=[a,b,c,(a+b+c)%3,report];
  for(const [step,index] of moves.entries()){
   const sc=SCENES[state.scene];state.pageIndex=paginateStory(sc.body(state)).length-1;choose(index);
   if(!validSave(state)||state.scene===sc.id)throw Error('Xu route blocked');
   if(state.age!==26||state.storyClock.year!==200||state.militaryCareer.rank!==before.militaryCareer.rank)throw Error('Xu date or rank changed');
   if(step>0&&state.militaryCareer.fieldPosition.active!==(step<3))throw Error('Xu lifecycle');
  }
  if(state.scene!=='ch07_01'||!auh4uEvidence(state,'xu200'))throw Error('Missing Xu record/return');
  for(const key of ['units','staff','appointmentHistory','combatService'])if(JSON.stringify(state.militaryCareer[key])!==JSON.stringify(before.militaryCareer[key]))throw Error('Xu military grant');
  if(state.coins!==before.coins||JSON.stringify(state.items)!==JSON.stringify(before.items)||JSON.stringify(state.innerCircle)!==JSON.stringify(before.innerCircle))throw Error('Xu goods/companion grant');
  const frozen=JSON.stringify(state);militaryPanel();if(!npcMemories('xuwen').includes(AUH4U_ACTIONS.xu200[state.flags.m2_200_action]))throw Error('Xu recall missing');if(JSON.stringify(state)!==frozen)throw Error('Xu view mutation');
  rows.push({branch,preference:a,station:b,action:c,exit:(a+b+c)%3,report});
 }
 return {rows,example:clone(state)};
}"""
FAN=r"""seed=>{
 const rows=[];
 for(const branch of ['Infantry','Cavalry'])for(let station=0;station<3;station++)for(let action=0;action<3;action++)for(let ending=0;ending<4;ending++){
  state=clone(seed);activeTab='story';if(branch==='Cavalry')state.militaryCareer.combatService={branch,unit:'Legacy cavalry section',commander:'Recorded officer',year:206,proof:'legacy:lawful-cavalry'};
  const before=clone(state);
  const step=index=>{const sc=SCENES[state.scene];state.pageIndex=paginateStory(sc.body(state)).length-1;choose(index);if(!validSave(state)||state.scene===sc.id)throw Error('Fancheng route blocked: '+banner);};
  step(0);if(state.scene!=='m2_207_fan_orders'||state.storyClock.year!==207||state.age!==33)throw Error('207 entry advanced early');
  step(station);if(!state.militaryCareer.fieldPosition.active)throw Error('207 position missing');
  step(action);if(state.militaryCareer.fieldPosition.active)throw Error('207 position stayed active');
  step(ending===0?0:1);
  if(ending>0){if(state.scene!=='m2_207_xushu_debrief'||state.storyClock.year!==207)throw Error('Audience wrong date');step(ending-1);}
  if(state.scene!=='ch08_pb55_foreword'||state.storyClock.year!==208||state.age!==34||!auh4uEvidence(state,'fan207'))throw Error('208 return');
  if(!!state.flags.historical_meet_xushu!==(ending>0))throw Error('Xu Shu acquaintance not chosen');
  for(const key of ['rank','units','staff','appointmentHistory','combatService'])if(JSON.stringify(state.militaryCareer[key])!==JSON.stringify(before.militaryCareer[key]))throw Error('207 military grant');
  if(state.coins!==before.coins||JSON.stringify(state.items)!==JSON.stringify(before.items)||JSON.stringify(state.innerCircle)!==JSON.stringify(before.innerCircle))throw Error('207 other grant');
  if(ending>0&&npcMemories('xushu').some(t=>t.includes('208 CE')))throw Error('207 meeting dated 208');
  step(0);if(state.scene!=='ch08_pb55_xushu'||SCENES[state.scene].body(state).includes('Xu Shu introduces himself'))throw Error('Live Xu Shu in 208');
  step(0);if(!!state.flags.historical_meet_xushu!==(ending>0))throw Error('208 letter granted meeting');
  rows.push({branch,rank:before.militaryCareer.rank,station,action,ending});
 }
 return {rows,example:clone(state)};
}"""

def main():
 parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--report',type=Path);args=parser.parse_args()
 with fixture(BASELINE) as (browser,url,result):
  base=browser.new_page();base.goto(url+'/baseline.html');earned=base.evaluate(START,False);declined=base.evaluate(START,True);base.close()
  for width in (390,1280):
   context=browser.new_context(viewport={'width':width,'height':900});page=context.new_page();errors=[];page.on('pageerror',lambda error:errors.append(str(error)));page.goto(url+'/active.html')
   ids=page.evaluate('Object.keys(SCENES)');assert set(earned['ids']).issubset(ids) and set(ids)-set(earned['ids'])==NEW
   xu=page.evaluate(XU,earned['snapshots']['ch06_10']);assert len(xu['rows'])==108
   fan=[]
   for data in (earned,declined):fan.append(page.evaluate(FAN,data['snapshots']['ch07_13']))
   assert sum(len(r['rows']) for r in fan)==144
   page.evaluate(r"""seeds=>{
    for(const [id,seed,year] of [['ch06_10',seeds.xu,201],['ch07_13',seeds.fan,208]]){
     const s=clone(seed);s.storyClock.year=year;s.flags.novelYear=year;
     const expected=id==='ch06_10'?'ch07_01':'ch08_pb55_foreword';
     if(SCENES[id].choices(s).some(o=>o.next!==expected))throw Error('Late save rewound');
    }
    state=clone(seeds.xu);state.scene='ch07_01';state.flags.m2_200_action='cover';state.flags.m2_200_complete=true;state.visited=[];state.history=[];
    state.militaryCareer.campaignEvidence={xu200:{schema:1,campaign:'xu200',source:'m2_200_xu_after',year:200,branch:'Infantry',action:'cover',account:AUH4U_ACTIONS.xu200.cover}};
    if(auh4uEvidence(state,'xu200')||militaryPanel().includes('aria-label="Witnessed campaign service"'))throw Error('Flag-only evidence');
   }""",{'xu':earned['snapshots']['ch06_10'],'fan':earned['snapshots']['ch07_13']})
   # Preserve an actual historical legacy acquaintance; no reconstruction or erasure.
   legacy=earned['snapshots']['ch08_pb55_xushu'];legacy['flags']['historical_meet_xushu']=True
   page.evaluate('s=>{localStorage.setItem(SAVE_KEY,JSON.stringify(s));handleAction("load-original");}',legacy);page.reload()
   page.evaluate('()=>{state.pageIndex=paginateStory(SCENES[state.scene].body(state)).length-1;choose(0);}')
   assert page.evaluate('state.flags.historical_meet_xushu===true&&state.scene==="ch08_pb55_council"')
   page.evaluate(r"""seed=>{
    state=clone(seed);const saved=JSON.stringify(state);militaryPanel();npcMemories('xuwen');if(JSON.stringify(state)!==saved)throw Error('Evidence view mutates');
    const historyOnly=clone(state);historyOnly.visited=[];if(!auh4uEvidence(historyOnly,'fan207'))throw Error('History-only service lost');
    const bad=clone(state);bad.militaryCareer.campaignEvidence.fan207.action='__proto__';if(auh4uEvidence(bad,'fan207'))throw Error('Invalid evidence enum');
    const once=JSON.stringify(state.militaryCareer.campaignEvidence);auh4uRecord(state,'fan207','m2_207_fan_report','m2_207_action');if(JSON.stringify(state.militaryCareer.campaignEvidence)!==once)throw Error('Duplicate evidence');
   }""",fan[0]['example'])
   page.evaluate('s=>{localStorage.setItem(SAVE_KEY,JSON.stringify(s));handleAction("load-original");}',xu['example']);page.reload();assert page.evaluate('validSave(state)&&auh4uEvidence(state,"xu200")')
   page.locator('#menuToggle').click();page.locator('#gameMenu [data-nav="military"]').click();assert page.locator('[aria-label="Witnessed campaign service"]').is_visible();assert page.evaluate('document.documentElement.scrollWidth<=innerWidth')
   assert not errors,errors
   result['checks'].append({'width':width,'xu200_pairwise_routes':108,'fan207_all_local_routes':144,'earned_and_declined_commission':'PASS','no_grants':'PASS','207_meeting_optional_208_copy_only':'PASS','legacy_acquaintance_preserved':'PASS','late_and_flag_only_negative':'PASS','evidence_idempotent_and_history_only':'PASS','http_reload_and_military_dom':'PASS','page_errors':errors});context.close()
 result['limits']='Xu route: pairwise preference/station/action/exit, both branches/reports. 207 routes: all local combinations, organic Sergeant/Private seeds, synthetic Cavalry variant. Full novel and physical-device file:// not certified.'
 write_report(result,args.report)
if __name__=='__main__':main()
