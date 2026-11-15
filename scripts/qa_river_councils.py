#!/usr/bin/env python3
"""Pairwise river proposals, active muster, knowledge and Character/Military."""
import argparse
from copy import deepcopy
from pathlib import Path
from qa_support import fixture, write_report, normalize_chapter_headers
from qa_m2_continuity import START
from qa_changban import ADVANCE

BASELINE = '3664d6d:GAME/ALL_UNDER_HEAVEN_v0.4.99.4w_CHANGBAN_THE_RECEIVING_LINE.html'
TO_HANJIN = r"""seed=>{
 state=clone(seed);activeTab='story';for(let i=0;i<20;i++){
  if(state.scene==='ch08_c72_01_guanyu_council')return clone(state);
  const sc=SCENES[state.scene];state.pageIndex=paginateStory(sc.body(state)).length-1;choose(0);
  if(sc.id===state.scene)throw Error('Baseline retreat blocked');
 }throw Error('Hanjin not reached');
}"""
ROUTES = r"""seed=>{
 const compact=clone(seed);for(const h of compact.history)h.body='';
 const realSave=save,realRender=render,realScroll=scrollTopNow;save=()=>{};render=()=>{};scrollTopNow=()=>{};
 const ids=['ch08_c72_01_guanyu_council','ch08_c72_02_shore_witnesses','ch08_pb55_liuqi_council','ch08_shu56_zhugeliang_terms','ch08_zhugeliang_ledger','ch08_lusu_quay','lc81_208_four_courts','ch08_c72_04_eastern_conditions','p86_208_pilots_and_seals','ch08_alliance_register','ch08_player_council'];
 const vectors=[[1,0,0],[0,1,0],[0,0,1],[1,1,0],[1,2,0],[1,0,1],[1,0,2],[0,1,1],[0,1,2],[1,1,1],[1,1,2]],rows=[];
 try{
 for(const branch of ['Infantry','Cavalry'])for(let a=0;a<3;a++)for(let b=0;b<3;b++)for(let c=0;c<3;c++){
  state=clone(compact);activeTab='story';if(branch==='Cavalry')state.militaryCareer.combatService={branch,unit:'Legacy cavalry section',commander:'Recorded officer',year:208,proof:'legacy:lawful-cavalry'};
  const before=clone(state),selected={};
  for(let step=0;step<45;step++){
   if(state.scene==='ch08_rc54_flotilla')break;
   const sc=SCENES[state.scene],column=ids.indexOf(sc.id),options=sc.choices(state),index=column<0?0:((vectors[column][0]*a+vectors[column][1]*b+vectors[column][2]*c)%3)%options.length;
   if(column>=0)selected[sc.id]=index;
   const body=sc.body(state);if(sc.id==='ch08_c72_02_shore_witnesses'&&(body.includes('Your hired craft')||body.includes('Your quartermaster')))throw Error('Phantom boat/staff');
   state.pageIndex=paginateStory(body).length-1;choose(index);
   if(!validSave(state)||state.scene===sc.id)throw Error('Council blocked '+sc.id+':'+banner);
   if(state.storyClock.year!==208||state.age!==34)throw Error('Council date');
  }
  if(state.scene!=='ch08_rc54_flotilla'||Object.keys(selected).length!==11)throw Error('Incomplete council path');
  for(const key of ['rank','rankProof','units','appointmentHistory','staff','superior','combatService'])if(JSON.stringify(state.militaryCareer[key])!==JSON.stringify(before.militaryCareer[key]))throw Error('Unchosen military change '+key);
  for(const key of ['coins','items','innerCircle'])if(JSON.stringify(state[key])!==JSON.stringify(before[key]))throw Error('Unchosen goods/recruit');
  if(state.flags.m3_208_river_scope!=='company'||!state.militaryCareer.fieldPosition.active||!(state.militaryCareer.fieldPosition.proof.startsWith('m3_4x:river-task:')||state.militaryCareer.fieldPosition.proof==='m3_4y:escort'))throw Error('Missing issued task');
  const pos=auh63SocialPosition(state);if(pos.position.includes('River campaign commander')||pos.affiliation.includes('own following'))throw Error('Character inflated authority');
  if(before.militaryCareer.rank==='Private'&&auh4wCanLead(state))throw Error('Private assigned command');
  const journal=state.journal.filter(e=>['An Earned Command','The Hanjin Boats','The Jiangxia Compact','The Eastern Argument'].includes(e.label));
  if(journal.some(e=>/your own scarce transports|your field command over a mobile wing|independence of your command|joint working command/.test(e.text)))throw Error('False Chronicle claim');
  const frozen=JSON.stringify(state);militaryPanel();auh63SocialPosition(state);if(JSON.stringify(state)!==frozen)throw Error('View mutation');
  rows.push({rank:before.militaryCareer.rank,branch,selected});
 }
 return {rows,example:clone(state)};
 }finally{save=realSave;render=realRender;scrollTopNow=realScroll;}
}"""

