#!/usr/bin/env python3
"""Voluntary western service, witnessed Baxi duty, warrants and river rejoin."""
import argparse
from copy import deepcopy
from pathlib import Path
from qa_support import fixture, write_report
from qa_m2_continuity import START
from qa_changban import ADVANCE
from qa_river_councils import TO_HANJIN
from qa_river_patrol import TO_FLOTILLA
from qa_red_cliffs import TO_ANCHORS
from qa_crossing210 import TO_TIDE

BASELINE='06515cd:GAME/ALL_UNDER_HEAVEN_v0.4.99.5c_THE_OPEN_BANK_CHARTER.html'
NEW={'m3_215_west_terms','m3_215_west_march','m3_216_baxi_orders','m3_216_baxi_contact','m3_216_baxi_report','m3_216_baxi_review','m3_216_west_homeward'}
TO_BORDER=r"""seed=>{
 state=clone(seed);activeTab='story';const a=save,b=render,c=scrollTopNow;save=()=>{};render=()=>{};scrollTopNow=()=>{};
 try{for(let i=0;i<140;i++){
  if(state.scene==='ch10_c58_02_border_oath')return clone(state);
  const sc=SCENES[state.scene];state.pageIndex=paginateStory(sc.body(state)).length-1;choose(0);if(sc.id===state.scene)throw Error('215 seed blocked '+sc.id+':'+banner);
 }throw Error('215 not reached');}finally{save=a;render=b;scrollTopNow=c;}
}"""
ROUTES=r"""seed=>{
 const compact=clone(seed);for(const h of compact.history)h.body='';
 const a=save,b=render,c=scrollTopNow;save=()=>{};render=()=>{};scrollTopNow=()=>{};const rows=[];let example=null,review=null,contact=null;
 const step=index=>{const sc=SCENES[state.scene];state.pageIndex=paginateStory(sc.body(state)).length-1;choose(index);if(state.scene===sc.id||!validSave(state))throw Error('Baxi blocked '+sc.id+':'+banner);};
 try{for(const branch of ['Infantry','Cavalry'])for(let station=0;station<3;station++)for(let action=0;action<3;action++)for(let report=0;report<3;report++)for(let decision=0;decision<(report===0?3:report===1?2:1);decision++){
  state=clone(compact);activeTab='story';
  if(branch==='Cavalry'){
   state.militaryCareer.combatService={branch,unit:'Synthetic lawful mounted formation',commander:'Recorded field officer',year:215,proof:'legacy:lawful-cavalry'};
   for(const u of state.militaryCareer.units)if(u.active!==false){u.cavalry=state.militaryCareer.rank==='Captain'?30:20;u.infantry=0;}
  }
  const before=clone(state);step(SCENES[state.scene].choices(state).findIndex(o=>o.next==='m3_215_west_terms'));step(0);step(0);
  if(state.storyClock.year!==216||state.age!==42||state.scene!=='m3_216_baxi_orders')throw Error('Baxi journey clock');
  step(station);contact=clone(state);if(!state.militaryCareer.fieldPosition.active||state.militaryCareer.fieldPosition.proof!=='m3_5d:baxi216')throw Error('Baxi order');
  step(action);if(!auh5dEvidence(state)||state.militaryCareer.fieldPosition.active)throw Error('Baxi service/relief');
  const recorded=JSON.stringify(state);auh5dRecord(state,['turn','hold','withdraw'][action]);if(JSON.stringify(state)!==recorded)throw Error('Replayed Baxi action');
  for(const key of ['rank','rankProof','units','appointmentHistory','staff','superior','combatService'])if(JSON.stringify(state.militaryCareer[key])!==JSON.stringify(before.militaryCareer[key]))throw Error('Pre-hearing military grant '+key);
  step(report);let offered=null;
  if(report<2){review=clone(state);offered=auh5dOffer(state);if(!!offered!==(report===0))throw Error('Offer gate '+JSON.stringify({rank:before.militaryCareer.rank,branch,station,action,report,offer:offered,units:state.militaryCareer.units,appointments:state.militaryCareer.appointmentHistory,evidence:auh5dEvidence(state),seen:auh4nSeen(state,'m3_216_baxi_report'),year:state.storyClock.year}));step(decision);}
  const accepted=report===0&&decision===0;
  if(state.militaryCareer.rank!==(accepted?offered.rank:before.militaryCareer.rank))throw Error('Wrong rank');
  if(accepted){
   const units=state.militaryCareer.units.filter(u=>u.active!==false);if(units.length!==(offered.rank==='Major'?3:1)||units.reduce((n,u)=>n+u.cavalry+u.infantry,0)!==offered.count||units.some(u=>u.source!=='m3_216_baxi_review:accepted'||(offered.rank==='Major'&&u.rank!=='Captain'))||state.militaryCareer.appointmentHistory.length!==before.militaryCareer.appointmentHistory.length+1)throw Error('Accepted muster/double count');
   if(auhMcStaffRoles(state.militaryCareer.rank).length!==(offered.rank==='Major'?5:offered.rank==='Captain'?3:1))throw Error('Five staff eligibility');
  }else for(const key of ['units','appointmentHistory','rankProof','superior'])if(JSON.stringify(state.militaryCareer[key])!==JSON.stringify(before.militaryCareer[key]))throw Error('Refusal changed '+key);
  for(const key of ['coins','items','innerCircle','civicCareer'])if(JSON.stringify(state[key])!==JSON.stringify(before[key]))throw Error('Unchosen grant '+key);
  if(JSON.stringify(state.militaryCareer.staff)!==JSON.stringify(before.militaryCareer.staff)||JSON.stringify(state.militaryCareer.combatService)!==JSON.stringify(before.militaryCareer.combatService))throw Error('Hired staff/branch transfer');
  const frozen=JSON.stringify(state);militaryPanel();npcMemories('zhangfei');civicPanel();auh5dAccept(state);if(JSON.stringify(state)!==frozen)throw Error('View/replayed acceptance mutation');
  step(0);if(state.scene!=='ch10_c58_03_watchfires'||state.storyClock.year!==216||state.age!==42||state.militaryCareer.fieldPosition.proof!=='m3_5d:river216'||!state.militaryCareer.fieldPosition.active)throw Error('216 return and river order');
  if(state.militaryCareer.superior?.proof==='m3_216_baxi_review:rotation')throw Error('Western superior followed east');
  step(action);if(state.storyClock.year!==217||state.age!==43||state.militaryCareer.fieldPosition.active||!auh5dFrontierEvidence(state)||!auh5dEvidence(state))throw Error('River rejoin');
  if(!SCENES[state.scene].body(state).includes(AUH5D_FRONTIER[state.flags.auh58_operation]))throw Error('217 callback');
  rows.push({originalRank:before.militaryCareer.rank,branch,station,action,report,decision,rank:state.militaryCareer.rank,total:auhStoryUIRecordedUnits(state).reduce((n,u)=>n+u[1]+u[2]+u[3],0)});example=clone(state);
 }return {rows,example,review,contact};}finally{save=a;render=b;scrollTopNow=c;}
}"""
PROJECT=r"""s=>['ch10_c58_01_western_messenger','ch10_c58_02_border_oath','ch10_c58_03_watchfires'].map(id=>({id,choices:SCENES[id].choices(s).slice(0,id==='ch10_c58_01_western_messenger'?1:3).map(o=>{
 const x=clone(s);o.effect(x);delete x.flags.m3_215_frontier_scope;delete x.militaryCareer.fieldPosition;if(x.militaryCareer.campaignEvidence)delete x.militaryCareer.campaignEvidence.frontier216;x.journal=clone(s.journal);return {next:o.next,state:x};
})}))"""

