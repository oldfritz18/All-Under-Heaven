#!/usr/bin/env python3
"""Played extraordinary Shu mandate, accession, first policy and 226–227 consequences."""
import argparse,json,tempfile
from pathlib import Path
from qa_support import fixture,write_report,DRAGON_NOMINATION_227_SCENES, HAN_DRAGON_229_SCENES
from qa_court224 import organic_court_seeds,TO_XII
from qa_designation221 import organic_designation_seed
BASELINE='5d35c4e:GAME/ALL_UNDER_HEAVEN_v0.4.99.5k_THE_UNSEALED_SUCCESSION.html'
NEW={'m4_225_reopen','m4_225_journey','m4_225_chamber','m4_225_liushan','m4_225_objections','m4_225_mandate','m4_225_vigil','m4_225_investiture','m4_225_proclamation','m4_225_private','m4_225_administration','m4_225_decree','m4_226_audit','m4_226_return','m4_225_closed'}
TO_225=r"""s=>{state=clone(s);const a=save,b=render,c=scrollTopNow;save=()=>{};render=()=>{};scrollTopNow=()=>{};try{for(const n of [SCENES[state.scene].choices(state).findIndex(o=>o.next==='m4_224_petition'),1,0,0,1,0,0]){const sc=SCENES[state.scene];state.pageIndex=paginateStory(sc.body(state)).length-1;choose(n);if(sc.id===state.scene)throw Error('225 seed '+sc.id+':'+banner);}return clone(state);}finally{save=a;render=b;scrollTopNow=c;}}"""

def organic_accession_seeds(p):
    seeds=organic_court_seeds(p)
    designation=organic_designation_seed(p)
    designation=p.evaluate(r"""s=>{state=clone(s);const a=save,b=render,c=scrollTopNow;save=()=>{};render=()=>{};scrollTopNow=()=>{};try{for(const n of [SCENES[state.scene].choices(state).findIndex(o=>o.next==='m4_221_summons'),0,0,0,0,0,0]){const sc=SCENES[state.scene];state.pageIndex=paginateStory(sc.body(state)).length-1;choose(n);if(sc.id===state.scene)throw Error('Designation seed');}return clone(state);}finally{save=a;render=b;scrollTopNow=c;}}""",designation)
    seeds.append(p.evaluate(TO_XII,{'seed':designation,'review':0,'custody':1,'mandate':1}))
    return [p.evaluate(TO_225,s) for s in seeds]

