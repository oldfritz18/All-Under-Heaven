#!/usr/bin/env python3
"""Approved outsider succession: a conditional designation is witnessed, not backfilled."""
import argparse,json,tempfile
from pathlib import Path
from qa_support import fixture,write_report,SHU_ACCESSION_225_SCENES,DRAGON_NOMINATION_227_SCENES, HAN_DRAGON_229_SCENES
from qa_hanzhong219 import organic_seeds
from qa_court224 import TO_XII
BASELINE='146c0b1:GAME/ALL_UNDER_HEAVEN_v0.4.99.5j_THE_COURT_THAT_CAN_REFUSE.html'
NEW={'m4_221_summons','m4_221_road','m4_221_private','m4_221_household','m4_221_designation','m4_221_return'}

def organic_designation_seed(p):
    west=organic_seeds(p)[4]
    royal=p.evaluate(r"""s=>{state=clone(s);const a=save,b=render,c=scrollTopNow;save=()=>{};render=()=>{};scrollTopNow=()=>{};try{for(let i=0;i<18;i++){if(state.scene==='ch10_c58_07_jing_219')return clone(state);const sc=SCENES[state.scene];state.pageIndex=paginateStory(sc.body(state)).length-1;choose(sc.id==='ch10_c58_06_frontier_218'?sc.choices(state).findIndex(o=>o.next==='m3_218_hanzhong_request'):sc.id==='m3_219_hanzhong_clash'?1:0);if(sc.id===state.scene)throw Error(sc.id+':'+banner);}throw Error('Royal route');}finally{save=a;render=b;scrollTopNow=c;}}""",west)
    return p.evaluate(TO_XII.replace("if(state.scene==='ch12_01')","if(state.scene==='ch11_p60_04_bridge_221')"),{'seed':royal,'custody':0,'mandate':0,'review':0})

