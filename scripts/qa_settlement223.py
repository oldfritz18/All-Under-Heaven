#!/usr/bin/env python3
"""223 custody/ratification and 224 bridge on legally reached service profiles."""
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
from qa_baxi216 import TO_BORDER
from qa_jing219 import TO_JING
from qa_eastern222 import TO_XI, TO_FRONT

BASELINE='e795cd9:GAME/ALL_UNDER_HEAVEN_v0.4.99.5f_THE_EASTERN_FIELD_WARRANT.html'
NEW={'m3_223_rolls','m3_223_ratification','m3_223_after_terms'}
TO_223=r"""config=>{
 state=clone(config.seed);activeTab='story';const a=save,b=render,c=scrollTopNow;save=()=>{};render=()=>{};scrollTopNow=()=>{};
 try{for(let i=0;i<65;i++){
  if(state.scene==='ch11_p60_08_turn_223')return clone(state);
  const sc=SCENES[state.scene];state.pageIndex=paginateStory(sc.body(state)).length-1;choose(sc.id==='m3_222_field_review'?config.review:0);if(sc.id===state.scene)throw Error('223 seed blocked '+sc.id+':'+banner);
 }throw Error('223 not reached');}finally{save=a;render=b;scrollTopNow=c;}
}"""
ROUTES=r"""seed=>{
 const compact=clone(seed);for(const h of compact.history)h.body='';
 const a=save,b=render,c=scrollTopNow;save=()=>{};render=()=>{};scrollTopNow=()=>{};const rows=[];let example=null,rolls=null;
 const step=i=>{const sc=SCENES[state.scene];state.pageIndex=paginateStory(sc.body(state)).length-1;choose(i);if(state.scene===sc.id||!validSave(state))throw Error('Settlement blocked '+sc.id+':'+banner);};
 try{for(const branch of ['Infantry','Cavalry'])for(let proposal=0;proposal<3;proposal++)for(let custody=0;custody<3;custody++)for(let mandate=0;mandate<3;mandate++){
  state=clone(compact);activeTab='story';if(branch==='Cavalry')state.militaryCareer.combatService={branch,unit:'Synthetic lawful mounted service',commander:'Recorded officer',year:223,proof:'legacy:lawful-cavalry'};
  const before=clone(state),sum=units=>units.filter(u=>u.active!==false).reduce((n,u)=>n+u.infantry+u.cavalry+u.archers,0),total=sum(before.militaryCareer.units);
  const choices=SCENES[state.scene].choices(state),political=choices.map((o,i)=>o.next==='ch11_p60_09_oath_223'?i:-1).filter(i=>i>=0);step(political[proposal]);
  if(!auh5gNotice(state)||state.civicCareer.settlement223)throw Error('Notice/proposal became appointment');
  const terms=(proposal+mandate)%3,archive=(custody+mandate)%3,answer=(proposal+custody)%3,field=(proposal+custody+mandate)%2,seal=(proposal+2*custody+mandate)%3;
  const picks={ch11_c73_05_successors_hearing_223:terms,p86_223_separate_obligations:archive,ch11_c74_03_officers_refuse_223:answer,ch11_c74_04_countermoves_223:field,ch11_06:seal};
  for(let i=0;state.scene!=='m3_223_rolls'&&i<22;i++)step(picks[state.scene]??0);
  if(state.scene!=='m3_223_rolls'||state.storyClock.year!==223||state.age!==49||state.civicCareer.settlement223)throw Error('Deferred 223 exit');
  rolls=clone(state);if(!auh5gReturnable(state))throw Error('Lawful formation not returnable');step(custody);
  if(state.scene!=='m3_223_ratification'||state.storyClock.year!==223)throw Error('Ratification entry');
  if(custody===1){if(sum(state.militaryCareer.units)!==0||!auh5gHandover(state)||state.militaryCareer.handover223.units.reduce((n,u)=>n+u.infantry+u.cavalry+u.archers,0)!==total)throw Error('Handover did not match receiving roll');}
  else if(JSON.stringify(state.militaryCareer.units)!==JSON.stringify(before.militaryCareer.units)||state.militaryCareer.handover223)throw Error('Unchosen unit transfer');
  step(mandate);if(!auh5gEvidence(state)||state.storyClock.year!==223||state.civicCareer.settlement223.accepted!==(mandate===0))throw Error('Ratification evidence');
  const once=JSON.stringify(state);civicPanel();militaryPanel();npcMemories('liubei');auh5gRecord(state,['chair','delegates','witness'][mandate]);auh5gChooseMilitary(state,'handover');if(JSON.stringify(state)!==once)throw Error('View/replay mutation');
  step(0);if(state.scene!=='ch12_01'||state.storyClock.year!==224||state.age!==50||!auh5gEvidence(state)||!state.flags.m3_223_bridge_done)throw Error('224 bridge');
  for(const key of ['rank','rankProof','appointmentHistory','staff','superior','commissionAuthority','combatService'])if(JSON.stringify(state.militaryCareer[key])!==JSON.stringify(before.militaryCareer[key]))throw Error('Unchosen military change '+key);
  for(const key of ['coins','items','innerCircle','dragonGenerals'])if(JSON.stringify(state[key])!==JSON.stringify(before[key]))throw Error('Unchosen grant '+key);
  for(const key of ['appointed','office','territory','officials','localCharter'])if(JSON.stringify(state.civicCareer[key])!==JSON.stringify(before.civicCareer[key]))throw Error('Civic office/old charter change '+key);
  if(auh65Crowned(state)||auh79Emperor(state))throw Error('Automatic crown');
  if(state.flags.historical_meet_liushan)throw Error('Report became direct meeting');
  const role=auh63SocialPosition(state).position;if(!role.startsWith(before.militaryCareer.rank)||((mandate!==0)&&role.includes('mandate-holder')))throw Error('Character mandate');
  if(custody===1){if(!role.includes(total?'formation returned':'release requested'))throw Error('Character active force after handover');
   if(!total&&(state.militaryCareer.handover223.status!=='personal_release_requested_no_force'||!auh5gStatus(state).includes('There was no personal formation')))throw Error('Private given a phantom transferred formation');
   for(const old of before.militaryCareer.units){const now=state.militaryCareer.units.find(u=>u.id===old.id);if(JSON.stringify(now)!==JSON.stringify(old.active!==false?{...old,active:false}:old))throw Error('Handover erased/changed a unit');}}
  const body=SCENES.ch12_01.body(state);if(!body.includes('Part II — The Heir of Shu.')||body.includes('The final years of your public service'))throw Error('XII bridge framing');
  rows.push({rank:before.militaryCareer.rank,branch,proposal,custody,mandate,terms,archive,answer,field,seal,before:total,after:sum(state.militaryCareer.units),reply:state.civicCareer.settlement223.reply});example=clone(state);
 }return {rows,example,rolls};}finally{save=a;render=b;scrollTopNow=c;}
}"""
PROJECT=r"""s=>['ch11_p60_08_turn_223','ch11_p60_09_oath_223','ch11_c73_05_successors_hearing_223','p86_223_separate_obligations','ch11_c74_03_officers_refuse_223','ch11_c74_04_countermoves_223','ch11_06'].map(id=>({id,choices:SCENES[id].choices(s).map(o=>{
 const x=clone(s);o.effect?.(x);for(const k of ['m3_223_scope','m3_223_exit_year'])delete x.flags[k];if(x.worldNotices){delete x.worldNotices.western223;if(!Object.keys(x.worldNotices).length)delete x.worldNotices;}x.journal=clone(s.journal);
 if(id==='ch11_06'){x.age=224-190+16;x.storyClock={...x.storyClock,year:224,anchorScene:'ch12_01'};x.flags.novelYear=224;}
 return {next:o.next==='m3_223_rolls'?'ch12_01':o.next,state:x};
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
        xi=[base.evaluate(TO_XI,s) for s in jing]
        fronts=[base.evaluate(TO_FRONT,{'seed':s,'policy':0,'travel':0}) for s in xi]
        configs=[(0,0),(1,0),(2,0),(3,1),(4,0),(7,0),(7,1),(0,1),(1,1),(3,0),(5,1),(6,1),(8,1)]
        seeds=[base.evaluate(TO_223,{'seed':fronts[i],'review':d}) for i,d in configs]
        assert [s['militaryCareer']['rank'] for s in seeds]==['Major','Captain','Captain','Private','Captain','General','Major','Captain','Sergeant','Sergeant','Captain','Captain','Private']
        legacy=base.evaluate(r"""s=>{state=clone(s);activeTab='story';for(let i=0;i<65;i++){if(state.scene==='ch12_01')return clone(state);const sc=SCENES[state.scene];state.pageIndex=paginateStory(sc.body(state)).length-1;choose(0);}throw Error('Legacy XII not reached');}""",seeds[0])
        old_ids=base.evaluate('Object.keys(SCENES)');base.close()
        for width in (390,1280):
            context=browser.new_context(viewport={'width':width,'height':900});page=context.new_page();errors=[];page.on('pageerror',lambda e:errors.append(str(e)));page.goto(url+'/active.html')
            assert set(page.evaluate('Object.keys(SCENES)'))-set(old_ids)==NEW
            runs=[page.evaluate(ROUTES,s) for s in seeds];assert sum(len(r['rows']) for r in runs)==702
            groups=['proposal','custody','mandate','terms','archive','answer','seal']
            for i,k in enumerate(groups):
                for l in groups[i+1:]:assert len({(r[k],r[l]) for r in runs[0]['rows']})==9,(k,l)
            assert {r['reply'] for run in runs for r in run['rows']}=={'one_escort','witnesses_only','trade_withdrawn'}
            base=context.new_page();base.goto(url+'/baseline.html')
            seed=deepcopy(seeds[0]);seed['flags']['m3_223_scope']='witnessed';assert page.evaluate(PROJECT,seed)==base.evaluate(PROJECT,seed)
            high=deepcopy(seeds[5]);high['flags'].pop('m3_222_field_scope',None);high['flags'].pop('m3_215_frontier_scope',None)
            parity=r"""s=>['ch11_p60_08_turn_223','ch11_p60_09_oath_223','ch11_c73_05_successors_hearing_223','ch11_c74_03_officers_refuse_223','ch11_c74_04_countermoves_223','ch11_06','ch12_01'].map(id=>({id,body:SCENES[id].body(s),choices:SCENES[id].choices(s).map(o=>{const x=clone(s);o.effect?.(x);return {label:o.label,next:o.next,state:x};})}))"""
            assert page.evaluate(parity,high)==base.evaluate(parity,high)
            personal=r"""s=>(SCENES.ch11_p60_08_turn_223.body(s).match(/<p>[\s\S]*?<\/p>/g)||[]).filter(p=>/private evening|friendship renewed|quiet parting|No private meeting|marriage you chose/.test(p))"""
            assert page.evaluate(personal,seeds[5])==base.evaluate(personal,seeds[5]);base.close()
            page.evaluate(r"""config=>{
             state=resolve(clone(config.legacy));const frozen=JSON.stringify(state);civicPanel();militaryPanel();npcMemories('liubei');if(state.civicCareer.settlement223||state.militaryCareer.handover223||state.worldNotices?.western223||JSON.stringify(state)!==frozen)throw Error('Legacy backfill');
             const history=clone(config.example);history.visited=[];if(!auh5gEvidence(history))throw Error('History-only settlement');
             const flags=clone(config.example);flags.visited=[];flags.history=[];if(auh5gEvidence(flags)||auh5gNotice(flags)||auh5gHandover(flags))throw Error('Flag-only settlement');
             const invalid=clone(config.example);invalid.civicCareer.settlement223.mandate='Governor';if(auh5gEvidence(invalid))throw Error('Invalid mandate');
             const notice=clone(config.example);notice.worldNotices.western223.account='invented';if(auh5gNotice(notice)||auh5gEvidence(notice))throw Error('Invalid notice');
             const future=clone(config.rolls);future.militaryCareer.fieldPosition={year:226,active:true,proof:'later'};const before=JSON.stringify(future.militaryCareer);auh5gChooseMilitary(future,'handover');if(auh5gReturnable(future)||JSON.stringify(future.militaryCareer)!==before)throw Error('Later posting changed');
             const unknown=clone(config.rolls);unknown.militaryCareer.units.find(u=>u.active!==false).source='unknown';if(auh5gReturnable(unknown))throw Error('Unknown formation transferred');
             const gov=clone(config.example);gov.civicCareer.appointed=true;gov.civicCareer.office='Governor';gov.civicCareer.territory='Recorded existing district';state=gov;if(!civicPanel().includes('Governor')||!auhMcCivicOffice(state))throw Error('Existing office erased');
             const a=save,b=render,c=scrollTopNow;save=()=>{};render=()=>{};scrollTopNow=()=>{};
             try{state=clone(config.rolls);state.age=70;for(const i of [0,1,0]){const sc=SCENES[state.scene];state.pageIndex=paginateStory(sc.body(state)).length-1;choose(i);}if(state.age!==71||state.storyClock.year!==224||!auh5gEvidence(state))throw Error('Older age/bridge');}finally{save=a;render=b;scrollTopNow=c;}
            }""",{'legacy':legacy,**runs[5]})
            # Full-history browser route preserves optional personal/neighbor
            # visits. Then explicitly hand back the General's 720 and decline
            # the chair, reload and inspect both archives.
            page.evaluate('s=>{state=clone(s);activeTab="story";render();}',seeds[5]);clicks=0
            while page.evaluate('state.scene')!='m3_223_rolls':
                assert clicks<65
                page.evaluate('()=>{state.pageIndex=paginateStory(SCENES[state.scene].body(state)).length-1;render();}')
                page.locator('[data-choice="0"], [data-action="next-scene"]').click();clicks+=1
            for index in (1,1,0):
                page.evaluate('()=>{state.pageIndex=paginateStory(SCENES[state.scene].body(state)).length-1;render();}')
                page.locator(f'[data-choice="{index}"]' if index else '[data-choice="0"], [data-action="next-scene"]').click();clicks+=1
            assert page.evaluate('state.scene==="ch12_01"&&state.militaryCareer.rank==="General"&&auh5gEvidence(state)&&auh5gHandover(state)&&!state.civicCareer.settlement223.accepted&&auhStoryUIRecordedUnits(state).length===0&&validSave(state)')
            page.reload();assert page.evaluate('auh5gEvidence(state)&&auh5gHandover(state)')
            page.locator('#menuToggle').click();page.locator('#gameMenu [data-nav="civic"]').click();assert page.locator('[aria-label="Local settlement in 223"]').is_visible()
            page.locator('#menuToggle').click();page.locator('#gameMenu [data-nav="military"]').click();assert page.locator('[aria-label="Military custody in 223"]').is_visible()
            assert page.evaluate('document.documentElement.scrollWidth<=innerWidth');assert not errors,errors
            result['checks'].append({'width':width,'routes_thirteen_organic_career_world_charter_seeds_two_current_branch_variants':702,'all_new_local_choices_and_seven_groups_pairwise':'PASS','handover_exact_force_no_rank_loss_and_other_choices_no_transfer':'PASS','accepted_declined_witness_local_only_no_crown_or_office_grants':'PASS','original_effects_and_seven_higher_legacy_nodes_parity':'PASS','personal_prose_and_optional_dom_paths_preserved':'PASS','notice_report_only_readonly_provenance_legacy_later_post':'PASS','223_deferred_224_once_and_old_age':'PASS','reload_civic_military_dom':'PASS','general_handover_and_delegate_dom_clicks':clicks,'page_errors':errors});context.close()
    result['limits']='Thirteen selected organic career/world/charter seeds; Cavalry current-service variants and higher legacy/Governor/older-age profiles synthetic. Original accepted force records remain intact until the tested handover. Full new proposal×custody×mandate; pairwise seven 3-way groups, not full product or all prior relationship states. Matrix suppresses paint/storage and compacts old history bodies; DOM full history. Not full M3/M11 or physical-device file:// certification.'
    write_report(result,args.report)
if __name__=='__main__':main()