MATRIX=r"""cfg=>{
 const input=clone(cfg.seed);for(const h of input.history)h.body='';const a=save,b=render,c=scrollTopNow;save=()=>{};render=()=>{};scrollTopNow=()=>{};const rows=[];let example=null,gate=null;
 const step=i=>{const sc=SCENES[state.scene];state.pageIndex=paginateStory(sc.body(state)).length-1;choose(i);if(sc.id===state.scene||!validSave(state))throw Error('Accession blocked '+sc.id+':'+banner);};
 const enter=(request,chamber=0,terms=0,account=0)=>{state=clone(input);activeTab='story';step(SCENES[state.scene].choices(state).findIndex(o=>o.next==='m4_225_reopen'));step(request);step(0);step(chamber);step(terms);step(account);if(state.scene!==(account===2?'m4_225_closed':'m4_225_mandate'))throw Error('Mandate not reached');};
 const check=crowned=>{if(auh5lShu(state)!==crowned||auh65Crowned(state)||auh79Emperor(state)||auh79RegionsEarned(state))throw Error('Authority conflated');const m=clone(state.militaryCareer);delete m.leave225;if(JSON.stringify(m)!==JSON.stringify(input.militaryCareer))throw Error('Accession changed military commission/muster/staff');for(const k of ['coins','items','relationships','innerCircle','dragonGenerals','health','realmNames'])if(JSON.stringify(state[k])!==JSON.stringify(input[k]))throw Error('Unchosen grant '+k);const frozen=JSON.stringify(state);civicPanel();militaryPanel();characterPanel();npcFacts('liushan');npcMemories('zhugeliang');auh5lAccede(state);auh5lDecree(state,'relief');auh5lAudit(state,'uphold');auh5lClose(state);if(JSON.stringify(state)!==frozen)throw Error('View/replay mutation');const restored=resolve(JSON.parse(JSON.stringify(state)));if(!validSave(restored)||auh5lShu(restored)!==crowned)throw Error('Accession lost on resolve');};
 const finish=(vow=0,privateAnswer=0,admin=0,policy=0,review=0)=>{if(state.scene!=='m4_225_vigil'||auh5lShu(state))throw Error('Premature crown');step(vow);if(auh5lShu(state))throw Error('Vigil became crown');step(0);if(!auh5lShu(state)||state.scene!=='m4_225_proclamation')throw Error('Oath did not accede');step(0);step(privateAnswer);step(admin);step(policy);if(state.storyClock.year!==226||state.age!==input.age+1||!auh5lPolicy(state))throw Error('Policy calendar/proof');step(review);if(!auh5lReview(state))throw Error('No policy review');step(0);if(state.scene!=='ch12_c62_02_frontier_227'||state.storyClock.year!==227||state.age!==input.age+2)throw Error('227 continuation');check(true);if(auh5lChancellor(state)!==(admin===0)||!!state.civicCareer.imperialOfficials?.chief!==(admin===0))throw Error('Chancellor confirmation/deferral');if(!SCENES[state.scene].body(state).includes({uphold:'first decree remains',amend:'both household and garrison',cancel:'broad decree is closed'}[state.civicCareer.shuPolicyReview226.answer]))throw Error('Cross-year policy callback');if(auhProtagonistPortraitStage(state)!=='emperor'||i84Family(state)!=='sovereign')throw Error('Portrait/ending scope');const ending=SCENES.lifetime_E01.body(state);if(!ending.includes('not a settlement of Wei and Wu'))throw Error('Shu-only ending scope');example=clone(state);};
 const close=()=>{step(0);if(state.scene!=='ch12_c62_01_seals_225'||state.storyClock.year!==225||state.age!==input.age||!state.flags.m4_225_hearing_closed)throw Error('Refusal/relay close');check(false);};
 try{
  for(let request=0;request<3;request++)for(let chamber=0;chamber<2;chamber++)for(let terms=0;terms<3;terms++)for(let account=0;account<2;account++){
   enter(request,chamber,terms,account);const qualified=auh5lQualified(state);const expected=['General','Grand General'].includes(input.militaryCareer.rank)&&request!==1&&(request!==2||chamber===1)&&terms!==2&&account===0;if(qualified!==expected)throw Error('Court consent gate');const offered=clone(state);if(qualified)gate=clone(state);
   for(const answer of ['refused','deferred',...(qualified?['accepted']:[])]){state=clone(offered);const ix=answer==='accepted'?0:qualified?(answer==='refused'?1:2):(answer==='refused'?0:1);step(ix);if(answer==='accepted')finish();else close();rows.push({kind:'court',request,chamber,terms,account,answer});}
  }
  for(let request=0;request<3;request++){
   for(const method of ['relay','deferred']){state=clone(input);step(SCENES[state.scene].choices(state).findIndex(o=>o.next==='m4_225_reopen'));step(request);step(method==='relay'?1:2);if(state.civicCareer.shuHearingVisit225||state.militaryCareer.leave225)throw Error('Remote presence grant');close();rows.push({kind:'remote',request,method});}
   state=clone(input);step(SCENES[state.scene].choices(state).findIndex(o=>o.next==='m4_225_reopen'));step(request);step(0);step(2);close();rows.push({kind:'withdraw',request});
   enter(request,0,0,2);close();rows.push({kind:'defer_hearing',request});
  }
  if(cfg.full){for(let vow=0;vow<3;vow++)for(let personal=0;personal<3;personal++)for(let admin=0;admin<2;admin++)for(let policy=0;policy<3;policy++)for(let review=0;review<3;review++){enter(0);step(0);finish(vow,personal,admin,policy,review);rows.push({kind:'policy',vow,personal,admin,policy,review});}
   enter(0);step(0);step(3);close();rows.push({kind:'vigil_withdraw'});for(let vow=0;vow<3;vow++){enter(0);step(0);step(vow);step(1);close();rows.push({kind:'oath_withdraw',vow});}
  }
  return {rows,example,gate};
 }finally{save=a;render=b;scrollTopNow=c;}
}"""

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--report',type=Path);args=ap.parse_args()
    with fixture(BASELINE) as (browser,url,result):
        p=browser.new_page();p.goto(url+'/baseline.html');seeds=organic_accession_seeds(p);ids=set(p.evaluate('Object.keys(SCENES)'));staff=p.evaluate('AUH_MC_SPECIAL_STAFF');p.close()
        for width in (390,1280):
            ctx=browser.new_context(viewport={'width':width,'height':900});p=ctx.new_page();errors=[];p.on('pageerror',lambda e:errors.append(str(e)));p.goto(url+'/active.html');assert not errors,errors;assert p.evaluate('auh5lShu(null)===false');current=set(p.evaluate('Object.keys(SCENES)'));assert ids<=current and current-ids in (NEW,NEW|DRAGON_NOMINATION_227_SCENES,NEW|DRAGON_NOMINATION_227_SCENES|HAN_DRAGON_229_SCENES) and len(current) in (716,728,742);assert p.evaluate('AUH_MC_SPECIAL_STAFF')==staff
            runs=[p.evaluate(MATRIX,{'seed':s,'full':i in (4,7,8)}) for i,s in enumerate(seeds)]
            rows=[r for run in runs for r in run['rows']];assert len(rows)==1284,len(rows)
            ex=runs[7]['example'];assert ex and ex['civicCareer']['shuMandate225']['basis']=='new_mandate225';assert runs[8]['example']['civicCareer']['shuMandate225']['basis']=='witnessed_conditional_designation221'
            old=ctx.new_page();old.goto(url+'/baseline.html');legacy=r"""seed=>{const states=[clone(seed)];const king=clone(seed);Object.assign(king.flags,{auh60_223:'independent',auh65_territory_held:true,auh65_council_approved:true,auh65_frontier_secured:true,auh65_crown_accepted:true,sovereign_title_earned:true,sovereign_claim_ratified:true});states.push(king);const union=clone(king);Object.assign(union.flags,{auh79_north:'settled',auh79_west:'settled',auh79_east:'settled',auh79_congress:'ratified',auh79_imperial_oath:true});states.push(union);return states.map(s=>{state=s;return {king:auh65Crowned(s),union:auh79Emperor(s),social:auh63SocialPosition(s),portrait:auhProtagonistPortraitStage(s),family:i84Family(s),civic:civicPanel(),military:militaryPanel(),ending:SCENES.lifetime_E01.body(s),body:SCENES.ch12_c62_01_seals_225.body(s),choices:SCENES.ch12_c62_01_seals_225.choices(s).filter(o=>o.next!=='m4_225_reopen').map(o=>{const x=clone(s);o.effect(x);return {label:o.label,next:o.next,state:x};})};});}""";before=old.evaluate(legacy,seeds[7]);assert before[1]['king'] and before[2]['union'];assert p.evaluate(legacy,seeds[7])==before;old.close()
            p.evaluate(r"""cfg=>{
             const hist=clone(cfg.example);hist.visited=[];if(!auh5lShu(hist)||!auh5lReview(hist))throw Error('History-only crown');const flags=clone(cfg.example);flags.history=[];flags.visited=[];if(auh5lShu(flags)||auh5lPolicy(flags)||auh5lMetShan(flags))throw Error('Flags-only crown');
             const bad=clone(cfg.example);bad.civicCareer.shuMandate225.liushanConsent=false;if(auh5lShu(bad))throw Error('No-consent crown');const wrong=clone(cfg.example);wrong.civicCareer.shuAccession225.scope='China';if(auh5lShu(wrong))throw Error('Wrong-scope crown');const prior=clone(cfg.example);prior.storyClock.year=224;if(auh5lShu(prior))throw Error('Future crown leaked');
             const later=clone(cfg.example);later.relationships.liubei.trust=0;later.militaryCareer.rank='Private';later.storyClock.year=235;later.militaryCareer.fieldPosition={year:235,active:true,proof:'later'};if(!auh5lShu(later)||!auh5lReview(later))throw Error('Later military rank erased civil office');
             state=clone(cfg.seed);const frozen=JSON.stringify(state);civicPanel();militaryPanel();characterPanel();if(state.civicCareer.shuAccession225||JSON.stringify(state)!==frozen)throw Error('Legacy migration grant');
             const gate=clone(cfg.gate);gate.civicCareer.shuHearingVisit225.direct=false;if(auh5lQualified(gate))throw Error('No direct consent hearing accepted');
             const displaced=clone(cfg.gate);displaced.militaryCareer.fieldPosition={year:229,active:true,proof:'later'};const unchanged=JSON.stringify(displaced);auh5lMandate(displaced,'accepted');if(JSON.stringify(displaced)!==unchanged||auh5lShu(displaced))throw Error('Later posting received dated mandate');
             const a=save,b=render,c=scrollTopNow;save=()=>{};render=()=>{};scrollTopNow=()=>{};try{
              state=clone(cfg.seed);state.age=69;const step=i=>{const sc=SCENES[state.scene];state.pageIndex=paginateStory(sc.body(state)).length-1;choose(i);if(sc.id===state.scene)throw Error('Negative route blocked '+sc.id+':'+banner);};step(SCENES[state.scene].choices(state).findIndex(o=>o.next==='m4_225_reopen'));step(0);const journey=clone(state);for(const invalid of ['active','later','unknown']){const x=clone(journey);if(invalid==='active')x.militaryCareer.fieldPosition.active=true;if(invalid==='later')x.militaryCareer.fieldPosition={year:229,active:false};if(invalid==='unknown')x.militaryCareer.units=[{id:'borrowed',source:'unknown',active:true,infantry:100,cavalry:0,archers:0}];const f=JSON.stringify(x);auh5lJourney(x,'personal');if(auh5lCanTravel(x)||JSON.stringify(x)!==f)throw Error('Invalid duty travel '+invalid);}
              for(let n=0;n<20&&state.scene!=='ch12_c62_02_frontier_227';n++)step(0);if(!auh5lShu(state)||state.age!==71||state.storyClock.year!==227)throw Error('Older age reset');
             }finally{save=a;render=b;scrollTopNow=c;}
            }""",{'seed':seeds[7],'example':ex,'gate':runs[7]['gate']})
            # Full-history DOM, no active troops: deliberate fresh mandate → oath
            # → policy → consequence. No backfilled Liu Bei designation.
            p.evaluate('s=>{state=clone(s);activeTab="story";render();}',seeds[7]);clicks=0
            while p.evaluate('state.scene')!='ch12_c62_02_frontier_227':
                assert clicks<20;p.evaluate('()=>{state.pageIndex=paginateStory(SCENES[state.scene].body(state)).length-1;render();}')
                scene=p.evaluate('state.scene');index=p.evaluate('SCENES[state.scene].choices(state).findIndex(o=>o.next==="m4_225_reopen")') if scene=='ch12_c62_01_seals_225' else (1 if scene in ('m4_225_private','m4_225_administration','m4_225_decree','m4_226_audit') else 0)
                p.locator(f'[data-choice="{index}"]' if index else '[data-choice="0"], [data-action="next-scene"]').click();clicks+=1
            assert clicks==15 and p.evaluate('auh5lShu(state)&&auh5lReview(state)&&!auh5lChancellor(state)&&auh5iRoll(state).length===0&&state.age===53&&state.storyClock.year===227&&!auh5kEvidence(state)&&!auh79Emperor(state)&&!auh65Crowned(state)')
            p.reload();assert p.evaluate('auh5lShu(state)&&auh5lReview(state)')
            for tab,selector in [('character','.character-facts'),('civic','[aria-label="Shu imperial administration"]'),('military','[aria-label="Shu imperial command"]')]:
                p.locator('#menuToggle').click();p.locator(f'#gameMenu [data-nav="{tab}"]').click();assert p.locator(selector).is_visible();assert 'Emperor of Shu' in p.locator('main').inner_text() if p.locator('main').count() else 'Emperor of Shu' in p.locator('body').inner_text()
            assert p.evaluate('document.documentElement.scrollWidth<=innerWidth')
            with tempfile.TemporaryDirectory() as folder:
                with p.expect_download() as dl:p.evaluate('exportSave()')
                path=Path(folder)/'shu.json';dl.value.save_as(path);data=json.loads(path.read_text());assert data['civicCareer']['shuAccession225']['scope']=='Shu-Han' and data['dragonGenerals']['active']==[]
                p.on('dialog',lambda d:d.accept());p.locator('#importFile').set_input_files(path);p.wait_for_function('banner.includes("Save imported and verified")');assert p.evaluate('auh5lShu(state)&&auh5lReview(state)&&auh5iRoll(state).length===0')
            assert not errors,errors
            result['checks'].append({'width':width,'canonical_local_paths':len(rows),'court_decision_paths':sum(r['kind']=='court' for r in rows),'journey_withdraw_defer_paths':sum(r['kind'] in ('remote','withdraw','defer_hearing') for r in rows),'ceremony_private_office_policy_review_combinations':sum(r['kind']=='policy' for r in rows),'last_vigil_oath_withdrawals':sum(r['kind'] in ('vigil_withdraw','oath_withdraw') for r in rows),'nine_organic_prior_profiles_fresh_vs_221_designation':'PASS','legacy_regional_and_union_projection_parity':'PASS','no_military_resources_relationships_staff_dragons_or_union_grants':'PASS','consent_history_scope_future_age_legacy_readonly_replay_resolve':'PASS','full_history_dom_choices':clicks,'zero_force_fresh_mandate_chancellor_defer_three_menus_export_import_reload':'PASS','registry':len(current),'page_errors':errors});ctx.close()
    result['limits']='Nine selected original-handler career/custody histories, including actual 221 designation and fresh mandate with no testament. Court decision grid exhaustive within enumerated five decisions; ceremony/private/office/policy/review Cartesian only on three selected qualified profiles, not all prior histories/worlds. Synthetic older/later/unknown/no-consent and legacy regional/union comparator states. Matrix compacts prior history and suppresses paint/storage; fifteen DOM clicks full history. This verifies M4-B and limited Chancellor/first policy integration, not full M4-C Dragons/M5–M7/XIX/Epilogue or physical file:// device QA.'
    write_report(result,args.report)
if __name__=='__main__':main()
