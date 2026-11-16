#!/usr/bin/env python3
"""5o: actual Xu Wen 230–231 choice-handler matrix from a played 190–230 history.

Scope: source-proven reconnaissance, not General/Dragon award or release QA.
Runs Chromium at 390/1280 through the existing localhost browser fixture.
"""
import argparse, json
from pathlib import Path
from qa_support import fixture, write_report
from qa_enthronement225 import organic_accession_seeds
from qa_dragon_nominations227 import TO_227

BASELINE = '5f306bf:GAME/ALL_UNDER_HEAVEN_v0.4.99.5n_THE_STANDARD_HE_CHOSE.html'
NEW = {'m4_230_xu_hearing','m4_230_xu_terms','m4_230_xu_order',
       'm4_230_xu_muster','m4_231_xu_road','m4_231_xu_contact',
       'm4_231_xu_return','m4_231_xu_review','m4_231_xu_close'}
SEED = r"""input=>{
 state=clone(input);
 const oldSave=save,oldRender=render,oldScroll=scrollTopNow;
 save=()=>{};render=()=>{};scrollTopNow=()=>{};
 const step=dest=>{
  const sc=SCENES[state.scene],opts=sc.choices(state);
  const ix=opts.findIndex(o=>o.next===dest);
  if(ix<0)throw Error('Missing played path '+sc.id+' -> '+dest);
  state.pageIndex=paginateStory(sc.body(state)).length-1;
  choose(ix);
  if(state.scene!==dest||!validSave(state))throw Error('Failed played path '+sc.id+' -> '+dest);
 };
 try{
  for(const dest of [
   'm4_227_dragon_council','m4_227_dragon_terms','m4_227_dragon_roll',
   'm4_227_nominate_xuwen','m4_227_dragon_reply','m4_227_dragon_roll',
   'm4_227_dragon_close','ch12_c62_02_frontier_227',
   'ch12_c62_03_road_228','ch12_c62_04_crossing_228',
   'ch12_c62_05_aftermath_229','ch12_c62_06_personal_230'
  ])step(dest);
  if(state.storyClock.year!==230||!auh5mNomination(state,'xuwen')||state.civicCareer.dragonNominations227.xuwen.status!=='conditional_interest')throw Error('No organic 230 Xu nomination gate '+state.storyClock.year);
  return clone(state);
 }finally{save=oldSave;render=oldRender;scrollTopNow=oldScroll;}
}"""

