#!/usr/bin/env python3
"""Fire assault, four world results, witnessed company service and 209 offers."""
import argparse
from copy import deepcopy
from pathlib import Path
from qa_support import fixture, write_report
from qa_m2_continuity import START
from qa_changban import ADVANCE
from qa_river_councils import TO_HANJIN
from qa_river_patrol import TO_FLOTILLA

BASELINE='2523c7e:GAME/ALL_UNDER_HEAVEN_v0.4.99.4y_THE_ASSIGNED_RIVER_PATROL.html'
TO_ANCHORS=r"""config=>{
 state=clone(config.seed);activeTab='story';
 const weak=['ch08_rc54_council','ch08_shu56_kongming_warroom','ch08_rc54_scout','ch08_shu56_zhangfei_shore','ch08_rc54_southern_dispute'];
 for(let i=0;i<55;i++){
  if(state.scene==='ch08_rc54_anchors')return clone(state);
  const sc=SCENES[state.scene];state.pageIndex=paginateStory(sc.body(state)).length-1;choose(config.weak&&weak.includes(sc.id)?2:0);
  if(sc.id===state.scene)throw Error('Baseline preparation blocked: '+sc.id+':'+banner);
 }throw Error('Fire anchors not reached');
}"""
ROUTES=r"""config=>{
 const compact=clone(config.seed);for(const h of compact.history)h.body='';
 const realSave=save,realRender=render,realScroll=scrollTopNow;save=()=>{};render=()=>{};scrollTopNow=()=>{};
 const ids=['ch08_rc54_letters','ch08_rc54_wind','ch08_player_river_battle','ch08_shu56_zhaoyun_flameline','ch08_rc54_choice_of_fire','ch08_rc54_pursuit','ch08_shu56_liubei_settlement','ch08_player_battle_result','ch08_06'];
 const vectors=[[1,0,0],[0,1,0],[0,0,1],[1,1,0],[1,2,0],[1,0,1],[1,0,2],[0,1,1],[0,1,2]],rows=[];
 const verify=typeof auh4zEvidence==='function';let offerSnapshot=null;
 try{
 for(const branch of config.branches||['Infantry','Cavalry'])for(let a=0;a<3;a++)for(let b=0;b<3;b++)for(let c=0;c<3;c++){
  state=clone(compact);activeTab='story';if(branch==='Cavalry'){state.militaryCareer.combatService={branch,unit:'Legacy mounted section',commander:'Recorded officer',year:208,proof:'legacy:lawful-cavalry'};state.militaryCareer.fieldPosition.formation='cavalry serving dismounted in the assigned deck file';}
  const before=clone(state),selected={};let exit=-1;
  for(let step=0;step<60;step++){
   if(state.scene==='ch09_01')break;
   const sc=SCENES[state.scene],col=ids.indexOf(sc.id),index=col<0?0:(vectors[col][0]*a+vectors[col][1]*b+vectors[col][2]*c)%3;
   if(col>=0)selected[sc.id]=index;
   if(sc.id==='ch08_06'){exit=index;offerSnapshot=clone(state);}
   const body=sc.body(state);state.pageIndex=paginateStory(body).length-1;choose(index);
   if(!validSave(state)||state.scene===sc.id)throw Error('Fire route blocked '+sc.id+':'+banner);
   if(sc.id!=='ch08_06'&&state.militaryCareer.rank!==before.militaryCareer.rank)throw Error('Unchosen promotion');
   if(sc.id==='ch08_rc54_morning'){
    if(state.storyClock.year!==209||state.age!==35||state.militaryCareer.fieldPosition.active)throw Error('Morning date/position');
    if(verify&&!auh4zEvidence(state))throw Error('Missing battle receipt');
   }
  }
  if(state.scene!=='ch09_01'||state.storyClock.year!==210||state.age!==36||Object.keys(selected).length!==9)throw Error('Incomplete battle/settlement');
  const promoted=before.militaryCareer.rank==='Sergeant'&&exit===0;
  if(state.militaryCareer.rank!==(promoted?'Captain':before.militaryCareer.rank))throw Error('Wrong commission outcome');
  if(state.militaryCareer.appointmentHistory.length!==before.militaryCareer.appointmentHistory.length+(promoted?1:0))throw Error('Duplicate commission');
  if(verify&&promoted&&state.militaryCareer.units.some(u=>['road-watch-201','m3-208-issued-company'].includes(u.id)&&u.rank!=='Captain'&&u.active!==false))throw Error('Old watch still counted');
  if(!promoted&&JSON.stringify(state.militaryCareer.units)!==JSON.stringify(before.militaryCareer.units))throw Error('Unchosen muster change');
  for(const key of ['staff','combatService'])if(JSON.stringify(state.militaryCareer[key])!==JSON.stringify(before.militaryCareer[key]))throw Error('Military grant '+key);
  for(const key of ['coins','items','innerCircle'])if(JSON.stringify(state[key])!==JSON.stringify(before[key]))throw Error('Goods/recruit grant');
  if(verify){
   const e=state.militaryCareer.campaignEvidence.redCliffs208;if(!auh4zEvidence(state)||e.rank!==before.militaryCareer.rank||e.branch!==branch)throw Error('Wrong receipt provenance');
   const once=JSON.stringify(state);militaryPanel();npcMemories('hansheng');auh4zRecord(state);if(JSON.stringify(state)!==once)throw Error('View/record not idempotent');
   if(auh63SocialPosition(state).position.includes('River campaign commander'))throw Error('Character invented fleet');
   if(SCENES.ch09_01.body(state).includes('Your disputed separate command still attracts'))throw Error('Unissued mandate callback');
  }
  rows.push({branch,a,b,c,selected,result:state.flags.auh54_war_result,leverage:state.flags.auh54_leverage,cost:state.flags.auh54_cost,rank:state.militaryCareer.rank,year:state.storyClock.year,age:state.age});
 }
 return {rows,example:clone(state),offer:offerSnapshot};
 }finally{save=realSave;render=realRender;scrollTopNow=realScroll;}
}"""

