#!/usr/bin/env python3
"""211–214 charter acceptance/delegation, six outcomes, Civic and saved clocks."""
import argparse
from copy import deepcopy
from pathlib import Path
from qa_support import fixture, write_report, normalize_chapter_headers
from qa_m2_continuity import START
from qa_changban import ADVANCE
from qa_river_councils import TO_HANJIN
from qa_river_patrol import TO_FLOTILLA
from qa_red_cliffs import TO_ANCHORS
from qa_crossing210 import TO_TIDE

BASELINE='06403a4:GAME/ALL_UNDER_HEAVEN_v0.4.99.5b_THE_WITNESSED_CROSSING.html'
TO_COUNCIL=r"""seed=>{
 state=clone(seed);activeTab='story';const a=save,b=render,c=scrollTopNow;save=()=>{};render=()=>{};scrollTopNow=()=>{};
 try{for(let i=0;i<80;i++){
  if(state.scene==='ch09_charter_council')return clone(state);
  const sc=SCENES[state.scene];state.pageIndex=paginateStory(sc.body(state)).length-1;choose(0);if(sc.id===state.scene)throw Error('Charter seed blocked '+sc.id+':'+banner);
 }throw Error('211 not reached');}finally{save=a;render=b;scrollTopNow=c;}
}"""
ROUTES=r"""seed=>{
 const compact=clone(seed);for(const h of compact.history)h.body='';const verify=typeof auh5cEvidence==='function';
 const a=save,b=render,c=scrollTopNow;save=()=>{};render=()=>{};scrollTopNow=()=>{};const rows=[];let example=null,legacyCrossing=null;
 try{for(const branch of ['Infantry','Cavalry'])for(let proposal=0;proposal<3;proposal++)for(let action=0;action<3;action++)for(let settlement=0;settlement<(verify?4:3);settlement++){
  state=clone(compact);activeTab='story';if(branch==='Cavalry')state.militaryCareer.combatService={branch,unit:'Legacy mounted section',commander:'Recorded officer',year:211,proof:'legacy:lawful-cavalry'};
  const before=clone(state),moves=[proposal,0,action,settlement,0];
  for(const [step,index] of moves.entries()){
   const sc=SCENES[state.scene];if(sc.id==='ch09_charter_crossing')legacyCrossing=clone(state);
   state.pageIndex=paginateStory(sc.body(state)).length-1;choose(index);
   if(!validSave(state)||state.scene===sc.id)throw Error('Charter blocked '+sc.id+':'+banner);
   if(verify&&step===1&&(state.storyClock.year!==212||state.age!==38||!state.militaryCareer.fieldPosition.active))throw Error('212 order/clock');
   if(step===2&&(state.storyClock.year!==212||state.age!==38||(verify&&state.militaryCareer.fieldPosition.active)))throw Error('212 action/relief');
   if(step===3&&(state.storyClock.year!==213||state.age!==39||(verify&&!auh5cEvidence(state))))throw Error('213 hearing');
  }
  if(state.scene!=='ch10_01'||state.storyClock.year!==214||state.age!==40)throw Error('214 original exit');
  for(const key of ['rank','rankProof','units','appointmentHistory','staff','superior','combatService'])if(JSON.stringify(state.militaryCareer[key])!==JSON.stringify(before.militaryCareer[key]))throw Error('Military grant '+key);
  for(const key of ['coins','items','innerCircle'])if(JSON.stringify(state[key])!==JSON.stringify(before[key]))throw Error('Unchosen grant '+key);
  if(state.civicCareer.appointed!==before.civicCareer.appointed||JSON.stringify(state.civicCareer.officials)!==JSON.stringify(before.civicCareer.officials)||auhMcCivicOffice(state))throw Error('Governor/officer grant');
  if(verify){
   const e=state.civicCareer.localCharter;if(!auh5cEvidence(state)||!auhMcCivicUnlocked(state)||e.delegated!==(settlement===3)||e.accepted!==(settlement!==3&&['self-governed','recognized','community-compact'].includes(e.result)))throw Error('Charter scope/acceptance');
   if(!e.military||e.military.branch!==branch)throw Error('Combat proof');
   const hasLeague=SCENES.ch11_04.choices(state).some(o=>o.label.startsWith('Propose a league of the river districts'));if(hasLeague!==(e.accepted&&e.result==='self-governed'))throw Error('League ownership gate');
   const once=JSON.stringify(state);civicPanel();militaryPanel();npcMemories('hansheng');auh5cRecord(state);if(JSON.stringify(state)!==once)throw Error('Read-only/idempotence');
   if(e.delegated&&auh63SocialPosition(state).position.includes('convenor'))throw Error('Declined chair awarded');
  }
  rows.push({rank:before.militaryCareer.rank,branch,proposal,action,settlement,result:state.flags.auh53_result,losses:state.flags.auh53_losses,year:state.storyClock.year,age:state.age});example=clone(state);
 }return {rows,example,legacyCrossing};}finally{save=a;render=b;scrollTopNow=c;}
}"""
PROJECT=r"""s=>['ch09_charter_council','ch09_charter_challenge','ch09_charter_crossing','ch09_charter_hearing','ch09_charter_aftermath'].map(id=>({id,choices:SCENES[id].choices(s).slice(0,3).map(o=>{
 const x=clone(s);o.effect(x);delete x.flags.m3_211_scope;delete x.flags.m3_213_delegate;delete x.civicCareer.localCharter;delete x.militaryCareer.fieldPosition;x.journal=clone(s.journal);
 if(id==='ch09_charter_challenge'){x.age=s.age;x.storyClock=clone(s.storyClock);x.flags.novelYear=s.flags.novelYear;}
 return {next:o.next,state:x};})}))"""

