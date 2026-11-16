#!/usr/bin/env python3
"""218–220 continuity, played Jing contact and actual rather than planned outcome."""
import argparse
from copy import deepcopy
from pathlib import Path
from qa_support import fixture, write_report, HANZHONG_219_SCENES, COURT_224_SCENES, DESIGNATION_221_SCENES, SHU_ACCESSION_225_SCENES, DRAGON_NOMINATION_227_SCENES, HAN_DRAGON_229_SCENES
from qa_m2_continuity import START
from qa_changban import ADVANCE
from qa_river_councils import TO_HANJIN
from qa_river_patrol import TO_FLOTILLA
from qa_red_cliffs import TO_ANCHORS
from qa_crossing210 import TO_TIDE
from qa_baxi216 import TO_BORDER

BASELINE='4b5d2ef:GAME/ALL_UNDER_HEAVEN_v0.4.99.5d_THE_BAXI_ROTATION.html'
NEW={'m3_219_jing_contact','m3_219_jing_after'}
TO_JING=r"""config=>{
 state=clone(config.seed);activeTab='story';const a=save,b=render,c=scrollTopNow;save=()=>{};render=()=>{};scrollTopNow=()=>{};
 const step=i=>{const sc=SCENES[state.scene];state.pageIndex=paginateStory(sc.body(state)).length-1;choose(i);if(state.scene===sc.id)throw Error('219 seed blocked '+sc.id+':'+banner);};
 try{
  if(config.west)for(const i of [3,0,0,1,1,0,0,0,1])step(i);else step(config.duty||0);
  let at218=null;
  for(let i=0;i<70;i++){
   if(state.scene==='ch10_c58_07_jing_219')return {seed:clone(state),at218};
   if(state.scene==='ch10_c58_06_frontier_218')at218=clone(state);step(0);
  }throw Error('219 not reached');
 }finally{save=a;render=b;scrollTopNow=c;}
}"""
ROUTES=r"""seed=>{
 const compact=clone(seed);for(const h of compact.history)h.body='';
 const a=save,b=render,c=scrollTopNow;save=()=>{};render=()=>{};scrollTopNow=()=>{};const rows=[];let example=null,contact=null;
 const step=i=>{const sc=SCENES[state.scene];state.pageIndex=paginateStory(sc.body(state)).length-1;choose(i);if(state.scene===sc.id||!validSave(state))throw Error('Jing blocked '+sc.id+':'+banner);};
 try{for(const branch of ['Infantry','Cavalry'])for(let policy=0;policy<3;policy++)for(let tactic=0;tactic<3;tactic++)for(let after=0;after<3;after++){
  state=clone(compact);activeTab='story';if(branch==='Cavalry'){
   state.militaryCareer.combatService={branch,unit:'Synthetic lawful mounted formation',commander:'Recorded field officer',year:218,proof:'legacy:lawful-cavalry'};
   for(const u of state.militaryCareer.units)if(u.active!==false){u.cavalry=state.militaryCareer.rank==='Private'?0:state.militaryCareer.rank==='Sergeant'?20:30;u.infantry=0;}
  }
  const before=clone(state);step(policy);contact=clone(state);
  if(state.scene!=='m3_219_jing_contact'||!state.militaryCareer.fieldPosition.active||state.militaryCareer.fieldPosition.proof!=='m3_5e:jing219')throw Error('219 issued order');
  step(tactic);if(state.scene!=='m3_219_jing_after'||!auh5eEvidence(state)||state.militaryCareer.fieldPosition.active)throw Error('219 contact/relief');
  const once=JSON.stringify(state);auh5eRecord(state,['press','steady','retire'][tactic]);militaryPanel();npcMemories('xuwen');civicPanel();if(JSON.stringify(state)!==once)throw Error('Jing replay/view mutation');
  const expected=(tactic===2||policy===2)?'civilian_fallback':policy===1&&tactic===0?'frontier_disputed':policy===1?'witnessed_border':auh58Outcome(state);
  if(state.flags.auh58_result!==expected)throw Error('Plan substituted for actual result');
  step(after);if(state.scene!=='ch10_c58_08_road_home')throw Error('219 road return');
  const road=SCENES[state.scene].body(state);if(!road.includes(state.militaryCareer.campaignEvidence.jing219.account))throw Error('Road callback');
  // Retain original household/relationship detours on the way to the inquiry.
  for(let i=0;state.scene!=='ch10_c73_01_missing_orders_219'&&i<16;i++)step(0);
  if(state.scene!=='ch10_c73_01_missing_orders_219')throw Error('Missing-orders entry');
  step((policy+tactic)%3);step((tactic+after)%3);
  if(state.scene!=='ch10_06'||!auh5eEvidence(state)||state.storyClock.year!==219||state.age!==45)throw Error('219 inquiry return');
  for(const key of ['rank','rankProof','units','appointmentHistory','staff','superior','combatService'])if(JSON.stringify(state.militaryCareer[key])!==JSON.stringify(before.militaryCareer[key]))throw Error('Jing military grant '+key);
  for(const key of ['coins','items','innerCircle','civicCareer','dragonGenerals'])if(JSON.stringify(state[key])!==JSON.stringify(before[key]))throw Error('Jing unchosen grant '+key);
  if(before.flags.auh66_spouse&&state.flags.auh66_spouse!==before.flags.auh66_spouse)throw Error('Lost spouse');
  rows.push({rank:before.militaryCareer.rank,branch,policy,tactic,after,method:(policy+tactic)%3,notice:(tactic+after)%3,result:state.militaryCareer.campaignEvidence.jing219.result,frontier:state.flags.auh58_result});example=clone(state);
 }return {rows,example,contact};}finally{save=a;render=b;scrollTopNow=c;}
}"""
PROJECT=r"""s=>['ch10_c58_07_jing_219','ch10_c73_01_missing_orders_219','ch10_c73_02_the_cost_of_truth_219','ch10_06'].map(id=>({id,choices:SCENES[id].choices(s).map(o=>{
 const x=clone(s);o.effect(x);delete x.flags.m3_219_scope;delete x.militaryCareer.fieldPosition;x.journal=clone(s.journal);return {next:o.next==='m3_219_jing_contact'?'ch10_c58_08_road_home':o.next,state:x};
})}))"""

