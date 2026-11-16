#!/usr/bin/env python3
"""M4-A petitions: actual journeys, relay knowledge and court refusal/limits."""
import argparse,tempfile,json
from pathlib import Path
from qa_support import fixture,write_report,DESIGNATION_221_SCENES,SHU_ACCESSION_225_SCENES,DRAGON_NOMINATION_227_SCENES
from qa_general222 import organic_reviews
from qa_hanzhong219 import organic_seeds

BASELINE='5841cf8:GAME/ALL_UNDER_HEAVEN_v0.4.99.5i_THE_SIXTH_STANDARD.html'
NEW={'m4_224_petition','m4_224_dispatch','m4_224_road','m4_224_chancery','m4_224_audience','m4_225_return'}
TO_XII=r"""cfg=>{state=clone(cfg.seed);const a=save,b=render,c=scrollTopNow;save=()=>{};render=()=>{};scrollTopNow=()=>{};try{for(let i=0;i<140;i++){if(state.scene==='ch12_01')return clone(state);const sc=SCENES[state.scene];state.pageIndex=paginateStory(sc.body(state)).length-1;choose(sc.id==='m3_223_rolls'?cfg.custody:sc.id==='m3_223_ratification'?cfg.mandate:sc.id==='m3_222_field_review'?cfg.review:0);if(sc.id===state.scene)throw Error(sc.id+':'+banner);}throw Error('XII not reached');}finally{save=a;render=b;scrollTopNow=c;}}"""

def organic_court_seeds(page):
    reviews,_=organic_reviews(page)
    configs=[(0,0,0,0),(1,0,0,1),(3,1,0,2),(4,0,0,0),(7,0,0,0),(7,0,1,1)]
    seeds=[page.evaluate(TO_XII,{'seed':reviews[i],'review':d,'custody':c,'mandate':m}) for i,d,c,m in configs]
    west=organic_seeds(page)[4]
    royal=page.evaluate(r"""s=>{state=clone(s);const a=save,b=render,c=scrollTopNow;save=()=>{};render=()=>{};scrollTopNow=()=>{};try{for(let i=0;i<18;i++){if(state.scene==='ch10_c58_07_jing_219')return clone(state);const sc=SCENES[state.scene];state.pageIndex=paginateStory(sc.body(state)).length-1;choose(sc.id==='ch10_c58_06_frontier_218'?sc.choices(state).findIndex(o=>o.next==='m3_218_hanzhong_request'):sc.id==='m3_219_hanzhong_clash'?1:0);if(sc.id===state.scene)throw Error(sc.id+':'+banner);}throw Error('Royal route');}finally{save=a;render=b;scrollTopNow=c;}}""",west)
    seeds += [page.evaluate(TO_XII,{'seed':royal,'review':0,'custody':c,'mandate':m}) for c,m in ((0,0),(1,1))]
    assert [s['militaryCareer']['rank'] for s in seeds]==['Major','Captain','Private','Captain','General','General','Grand General','Grand General']
    return seeds