def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--report',type=Path);args=parser.parse_args()
    with fixture(BASELINE) as (browser,url,result):
        base=browser.new_page();base.goto(url+'/baseline.html')
        initial=[base.evaluate(START,d) for d in (False,True)]
        starts=[base.evaluate(ADVANCE,{'seed':s['snapshots']['ch08_pb55_xushu'],'decision':d}) for s in initial for d in (0,1)]
        hanjin=[base.evaluate(TO_HANJIN,s) for s in starts];flotilla=[base.evaluate(TO_FLOTILLA,s) for s in hanjin]
        anchors=[base.evaluate(TO_ANCHORS,{'seed':s,'weak':False}) for s in flotilla]
        tide=[base.evaluate(TO_TIDE,{'seed':s,'world':'south'}) for s in anchors]
        tide.append(base.evaluate(TO_TIDE.replace('ch08_06:1','ch08_06:0'),{'seed':anchors[1],'world':'south'}))
        weak=base.evaluate(TO_ANCHORS,{'seed':flotilla[0],'weak':True})
        tide += [base.evaluate(TO_TIDE,{'seed':weak if world=='north' else anchors[0],'world':world}) for world in ('north','separate')]
        seeds=[base.evaluate(TO_BORDER,s) for s in tide]
        seeds.append(base.evaluate(TO_BORDER.replace('choose(0);',"choose(sc.id==='ch09_charter_hearing'?3:0);"),tide[3]))
        assert [s['militaryCareer']['rank'] for s in seeds]==['Captain','Sergeant','Sergeant','Private','Captain','Captain','Captain','Private']
        assert seeds[-1]['civicCareer']['localCharter']['delegated'] and not seeds[-1]['civicCareer']['localCharter']['accepted']
        old_ids=base.evaluate('Object.keys(SCENES)');base.close()
        for width in (390,1280):
            context=browser.new_context(viewport={'width':width,'height':900});page=context.new_page();errors=[];page.on('pageerror',lambda e:errors.append(str(e)));page.goto(url+'/active.html')
            later={'m3_219_jing_contact','m3_219_jing_after'}
            added=set(page.evaluate('Object.keys(SCENES)'))-set(old_ids)
            eastern={'m3_222_field_review','m3_222_after_review'}
            settlement={'m3_223_rolls','m3_223_ratification','m3_223_after_terms'}
            assert added in (NEW,NEW|later,NEW|later|eastern,NEW|later|eastern|settlement),added-NEW
            assert page.evaluate('ids=>ids.every(id=>SCENES[id].displayChapter===10)',list(NEW))
            runs=[page.evaluate(ROUTES,s) for s in seeds];assert sum(len(r['rows']) for r in runs)==864
            ranks={r['rank'] for run in runs for r in run['rows']};assert ranks=={'Private','Sergeant','Captain','Major'}
            assert any(r['rank']=='Major' and r['total']==180 for r in runs[0]['rows'])
            assert all(r['rank']!='Major' for r in runs[4]['rows'])  # Captain without company receives a company, not a larger command.
            base=context.new_page();base.goto(url+'/baseline.html');assert page.evaluate(PROJECT,seeds[0])==base.evaluate(PROJECT,seeds[0])
            major=deepcopy(seeds[0]);major['militaryCareer']['rank']='Major'
            legacy=r"""s=>['ch10_c58_01_western_messenger','ch10_c58_02_border_oath','ch10_c58_03_watchfires'].map(id=>({id,body:SCENES[id].body(s),choices:SCENES[id].choices(s).slice(0,id==='ch10_c58_01_western_messenger'?1:3).map(o=>{const x=clone(s);o.effect(x);return {next:o.next,label:o.label,state:x};})}))"""
            assert page.evaluate(legacy,major)==base.evaluate(legacy,major)
            assert not page.evaluate('s=>auh5dEntry(s)',major);base.close()
            page.evaluate(r"""config=>{
             const step=i=>{const sc=SCENES[state.scene];state.pageIndex=paginateStory(sc.body(state)).length-1;choose(i);if(state.scene===sc.id)throw Error('Negative route blocked '+banner);};
             const a=save,b=render,c=scrollTopNow;save=()=>{};render=()=>{};scrollTopNow=()=>{};
             try{
              state=clone(config.seed);step(SCENES[state.scene].choices(state).length-1);step(1);if(state.scene!=='ch10_c58_02_border_oath'||state.storyClock.year!==215||auh5dEvidence(state)||auh5dEntry(state))throw Error('Rotation refusal');step(0);if(state.scene!=='ch10_c58_03_watchfires'||state.storyClock.year!==216||!state.militaryCareer.fieldPosition.active)throw Error('Old river route');
              state=clone(config.seed);step(SCENES[state.scene].choices(state).length-1);step(0);step(1);if(state.scene!=='m3_216_west_homeward'||auh5dEvidence(state)||state.militaryCareer.rank!==config.seed.militaryCareer.rank)throw Error('Staging return granted service');step(0);
              state=clone(config.seed);state.age=61;step(SCENES[state.scene].choices(state).length-1);step(0);step(0);if(state.age!==62||state.storyClock.year!==216)throw Error('Legacy starting age reset');
              const noVisit=clone(config.example);noVisit.visited=[];noVisit.history=[];if(auh5dEvidence(noVisit)||auh5dFrontierEvidence(noVisit))throw Error('Flag-only service');
              const hist=clone(config.example);hist.visited=[];if(!auh5dEvidence(hist)||!auh5dFrontierEvidence(hist))throw Error('History-only service');
              const invalid=clone(config.example);invalid.militaryCareer.campaignEvidence.baxi216.action='__proto__';if(auh5dEvidence(invalid))throw Error('Invalid enum');
              const old=clone(config.seed),frozen=JSON.stringify(old);state=old;militaryPanel();npcMemories('zhangfei');if(JSON.stringify(old)!==frozen||old.militaryCareer.campaignEvidence.baxi216)throw Error('Legacy backfill');
              const late=clone(config.seed);late.storyClock.year=218;if(auh5dEntry(late))throw Error('Late rotation');delete late.militaryCareer.combatService;late.storyClock.year=215;if(auh5dEntry(late))throw Error('Unknown branch entry');
              state=clone(config.contact);state.militaryCareer.fieldPosition={year:219,active:true,proof:'later'};auh5dPosition(state,'ridge',true);auh5dRecord(state,'turn');if(state.militaryCareer.fieldPosition.proof!=='later'||state.flags.m3_216_baxi_action)throw Error('Later posting overwritten');
              state=clone(config.review);state.flags.m3_216_baxi_account='checked';delete state.flags.m3_216_review;const offered=auh5dOffer(state);if(!offered)throw Error('Organic offer missing');
              const forged=clone(state);forged.militaryCareer.units[forged.militaryCareer.units.length-1].source='unknown';if(auh5dOffer(forged))throw Error('Unknown muster source');
              const flagOnly=clone(state);flagOnly.visited=[];flagOnly.history=[];if(auh5dOffer(flagOnly))throw Error('Flag-only commission');
              const badBranch=clone(state);delete badBranch.militaryCareer.combatService;if(auh5dOffer(badBranch))throw Error('Unknown branch commission');
             }finally{save=a;render=b;scrollTopNow=c;}
            }""",{'seed':seeds[0],**runs[0]})
            # Full-history browser route: volunteer, journey, order, fight, review,
            # accept Major, handover and a river action. No synthetic rank jump.
            page.evaluate('s=>{state=clone(s);activeTab="story";render();}',seeds[0])
            for index in (3,0,0,1,1,0,0,0,1):
                page.evaluate('()=>{state.pageIndex=paginateStory(SCENES[state.scene].body(state)).length-1;render();}')
                page.locator(f'[data-choice="{index}"]' if index else '[data-choice="0"], [data-action="next-scene"]').click()
            assert page.evaluate('state.scene==="ch10_c58_04_personal_dispatch"&&state.militaryCareer.rank==="Major"&&auh5dEvidence(state)&&auh5dFrontierEvidence(state)&&validSave(state)')
            page.reload();assert page.evaluate('state.militaryCareer.rank==="Major"&&auh5dEvidence(state)')
            page.locator('#menuToggle').click();page.locator('#gameMenu [data-nav="military"]').click()
            assert page.locator('[aria-label="Baxi service in 216"]').is_visible();assert page.locator('[aria-label="River screen in 216"]').is_visible()
            assert page.evaluate('document.documentElement.scrollWidth<=innerWidth')
            assert not errors,errors
            result['checks'].append({'width':width,'all_local_routes_eight_organic_career_world_charter_seeds_two_branches':864,'earned_or_refused_warrants_and_exact_muster':'PASS','captain_without_company_receives_company_only':'PASS','five_staff_eligibility_no_appointments':'PASS','original_effects_and_higher_command_legacy_parity':'PASS','no_other_grants_and_staging_refusal':'PASS','positions_clock_old_age_provenance_idempotence_later_post':'PASS','reload_military_dom':'PASS','organic_captain_to_major_dom_clicks':9,'page_errors':errors});context.close()
    result['limits']='Five organic career seeds plus two organic world variants (northern/separate) and one delegated-charter route; not the full world×career product. Cavalry and higher-command parity variants synthetic. Full local 3×3×(3+2+1) decisions, both branches. Matrix suppresses paint/storage and compacts old history bodies; DOM uses full history. Not full Chapter X/M3 or physical-device file:// certification.'
    write_report(result,args.report)
if __name__=='__main__':main()
