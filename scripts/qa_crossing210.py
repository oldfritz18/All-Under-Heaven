#!/usr/bin/env python3
"""All local crossing choices, eight replies, actual task evidence and legacy."""
import argparse
from copy import deepcopy
from pathlib import Path
from qa_support import fixture, write_report, normalize_chapter_headers
from qa_m2_continuity import START
from qa_changban import ADVANCE
from qa_river_councils import TO_HANJIN
from qa_river_patrol import TO_FLOTILLA
from qa_red_cliffs import TO_ANCHORS

BASELINE='300ebb3:GAME/ALL_UNDER_HEAVEN_v0.4.99.5a_CHAPTERS_VIII_IX_X_RECONCILED.html'
TO_TIDE=r"""config=>{
 state=clone(config.seed);activeTab='story';
 const fire={ch08_rc54_letters:config.world==='south'||config.world==='separate'?0:2,ch08_rc54_wind:config.world==='south'||config.world==='separate'?0:2,ch08_player_river_battle:config.world==='south'||config.world==='separate'?2:1,ch08_rc54_choice_of_fire:config.world==='south'?0:config.world==='contested'?2:1,ch08_rc54_pursuit:1,ch08_06:1};
 const realSave=save,realRender=render,realScroll=scrollTopNow;save=()=>{};render=()=>{};scrollTopNow=()=>{};
 try{for(let i=0;i<70;i++){
  if(state.scene==='ch09_p57_01_tide')return clone(state);
  const sc=SCENES[state.scene];state.pageIndex=paginateStory(sc.body(state)).length-1;choose(fire[sc.id]??0);if(sc.id===state.scene)throw Error('210 seed blocked '+sc.id);
 }throw Error('210 tide not reached');}finally{save=realSave;render=realRender;scrollTopNow=realScroll;}
}"""
ROUTES=r"""seed=>{
 const compact=clone(seed);for(const h of compact.history)h.body='';const verify=typeof auh5bEvidence==='function';
 const realSave=save,realRender=render,realScroll=scrollTopNow;save=()=>{};render=()=>{};scrollTopNow=()=>{};
 const rows=[];try{
 for(const branch of ['Infantry','Cavalry'])for(let testimony=0;testimony<3;testimony++)for(let policy=0;policy<4;policy++)for(let action=0;action<3;action++){
  state=clone(compact);activeTab='story';if(branch==='Cavalry')state.militaryCareer.combatService={branch,unit:'Legacy mounted section',commander:'Recorded officer',year:210,proof:'legacy:lawful-cavalry'};
  const before=clone(state),picks={ch09_p57_02_testimony:testimony,ch09_p57_04_terms:policy,ch09_p57_06_landing:action};let done=false;
  for(let i=0;i<24;i++){
   const sc=SCENES[state.scene];state.pageIndex=paginateStory(sc.body(state)).length-1;choose(picks[sc.id]??0);
   if(state.scene===sc.id||!validSave(state))throw Error('210 route blocked '+sc.id+':'+banner);
   if(state.storyClock.year!==210||state.age!==36)throw Error('210 clock');
   if(verify&&['ch09_p57_05_scouts','ch09_p57_06_landing'].includes(sc.id)&&!state.militaryCareer.fieldPosition.active)throw Error('No active local order');
   if(verify&&sc.id==='ch09_p57_07_verdict'&&state.militaryCareer.fieldPosition.active)throw Error('Order active after relief');
   if(sc.id==='ch09_p57_09_depart'){done=true;break;}
  }
  if(!done)throw Error('210 departure not reached');
  for(const key of ['rank','rankProof','units','appointmentHistory','staff','superior','combatService'])if(JSON.stringify(state.militaryCareer[key])!==JSON.stringify(before.militaryCareer[key]))throw Error('Unchosen military change '+key);
  for(const key of ['coins','items','innerCircle','civicCareer'])if(JSON.stringify(state[key])!==JSON.stringify(before[key]))throw Error('Unchosen grant '+key);
  if(verify){
   if(!auh5bEvidence(state))throw Error('Missing crossing evidence');
   const e=state.militaryCareer.campaignEvidence.crossing210;if(e.rank!==before.militaryCareer.rank||e.branch!==branch||e.action!==['hold','negotiate','evacuate'][action]||e.policy!==['liu','independent','north','civil'][policy])throw Error('Wrong evidence');
   const once=JSON.stringify(state);militaryPanel();civicPanel();npcMemories('xuwen');auh5bRecord(state);if(JSON.stringify(state)!==once)throw Error('View/record mutation');
   if(!auh63SocialPosition(state).position.includes('local crossing'))throw Error('Character scope');
  }
  rows.push({rank:before.militaryCareer.rank,world:before.flags.auh54_war_result,branch,testimony,policy,action,result:state.flags.auh57_result});
 }return {rows,example:clone(state)};}finally{save=realSave;render=realRender;scrollTopNow=realScroll;}
}"""
PROJECT=r"""s=>['ch09_p57_01_tide','ch09_p57_02_testimony','ch09_p57_03_letters','ch09_p57_04_terms','ch09_p57_05_scouts','ch09_p57_06_landing','ch09_p57_07_verdict','ch09_p57_08_council','ch09_p57_09_depart'].map(id=>({id,choices:SCENES[id].choices(s).map(o=>{const x=clone(s);o.effect(x);delete x.flags.m3_210_scope;delete x.militaryCareer.fieldPosition;if(x.militaryCareer.campaignEvidence)delete x.militaryCareer.campaignEvidence.crossing210;x.journal=clone(s.journal);return {next:o.next,state:x};})}))"""