ROUTES=r"""seed=>{
 const input=clone(seed);for(const h of input.history)h.body='';const a=save,b=render,c=scrollTopNow;save=()=>{};render=()=>{};scrollTopNow=()=>{};const rows=[];let example=null,dispatch=null,answer=null;
 const step=i=>{const sc=SCENES[state.scene];state.pageIndex=paginateStory(sc.body(state)).length-1;choose(i);if(sc.id===state.scene||!validSave(state))throw Error('Court blocked '+sc.id+':'+banner);};
 try{for(let purpose=0;purpose<3;purpose++)for(const method of ['personal','relay','withdrawn'])for(let route=0;route<(method==='withdrawn'?1:3);route++)for(let advice=0;advice<(method==='withdrawn'||route===2?1:3);advice++)for(let response=0;response<3;response++){
  state=clone(input);activeTab='story';const before=clone(state);step(SCENES[state.scene].choices(state).findIndex(o=>o.next==='m4_224_petition'));step(purpose);dispatch=clone(state);
  const travel=auh5jCanTravel(state);if(!travel)throw Error('Organic travel unavailable');step({personal:0,relay:1,withdrawn:2}[method]);
  if(method!=='withdrawn'){step(route);if(route!==2)step(advice);}
  if(state.scene!=='m4_224_audience'||state.storyClock.year!==224||state.age!==before.age||auh5jEvidence(state))throw Error('Reply before audience');answer=clone(state);
  const admitted=method==='personal'&&route===0&&advice!==2&&['General','Grand General'].includes(before.militaryCareer.rank);
  if(auh5jRoyalAudience(state)!==admitted)throw Error('Audience admission');step(response);
  if(state.scene!=='m4_225_return'||state.storyClock.year!==225||state.age!==before.age+1||!auh5jEvidence(state))throw Error('Court record/calendar');step(0);
  if(state.scene!=='ch12_c62_01_seals_225'||state.storyClock.year!==225||state.age!==before.age+1||!state.flags.m4_225_home_done||!auh5jEvidence(state))throw Error('225 return');
  const e=state.civicCareer.shuPetition224;if(e.royalAudience!==admitted)throw Error('False royal meeting');
  const reaction=AUH5J_RESPONSES[e.response];if(!SCENES.m4_225_return.body(state).includes(reaction)||!SCENES.ch12_c62_01_seals_225.body(state).includes(reaction)||!civicPanel().includes(reaction))throw Error('Reply lost at return/public hearing/Civic');
  if(admitted&&!npcMemories('liushan').some(m=>m.includes(reaction)))throw Error('Witnessed court response memory lost');
  state.militaryCareer.units.forEach((u,i)=>{if(JSON.stringify(u)!==JSON.stringify(before.militaryCareer.units[i]))throw Error('Unit custody changed');});
  const m=clone(state.militaryCareer);delete m.leave224;if(JSON.stringify(m)!==JSON.stringify(before.militaryCareer))throw Error('Grade/staff/authority changed');
  const c=clone(state.civicCareer);delete c.shuPetition224;if(JSON.stringify(c)!==JSON.stringify(before.civicCareer))throw Error('Court created office');
  for(const k of ['coins','items','relationships','innerCircle','dragonGenerals','health'])if(JSON.stringify(state[k])!==JSON.stringify(before[k]))throw Error('Court grant '+k);
  if(auh65Crowned(state)||auh79Emperor(state))throw Error('Court crowned player');
  if(!!auh5jLeave(state)!==(method==='personal')||method==='personal'&&state.militaryCareer.leave224.returnedYear!==225)throw Error('Journey provenance');
  if(!method.startsWith('personal')&&hasWitnessed('liushan'))throw Error('Relay became encounter');
  const frozen=JSON.stringify(state);civicPanel();militaryPanel();npcMemories('liushan');auh63SocialPosition(state);auh5jAnswer(state,'acknowledged');auh5jDispatch(state,'personal');auh5jRoute(state,'checked');if(JSON.stringify(state)!==frozen)throw Error('View/replay mutation');
  const restored=resolve(JSON.parse(JSON.stringify(state)));if(!validSave(restored)||!auh5jEvidence(restored))throw Error('Court receipt lost on resolve');
  rows.push({purpose,method,route,advice,response,royal:admitted,result:e.result});example=clone(state);
 }return {rows,example,dispatch,answer};}finally{save=a;render=b;scrollTopNow=c;}
}"""