MATRIX = r"""input=>{
 const original=clone(input),rows=[];
 const oldSave=save,oldRender=render,oldScroll=scrollTopNow;
 save=()=>{};render=()=>{};scrollTopNow=()=>{};
 const unitCount=s=>auhStoryUIRecordedUnits(s).reduce((v,u)=>v+u[1]+u[2]+u[3],0);
 const before=unitCount(original);
 const keys=['coins','items','relationships','innerCircle','dragonGenerals','health','realmNames'];
 const fixed=Object.fromEntries(keys.map(k=>[k,JSON.stringify(original[k])]));
 const rank=JSON.stringify(original.militaryCareer.rank);
 const staff=JSON.stringify(original.militaryCareer.staff);
 const step=dest=>{
   const sc=SCENES[state.scene],opts=sc.choices(state),ix=opts.findIndex(o=>o.next===dest);
   if(ix<0)throw Error('No route '+sc.id+' -> '+dest);
   state.pageIndex=paginateStory(sc.body(state)).length-1;
   choose(ix);
   if(state.scene!==dest||!validSave(state))throw Error('Blocked '+sc.id+' -> '+dest);
 };
 const chooseAt=i=>{
   const sc=SCENES[state.scene];
   state.pageIndex=paginateStory(sc.body(state)).length-1;
   const target=sc.choices(state)[i]?.next;
   if(!target)throw Error('No choice '+i+' at '+sc.id);
   choose(i);
   if(state.scene!==target||!validSave(state))throw Error('Choice failed '+sc.id+'['+i+']');
 };
 try{
 for(let scope=0;scope<2;scope++)
 for(let presence=0;presence<2;presence++)
 for(let plan=0;plan<3;plan++)
 for(let response=0;response<3;response++)
 for(let report=0;report<3;report++){
   state=clone(original);
   step('m4_230_xu_hearing');
   chooseAt(0);chooseAt(scope);chooseAt(presence);
   if(state.scene!=='m4_230_xu_muster'||state.storyClock.year!==230||auh5oMusterProof(state))
     throw Error('Premature muster');
   chooseAt(0);
   if(state.scene!=='m4_231_xu_road'||state.storyClock.year!==231||!auh5oMusterProof(state)||!auh5oLiveUnit(state))
     throw Error('No physical transfer');
   if(unitCount(state)!==(before||240))throw Error('Troop duplication/lost receiving release');
   chooseAt(plan);chooseAt(response);
   if(!auh5oService(state))throw Error('No independently witnessed scout account');
   const e=state.militaryCareer.xuService231;
   if(e.presence!==(presence===0?'field':'court'))throw Error('False emperor battlefield presence');
   if(!!e.wound!==(presence===0&&plan===2&&response===2))throw Error('False injury');
   chooseAt(report);
   if(state.scene!=='m4_231_xu_review')throw Error('Missing review');
   chooseAt(0);
   if(!auh5oReviewProof(state)||state.npcMilitaryCareers?.xuwen||
      (state.dragonGenerals?.active||[]).includes('xuwen'))
     throw Error('Review became unauthorized rank/Dragon');
   if(state.flags.m4_xu_review!==(report===2?'deferred':'recognized'))
     throw Error('Unwitnessed qualification');
   if(unitCount(state)!==(before||240))throw Error('Unit moved before closure');
   step('ch12_c62_07_council_232');
   if(!state.flags.m4_xu_closed||!state.flags.m4_xu_unit_returned||
      state.storyClock.year!==232||state.age!==original.age+2||unitCount(state)!==before)
     throw Error('Custody or year not restored');
   for(const k of keys)if(JSON.stringify(state[k])!==fixed[k])throw Error('Unexpected grant '+k);
   if(JSON.stringify(state.militaryCareer.rank)!==rank||
      JSON.stringify(state.militaryCareer.staff)!==staff)throw Error('Player promotion/staff grant');
   if(!SCENES[state.scene].body(state).includes('reconnaissance of 231'))
     throw Error('232 callback missing');
   const frozen=JSON.stringify(state);
   militaryPanel();civicPanel();npcMemories('xuwen');auh5oClose(state);
   if(JSON.stringify(state)!==frozen)throw Error('Reader/replay mutation');
   const migrated=resolve(JSON.parse(JSON.stringify(state)));
   if(!validSave(migrated)||migrated.dragonGenerals.active.length!==original.dragonGenerals.active.length)
     throw Error('Save roundtrip or other Dragons changed');
   rows.push({scope,presence,plan,response,report,result:e.result,wound:e.wound});
 }
 return {routes:rows.length,example:rows.find(r=>r.wound),initialTroops:before};
 }finally{save=oldSave;render=oldRender;scrollTopNow=oldScroll;}
}"""

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--report',type=Path)
    args=ap.parse_args()
    with fixture(BASELINE) as (browser,url,result):
        baseline=browser.new_page()
        baseline.goto(url+'/baseline.html')
        seed=baseline.evaluate(TO_227,organic_accession_seeds(baseline)[7])
        seed=baseline.evaluate(SEED,seed)
        ids=set(baseline.evaluate('Object.keys(SCENES)'))
        staff=baseline.evaluate('AUH_MC_SPECIAL_STAFF')
        baseline.close()
        for width in (390,1280):
            ctx=browser.new_context(viewport={'width':width,'height':900})
            p=ctx.new_page()
            errors=[]
            p.on('pageerror',lambda e:errors.append(str(e)))
            p.goto(url+'/active.html')
            assert not errors,errors
            current=set(p.evaluate('Object.keys(SCENES)'))
            assert ids<=current and current-ids==NEW and len(current)==751
            assert p.evaluate('AUH_MC_SPECIAL_STAFF')==staff
            matrix=p.evaluate(MATRIX,seed)
            assert matrix['routes']==108,matrix
            result['checks'].append({'viewport':width,'routes':108,'report':matrix,'page_errors':errors})
            p.close();ctx.close()
        result['status']='PASS_TARGETED_CHOICE_HANDLERS_NOT_PHYSICAL_FILE_URL_OR_FULL_EDITORIAL'
        write_report(result,args.report)

if __name__=='__main__':main()