def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--report',type=Path);args=parser.parse_args()
    with fixture(BASELINE) as (browser,url,result):
        base=browser.new_page();base.goto(url+'/baseline.html')
        initial=[base.evaluate(START,d) for d in (False,True)]
        starts=[base.evaluate(ADVANCE,{'seed':s['snapshots']['ch08_pb55_xushu'],'decision':d}) for s in initial for d in (0,1)]
        hanjin=[base.evaluate(TO_HANJIN,s) for s in starts];flotillas=[base.evaluate(TO_FLOTILLA,s) for s in hanjin]
        strong=[base.evaluate(TO_ANCHORS,{'seed':s,'weak':False}) for s in flotillas]
        weak=base.evaluate(TO_ANCHORS,{'seed':flotillas[0],'weak':True})
        seeds=[base.evaluate(TO_TIDE,{'seed':strong[0] if world!='north' else weak,'world':world}) for world in ('south','separate','contested','north')]
        seeds += [base.evaluate(TO_TIDE,{'seed':strong[i],'world':'south'}) for i in (1,2,3)]
        assert {s['flags']['auh54_war_result'] for s in seeds}=={'southern_breakthrough','independent_command','contested_river','northern_foothold'}
        expected=base.evaluate(ROUTES,seeds[0])['rows'];old_save=base.evaluate(ROUTES,seeds[-1])['example'];base.close()
        for width in (390,1280):
            context=browser.new_context(viewport={'width':width,'height':900});page=context.new_page();errors=[];page.on('pageerror',lambda e:errors.append(str(e)));page.goto(url+'/active.html')
            assert set(initial[0]['ids']).issubset(page.evaluate('Object.keys(SCENES)'))
            runs=[page.evaluate(ROUTES,s) for s in seeds];assert sum(len(r['rows']) for r in runs)==504
            outcomes={r['result'] for run in runs for r in run['rows']};assert len(outcomes)==8,outcomes
            assert runs[0]['rows']==expected
            base=context.new_page();base.goto(url+'/baseline.html');assert page.evaluate(PROJECT,seeds[0])==base.evaluate(PROJECT,seeds[0])
            major=deepcopy(seeds[0]);major['militaryCareer']['rank']='Major'
            high=r"""s=>Object.keys(SCENES).filter(id=>/^ch09_p57_/.test(id)).map(id=>({id,body:SCENES[id].body(s),choices:SCENES[id].choices(s).map(o=>{const x=clone(s);o.effect(x);return {label:o.label,next:o.next,state:x};})}))"""
            assert normalize_chapter_headers(page.evaluate(high,major))==normalize_chapter_headers(base.evaluate(high,major));base.close()
            page.evaluate(r"""seed=>{
             state=clone(seed);const history=clone(state);history.visited=[];if(!auh5bEvidence(history))throw Error('History-only lost');
             const invalid=clone(state);invalid.militaryCareer.campaignEvidence.crossing210.action='__proto__';if(auh5bEvidence(invalid))throw Error('Invalid enum');
             const empty=clone(state);empty.visited=[];empty.history=[];if(auh5bEvidence(empty))throw Error('Flag-only evidence');delete empty.militaryCareer.campaignEvidence.crossing210;auh5bRecord(empty);if(empty.militaryCareer.campaignEvidence.crossing210)throw Error('Retroactive record');
             const later=clone(state);later.militaryCareer.fieldPosition={year:214,proof:'later-post',active:true};auh5bPosition(later,'return',false);if(later.militaryCareer.fieldPosition.proof!=='later-post'||!later.militaryCareer.fieldPosition.active||!auh5bEvidence(later))throw Error('Later posting/past evidence');
             const unknown=clone(state);delete unknown.militaryCareer.combatService;delete unknown.militaryCareer.campaignEvidence.crossing210;auh5bRecord(unknown);if(unknown.militaryCareer.campaignEvidence.crossing210)throw Error('Unknown branch credit');
             localStorage.setItem(SAVE_KEY,JSON.stringify(state));handleAction('load-original');
            }""",runs[0]['example']);page.reload();assert page.evaluate('validSave(state)&&auh5bEvidence(state)')
            page.locator('#menuToggle').click();page.locator('#gameMenu [data-nav="military"]').click();assert page.locator('[aria-label="Witnessed crossing terms in 210"]').is_visible();assert page.evaluate('document.documentElement.scrollWidth<=innerWidth')
            page.evaluate('s=>{state=resolve(clone(s));const saved=JSON.stringify(state);militaryPanel();if(auh5bEvidence(state)||state.militaryCareer.campaignEvidence.crossing210||JSON.stringify(state)!==saved)throw Error("Legacy backfill");}',old_save)
            page.evaluate('s=>{state=clone(s);activeTab="story";render();}',seeds[-1]);clicks=0
            while not page.evaluate('auh5bEvidence(state)&&state.scene!=="ch09_p57_09_depart"'):
                page.evaluate('()=>{state.pageIndex=paginateStory(SCENES[state.scene].body(state)).length-1;render();}')
                page.locator('[data-choice="0"], [data-action="next-scene"]').click();clicks+=1;assert clicks<25
            assert page.evaluate('state.militaryCareer.rank==="Private"&&state.storyClock.year===210')
            assert not errors,errors
            result['checks'].append({'width':width,'all_local_routes_seven_organic_career_world_seeds_two_branches':504,
                'eight_replies':sorted(outcomes),'existing_effects_and_one_full_reply_matrix_parity':'PASS','nine_major_nodes_full_parity':'PASS',
                'no_rank_muster_staff_goods_civic_office_or_recruit_grants':'PASS','issued_position_and_relief':'PASS',
                'evidence_idempotence_readonly_provenance_and_legacy_no_backfill':'PASS','reload_military_dom':'PASS','full_history_private_dom_clicks':clicks,'page_errors':errors});context.close()
    result['limits']='All local 3×4×3 choices on seven selected organic career/world seeds, both branches; Cavalry/Major synthetic. Not the full world×rank product or 211–219 audit. Matrix compacts history bodies/suppresses paint/storage; DOM uses full history. No physical-device file:// certification.'
    write_report(result,args.report)
if __name__=='__main__':main()