def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--report',type=Path);args=parser.parse_args()
    with fixture(BASELINE) as (browser,url,result):
        base=browser.new_page();base.goto(url+'/baseline.html')
        initial=[base.evaluate(START, decline) for decline in (False,True)]
        starts=[base.evaluate(ADVANCE,{'seed':s['snapshots']['ch08_pb55_xushu'],'decision':d}) for s in initial for d in (0,1)]
        seeds=[base.evaluate(TO_HANJIN,s) for s in starts];base.close()
        for width in (390,1280):
            context=browser.new_context(viewport={'width':width,'height':900});page=context.new_page();errors=[];page.on('pageerror',lambda error:errors.append(str(error)));page.goto(url+'/active.html')
            assert set(initial[0]['ids']).issubset(page.evaluate('Object.keys(SCENES)'))
            runs=[page.evaluate(ROUTES,seed) for seed in seeds];assert sum(len(r['rows']) for r in runs)==216
            # Confirm the generated matrix actually covers every local pair.
            rowset=runs[0]['rows'][:27];ids=list(rowset[0]['selected'])
            for i,left in enumerate(ids):
                for right in ids[i+1:]:
                    pairs={(r['selected'][left],r['selected'][right]) for r in rowset}
                    lc=len({r['selected'][left] for r in rowset});rc=len({r['selected'][right] for r in rowset});assert len(pairs)==lc*rc
            # Unmodified high-command nodes keep their prior body/labels/effects.
            major=deepcopy(seeds[0]);major['militaryCareer']['rank']='Major'
            project=r"""s=>['ch08_c72_01_guanyu_council','ch08_c72_02_shore_witnesses','ch08_pb55_jiangxia','ch08_pb55_liuqi_council','ch08_shu56_zhugeliang_terms','ch08_pb55_embassy','ch08_pb55_bridge','ch08_zhugeliang_ledger','ch08_lusu_quay','lc81_208_four_courts','ch08_c72_03_lusu_table','ch08_c72_04_eastern_conditions','p86_208_pilots_and_seals','ch08_alliance_register','ch08_player_council'].map(id=>({id,body:SCENES[id].body(s),choices:SCENES[id].choices(s).map(o=>{const x=clone(s);o.effect(x);return {label:o.label,next:o.next,state:x};})}))"""
            base=context.new_page();base.goto(url+'/baseline.html');assert normalize_chapter_headers(page.evaluate(project,major))==normalize_chapter_headers(base.evaluate(project,major));base.close()
            page.evaluate(r"""s=>{
             state=clone(s);const once=JSON.stringify(state.militaryCareer);SCENES.ch08_player_council.choices(state)[0].effect(state);if(JSON.stringify(state.militaryCareer)!==once&&state.flags.auh52_war_command==='wing'){
              // The tested example may have selected another task. Repeating an
              // identical issued task must settle on identical military state.
              const twice=JSON.stringify(state.militaryCareer);SCENES.ch08_player_council.choices(state)[0].effect(state);if(JSON.stringify(state.militaryCareer)!==twice)throw Error('Task not stable');
             }
             const late=clone(state);late.militaryCareer.fieldPosition={year:214,proof:'later',active:true};SCENES.ch08_player_council.choices(late)[0].effect(late);if(late.militaryCareer.fieldPosition.proof!=='later')throw Error('Later posting overwritten');
             localStorage.setItem(SAVE_KEY,JSON.stringify(s));handleAction('load-original');
            }""",runs[3]['example']);page.reload();assert page.evaluate('validSave(state)&&state.flags.m3_208_river_scope==="company"&&state.militaryCareer.rank==="Private"')
            page.locator('#menuToggle').click();page.locator('#gameMenu [data-nav="military"]').click();assert 'issued river combat task' in page.locator('#screen').inner_text();assert page.evaluate('document.documentElement.scrollWidth<=innerWidth')
            page.evaluate('s=>{state=clone(s);activeTab="story";render();}',seeds[3]);clicks=0
            while page.evaluate('state.scene!=="ch08_rc54_flotilla"'):
                page.evaluate('()=>{state.pageIndex=paginateStory(SCENES[state.scene].body(state)).length-1;render();}')
                page.locator('[data-choice="0"], [data-action="next-scene"]').click();clicks+=1;assert clicks<45
            assert page.evaluate('state.militaryCareer.rank==="Private"&&state.flags.m3_208_river_scope==="company"')
            page.evaluate(r"""()=>{
             for(const h of state.history)h.body='';
             const realSave=save,realRender=render,realScroll=scrollTopNow;save=()=>{};render=()=>{};scrollTopNow=()=>{};
             try{for(let i=0;i<70&&state.storyClock.year===208;i++){
              const sc=SCENES[state.scene];state.pageIndex=paginateStory(sc.body(state)).length-1;choose(0);if(sc.id===state.scene)throw Error('Aftermath blocked');
             }
             if(state.storyClock.year!==209||state.militaryCareer.fieldPosition.active||!(state.militaryCareer.fieldPosition.proof.startsWith('m3_4x:river-task:')||state.militaryCareer.fieldPosition.proof==='m3_4y:escort'))throw Error('Issued task not retired at played morning review');
             }finally{save=realSave;render=realRender;scrollTopNow=realScroll;}
            }""")
            assert not errors,errors
            result['checks'].append({'width':width,'pairwise_routes_four_careers_two_branches':216,'eleven_choice_groups_all_pairs':'PASS',
                'no_rank_units_staff_ships_goods_or_recruit_grants':'PASS','recorded_muster_and_private_authority':'PASS',
                'chronicle_character_military_scope':'PASS','fifteen_legacy_major_nodes_parity':'PASS',
                'later_post_and_task_idempotence':'PASS','played_morning_review_retires_issued_task':'PASS','reload_and_military_dom':'PASS','full_history_private_dom_clicks':clicks,'page_errors':errors});context.close()
    result['limits']='River councils through issue of company task only. Later Red Cliffs battle/settlement prose, 209 commission and chapter rethreading remain pending. Matrix suppresses paint/storage and old history bodies; separate DOM route uses full history. Cavalry/Major synthetic; no physical-device file://.'
    write_report(result,args.report)
if __name__=='__main__':main()