def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--report',type=Path);args=parser.parse_args()
    with fixture(BASELINE) as (browser,url,result):
        base=browser.new_page();base.goto(url+'/baseline.html')
        initial=[base.evaluate(START,d) for d in (False,True)]
        starts=[base.evaluate(ADVANCE,{'seed':s['snapshots']['ch08_pb55_xushu'],'decision':d}) for s in initial for d in (0,1)]
        flotilla=[base.evaluate(TO_FLOTILLA,base.evaluate(TO_HANJIN,s)) for s in starts]
        anchors=[base.evaluate(TO_ANCHORS,{'seed':s,'weak':False}) for s in flotilla]
        tide=[base.evaluate(TO_TIDE,{'seed':s,'world':'south'}) for s in anchors]
        tide.append(base.evaluate(TO_TIDE.replace('ch08_06:1','ch08_06:0'),{'seed':anchors[1],'world':'south'}))
        weak=base.evaluate(TO_ANCHORS,{'seed':flotilla[0],'weak':True})
        tide += [base.evaluate(TO_TIDE,{'seed':weak if world=='north' else anchors[0],'world':world}) for world in ('north','separate')]
        border=[base.evaluate(TO_BORDER,s) for s in tide]
        reached=[base.evaluate(TO_JING,{'seed':s}) for s in border]
        reached += [base.evaluate(TO_JING,{'seed':border[0],'west':True})]
        reached += [base.evaluate(TO_JING,{'seed':border[0],'duty':i}) for i in (1,2)]
        seeds=[r['seed'] for r in reached];assert seeds[7]['militaryCareer']['rank']=='Major'
        old_ids=base.evaluate('Object.keys(SCENES)');base.close()
        for width in (390,1280):
            context=browser.new_context(viewport={'width':width,'height':900});page=context.new_page();errors=[];page.on('pageerror',lambda e:errors.append(str(e)));page.goto(url+'/active.html')
            added=set(page.evaluate('Object.keys(SCENES)'))-set(old_ids)
            later={'m3_222_field_review','m3_222_after_review'}
            settlement={'m3_223_rolls','m3_223_ratification','m3_223_after_terms'}
            general={'m3_222_standard','m3_222_command_lanes','m3_222_rider_at_the_bend','m3_222_first_return'}
            assert added in (NEW,NEW|later,NEW|later|settlement,NEW|later|settlement|general,NEW|later|settlement|general|HANZHONG_219_SCENES,NEW|later|settlement|general|HANZHONG_219_SCENES|COURT_224_SCENES,NEW|later|settlement|general|HANZHONG_219_SCENES|COURT_224_SCENES|DESIGNATION_221_SCENES,NEW|later|settlement|general|HANZHONG_219_SCENES|COURT_224_SCENES|DESIGNATION_221_SCENES|SHU_ACCESSION_225_SCENES,NEW|later|settlement|general|HANZHONG_219_SCENES|COURT_224_SCENES|DESIGNATION_221_SCENES|SHU_ACCESSION_225_SCENES|DRAGON_NOMINATION_227_SCENES,NEW|later|settlement|general|HANZHONG_219_SCENES|COURT_224_SCENES|DESIGNATION_221_SCENES|SHU_ACCESSION_225_SCENES|DRAGON_NOMINATION_227_SCENES|HAN_DRAGON_229_SCENES),added-NEW
            runs=[page.evaluate(ROUTES,s) for s in seeds];assert sum(len(r['rows']) for r in runs)==540
            local={r['result'] for run in runs for r in run['rows']};assert len(local)==9
            assert {r['frontier'] for run in runs for r in run['rows']}=={'civilian_fallback','frontier_disputed','witnessed_border','allied_frontier','independent_defended'}
            # All pairs among policy, tactic, aftermath, inquiry and notice.
            group=['policy','tactic','after','method','notice']
            for i,k in enumerate(group):
                for l in group[i+1:]:assert len({(r[k],r[l]) for r in runs[0]['rows']})==9,(k,l)
            base=context.new_page();base.goto(url+'/baseline.html');assert page.evaluate(PROJECT,seeds[0])==base.evaluate(PROJECT,seeds[0])
            major=deepcopy(seeds[0]);major['militaryCareer']['rank']='Major';major['flags'].pop('m3_215_frontier_scope',None)
            legacy=r"""s=>['ch10_c58_06_frontier_218','ch10_c58_07_jing_219','ch10_c58_08_road_home','ch10_c73_01_missing_orders_219','ch10_c73_02_the_cost_of_truth_219','ch10_06'].map(id=>({id,body:SCENES[id].body(s),choices:SCENES[id].choices(s).map(o=>{const x=clone(s);o.effect(x);return {label:o.label,next:o.next,state:x};})}))"""
            assert page.evaluate(legacy,major)==base.evaluate(legacy,major)
            example=runs[0]['example'];tail=r"""s=>{const b=SCENES.ch10_c58_08_road_home.body(s).match(/<p>[\s\S]*?<\/p>/g);return [b[0],...b.slice(2)];}"""
            assert page.evaluate(tail,example)==base.evaluate(tail,example)
            # Prove current evidence never implies a journey to Hanzhong.
            body=page.evaluate('s=>SCENES.ch10_c58_06_frontier_218.body(s)',reached[7]['at218'])
            assert 'does not place you at a battle fought after your rotation returned' in body
            base.close()
            page.evaluate(r"""config=>{
             const s=clone(config.example),frozen=JSON.stringify(s);state=s;militaryPanel();npcMemories('hansheng');SCENES.ch10_c58_08_road_home.body(s);if(JSON.stringify(s)!==frozen)throw Error('View mutation');
             const hist=clone(s);hist.visited=[];if(!auh5eEvidence(hist))throw Error('History-only Jing');
             const flags=clone(s);flags.visited=[];flags.history=[];if(auh5eEvidence(flags))throw Error('Flag-only Jing');
             for(const key of ['result','account','frontierResult']){const invalid=clone(s);invalid.militaryCareer.campaignEvidence.jing219[key]='invalid';if(auh5eEvidence(invalid))throw Error('Invalid record '+key);}
             const old=clone(config.seed);state=resolve(old);const before=JSON.stringify(state);militaryPanel();if(state.militaryCareer.campaignEvidence.jing219||JSON.stringify(state)!==before)throw Error('Legacy backfill');
             const future=clone(config.contact);future.militaryCareer.fieldPosition={year:222,proof:'later',active:true};auh5ePosition(future,true);auh5eRecord(future,'press');if(future.militaryCareer.fieldPosition.proof!=='later'||future.flags.m3_219_tactic)throw Error('Later post');
             const unknown=clone(config.seed);delete unknown.militaryCareer.combatService;if(SCENES.ch10_c58_07_jing_219.choices(unknown).some(o=>o.next==='m3_219_jing_contact'))throw Error('Unknown branch assignment');
             const late=clone(config.seed);late.storyClock.year=221;if(SCENES.ch10_c58_07_jing_219.choices(late).some(o=>o.next==='m3_219_jing_contact'))throw Error('Late assignment');
             const a=save,b=render,c=scrollTopNow;save=()=>{};render=()=>{};scrollTopNow=()=>{};
             try{for(let option=0;option<SCENES.ch10_06.choices(s).length;option++){
              state=clone(s);state.pageIndex=paginateStory(SCENES.ch10_06.body(state)).length-1;choose(option);if(state.scene!=='ch11_01'||state.storyClock.year!==220||state.age!==46||!validSave(state)||!auh5eEvidence(state))throw Error('220 estate exit');
             }}finally{save=a;render=b;scrollTopNow=c;}
            }""",{'seed':seeds[0],**runs[0]})
            # Full-history Private route: a parley broken by the chosen stroke,
            # household aftermath, retained family detours and the winter inquiry.
            page.evaluate('s=>{state=clone(s);activeTab="story";render();}',seeds[3]);clicks=0
            for index in (1,0,1):
                page.evaluate('()=>{state.pageIndex=paginateStory(SCENES[state.scene].body(state)).length-1;render();}')
                page.locator(f'[data-choice="{index}"]' if index else '[data-choice="0"], [data-action="next-scene"]').click();clicks+=1
            while page.evaluate('state.scene')!='ch10_06':
                assert clicks<18
                page.evaluate('()=>{state.pageIndex=paginateStory(SCENES[state.scene].body(state)).length-1;render();}')
                page.locator('[data-choice="0"], [data-action="next-scene"]').click();clicks+=1
            assert page.evaluate('state.militaryCareer.rank==="Private"&&state.flags.auh58_result==="frontier_disputed"&&auh5eEvidence(state)')
            page.reload();assert page.evaluate('state.militaryCareer.rank==="Private"&&auh5eEvidence(state)')
            page.locator('#menuToggle').click();page.locator('#gameMenu [data-nav="military"]').click();assert page.locator('[aria-label="Jing contact in 219"]').is_visible()
            assert page.evaluate('document.documentElement.scrollWidth<=innerWidth');assert not errors,errors
            result['checks'].append({'width':width,'routes_ten_organic_career_world_duty_seeds_two_branches':540,'nine_local_results_and_five_frontier_results':sorted(local),'five_choice_groups_all_pairs':'PASS','original_policy_inquiry_property_effects_parity':'PASS','six_legacy_major_nodes_full_parity':'PASS','marriage_market_tail_preserved':'PASS','no_rank_muster_staff_goods_civic_or_recruit_grants':'PASS','evidence_readonly_replay_negative_legacy_later_post':'PASS','all_property_exits_to_220':'PASS','reload_military_dom':'PASS','full_history_private_dom_clicks':clicks,'page_errors':errors});context.close()
    result['limits']='Ten selected organic career/world/duty seeds, both branches; Cavalry and legacy Major parity synthetic. All policy×tactic×aftermath and pairwise five local groups; not their full Cartesian product or all prior relationships. Matrix suppresses paint/storage and compacts history bodies; DOM full history. Hanzhong is sourced news, not direct attendance. No full X/XI/M3 or physical-device file:// certification.'
    write_report(result,args.report)
if __name__=='__main__':main()
