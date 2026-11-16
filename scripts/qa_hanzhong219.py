#!/usr/bin/env python3
"""M3-B: western service, earned early General and separate Sixth Tiger arc."""
import argparse,json,tempfile
from pathlib import Path
from qa_support import fixture,write_report,COURT_224_SCENES,DESIGNATION_221_SCENES, SHU_ACCESSION_225_SCENES
from qa_jing219 import START,ADVANCE,TO_HANJIN,TO_FLOTILLA,TO_ANCHORS,TO_TIDE,TO_BORDER,TO_JING

BASELINE='90e0d40:GAME/ALL_UNDER_HEAVEN_v0.4.99.5h_THE_ACCEPTED_STANDARD.html'
NEW={'m3_218_hanzhong_request','m3_218_hanzhong_road','m3_219_hanzhong_council','m3_219_hanzhong_orders','m3_219_hanzhong_clash','m3_219_hanzhong_return','m3_219_hanzhong_warrant','m3_219_hanzhong_hearing','m3_219_tiger_council','m3_219_tiger_standard','m3_219_tiger_first_orders','m3_219_tiger_aftermath','m3_219_west_homeward'}

def organic_seeds(page):
    starts=[page.evaluate(START,d) for d in (False,True)]
    early=[page.evaluate(ADVANCE,{'seed':s['snapshots']['ch08_pb55_xushu'],'decision':d}) for s in starts for d in (0,1)]
    anchors=[page.evaluate(TO_ANCHORS,{'seed':page.evaluate(TO_FLOTILLA,page.evaluate(TO_HANJIN,s)),'weak':False}) for s in early]
    borders=[page.evaluate(TO_BORDER,page.evaluate(TO_TIDE,{'seed':s,'world':'south'})) for s in anchors]
    seeds=[page.evaluate(TO_JING,{'seed':s})['at218'] for s in borders]
    seeds.append(page.evaluate(TO_JING,{'seed':borders[0],'west':True})['at218'])
    assert [s['militaryCareer']['rank'] for s in seeds]==['Captain','Sergeant','Sergeant','Private','Major']
    return seeds