def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--report',type=Path);args=parser.parse_args()
    with fixture(BASELINE) as (browser,url,result):
        base=browser.new_page();base.goto(url+'/baseline.html')
        initial=[base.evaluate(START,d) for d in (False,True)]
        starts=[base.evaluate(ADVANCE,{'seed':s['snapshots']['ch08_pb55_xushu'],'decision':d}) for s in initial for d in (0,1)]
        hanjin=[base.evaluate(TO_HANJIN,s) for s in starts];flotilla=[base.evaluate(TO_FLOTILLA,s) for s in hanjin]
        strong=[base.evaluate(TO_ANCHORS,{'seed':s,'weak':False}) for s in flotilla]
        weak=base.evaluate(TO_ANCHORS,{'seed':flotilla[0],'weak':True})
        tide=[base.evaluate(TO_TIDE,{'seed':s,'world':'south'}) for s in strong]+[base.evaluate(TO_TIDE,{'seed':weak,'world':'north'})]
        seeds=[base.evaluate(TO_COUNCIL,s) for s in tide]
        baseline=base.evaluate(ROUTES,seeds[0]);base.close()
        for width in (390,1280):
            context=browser.new_context(viewport={'width':width,'height':900});page=context.new_page();errors=[];page.on('pageerror',lambda e:errors.append(str(e)));page.goto(url+'/active.html')
            assert set(initial[0]['ids']).issubset(page.evaluate('Object.keys(SCENES)'))
            runs=[page.evaluate(ROUTES,s) for s in seeds];assert sum(len(r['rows']) for r in runs)==360
            outcomes={row['result'] for run in runs for row in run['rows']};assert len(outcomes)==6,outcomes
            assert [row for row in runs[0]['rows'] if row['settlement']<3]==baseline['rows']
            base=context.new_page();base.goto(url+'/baseline.html')
            seed=deepcopy(seeds[0]);seed['flags']['m3_211_scope']='local-charter';assert page.evaluate(PROJECT,seed)==base.evaluate(PROJECT,seed)
            major=deepcopy(seeds[0]);major['militaryCareer']['rank']='Major'
            high=r"""s=>Object.keys(SCENES).filter(id=>id.startsWith('ch09_charter_')).map(id=>({id,body:SCENES[id].body(s).replace('<em>212 CE.</em>','<em>'+s.storyClock.year+' CE.</em>'),choices:SCENES[id].choices(s).map(o=>{const x=clone(s);o.effect(x);return {label:o.label,next:o.next,state:x};})}))"""
            assert normalize_chapter_headers(page.evaluate(high,major))==normalize_chapter_headers(base.evaluate(high,major));base.close()
            page.evaluate(r"""seed=>{
             state=clone(seed);const history=clone(state);history.visited=[];if(!auh5cEvidence(history))throw Error('History-only charter');
             const empty=clone(state);empty.visited=[];empty.history=[];if(auh5cEvidence(empty)||auhMcCivicUnlocked(empty))throw Error('Flag-only unlock');delete empty.civicCareer.localCharter;auh5cRecord(empty);if(empty.civicCareer.localCharter)throw Error('Backfilled charter');
             const invalid=clone(state);invalid.civicCareer.localCharter.result='__proto__';if(auh5cEvidence(invalid))throw Error('Invalid result');
             const future=clone(state);future.storyClock.year=212;future.militaryCareer.fieldPosition={year:218,proof:'later',active:true};auh5cPosition(future,'return',false);if(future.militaryCareer.fieldPosition.proof!=='later'||!auh5cEvidence(future))throw Error('Later position/past charter');
             const governor=clone(state);governor.civicCareer.appointed=true;governor.civicCareer.office='Governor';governor.civicCareer.territory='Recorded legacy district';state=governor;if(!auhMcCivicOffice(state)||!civicPanel().includes('Governor'))throw Error('Formal office suppressed');
             state=clone(seed);localStorage.setItem(SAVE_KEY,JSON.stringify(state));handleAction('load-original');
            }""",runs[0]['example']);page.reload();assert page.evaluate('validSave(state)&&auh5cEvidence(state)')
            page.locator('#menuToggle').click();page.locator('#gameMenu [data-nav="civic"]').click();assert page.locator('[aria-label="Witnessed local charter"]').is_visible();assert page.evaluate('document.documentElement.scrollWidth<=innerWidth')
            page.evaluate(r"""saved=>{
             state=resolve(clone(saved.example));const old=JSON.stringify(state);civicPanel();if(auh5cEvidence(state)||state.civicCareer.localCharter||JSON.stringify(state)!==old)throw Error('Legacy charter backfill');
             const crossing=resolve(clone(saved.legacyCrossing)),before=JSON.stringify(crossing);if(crossing.storyClock.year!==211||!SCENES.ch09_charter_crossing.body(crossing).includes('<em>211 CE.</em>')||JSON.stringify(crossing)!==before)throw Error('Legacy 211 age/date mutated');
             for(const year of [214,215]){const s=clone(crossing);s.storyClock.year=year;const frozen=JSON.stringify(s),body=SCENES.ch10_c58_01_western_messenger.body(s).trimStart();if(!(body.startsWith('<p>'+year+' CE.')||body.startsWith('<p><em>'+year+' CE.</em>'))||JSON.stringify(s)!==frozen)throw Error('Messenger saved clock mismatch');}
            }""",baseline)
            # Unknown combat branch can still witness civic proceedings, with no
            # invented military proof. Also exercise the explicit chair refusal.
            page.evaluate(r"""seed=>{
             state=clone(seed);delete state.militaryCareer.combatService;const a=save,b=render,c=scrollTopNow;save=()=>{};render=()=>{};scrollTopNow=()=>{};
             try{for(let i=0;i<5;i++){const sc=SCENES[state.scene];state.pageIndex=paginateStory(sc.body(state)).length-1;choose(i===3?3:0);}
              if(!auh5cEvidence(state)||state.civicCareer.localCharter.military!==null||!state.civicCareer.localCharter.delegated||state.civicCareer.localCharter.accepted)throw Error('Civic witness became fighter/ruler');
             }finally{save=a;render=b;scrollTopNow=c;}
            }""",seeds[3])
            page.evaluate('s=>{state=clone(s);activeTab="story";render();}',seeds[3])
            for index in (1,0,1,3):
                page.evaluate('()=>{state.pageIndex=paginateStory(SCENES[state.scene].body(state)).length-1;render();}')
                page.locator(f'[data-choice="{index}"]' if index else '[data-choice="0"], [data-action="next-scene"]').click()
            assert page.evaluate('state.storyClock.year===213&&state.militaryCareer.rank==="Private"&&auh5cEvidence(state)&&state.civicCareer.localCharter.delegated&&!state.civicCareer.localCharter.accepted')
            page.locator('#menuToggle').click();page.locator('#gameMenu [data-nav="civic"]').click();assert page.locator('[aria-label="Witnessed local charter"]').is_visible()
            assert not errors,errors
            result['checks'].append({'width':width,'all_local_charter_routes_five_organic_career_world_seeds_two_branches':360,'six_legacy_outcomes':sorted(outcomes),
                'old_27_routes_per_branch_and_original_effects_parity':'PASS','higher_command_legacy_parity_except_saved_year_label':'PASS',
                'accept_decline_pending_and_civic_local_only':'PASS','no_military_staff_gov_or_goods_grants':'PASS','212_213_214_clock_and_retired_position':'PASS',
                'provenance_readonly_idempotence_legacy_unknown_branch':'PASS','214_215_messenger_labels_preserve_age':'PASS','reload_and_civic_dom':'PASS','private_delegate_dom_clicks':4,'page_errors':errors});context.close()
    result['limits']='Five selected organic career/world seeds, all local 3×3×4 choices, both branches; Cavalry/Major/Governor negative/parity profiles synthetic. Not all earlier-world combinations or full Chapter X/M3. Matrix suppresses paint/storage and old history bodies; DOM uses full history. Physical-device file:// unverified.'
    write_report(result,args.report)
if __name__=='__main__':main()
