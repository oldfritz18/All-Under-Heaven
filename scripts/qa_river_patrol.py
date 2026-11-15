#!/usr/bin/env python3
"""Assigned escort, bounded patrol decisions, first contact and memory."""
import argparse
from copy import deepcopy
from pathlib import Path
from qa_support import fixture, write_report
from qa_m2_continuity import START
from qa_changban import ADVANCE
from qa_river_councils import TO_HANJIN

BASELINE='230ee02:GAME/ALL_UNDER_HEAVEN_v0.4.99.4x_RIVER_COUNCILS_AND_ORDERS.html'
TO_FLOTILLA=r"""seed=>{
 state=clone(seed);activeTab='story';for(let i=0;i<40;i++){
  if(state.scene==='ch08_rc54_flotilla')return clone(state);
  const sc=SCENES[state.scene];state.pageIndex=paginateStory(sc.body(state)).length-1;choose(0);if(sc.id===state.scene)throw Error('Baseline councils blocked');
 }throw Error('Flotilla not reached');
}"""
ROUTES=r"""seed=>{
 const compact=clone(seed);for(const h of compact.history)h.body='';
 const realSave=save,realRender=render,realScroll=scrollTopNow;save=()=>{};render=()=>{};scrollTopNow=()=>{};
 const rows=[];try{
 for(const branch of ['Infantry','Cavalry'])for(let a=0;a<3;a++)for(let b=0;b<3;b++)for(let c=0;c<3;c++){
  state=clone(compact);activeTab='story';if(branch==='Cavalry')state.militaryCareer.combatService={branch,unit:'Legacy mounted section',commander:'Recorded officer',year:208,proof:'legacy:lawful-cavalry'};
  const before=clone(state),moves=[0,a,0,b,c,0,(a+b)%3,(a+c)%3,0];
  for(const [i,index] of moves.entries()){
   const sc=SCENES[state.scene];state.pageIndex=paginateStory(sc.body(state)).length-1;choose(index);
   if(!validSave(state)||state.scene===sc.id)throw Error('Patrol blocked '+sc.id+':'+banner);
   if(state.storyClock.year!==208||state.age!==34)throw Error('Patrol date');
   if(!state.militaryCareer.fieldPosition.active||state.militaryCareer.fieldPosition.proof!=='m3_4y:escort')throw Error('Assigned escort missing');
   if(branch==='Cavalry'&&!state.militaryCareer.fieldPosition.formation.includes('dismounted'))throw Error('Horse on deck fiction');
  }
  if(state.scene!=='ch08_03'||!auh4yEvidence(state))throw Error('No patrol return evidence');
  for(const key of ['rank','rankProof','units','appointmentHistory','staff','superior','combatService'])if(JSON.stringify(state.militaryCareer[key])!==JSON.stringify(before.militaryCareer[key]))throw Error('Military grant '+key);
  for(const key of ['coins','items','innerCircle'])if(JSON.stringify(state[key])!==JSON.stringify(before[key]))throw Error('Goods/recruit grant');
  if(state.militaryCareer.campaignEvidence.riverRecon208.action!==['pilots','enemy','refuge'][c])throw Error('Wrong report');
  const frozen=JSON.stringify(state);militaryPanel();npcMemories('hansheng');if(JSON.stringify(state)!==frozen)throw Error('View mutation');
  const m=state.militaryCareer.campaignEvidence.riverRecon208.account;if(!npcMemories('hansheng').includes(m))throw Error('No sourced recall');
  const beforeReplay=JSON.stringify(state.militaryCareer);SCENES.ch08_rc54_first_clash.choices(state)[0].effect(state);if(JSON.stringify(state.militaryCareer)!==beforeReplay)throw Error('Duplicate patrol evidence');
  rows.push({rank:before.militaryCareer.rank,branch,doctrine:a,plan:b,scout:c,shore:(a+b)%3,dispute:(a+c)%3});
 }return {rows,example:clone(state)};
 }finally{save=realSave;render=realRender;scrollTopNow=realScroll;}
}"""
PROJECT=r"""s=>['ch08_rc54_flotilla','ch08_rc54_council','ch08_rc54_pilots','ch08_shu56_kongming_warroom','ch08_rc54_scout','ch08_rc54_first_clash','ch08_shu56_zhangfei_shore','ch08_rc54_southern_dispute','ch08_rc54_twilight'].map(id=>({id,choices:SCENES[id].choices(s).map(o=>{
 const x=clone(s);o.effect(x);x.journal=clone(s.journal);delete x.militaryCareer.fieldPosition;if(x.militaryCareer.campaignEvidence)delete x.militaryCareer.campaignEvidence.riverRecon208;delete x.flags.m3_208_embarked;
 return {next:o.next,state:x};})}))"""