def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--report',type=Path);args=parser.parse_args()
    with fixture(BASELINE) as (browser,url,result):
        base=browser.new_page();base.goto(url+'/baseline.html')
        initial=[base.evaluate(START,d) for d in (False,True)]
        starts=[base.evaluate(ADVANCE,{'seed':s['snapshots']['ch08_pb55_xushu'],'decision':d}) for s in initial for d in (0,1)]
        hanjin=[base.evaluate(TO_HANJIN,s) for s in starts];flotillas=[base.evaluate(TO_FLOTILLA,s) for s in hanjin]
        strong=[base.evaluate(TO_ANCHORS,{'seed':s,'weak':False}) for s in flotillas]
        weak=[base.evaluate(TO_ANCHORS,{'seed':flotillas[i],'weak':True}) for i in (0,3)]
        baseline_rows=[base.evaluate(ROUTES,{'seed':s,'branches':['Infantry']})['rows'] for s in (strong[0],weak[1])];base.close()
        for width in (390,1280):
            context=browser.new_context(viewport={'width':width,'height':900});page=context.new_page();errors=[];page.on('pageerror',lambda e:errors.append(str(e)));page.goto(url+'/active.html')
            assert set(initial[0]['ids']).issubset(page.evaluate('Object.keys(SCENES)'))
            runs=[page.evaluate(ROUTES,{'seed':s}) for s in strong+weak];assert sum(len(r['rows']) for r in runs)==324
            observed={r['result'] for run in runs for r in run['rows']};assert observed=={'southern_breakthrough','contested_river','northern_foothold','independent_command'},observed
            for old,current in zip(baseline_rows,(runs[0],runs[5])):assert old==[r for r in current['rows'] if r['branch']=='Infantry']
            rowset=runs[0]['rows'][:27];ids=list(rowset[0]['selected'])
            for i,left in enumerate(ids):
                for right in ids[i+1:]:assert len({(r['selected'][left],r['selected'][right]) for r in rowset})==9
            page.evaluate(r"""seed=>{
             state=clone(seed);const h=clone(state);h.visited=[];if(!auh4zEvidence(h))throw Error('History-only battle');
             const missing=clone(state);missing.visited=[];missing.history=[];if(auh4zEvidence(missing))throw Error('Flag-only battle');delete missing.militaryCareer.campaignEvidence.redCliffs208;auh4zRecord(missing);if(missing.militaryCareer.campaignEvidence.redCliffs208)throw Error('Retroactive record');
             const invalid=clone(state);invalid.militaryCareer.campaignEvidence.redCliffs208.action='__proto__';if(auh4zEvidence(invalid))throw Error('Invalid action accepted');
             const later=clone(state);later.militaryCareer.fieldPosition={year:214,proof:'later',active:true};if(!auh4zEvidence(later))throw Error('Later position erased past evidence');
             const sgt=clone(state);sgt.militaryCareer.rank='Sergeant';delete sgt.militaryCareer.campaignEvidence.redCliffs208;sgt.scene='ch08_06';const before=clone(sgt);SCENES.ch08_06.choices(sgt)[0].effect(sgt);auhStoryUIChoice(sgt,before,'ch08_06',0);if(sgt.militaryCareer.rank!=='Sergeant')throw Error('Unwitnessed new offer promoted');
             localStorage.setItem(SAVE_KEY,JSON.stringify(state));handleAction('load-original');
            }""",runs[0]['example']);page.reload();assert page.evaluate('validSave(state)&&auh4zEvidence(state)')
            page.locator('#menuToggle').click();page.locator('#gameMenu [data-nav="military"]').click();assert page.locator('[aria-label="Witnessed Red Cliffs service"]').is_visible();assert page.evaluate('document.documentElement.scrollWidth<=innerWidth')
            # No retroactive receipt on a real 4y post-battle save. Its existing
            # Sergeant offer remains accepted only by the explicit field choice.
            base=context.new_page();base.goto(url+'/baseline.html');old_route=base.evaluate(ROUTES,{'seed':strong[1],'branches':['Infantry']});base.close()
            page.evaluate(r"""saved=>{
             state=resolve(clone(saved.example));if(auh4zEvidence(state)||state.militaryCareer.campaignEvidence.redCliffs208)throw Error('Legacy receipt backfill');
             state=resolve(clone(saved.offer));if(state.militaryCareer.rank!=='Sergeant')throw Error('Invalid legacy offer fixture');const before=clone(state);const o=SCENES.ch08_06.choices(state)[0];if(!o.label.includes('Accept the written'))throw Error('Legacy offer label');o.effect(state);auhStoryUIChoice(state,before,'ch08_06',0);if(state.militaryCareer.rank!=='Captain')throw Error('Legacy offer removed');
            }""",old_route)
            # Synthetic older-order resume: the accepted real watch/warrant is
            # retained, but no 4x/4y order proof is available. Play the new battle
            # normally; preserve its old review offer without inventing receipt.
            page.evaluate(r"""seed=>{
             state=clone(seed);for(const h of state.history)h.body='';
             state.militaryCareer.fieldPosition={year:191,proof:'pan_05:front',active:false};delete state.flags.m3_208_embarked;
             const realSave=save,realRender=render,realScroll=scrollTopNow;save=()=>{};render=()=>{};scrollTopNow=()=>{};
             const step=()=>{const sc=SCENES[state.scene];state.pageIndex=paginateStory(sc.body(state)).length-1;choose(0);if(sc.id===state.scene)throw Error('Legacy resume blocked');};
             try{
              for(let i=0;i<50&&state.scene!=='ch08_06';i++)step();
              if(state.scene!=='ch08_06'||auh4zEvidence(state)||state.militaryCareer.campaignEvidence.redCliffs208||!auh4zCaptainEligible(state))throw Error('Legacy resume offer/receipt');
              if(!SCENES.ch08_06.choices(state)[0].label.includes('Accept the written'))throw Error('Legacy resume acceptance hidden');step();
              if(state.militaryCareer.rank!=='Captain'||state.militaryCareer.units.some(u=>u.id==='road-watch-201'&&u.active!==false))throw Error('Legacy resume commission/muster');
             }finally{save=realSave;render=realRender;scrollTopNow=realScroll;}
            }""",strong[1])
            page.evaluate('s=>{state=clone(s);activeTab="story";render();}',strong[3]);clicks=0
            while page.evaluate('state.scene!=="ch09_01"'):
                page.evaluate('()=>{state.pageIndex=paginateStory(SCENES[state.scene].body(state)).length-1;render();}')
                page.locator('[data-choice="0"], [data-action="next-scene"]').click();clicks+=1;assert clicks<60
            assert page.evaluate('state.militaryCareer.rank==="Private"&&auh4zEvidence(state)&&state.storyClock.year===210')
            assert not errors,errors
            result['checks'].append({'width':width,'routes_four_careers_two_branches_and_two_weak_preparations':324,
                'nine_choice_groups_all_pairs':'PASS','four_world_outcomes':sorted(observed),'original_calculation_and_two_route_matrices_parity':'PASS',
                '209_explicit_accept_and_refusal_no_duplicate_muster':'PASS','no_other_grants':'PASS','provenance_idempotence_readonly_and_later_post':'PASS',
                'legacy_save_no_backfill_and_offer_preserved':'PASS','synthetic_midarc_legacy_order_resume':'PASS','reload_military_dom':'PASS','full_history_private_dom_clicks':clicks,'page_errors':errors});context.close()
    result['limits']='Fire assault/settlement company paths through 210; pairwise nine 3-way groups, not full Cartesian product. Two legacy outcome matrices compared; higher-command prose uses fallback. Cavalry synthetic; no physical-device file:// or full M3 certification. Chapter labels remain to reconcile.'
    write_report(result,args.report)
if __name__=='__main__':main()