CAMPAIGNS=r"""seed=>{
 const input=clone(seed);for(const h of input.history)h.body='';
 const a=save,b=render,c=scrollTopNow;save=()=>{};render=()=>{};scrollTopNow=()=>{};const rows=[];let gate=null,contact=null,accepted=null;
 const step=i=>{const sc=SCENES[state.scene];state.pageIndex=paginateStory(sc.body(state)).length-1;choose(i);if(sc.id===state.scene||!validSave(state))throw Error('Hanzhong blocked '+sc.id+':'+banner);};
 try{for(const branch of ['Infantry','Cavalry'])for(let mission=0;mission<3;mission++)for(let role=0;role<3;role++)for(let action=0;action<3;action++)for(let report=0;report<3;report++){
  state=clone(input);activeTab='story';if(branch==='Cavalry'){state.militaryCareer.combatService={branch,unit:'Synthetic lawful mounted rotation',commander:'Recorded receiving officer',year:218,proof:'legacy:lawful-cavalry'};for(const u of state.militaryCareer.units)if(u.active!==false){u.cavalry=state.militaryCareer.rank==='Sergeant'?20:30;u.infantry=0;}}
  const before=clone(state),ix=SCENES[state.scene].choices(state).findIndex(o=>o.next==='m3_218_hanzhong_request');if(ix<0)throw Error('Western rotation missing');step(ix);step(0);accepted=clone(state);
  if(!auh5iRotation(state)||auh5iBattle(state)||state.storyClock.year!==218||state.age!==before.age)throw Error('Request became participation');
  step(0);if(state.storyClock.year!==219||state.age!==before.age+1)throw Error('Travel did not advance once');
  if(auh5iMet(state,'huangzhong')||auh5iMet(state,'machao'))throw Error('News became meeting');
  step(mission);if(!auh5iMet(state,'huangzhong')||!auh5iMet(state,'zhaoyun')||auh5iMet(state,'machao')||!state.militaryCareer.fieldPosition.active)throw Error('Council/issued position');
  if(npcMemories('zhaoyun').some(t=>t.includes('checked your local return')))throw Error('Future return memory');
  step(role);contact=clone(state);step(action);if(!auh5iBattle(state)||state.militaryCareer.fieldPosition.active)throw Error('Contact not received');step(report);
  if(state.scene!=='m3_219_hanzhong_warrant'||state.militaryCareer.rank!==before.militaryCareer.rank)throw Error('Unaccepted promotion');
  const offer=auh5iGeneralOffer(state),expected=before.militaryCareer.rank==='Major'&&report===0&&((mission===0&&action===1)||(mission===1&&action===0));
  if(!!offer!==expected)throw Error('Early General merit mismatch '+JSON.stringify({mission,role,action,report,rank:before.militaryCareer.rank}));
  if(JSON.stringify(state.militaryCareer.units)!==JSON.stringify(before.militaryCareer.units)||JSON.stringify(state.militaryCareer.appointmentHistory)!==JSON.stringify(before.militaryCareer.appointmentHistory))throw Error('Battle manufactured muster/appointment');
  for(const k of ['staff','rankProof','superior','commissionAuthority'])if(JSON.stringify(state.militaryCareer[k])!==JSON.stringify(before.militaryCareer[k]))throw Error('Battle changed '+k);
  for(const k of ['coins','items','innerCircle','dragonGenerals','civicCareer','relationships','health'])if(JSON.stringify(state[k])!==JSON.stringify(before[k]))throw Error('Battle unchosen grant '+k);
  if(state.militaryCareer.legendaryGroup||auh65Crowned(state)||auh79Emperor(state)||auh5iTigerEvidence(state))throw Error('Battle granted title');
  if(state.militaryCareer.campaignEvidence.hanzhong219.wound!==((role===1&&action===0)?'forearm_cut':null))throw Error('Personal combat wound');
  rows.push({rank:before.militaryCareer.rank,branch,mission,role,action,report,result:state.militaryCareer.campaignEvidence.hanzhong219.result,offered:!!offer});
  if(expected&&branch==='Infantry'&&mission===0&&role===0&&action===1)gate=clone(state);
 }return {rows,gate,contact,accepted};}finally{save=a;render=b;scrollTopNow=c;}
}"""
CEREMONIES=r"""gate=>{
 const a=save,b=render,c=scrollTopNow;save=()=>{};render=()=>{};scrollTopNow=()=>{};const rows=[];let example=null,proposal=null,commission=null;
 const step=i=>{const sc=SCENES[state.scene];state.pageIndex=paginateStory(sc.body(state)).length-1;choose(i);if(sc.id===state.scene||!validSave(state))throw Error('Tiger blocked '+sc.id+':'+banner);};
 try{for(let warrant=0;warrant<3;warrant++)for(let hearing=0;hearing<3;hearing++){
  state=clone(gate);step(warrant);const commissioned=clone(state);if(auh5iGeneralEvidence(state)!==(warrant===0)||state.militaryCareer.rank!==(warrant===0?'General':'Major'))throw Error('Accepted early warrant');
  step(hearing);const council=clone(state);if(!auh5iHeardCourt(state)||!auh5iMet(state,'machao')||!auh5iMet(state,'liubei')||!!auh5iTigerOffer(state)!==(warrant===0))throw Error('Royal hearing/merit');
  for(let offer=0;offer<(warrant===0?3:1);offer++)for(let final=0;final<((warrant===0&&offer===0)?5:1);final++)for(let duty=0;duty<3;duty++)for(let after=0;after<3;after++){
   state=clone(council);step(offer);proposal=clone(state);const beforeInvest=clone(state);
   if(warrant===0&&offer===0)step(final);
   const tiger=warrant===0&&offer===0&&final<3;
   if(auh5iTigerEvidence(state)!==tiger||auhMcVerifiedCareerRank(state)!==(tiger?'Grand General':warrant===0?'General':'Major'))throw Error('Unearned/refused legendary rank');
   if(JSON.stringify(state.militaryCareer.units)!==JSON.stringify(commissioned.militaryCareer.units))throw Error('Honour created troops');
   if(state.militaryCareer.appointmentHistory.length!==gate.militaryCareer.appointmentHistory.length+(warrant===0?1:0)+(tiger?1:0))throw Error('Repeated appointment');
   if(warrant===0&&!auh5iGeneralUnits(auh5iRoll(state)))throw Error('Wrong reformed force');
   if(warrant!==0&&JSON.stringify(state.militaryCareer.units)!==JSON.stringify(gate.militaryCareer.units))throw Error('Refused General changed roll');
   if(!tiger&&warrant===0)for(const k of ['rankProof','superior','commissionAuthority'])if(JSON.stringify(state.militaryCareer[k])!==JSON.stringify(commissioned.militaryCareer[k]))throw Error('Refused Tiger changed '+k);
   if(tiger&&npcMemories('hansheng').some(t=>t.includes('After the Hanzhong recognition he sat')))throw Error('Future private aftermath memory');
   commission=clone(state);step(duty);if(!state.militaryCareer.fieldPosition.active||state.militaryCareer.fieldPosition.proof!=='m3_5i:royal_return219')throw Error('First duty not actual');step(after);if(state.militaryCareer.fieldPosition.active)throw Error('First duty not closed');step(0);
   if(state.scene!=='ch10_c58_07_jing_219'||state.storyClock.year!==219||state.age!==gate.age||!state.flags.m3_hanzhong_home||auh5iTigerEvidence(state)!==tiger)throw Error('Eastern return/age');
   for(const k of ['coins','items','innerCircle','dragonGenerals','civicCareer','relationships','health'])if(JSON.stringify(state[k])!==JSON.stringify(gate[k]))throw Error('Ceremony unchosen grant '+k);
   if(JSON.stringify(state.militaryCareer.staff)!==JSON.stringify(gate.militaryCareer.staff)||auh65Crowned(state)||auh79Emperor(state))throw Error('Staff/crown awarded');
   const frozen=JSON.stringify(state);militaryPanel();civicPanel();npcMemories('machao');auh63SocialPosition(state);auh5iInvest(state,'duty');auh5iWarrant(state,'accepted');auh5iClose(state,'listen');auh5iDuty(state,'lead');auh5iPosition(state,'contact',true);if(JSON.stringify(state)!==frozen)throw Error('Views/replay mutation');
   const restored=resolve(JSON.parse(JSON.stringify(state)));if(!validSave(restored)||auh5iTigerEvidence(restored)!==tiger)throw Error('Resolve lost evidence');
   if(tiger&&!auh63SocialPosition(state).position.includes('Sixth Tiger General'))throw Error('Character honour missing');
   rows.push({warrant,hearing,offer,final,duty,after,tiger});if(tiger)example=clone(state);
  }
 }return {rows,example,proposal,commission};}finally{save=a;render=b;scrollTopNow=c;}
}"""

