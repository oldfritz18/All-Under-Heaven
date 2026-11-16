#!/usr/bin/env python3
"""220–222 authority, actual field service and explicitly accepted warrants."""
import argparse
from copy import deepcopy
from pathlib import Path
from qa_support import fixture, write_report, HANZHONG_219_SCENES, COURT_224_SCENES, DESIGNATION_221_SCENES, SHU_ACCESSION_225_SCENES
from qa_m2_continuity import START
from qa_changban import ADVANCE
from qa_river_councils import TO_HANJIN
from qa_river_patrol import TO_FLOTILLA
from qa_red_cliffs import TO_ANCHORS
from qa_crossing210 import TO_TIDE
from qa_baxi216 import TO_BORDER
from qa_jing219 import TO_JING

BASELINE='0de1ac7:GAME/ALL_UNDER_HEAVEN_v0.4.99.5e_THE_DOWNSTREAM_APPROACH.html'
NEW={'m3_222_field_review','m3_222_after_review'}
TO_XI=r"""seed=>{
 state=clone(seed);activeTab='story';const a=save,b=render,c=scrollTopNow;save=()=>{};render=()=>{};scrollTopNow=()=>{};
 try{for(let i=0;i<45;i++){
  if(state.scene==='ch11_01')return clone(state);
  const sc=SCENES[state.scene];state.pageIndex=paginateStory(sc.body(state)).length-1;choose(0);if(sc.id===state.scene)throw Error('XI seed blocked '+sc.id+':'+banner);
 }throw Error('220 not reached');}finally{save=a;render=b;scrollTopNow=c;}
}"""
TO_FRONT=r"""config=>{
 state=clone(config.seed);activeTab='story';const a=save,b=render,c=scrollTopNow;save=()=>{};render=()=>{};scrollTopNow=()=>{};
 try{for(let i=0;i<45;i++){
  if(state.scene==='ch11_p60_05_eastern_front_222')return clone(state);
  const sc=SCENES[state.scene],index=sc.id==='ch11_p60_02_decree'?config.policy:sc.id==='ch11_p60_04_bridge_221'?config.travel:0;
  state.pageIndex=paginateStory(sc.body(state)).length-1;choose(index);if(sc.id===state.scene)throw Error('Eastern seed blocked '+sc.id+':'+banner);
 }throw Error('Eastern front not reached');}finally{save=a;render=b;scrollTopNow=c;}
}"""
ROUTES=r"""seed=>{
 const compact=clone(seed);for(const h of compact.history)h.body='';
 const a=save,b=render,c=scrollTopNow;save=()=>{};render=()=>{};scrollTopNow=()=>{};const rows=[];let review=null,example=null,order=null;
 const step=i=>{const sc=SCENES[state.scene];state.pageIndex=paginateStory(sc.body(state)).length-1;choose(i);if(state.scene===sc.id||!validSave(state))throw Error('Eastern route blocked '+sc.id+':'+banner);};
 try{for(const branch of ['Infantry','Cavalry'])for(let policy=0;policy<3;policy++)for(let travel=0;travel<3;travel++){
  state=clone(compact);activeTab='story';if(branch==='Cavalry'){
   state.militaryCareer.combatService={branch,unit:'Synthetic lawful mounted formation',commander:'Recorded field officer',year:220,proof:'legacy:lawful-cavalry'};
   for(const u of state.militaryCareer.units)if(u.active!==false){u.cavalry=state.militaryCareer.rank==='Sergeant'?20:30;u.infantry=0;}
  }
  const stageStart=clone(state);
  for(let i=0;i<45&&state.scene!=='ch11_p60_05_eastern_front_222';i++){
   const id=state.scene;step(id==='ch11_p60_02_decree'?policy:id==='ch11_p60_04_bridge_221'?travel:0);
  }
  if(state.scene!=='ch11_p60_05_eastern_front_222'||state.storyClock.year!==222||state.age!==48)throw Error('222 entry/calendar');
  for(const key of ['rank','units','appointmentHistory','staff','superior'])if(JSON.stringify(state.militaryCareer[key])!==JSON.stringify(stageStart.militaryCareer[key]))throw Error('Proposal awarded '+key);
  if(!auh63SocialPosition(state).position.startsWith(state.militaryCareer.rank+' / '))throw Error('Character proposal rank');
  const front=clone(state);
  for(let path=0;path<8;path++)for(let decision=0;decision<(path<6&&path%2===0?3:2);decision++){
   state=clone(front);const before=clone(state),mission=path<6?0:path===6?1:2;step(mission);order=clone(state);
   if(!state.militaryCareer.fieldPosition.active||state.militaryCareer.fieldPosition.proof!=='m3_5f:eastern222')throw Error('Issued eastern position');
   if(mission===0){step(Math.floor(path/2));if(!state.militaryCareer.fieldPosition.active)throw Error('Chosen role not active');step(path%2);if(state.militaryCareer.fieldPosition.active)throw Error('Clash not relieved');step(0);}
   step(0);if(state.scene!=='m3_222_field_review'||!auh5fEvidence(state)||state.militaryCareer.fieldPosition.active)throw Error('Eastern return evidence');
   const offered=auh5fOffer(state);if(!!offered!==(path<6&&path%2===0))throw Error('Warrant eligibility '+JSON.stringify({rank:before.militaryCareer.rank,branch,path,offer:offered,units:state.militaryCareer.units}));
   review=clone(state);step(decision);const accepted=path<6&&path%2===0&&decision===0;
   const expectedRank=accepted?offered.rank:before.militaryCareer.rank;
   if(state.militaryCareer.rank!==expectedRank)throw Error('Unaccepted rank');
   if(accepted){
    const active=state.militaryCareer.units.filter(u=>u.active!==false),foot=active.reduce((n,u)=>n+u.infantry,0),horse=active.reduce((n,u)=>n+u.cavalry,0);
    if(foot!==offered.infantry||horse!==offered.cavalry||active.length!==(['General','Major'].includes(offered.rank)?3:1)||active.some(u=>u.source!=='m3_222_field_review:accepted')||state.militaryCareer.appointmentHistory.length!==before.militaryCareer.appointmentHistory.length+1)throw Error('Warrant muster/double count');
    if(offered.rank==='General'&&(foot!==600||horse!==120||active.some(u=>u.rank!=='Major')||state.militaryCareer.legendaryGroup))throw Error('General brigade or free legendary honour');
   }else for(const key of ['rankProof','units','appointmentHistory','superior','commissionAuthority'])if(JSON.stringify(state.militaryCareer[key])!==JSON.stringify(before.militaryCareer[key]))throw Error('Refusal changed '+key);
   for(const key of ['coins','items','innerCircle','civicCareer','dragonGenerals'])if(JSON.stringify(state[key])!==JSON.stringify(before[key]))throw Error('Unchosen grant '+key);
   for(const key of ['staff','combatService'])if(JSON.stringify(state.militaryCareer[key])!==JSON.stringify(before.militaryCareer[key]))throw Error('Unchosen staff/branch '+key);
   if(!!state.flags.historical_meet_luxun!==(!!before.flags.historical_meet_luxun||mission===1))throw Error('Lu Xun acquaintance');
   const frozen=JSON.stringify(state);militaryPanel();civicPanel();npcMemories('xuwen');auh5fRecord(state);auh5fAccept(state);if(JSON.stringify(state)!==frozen)throw Error('Views/receipt/accept replay');
   if(!auh63SocialPosition(state).position.startsWith(expectedRank+' / '))throw Error('Character accepted/refused rank');
   step(0);for(let i=0;i<4&&['m3_222_standard','m3_222_command_lanes','m3_222_rider_at_the_bend','m3_222_first_return'].includes(state.scene);i++)step(0);if(state.scene!=='ch11_p60_07_meeting_222'||state.storyClock.year!==222||state.age!==48)throw Error('Meeting/clock');
   step(SCENES[state.scene].choices(state).findIndex(o=>o.next==='ch11_p60_08_turn_223'));
   if(state.storyClock.year!==223||state.age!==49||!auh5fEvidence(state))throw Error('223 personal exit');
   rows.push({rank:before.militaryCareer.rank,branch,policy,travel,path,decision,accepted,newRank:state.militaryCareer.rank,mission:state.flags.auh60_222});example=clone(state);
  }
 }return {rows,review,example,order};}finally{save=a;render=b;scrollTopNow=c;}
}"""
PROJECT=r"""s=>['ch11_p60_01_the_two_seals','ch11_p60_02_decree','ch11_p60_03_witnesses','ch11_p60_04_bridge_221','ch11_c73_03_counterseals_220','ch11_c73_04_the_messenger_cost_220','ch11_p60_05_eastern_front_222','ch11_p61_01_at_the_standard_222','ch11_p61_02_clash_222','ch11_p61_03_cost_of_command_222','ch11_p60_06_cost_222'].map(id=>({id,choices:SCENES[id].choices(s).map(o=>{
 const x=clone(s);o.effect?.(x);for(const k of ['m3_222_field_scope','m3_222_rankAtOrder','m3_222_branch'])delete x.flags[k];if(x.militaryCareer.campaignEvidence)delete x.militaryCareer.campaignEvidence.eastern222;delete x.militaryCareer.fieldPosition;x.journal=clone(s.journal);return {next:o.next==='m3_222_field_review'?'ch11_p60_07_meeting_222':o.next,state:x};
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
        tide += [base.evaluate(TO_TIDE,{'seed':weak if w=='north' else anchors[0],'world':w}) for w in ('north','separate')]
        border=[base.evaluate(TO_BORDER,s) for s in tide]
        jing=[base.evaluate(TO_JING,{'seed':s})['seed'] for s in border]
        jing.append(base.evaluate(TO_JING,{'seed':border[0],'west':True})['seed'])
        delegate=base.evaluate(TO_BORDER.replace('choose(0);',"choose(sc.id==='ch09_charter_hearing'?3:0);"),tide[3])
        jing.append(base.evaluate(TO_JING,{'seed':delegate})['seed'])
        seeds=[base.evaluate(TO_XI,s) for s in jing];assert seeds[7]['militaryCareer']['rank']=='Major'
        old_front=base.evaluate(TO_FRONT,{'seed':seeds[0],'policy':0,'travel':0})
        assert old_front['storyClock']['year']==221
        legacy=base.evaluate(r"""s=>{state=clone(s);activeTab='story';for(const i of [0,0,0]){const sc=SCENES[state.scene];state.pageIndex=paginateStory(sc.body(state)).length-1;choose(i);}return clone(state);}""",old_front)
        ids=base.evaluate('Object.keys(SCENES)');base.close()
        for width in (390,1280):
            context=browser.new_context(viewport={'width':width,'height':900});page=context.new_page();errors=[];page.on('pageerror',lambda e:errors.append(str(e)));page.goto(url+'/active.html')
            added=set(page.evaluate('Object.keys(SCENES)'))-set(ids)
            settlement={'m3_223_rolls','m3_223_ratification','m3_223_after_terms'}
            general={'m3_222_standard','m3_222_command_lanes','m3_222_rider_at_the_bend','m3_222_first_return'}
            assert added in (NEW,NEW|settlement,NEW|settlement|general,NEW|settlement|general|HANZHONG_219_SCENES,NEW|settlement|general|HANZHONG_219_SCENES|COURT_224_SCENES,NEW|settlement|general|HANZHONG_219_SCENES|COURT_224_SCENES|DESIGNATION_221_SCENES,NEW|settlement|general|HANZHONG_219_SCENES|COURT_224_SCENES|DESIGNATION_221_SCENES|SHU_ACCESSION_225_SCENES),added-NEW
            runs=[page.evaluate(ROUTES,s) for s in seeds]
            assert sum(len(r['rows']) for r in runs)==3078
            assert {r['newRank'] for run in runs for r in run['rows']}=={'Private','Sergeant','Captain','Major','General'}
            assert all(r['newRank']!='Major' for r in runs[4]['rows'])  # Captain without a company.
            new_front=page.evaluate(TO_FRONT,{'seed':seeds[0],'policy':0,'travel':0})
            assert new_front['storyClock']['year']==222 and new_front['age']==old_front['age']+1
            base=context.new_page();base.goto(url+'/baseline.html');assert page.evaluate(PROJECT,new_front)==base.evaluate(PROJECT,new_front)
            high=deepcopy(new_front);high['militaryCareer']['rank']='Major';high['flags'].pop('m3_215_frontier_scope',None)
            high_test=r"""s=>['ch11_p60_01_the_two_seals','ch11_p60_02_decree','ch11_p60_03_witnesses','ch11_p60_04_bridge_221','ch11_p60_05_eastern_front_222','ch11_p61_01_at_the_standard_222','ch11_p61_02_clash_222','ch11_p61_03_cost_of_command_222','ch11_p60_06_cost_222'].map(id=>({id,body:SCENES[id].body(s),choices:SCENES[id].choices(s).map(o=>{const x=clone(s);o.effect?.(x);return {label:o.label,next:o.next,state:x};})}))"""
            assert page.evaluate(high_test,high)==base.evaluate(high_test,high)
            sample=runs[7]['example'];tail=r"""s=>SCENES.ch11_p60_07_meeting_222.body(s).replace(/<p>[\s\S]*?<\/p>/,'').replace(/<p>The first movement account under your General warrant[\s\S]*?<\/p>/,'')"""
            assert page.evaluate(tail,sample)==base.evaluate(tail,sample);base.close()
            page.evaluate(r"""config=>{
             const old=resolve(clone(config.legacy));state=old;const frozen=JSON.stringify(state);militaryPanel();SCENES.ch11_p61_03_cost_of_command_222.body(state);if(state.storyClock.year!==221||state.age!==47||state.militaryCareer.campaignEvidence.eastern222||JSON.stringify(state)!==frozen)throw Error('Legacy age/backfill');
             const hist=clone(config.example);hist.visited=[];if(!auh5fEvidence(hist))throw Error('History-only eastern');
             const flags=clone(config.example);flags.visited=[];flags.history=[];if(auh5fEvidence(flags)||auh5fOffer(flags))throw Error('Flag-only eastern');
             const invalid=clone(config.example);invalid.militaryCareer.campaignEvidence.eastern222.account='invented';if(auh5fEvidence(invalid))throw Error('Invalid account');
             const future=clone(config.order);future.militaryCareer.fieldPosition={year:224,active:true,proof:'later'};auh5fPosition(future,'wrong',true,true);if(future.militaryCareer.fieldPosition.proof!=='later')throw Error('Later post');
             const a=save,b=render,c=scrollTopNow;save=()=>{};render=()=>{};scrollTopNow=()=>{};
             try{
              const older=clone(config.start);older.age=62;state=older;
              for(let i=0;state.scene!=='ch11_p60_05_eastern_front_222'&&i<45;i++){const sc=SCENES[state.scene];state.pageIndex=paginateStory(sc.body(state)).length-1;choose(0);}
              if(state.age!==64||state.storyClock.year!==222)throw Error('Original starting age reset');
              state=clone(config.front);delete state.militaryCareer.combatService;state.pageIndex=paginateStory(SCENES[state.scene].body(state)).length-1;choose(0);if(state.militaryCareer.fieldPosition.proof==='m3_5f:eastern222')throw Error('Unknown branch order');
             }finally{save=a;render=b;scrollTopNow=c;}
            }""",{'legacy':legacy,'start':seeds[0],'front':new_front,**runs[7]})
            # Organic Major path and real UI acceptance, with full history.
            page.evaluate('s=>{state=clone(s);activeTab="story";render();}',seeds[7]);clicks=0
            while page.evaluate('state.scene')!='m3_222_field_review':
                assert clicks<45
                page.evaluate('()=>{state.pageIndex=paginateStory(SCENES[state.scene].body(state)).length-1;render();}')
                page.locator('[data-choice="0"], [data-action="next-scene"]').click();clicks+=1
            assert page.evaluate('auh5fOffer(state)?.rank==="General"')
            page.evaluate(r"""()=>{
             const good=clone(state);if(!auh5fOffer(good))throw Error('Good General offer');
             const bad=clone(good);bad.militaryCareer.units.find(u=>u.active!==false).source='unknown';if(auh5fOffer(bad))throw Error('Unknown muster source');
             const past=clone(good);delete past.militaryCareer.campaignEvidence.jing219;if(auh5fOffer(past))throw Error('Missing prior merits');
             const unknown=clone(good);delete unknown.militaryCareer.combatService;if(auh5fOffer(unknown))throw Error('Unknown branch warrant');
            }""")
            page.evaluate('()=>{state.pageIndex=paginateStory(SCENES[state.scene].body(state)).length-1;render();}')
            page.locator('[data-choice="0"]').click();clicks+=1
            assert page.evaluate('state.militaryCareer.rank==="General"&&auh5fEvidence(state)&&validSave(state)&&auhStoryUIRecordedUnits(state).reduce((n,u)=>n+u[1]+u[2]+u[3],0)===720')
            page.reload();assert page.evaluate('state.militaryCareer.rank==="General"&&auh5fEvidence(state)')
            page.locator('#menuToggle').click();page.locator('#gameMenu [data-nav="military"]').click();assert page.locator('[aria-label="Eastern service in 222"]').is_visible()
            assert page.evaluate('document.documentElement.scrollWidth<=innerWidth');assert not errors,errors
            result['checks'].append({'width':width,'routes_nine_organic_career_world_charter_seeds_two_branches':3078,'all_three_220_proposals_and_221_requests_eight_mission_role_outcomes':'PASS','explicit_warrants_refusal_pending_and_exact_muster':'PASS','general_combined_arms_no_legendary_or_staff_grants':'PASS','captain_without_company_assignment_only':'PASS','222_entry_and_legacy_age_header_no_backfill':'PASS','original_effects_and_nine_legacy_major_nodes_parity':'PASS','character_rank_and_preserved_personal_tail':'PASS','provenance_readonly_replay_unknown_source_later_post':'PASS','reload_military_dom':'PASS','organic_major_to_general_dom_clicks':clicks,'page_errors':errors});context.close()
    result['limits']='Nine selected organic career/world/charter seeds; Cavalry and legacy Major parity synthetic. Full local 3×3 proposals/travel, six raid role/action paths plus parley/shelter, available accept/refuse/defer. Not all earlier relationships/world products, entire XI/223/M3, or physical-device file://. Matrix suppresses paint/storage and compacts history bodies; DOM full history.'
    write_report(result,args.report)
if __name__=='__main__':main()