def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--report',type=Path);args=parser.parse_args()
    with fixture(BASELINE) as (browser,url,result):
        old=browser.new_page();old.goto(url+'/baseline.html');seeds=organic_court_seeds(old);ids=set(old.evaluate('Object.keys(SCENES)'));old.close()
        for width in (390,1280):
            context=browser.new_context(viewport={'width':width,'height':900});p=context.new_page();errors=[];p.on('pageerror',lambda e:errors.append(str(e)));p.goto(url+'/active.html')
            current=set(p.evaluate('Object.keys(SCENES)'));assert ids<=current and current-ids in (NEW,NEW|DESIGNATION_221_SCENES,NEW|DESIGNATION_221_SCENES|SHU_ACCESSION_225_SCENES,NEW|DESIGNATION_221_SCENES|SHU_ACCESSION_225_SCENES|DRAGON_NOMINATION_227_SCENES) and len(current) in (695,701,716,728)
            runs=[p.evaluate(ROUTES,s) for s in seeds];assert sum(len(r['rows']) for r in runs)==1080
            assert {r['result'] for run in runs for r in run['rows']}=={'withdrawn','unverified','case_registered','local_terms','service_report'}
            old=context.new_page();old.goto(url+'/baseline.html')
            parity=r"""s=>['ch12_01','ch12_c62_01_seals_225'].map(id=>({id,body:SCENES[id].body(s),choices:SCENES[id].choices(s).map(o=>{const x=clone(s);o.effect(x);delete x.flags.m4_224_scope;return {label:o.next==='m4_224_petition'?'Continue':o.label,next:o.next==='m4_224_petition'?'ch12_c62_01_seals_225':o.next,state:x};})}))"""
            assert p.evaluate(parity,seeds[6])==old.evaluate(parity,seeds[6])
            old.close()
            p.evaluate(r"""cfg=>{
             const hist=clone(cfg.example);hist.visited=[];if(!auh5jEvidence(hist))throw Error('History-only court proof');
             const flags=clone(cfg.example);flags.visited=[];flags.history=[];if(auh5jEvidence(flags)||auh5jChancellor(flags)||auh5jLeave(flags))throw Error('Flags-only court proof');
             const bad=clone(cfg.example);bad.civicCareer.shuPetition224.result='Emperor';if(auh5jEvidence(bad))throw Error('Invalid court result');
             const late=clone(cfg.dispatch);late.militaryCareer.fieldPosition={year:226,active:true,proof:'later'};const before=JSON.stringify(late);auh5jDispatch(late,'personal');if(auh5jCanTravel(late)||JSON.stringify(late)!==before)throw Error('Later duty overridden');
             const unknown=clone(cfg.dispatch);unknown.militaryCareer.units.find(u=>u.active!==false).source='unknown';if(auh5jCanTravel(unknown))throw Error('Unknown force journey');
             const legacy=resolve(clone(cfg.seed));state=legacy;const original=JSON.stringify(state);civicPanel();militaryPanel();npcMemories('liushan');if(state.civicCareer.shuPetition224||state.militaryCareer.leave224||JSON.stringify(state)!==original)throw Error('Legacy backfill');
             const old=clone(cfg.seed);old.storyClock.year=226;old.age+=2;if(auh5jStartable(old)||SCENES.ch12_01.choices(old).some(o=>o.next==='m4_224_petition'))throw Error('Old save rewound');
             const gov=clone(cfg.answer);gov.civicCareer.appointed=true;gov.civicCareer.office='Governor';gov.civicCareer.territory='Existing province';if(auh5jRoyalAudience(gov)!==(gov.flags.m4_224_method==='personal'&&gov.flags.m4_224_route==='checked'&&gov.flags.m4_224_advice!=='local'))throw Error('Governor admission');state=gov;if(!civicPanel().includes('Governor'))throw Error('Governor office erased');
             const a=save,b=render,c=scrollTopNow;save=()=>{};render=()=>{};scrollTopNow=()=>{};try{
              state=clone(cfg.seed);state.age=69;for(let n=0;n<9&&state.scene!=='ch12_c62_01_seals_225';n++){const sc=SCENES[state.scene];state.pageIndex=paginateStory(sc.body(state)).length-1;choose(sc.id==='ch12_01'?sc.choices(state).findIndex(o=>o.next==='m4_224_petition'):0);if(state.scene===sc.id)throw Error(sc.id+':'+banner);}if(state.age!==70||state.storyClock.year!==225||!auh5jEvidence(state))throw Error('Older court age');
             }finally{save=a;render=b;scrollTopNow=c;}
            }""",{'seed':seeds[6],**runs[6]})
            p.evaluate(r"""seed=>{
             const a=save,b=render,c=scrollTopNow;save=()=>{};render=()=>{};scrollTopNow=()=>{};
             const step=i=>{const sc=SCENES[state.scene];state.pageIndex=paginateStory(sc.body(state)).length-1;choose(i);if(sc.id===state.scene)throw Error('Governor route blocked '+sc.id+':'+banner);};
             try{
              // Synthetic pre-existing civil appointment; military rank remains
              // the organically earned Captain, below the royal military gate.
              state=clone(seed);state.civicCareer.appointed=true;state.civicCareer.office='Governor';state.civicCareer.territory='Existing province';
              step(SCENES[state.scene].choices(state).findIndex(o=>o.next==='m4_224_petition'));step(1);step(0);step(0);step(1);
              if(!auh5jRoyalAudience(state)||state.militaryCareer.rank!=='Captain')throw Error('Governor did not receive qualified civil admission');
              const royal=clone(state);delete royal.civicCareer.appointed;if(auh5jRoyalAudience(royal))throw Error('Captain acquired royal admission from service alone');
              step(0);step(0);if(!auh5jEvidence(state)||!hasWitnessed('liushan')||!state.civicCareer.shuPetition224.civicAdmission||!civicPanel().includes('Governor'))throw Error('Governor court proof or office lost');
              state.militaryCareer.rank='Private';state.civicCareer.appointed=false;state.storyClock.year=231;
              if(!auh5jEvidence(state)||!hasWitnessed('liushan'))throw Error('Later office or rank erased a witnessed audience');
              const frozen=JSON.stringify(state);civicPanel();militaryPanel();npcFacts('liushan');npcMemories('liushan');if(JSON.stringify(state)!==frozen)throw Error('Historical court views mutated state');
              const forged=clone(state);forged.civicCareer.shuPetition224.departureRank='Grand General';if(auh5jEvidence(forged))throw Error('Forged departure grade survived');
             }finally{save=a;render=b;scrollTopNow=c;}
            }""",seeds[1])
            # Full-history former Grand General with no active troops travels,
            # receives an audience, returns and still has exactly zero troops.
            p.evaluate('s=>{state=clone(s);activeTab="story";render();}',seeds[7]);clicks=0
            while p.evaluate('state.scene')!='ch12_c62_01_seals_225':
                assert clicks<10
                p.evaluate('()=>{state.pageIndex=paginateStory(SCENES[state.scene].body(state)).length-1;render();}')
                scene=p.evaluate('state.scene');index=p.evaluate('SCENES[state.scene].choices(state).findIndex(o=>o.next==="m4_224_petition")') if scene=='ch12_01' else (1 if scene in ('m4_224_petition','m4_224_chancery') else 0)
                p.locator(f'[data-choice="{index}"]' if index else '[data-choice="0"], [data-action="next-scene"]').click();clicks+=1
            assert clicks==7 and p.evaluate('auh5jEvidence(state)&&auh5jLeave(state)&&state.civicCareer.shuPetition224.royalAudience&&hasWitnessed("liushan")&&state.militaryCareer.rank==="Grand General"&&auh5iRoll(state).length===0&&state.storyClock.year===225&&state.age===51&&!auh79Emperor(state)&&!auh65Crowned(state)')
            p.reload();assert p.evaluate('auh5jEvidence(state)&&hasWitnessed("liushan")')
            p.locator('#menuToggle').click();p.locator('#gameMenu [data-nav="civic"]').click();assert p.locator('[aria-label="Shu court petition in 224"]').is_visible()
            p.locator('#menuToggle').click();p.locator('#gameMenu [data-nav="people"]').click();p.locator('[data-people-gender="male"]').click();p.locator('[data-people-category="neutral"]').click();assert p.locator('.npc-card').filter(has_text='Liu Shan').is_visible()
            assert p.evaluate('document.documentElement.scrollWidth<=innerWidth')
            with tempfile.TemporaryDirectory() as folder:
                with p.expect_download() as dl:p.evaluate('exportSave()')
                exported=Path(folder)/'court.json';dl.value.save_as(exported);data=json.loads(exported.read_text());assert data['civicCareer']['shuPetition224']['result']=='case_registered'
                p.on('dialog',lambda dialog:dialog.accept());p.locator('#importFile').set_input_files(exported);p.wait_for_function('banner.includes("Save imported and verified")');assert p.evaluate('auh5jEvidence(state)&&auh5iTigerEvidence(state)&&auh5iRoll(state).length===0')
            assert not errors,errors
            result['checks'].append({'width':width,'routes_eight_organic_career_charter_custody_profiles':1080,'all_purpose_method_route_hearing_response_paths_and_five_results':'PASS','actual_audience_vs_relay_and_unverified_private_no_audience':'PASS','rank_muster_custody_staff_offices_inventory_relationships_unchanged':'PASS','no_crown_succession_or_ministry_grant':'PASS','224_to_225_once_and_old_age_legacy_later_post_guards':'PASS','readonly_provenance_json_resolve':'PASS','governor_admission_captain_denial_historical_office_loss':'PASS','reply_changes_return_hearing_civic_actual_memory':'PASS','full_history_dom_choices':clicks,'grand_general_zero_force_export_file_import_reload_people_civic':'PASS','registry':len(current),'page_errors':errors});context.close()
    result['limits']='Eight selected prior career/custody/charter profiles generated via original handlers, including accepted Sixth Tiger and actual 223 handover. Governor/later-post/older-age comparators synthetic. Full canonical new local paths, not all prior worlds/relationships. Matrix compacts historical bodies and suppresses paint/storage; seven DOM choices keep full history. This is M4-A court foundation, not Shu enthronement/imperial first decision, Issue #1/#2 or real-device file:// certification.'
    write_report(result,args.report)
if __name__=='__main__':main()