def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--report',type=Path);args=parser.parse_args()
    with fixture(BASELINE) as (browser,url,result):
        base=browser.new_page();base.goto(url+'/baseline.html')
        initial=[base.evaluate(START,d) for d in (False,True)]
        starts=[base.evaluate(ADVANCE,{'seed':s['snapshots']['ch08_pb55_xushu'],'decision':d}) for s in initial for d in (0,1)]
        hanjin=[base.evaluate(TO_HANJIN,s) for s in starts];seeds=[base.evaluate(TO_FLOTILLA,s) for s in hanjin];base.close()
        for width in (390,1280):
            context=browser.new_context(viewport={'width':width,'height':900});page=context.new_page();errors=[];page.on('pageerror',lambda e:errors.append(str(e)));page.goto(url+'/active.html')
            assert set(initial[0]['ids']).issubset(page.evaluate('Object.keys(SCENES)'))
            runs=[page.evaluate(ROUTES,s) for s in seeds];assert sum(len(r['rows']) for r in runs)==216
            base=context.new_page();base.goto(url+'/baseline.html')
            for seed in (seeds[0],seeds[3]):assert page.evaluate(PROJECT,seed)==base.evaluate(PROJECT,seed)
            major=deepcopy(seeds[0]);major['militaryCareer']['rank']='Major'
            high=r"""s=>['ch08_rc54_flotilla','ch08_rc54_council','ch08_rc54_pilots','ch08_shu56_kongming_warroom','ch08_rc54_scout','ch08_rc54_first_clash','ch08_shu56_zhangfei_shore','ch08_rc54_southern_dispute','ch08_rc54_twilight'].map(id=>({id,body:SCENES[id].body(s),choices:SCENES[id].choices(s).map(o=>{const x=clone(s);o.effect(x);return {label:o.label,next:o.next,state:x};})}))"""
            assert page.evaluate(high,major)==base.evaluate(high,major);base.close()
            page.evaluate(r"""seed=>{
             state=clone(seed);const history=clone(state);history.visited=[];if(!auh4yEvidence(history))throw Error('History evidence');
             const empty=clone(state);empty.history=[];empty.visited=[];if(auh4yEvidence(empty))throw Error('Flag-only evidence');delete empty.militaryCareer.campaignEvidence.riverRecon208;SCENES.ch08_rc54_first_clash.choices(empty)[0].effect(empty);if(empty.militaryCareer.campaignEvidence.riverRecon208)throw Error('Flag-only record');
             const invalid=clone(state);invalid.militaryCareer.campaignEvidence.riverRecon208.action='__proto__';if(auh4yEvidence(invalid))throw Error('Invalid action');
             const late=clone(state);late.militaryCareer.fieldPosition={year:214,proof:'later',active:true};auh4yPosition(late);if(late.militaryCareer.fieldPosition.proof!=='later')throw Error('Later posting changed');
             localStorage.setItem(SAVE_KEY,JSON.stringify(state));handleAction('load-original');
            }""",runs[0]['example']);page.reload();assert page.evaluate('validSave(state)&&auh4yEvidence(state)')
            page.locator('#menuToggle').click();page.locator('#gameMenu [data-nav="military"]').click();assert page.locator('[aria-label="Witnessed river reconnaissance"]').is_visible();assert page.evaluate('document.documentElement.scrollWidth<=innerWidth')
            page.evaluate('s=>{state=clone(s);activeTab="story";render();}',seeds[3])
            for _ in range(9):
                page.evaluate('()=>{state.pageIndex=paginateStory(SCENES[state.scene].body(state)).length-1;render();}')
                page.locator('[data-choice="0"], [data-action="next-scene"]').click()
            assert page.evaluate('state.scene==="ch08_03"&&state.militaryCareer.rank==="Private"&&auh4yEvidence(state)')
            assert not errors,errors
            result['checks'].append({'width':width,'pairwise_routes_four_careers_two_branches':216,
                'all_legacy_choice_effects_parity_except_documented_scope_evidence':'PASS','nine_legacy_major_nodes_full_parity':'PASS',
                'no_grants_and_cavalry_dismounted_service':'PASS','branch_report_memory_readonly_idempotence':'PASS',
                'negative_provenance_and_later_post':'PASS','reload_military_dom':'PASS','full_history_private_dom_clicks':9,'page_errors':errors});context.close()
    result['limits']='Nine preparation/patrol nodes through ch08_03; five 3-way choices pairwise. Later fire battle/settlement and chapter relabeling pending. Matrix suppresses old history bodies/render/storage; DOM uses full history. Cavalry/Major synthetic, no physical-device file://.'
    write_report(result,args.report)
if __name__=='__main__':main()