def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--report',type=Path);args=parser.parse_args()
    with fixture(BASELINE) as (browser,url,result):
        base=browser.new_page();base.goto(url+'/baseline.html');seeds=organic_seeds(base);ids=set(base.evaluate('Object.keys(SCENES)'));roles=base.evaluate('AUH_MC_SPECIAL_STAFF');base.close()
        for width in (390,1280):
            context=browser.new_context(viewport={'width':width,'height':900});p=context.new_page();errors=[];p.on('pageerror',lambda e:errors.append(str(e)));p.goto(url+'/active.html')
            current=set(p.evaluate('Object.keys(SCENES)'));assert ids<=current and current-ids in (NEW,NEW|COURT_224_SCENES,NEW|COURT_224_SCENES|DESIGNATION_221_SCENES,NEW|COURT_224_SCENES|DESIGNATION_221_SCENES|SHU_ACCESSION_225_SCENES) and len(current)==len(ids)+len(current-ids)
            assert p.evaluate('AUH_MC_SPECIAL_STAFF')==roles
            campaigns=[p.evaluate(CAMPAIGNS,s) for s in seeds];assert sum(len(r['rows']) for r in campaigns)==810
            assert len({r['result'] for c in campaigns for r in c['rows']})==9
            good=campaigns[4]['gate'];assert good
            ceremonial=p.evaluate(CEREMONIES,good);assert len(ceremonial['rows'])==243
            # A mounted profile is established before the new order/rotation,
            # so the game itself writes its branch evidence. Original career
            # histories remain organic; this service/muster variant is synthetic.
            mounted=p.evaluate(r"""s=>{const x=clone(s);x.militaryCareer.combatService={branch:'Cavalry',unit:'Synthetic lawful mounted rotation',commander:'Recorded officer',year:218,proof:'legacy:lawful-cavalry'};for(const u of x.militaryCareer.units)if(u.active!==false){u.infantry=0;u.cavalry=30;}return x;}""",seeds[4])
            # Reach a mounted receipt through the original choice handlers.
            mounted_gate=p.evaluate(r"""s=>{state=clone(s);const a=save,b=render,c=scrollTopNow;save=()=>{};render=()=>{};scrollTopNow=()=>{};try{for(let i=0;i<12;i++){if(state.scene==='m3_219_hanzhong_warrant')return clone(state);const sc=SCENES[state.scene],n=sc.id==='ch10_c58_06_frontier_218'?sc.choices(state).findIndex(o=>o.next==='m3_218_hanzhong_request'):sc.id==='m3_219_hanzhong_clash'?1:0;state.pageIndex=paginateStory(sc.body(state)).length-1;choose(n);if(state.scene===sc.id)throw Error(sc.id+':'+banner);}throw Error('Mounted gate');}finally{save=a;render=b;scrollTopNow=c;}}""",mounted)
            mounted_ceremony=p.evaluate(CEREMONIES,mounted_gate);assert len(mounted_ceremony['rows'])==243
            old=context.new_page();old.goto(url+'/baseline.html')
            parity=r"""s=>['ch10_c58_06_frontier_218','ch10_c58_07_jing_219','ch11_01','ch12_01','i84_lifetime_sovereign','i84_lifetime_general','i84_lifetime_final'].map(id=>({id,body:SCENES[id].body(s),choices:SCENES[id].choices(s).filter(o=>o.next!=='m3_218_hanzhong_request').map(o=>{const x=clone(s);o.effect(x);return {label:o.label,next:o.next,state:x};})}))"""
            assert p.evaluate(parity,seeds[4])==old.evaluate(parity,seeds[4]);old.close()
            p.evaluate(r"""cfg=>{
             const e=cfg.ceremony.example;const changed=clone(e);changed.relationships.liubei.trust=-4;if(!auh5iTigerEvidence(changed)||auhMcVerifiedCareerRank(changed)!=='Grand General')throw Error('Later relationship erased historical commission');
             const hist=clone(e);hist.visited=[];if(!auh5iBattle(hist)||!auh5iTigerEvidence(hist))throw Error('History-only evidence');
             const flags=clone(e);flags.history=[];flags.visited=[];if(auh5iBattle(flags)||auh5iTigerEvidence(flags)||auhMcVerifiedCareerRank(flags))throw Error('Flag-only appointment');
             for(const key of ['authority','rank','proof','vow']){const x=clone(e);x.militaryCareer.sixthTiger219[key]='invented';if(auh5iTigerEvidence(x))throw Error('Invalid Tiger '+key);}
             const invalid=clone(e);invalid.militaryCareer.campaignEvidence.hanzhong219.account='invented';if(auh5iBattle(invalid)||auh5iTigerEvidence(invalid))throw Error('Invalid combat account');
             const noPrior=clone(cfg.gate);noPrior.militaryCareer.appointmentHistory.find(a=>a.proof==='auh3e:m3_216_baxi_review:military').rank='Captain';if(auh5iGeneralOffer(noPrior))throw Error('Unproved prior Major');
             const badRoll=clone(cfg.gate);badRoll.militaryCareer.units.find(u=>u.active!==false).source='unknown';if(auh5iGeneralOffer(badRoll))throw Error('Unknown muster promoted');
             const blockedRoad=clone(cfg.accepted);blockedRoad.militaryCareer.fieldPosition.year=222;const roadBefore=JSON.stringify(blockedRoad);auh5iArrive(blockedRoad);if(JSON.stringify(blockedRoad)!==roadBefore)throw Error('Later posting advanced travel');
             const later=clone(cfg.contact);later.militaryCareer.fieldPosition={year:222,active:true,proof:'later:kept'};const frozen=JSON.stringify(later);auh5iFight(later,'counter');auh5iPosition(later,'received',false);if(JSON.stringify(later)!==frozen||auh5iCurrent(later))throw Error('Later post overwritten');
             const same=clone(cfg.contact);same.militaryCareer.fieldPosition={year:219,active:true,proof:'other:kept'};const sameFrozen=JSON.stringify(same);auh5iFight(same,'hold');if(JSON.stringify(same)!==sameFrozen)throw Error('Other 219 post overwritten');
             const unseen=clone(cfg.seed);delete unseen.militaryCareer.combatService;if(auh5iEntry(unseen))throw Error('Unknown service branch');
             const legacy=resolve(clone(cfg.seed));state=legacy;const before=JSON.stringify(state);militaryPanel();npcMemories('machao');if(state.militaryCareer.hanzhongRotation||state.militaryCareer.sixthTiger219||JSON.stringify(state)!==before)throw Error('Legacy backfill');
             const gov=clone(e);gov.civicCareer.appointed=true;gov.civicCareer.office='Governor';gov.civicCareer.territory='Existing province';state=gov;if(!auhMcCivicOffice(state)||!civicPanel().includes('Governor'))throw Error('Existing Governor erased');
             const a=save,b=render,c=scrollTopNow;save=()=>{};render=()=>{};scrollTopNow=()=>{};
             const step=i=>{const sc=SCENES[state.scene];state.pageIndex=paginateStory(sc.body(state)).length-1;choose(i);if(state.scene===sc.id)throw Error(sc.id+':'+banner);};
             try{
              for(const answer of [1,2]){state=clone(cfg.seed);step(SCENES[state.scene].choices(state).findIndex(o=>o.next==='m3_218_hanzhong_request'));step(answer);if(state.scene!=='ch10_c58_06_frontier_218'||state.storyClock.year!==218||state.age!==cfg.seed.age||state.militaryCareer.hanzhongRotation)throw Error('Rotation refused/deferred');step(0);if(state.storyClock.year!==219||state.age!==cfg.seed.age+1||auh5iBattle(state))throw Error('Refusal east continuation');}
              state=clone(cfg.gate);step(0);step(0);const prospective=clone(state);const distrust=clone(state);distrust.relationships.liubei.trust=0;if(auh5iTigerOffer(distrust))throw Error('Untrusted General received Tiger offer');const malformed=clone(state);malformed.relationships.liubei.respect='6';if(auh5iTigerOffer(malformed))throw Error('Malformed confidence grant');prospective.history=prospective.history.filter(h=>h.sceneId!=='liubei_meeting');prospective.visited=prospective.visited.filter(id=>id!=='liubei_meeting');if(auh5iTigerOffer(prospective))throw Error('Missing long service received honour');prospective.scene='m3_219_tiger_standard';prospective.flags.m3_tiger_proposal='accepted';if(auh5iCeremony(prospective)||!SCENES.m3_219_tiger_standard.body(prospective).includes('does not verify'))throw Error('Fake ceremony prose');const initial=JSON.stringify(prospective);auh5iInvest(prospective,'living');if(JSON.stringify(prospective)!==initial)throw Error('Direct fake investiture');
              state=clone(cfg.seed);state.age=69;step(SCENES[state.scene].choices(state).findIndex(o=>o.next==='m3_218_hanzhong_request'));step(0);step(0);if(state.age!==70||state.storyClock.year!==219)throw Error('Older age reset');
             }finally{save=a;render=b;scrollTopNow=c;}
            }""",{'seed':seeds[4],'gate':good,'ceremony':ceremonial,'contact':campaigns[4]['contact'],'accepted':campaigns[4]['accepted']})
            # All 13 new scenes are chosen in the real DOM with full history.
            p.evaluate('s=>{state=clone(s);activeTab="story";render();}',seeds[4]);clicks=0
            choices={'m3_219_hanzhong_council':1,'m3_219_hanzhong_orders':1,'m3_219_hanzhong_hearing':2,'m3_219_tiger_standard':2,'m3_219_tiger_aftermath':2}
            while p.evaluate('state.scene')!='ch10_c58_07_jing_219':
                assert clicks<18
                p.evaluate('()=>{state.pageIndex=paginateStory(SCENES[state.scene].body(state)).length-1;render();}')
                scene=p.evaluate('state.scene');index=p.evaluate('SCENES[state.scene].choices(state).findIndex(o=>o.next==="m3_218_hanzhong_request")') if scene=='ch10_c58_06_frontier_218' else choices.get(scene,0)
                p.locator(f'[data-choice="{index}"]' if index else '[data-choice="0"], [data-action="next-scene"]').click();clicks+=1
            assert clicks==14 and p.evaluate('auh5iTigerEvidence(state)&&auh5iGeneralUnits(auh5iRoll(state))&&state.militaryCareer.rank==="Grand General"&&state.flags.m3_hanzhong_recovered&&state.storyClock.year===219&&state.age===45')
            p.reload();assert p.evaluate('auh5iTigerEvidence(state)&&validSave(state)')
            p.locator('#menuToggle').click();p.locator('#gameMenu [data-nav="military"]').click();assert p.locator('[aria-label="Hanzhong service in 219"]').is_visible()
            assert 'Sixth Tiger General' in p.locator('body').inner_text();assert p.evaluate('document.documentElement.scrollWidth<=innerWidth')
            p.locator('#menuToggle').click();p.locator('#gameMenu [data-nav="character"]').click();p.locator('[data-character-tab="health"]').click();assert 'forearm cut' in p.locator('body').inner_text() and 'small scar' in p.locator('body').inner_text()
            p.locator('#menuToggle').click();p.locator('#gameMenu [data-nav="people"]').click();p.locator('[data-people-gender="male"]').click();p.locator('[data-people-category="neutral"]').click()
            assert p.locator('.npc-card').filter(has_text='Ma Chao').is_visible() and p.locator('.npc-card').filter(has_text='Huang Zhong').is_visible()

            with tempfile.TemporaryDirectory() as directory:
                with p.expect_download() as dl:p.evaluate('exportSave()')
                exported=Path(directory)/'sixth-tiger.json';dl.value.save_as(exported);data=json.loads(exported.read_text());assert data['militaryCareer']['sixthTiger219']['vow']=='duty'
                p.on('dialog',lambda dialog:dialog.accept());p.locator('#importFile').set_input_files(exported)
                p.wait_for_function('banner.includes("Save imported and verified")');assert p.evaluate('auh5iTigerEvidence(state)&&auhMcVerifiedCareerRank(state)==="Grand General"')
            # Played state continues through the original Jing and 220–223 paths.
            later=p.evaluate(r"""()=>{const a=save,b=render,c=scrollTopNow;save=()=>{};render=()=>{};scrollTopNow=()=>{};let n=0;try{activeTab='story';for(;n<120&&state.scene!=='m3_223_rolls';n++){const sc=SCENES[state.scene];state.pageIndex=paginateStory(sc.body(state)).length-1;choose(0);if(state.scene===sc.id)throw Error('Later continuation '+sc.id+':'+banner);}if(state.scene!=='m3_223_rolls'||!auh5gReturnable(state)||!auh5iTigerEvidence(state))throw Error('Western formation not returnable');if(auhMcKnownSuperior(state,'').includes('Liu Bei'))throw Error('Departed ruler remains current personal superior');for(const i of [1,1,0]){const sc=SCENES[state.scene];state.pageIndex=paginateStory(sc.body(state)).length-1;choose(i);}if(state.scene!=='ch12_01'||state.storyClock.year!==224||state.age!==50||auh5iRoll(state).length||!auh5iTigerEvidence(state)||!auh5gHandover(state)||!auh5gEvidence(state)||state.militaryCareer.rank!=='Grand General')throw Error('223 transfer/224 continuity');return n;}finally{save=a;render=b;scrollTopNow=c;save();render();}}""")
            assert not errors,errors
            result['checks'].append({'width':width,'campaign_routes_five_organic_career_profiles_two_current_branches':810,'nine_local_results_and_personal_wound':'PASS','general_and_tiger_ceremony_routes_two_branches':486,'accepted_refused_deferred_no_duplicate_muster_or_free_civic_staff_dragons':'PASS','royal_cast_actual_meetings_remote_guanyu_and_legacy_unchanged':'PASS','provenance_history_readonly_later_post_age_guards':'PASS','full_history_dom_choices':clicks,'people_new_actual_encounters_character_health_and_existing_wounds_preserved':'PASS','actual_json_download_file_import_and_http_reload':'PASS','organic_continuation_to_224_handler_steps':later,'720_handover_preserves_grand_general_and_honour':'PASS','registry':len(current),'page_errors':errors});context.close()
    result['limits']='Five prior career profiles reached through original handlers; current Cavalry service/muster and Governor/later-post/older-age comparators synthetic. Full 3^4 mission/role/action/report per career/branch, canonical conditional warrant/hearing/proposal/investiture/duty/aftermath routes. Matrix compacts historical bodies and suppresses paint/storage; 14 DOM choices keep full history. Later 219–224 continuation uses actual handlers, not DOM. No exhaustive world/relationship products, full M3/M4/Issue #1/#2 or physical-device file:// certification.'
    write_report(result,args.report)
if __name__=='__main__':main()