MATRIX=r"""seed=>{
 const input=clone(seed);for(const h of input.history)h.body='';const a=save,b=render,c=scrollTopNow;save=()=>{};render=()=>{};scrollTopNow=()=>{};let accepted=null,decisionSeed=null;const rows=[];
 const step=i=>{const sc=SCENES[state.scene];state.pageIndex=paginateStory(sc.body(state)).length-1;choose(i);if(sc.id===state.scene||!validSave(state))throw Error('Designation blocked '+sc.id+':'+banner);};
 const paths=[[1],[2],[0,1],[0,2],[0,0,1],[0,0,2],...[0,1,2].flatMap(arg=>Array.from({length:arg===2?2:5},(_,last)=>[0,0,0,arg,last]))];
 try{for(const path of paths){state=clone(input);activeTab='story';step(SCENES[state.scene].choices(state).findIndex(o=>o.next==='m4_221_summons'));for(const n of path){if(state.scene==='m4_221_designation')decisionSeed=clone(state);step(n);}if(state.scene!=='m4_221_return')throw Error('No receiving return');const designated=path.length===5&&path[3]<2&&path[4]<3;if(auh5kEvidence(state)!==designated)throw Error('Unexpected designation');step(0);if(state.scene!=='ch11_p60_04_bridge_221'||state.storyClock.year!==221||state.age!==input.age||!auh5kReview(state)||auh5kEvidence(state)!==designated)throw Error('Review close/calendar');
  const m=clone(state.militaryCareer);delete m.leave221;if(JSON.stringify(m)!==JSON.stringify(input.militaryCareer))throw Error('Review changed military authority/units/staff');const civil=clone(state.civicCareer);delete civil.shuDesignation221;delete civil.shuReview221;if(JSON.stringify(civil)!==JSON.stringify(input.civicCareer))throw Error('Review changed office');for(const k of ['coins','items','relationships','innerCircle','dragonGenerals','health','realmNames'])if(JSON.stringify(state[k])!==JSON.stringify(input[k]))throw Error('Review grant '+k);
  if(auh65Crowned(state)||auh79Emperor(state)||hasWitnessed('liushan'))throw Error('Designation became crown/union/royal meeting');
  const frozen=JSON.stringify(state);militaryPanel();civicPanel();npcMemories('liubei');auh63SocialPosition(state);auh5kClose(state);auh5kDecision(state,'account');if(JSON.stringify(state)!==frozen)throw Error('View/replay mutation');const restored=resolve(JSON.parse(JSON.stringify(state)));if(!validSave(restored)||!auh5kReview(restored)||auh5kEvidence(restored)!==designated)throw Error('Resolve lost review');
  rows.push({path,designated,method:state.flags.m4_221_method,decision:state.flags.m4_221_decision||null});if(designated)accepted=clone(state);
 }return {rows,accepted,decisionSeed};}finally{save=a;render=b;scrollTopNow=c;}
}"""

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--report',type=Path);args=ap.parse_args()
    with fixture(BASELINE) as (browser,url,result):
        p=browser.new_page();p.goto(url+'/baseline.html');seed=organic_designation_seed(p);ids=set(p.evaluate('Object.keys(SCENES)'));p.close()
        for width in (390,1280):
            context=browser.new_context(viewport={'width':width,'height':900});p=context.new_page();errors=[];p.on('pageerror',lambda e:errors.append(str(e)));p.goto(url+'/active.html');current=set(p.evaluate('Object.keys(SCENES)'));assert ids<=current and current-ids in (NEW,NEW|SHU_ACCESSION_225_SCENES,NEW|SHU_ACCESSION_225_SCENES|DRAGON_NOMINATION_227_SCENES,NEW|SHU_ACCESSION_225_SCENES|DRAGON_NOMINATION_227_SCENES|HAN_DRAGON_229_SCENES) and len(current) in (701,716,728,742)
            run=p.evaluate(MATRIX,seed);assert len(run['rows'])==18 and sum(x['designated'] for x in run['rows'])==6
            old=context.new_page();old.goto(url+'/baseline.html');project=r"""s=>SCENES.ch11_p60_04_bridge_221.choices(s).filter(o=>o.next!=='m4_221_summons').map(o=>{const x=clone(s);o.effect(x);return {label:o.label,next:o.next,state:x};})""";assert old.evaluate(project,seed)==p.evaluate(project,seed);old.close()
            p.evaluate(r"""cfg=>{
             const hist=clone(cfg.accepted);hist.visited=[];if(!auh5kEvidence(hist)||!auh5kReview(hist))throw Error('History-only proof');const flags=clone(cfg.accepted);flags.visited=[];flags.history=[];if(auh5kEvidence(flags)||auh5kReview(flags)||auh5kLeave(flags))throw Error('Flags-only grant');
             const bad=clone(cfg.accepted);bad.civicCareer.shuDesignation221.authority='borrowed';if(auh5kEvidence(bad))throw Error('Forged authority');const confidence=clone(cfg.accepted);confidence.civicCareer.shuDesignation221.confidence.trust='6';if(auh5kEvidence(confidence))throw Error('Malformed confidence');
             const later=clone(cfg.accepted);later.relationships.liubei.trust=0;later.militaryCareer.fieldPosition={year:228,active:true,proof:'later'};later.storyClock.year=228;if(!auh5kEvidence(later)||!auh5kReview(later))throw Error('Later confidence/post erased historical event');
             for(const kind of ['late','active','unknown','lower','no_history']){const s=clone(cfg.seed);if(kind==='late')s.storyClock.year=224;if(kind==='active')s.militaryCareer.fieldPosition.active=true;if(kind==='unknown')s.militaryCareer.units.find(u=>u.active!==false).source='unknown';if(kind==='lower')s.militaryCareer.rank='Private';if(kind==='no_history'){s.history=[];s.visited=[];}if(auh5kStartable(s)||SCENES.ch11_p60_04_bridge_221.choices(s).some(o=>o.next==='m4_221_summons'))throw Error('Invalid entry '+kind);}
             state=resolve(clone(cfg.seed));const frozen=JSON.stringify(state);civicPanel();militaryPanel();npcMemories('liubei');if(state.civicCareer.shuDesignation221||JSON.stringify(state)!==frozen)throw Error('Legacy backfill');
             const a=save,b=render,c=scrollTopNow;save=()=>{};render=()=>{};scrollTopNow=()=>{};try{for(const oldAge of [false,true]){state=clone(cfg.seed);if(oldAge)state.age=70;const entry=SCENES[state.scene].choices(state).findIndex(o=>o.next==='m4_221_summons');for(const n of [entry,0,0,0,0,0,0]){const sc=SCENES[state.scene];state.pageIndex=paginateStory(sc.body(state)).length-1;choose(n);if(state.scene===sc.id)throw Error('Age route blocked');}if(state.age!==(oldAge?70:cfg.seed.age)||!auh5kEvidence(state))throw Error('Age rewound');}}finally{save=a;render=b;scrollTopNow=c;}
            }""",{'seed':seed,**run})
            p.evaluate('s=>{state=clone(s);activeTab="story";render();}',seed)
            for index in [p.evaluate('SCENES[state.scene].choices(state).findIndex(o=>o.next==="m4_221_summons")'),0,0,0,1,1,0]:
                p.evaluate('()=>{state.pageIndex=paginateStory(SCENES[state.scene].body(state)).length-1;render();}');p.locator(f'[data-choice="{index}"]' if index else '[data-choice="0"], [data-action="next-scene"]').click()
            assert p.evaluate('state.scene==="ch11_p60_04_bridge_221"&&auh5kEvidence(state)&&auh5kReview(state)&&state.age===47&&state.storyClock.year===221&&!hasWitnessed("liushan")')
            p.reload();assert p.evaluate('auh5kEvidence(state)&&auh5kReview(state)')
            p.locator('#menuToggle').click();p.locator('#gameMenu [data-nav="civic"]').click();assert p.locator('[aria-label="Royal review in 221"]').is_visible();assert p.evaluate('document.documentElement.scrollWidth<=innerWidth')
            with tempfile.TemporaryDirectory() as folder:
                with p.expect_download() as dl:p.evaluate('exportSave()')
                path=Path(folder)/'designation.json';dl.value.save_as(path);assert json.loads(path.read_text())['civicCareer']['shuDesignation221']['consentPending'] is True
                p.on('dialog',lambda d:d.accept());p.locator('#importFile').set_input_files(path);p.wait_for_function('banner.includes("Save imported and verified")');assert p.evaluate('auh5kEvidence(state)&&auh5iTigerEvidence(state)')
            # Actual future handlers preserve the existing 223 proclamation and
            # never turn the earlier conditional intention into a secret crown.
            continued=p.evaluate(TO_XII,{'seed':p.evaluate('clone(state)'),'custody':1,'mandate':1,'review':0});assert continued['scene']=='ch12_01' and continued['storyClock']['year']==224 and continued['age']==50
            assert p.evaluate('auh5kEvidence(state)&&auh5kReview(state)&&auh5gNotice(state)&&!auh65Crowned(state)&&!auh79Emperor(state)&&auh5iRoll(state).length===0')
            court=r"""()=>{const a=save,b=render,c=scrollTopNow;save=()=>{};render=()=>{};scrollTopNow=()=>{};try{for(const n of [SCENES[state.scene].choices(state).findIndex(o=>o.next==='m4_224_petition'),1,0,0,1,0,0]){const sc=SCENES[state.scene];state.pageIndex=paginateStory(sc.body(state)).length-1;choose(n);if(sc.id===state.scene)throw Error('Court callback blocked '+sc.id+':'+banner);}return auh5kEvidence(state)&&auh5jEvidence(state)&&state.storyClock.year===225&&state.age===51&&state.civicCareer.shuPetition224.royalAudience&&!auh79Emperor(state)&&!auh65Crowned(state);}finally{save=a;render=b;scrollTopNow=c;}}""";assert p.evaluate(court)
            assert not errors,errors
            result['checks'].append({'width':width,'canonical_local_paths':18,'accepted_designations':6,'no_rank_units_staff_crown_office_resource_relation_or_liushan_meeting_grant':'PASS','history_confidence_authority_legacy_age_later_duty_guards':'PASS','pure_views_replay_resolve':'PASS','old_deployment_choices_exact':'PASS','full_history_dom_choices':7,'civic_reload_download_file_import':'PASS','actual_223_notice_handover_224_225_court_callback':'PASS','registry':len(current),'page_errors':errors});context.close()
    result['limits']='One organic Sixth Tiger career generated through original 190–221 handlers; all 18 canonical local paths. Older/lower/unknown-force/later-post/forged comparators synthetic; not all prior worlds/relationships. Matrix compacts old historical bodies and suppresses paint/storage, seven DOM choices retain full history; later 223–225 continuation uses handlers. No actual Liu Shan meeting in 221, final mandate, coronation, Dragon appointment or device file:// certification.'
    write_report(result,args.report)
if __name__=='__main__':main()
