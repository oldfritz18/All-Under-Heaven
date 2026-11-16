#!/usr/bin/env python3
"""Issue #1 M3-A: accepted General recognition, first orders and return."""
import argparse
from copy import deepcopy
from pathlib import Path
from qa_support import fixture, write_report, HANZHONG_219_SCENES, COURT_224_SCENES, DESIGNATION_221_SCENES, SHU_ACCESSION_225_SCENES, DRAGON_NOMINATION_227_SCENES, HAN_DRAGON_229_SCENES
from qa_eastern222 import START, ADVANCE, TO_HANJIN, TO_FLOTILLA, TO_ANCHORS, TO_TIDE, TO_BORDER, TO_JING, TO_XI, TO_FRONT

BASELINE='61ce7c6:GAME/ALL_UNDER_HEAVEN_v0.4.99.5g_THE_ROLLS_AND_THE_CHAIR.html'
NEW={'m3_222_standard','m3_222_command_lanes','m3_222_rider_at_the_bend','m3_222_first_return'}
TO_REVIEW=r"""s=>{state=clone(s);const a=save,b=render,c=scrollTopNow;save=()=>{};render=()=>{};scrollTopNow=()=>{};try{for(let i=0;i<12;i++){if(state.scene==='m3_222_field_review')return clone(state);const sc=SCENES[state.scene];state.pageIndex=paginateStory(sc.body(state)).length-1;choose(0);if(sc.id===state.scene)throw Error('Review blocked '+sc.id+':'+banner);}throw Error('Review not reached');}finally{save=a;render=b;scrollTopNow=c;}}"""

def organic_reviews(page):
    initial=[page.evaluate(START,d) for d in (False,True)]
    starts=[page.evaluate(ADVANCE,{'seed':s['snapshots']['ch08_pb55_xushu'],'decision':d}) for s in initial for d in (0,1)]
    flotilla=[page.evaluate(TO_FLOTILLA,page.evaluate(TO_HANJIN,s)) for s in starts]
    anchors=[page.evaluate(TO_ANCHORS,{'seed':s,'weak':False}) for s in flotilla]
    tide=[page.evaluate(TO_TIDE,{'seed':s,'world':'south'}) for s in anchors]
    tide.append(page.evaluate(TO_TIDE.replace('ch08_06:1','ch08_06:0'),{'seed':anchors[1],'world':'south'}))
    weak=page.evaluate(TO_ANCHORS,{'seed':flotilla[0],'weak':True})
    tide += [page.evaluate(TO_TIDE,{'seed':weak if w=='north' else anchors[0],'world':w}) for w in ('north','separate')]
    border=[page.evaluate(TO_BORDER,s) for s in tide]
    jing=[page.evaluate(TO_JING,{'seed':s})['seed'] for s in border]
    jing.append(page.evaluate(TO_JING,{'seed':border[0],'west':True})['seed'])
    delegate=page.evaluate(TO_BORDER.replace('choose(0);',"choose(sc.id==='ch09_charter_hearing'?3:0);"),tide[3])
    jing.append(page.evaluate(TO_JING,{'seed':delegate})['seed'])
    reviews=[page.evaluate(TO_REVIEW,page.evaluate(TO_FRONT,{'seed':page.evaluate(TO_XI,s),'policy':0,'travel':0})) for s in jing]
    assert reviews[7]['militaryCareer']['rank']=='Major'
    mounted=page.evaluate(TO_XI,jing[7])
    mounted['militaryCareer']['combatService']={'branch':'Cavalry','unit':'Synthetic lawful mounted service','commander':'Recorded field officer','year':220,'proof':'legacy:lawful-cavalry'}
    for u in mounted['militaryCareer']['units']:
        if u.get('active') is not False:u['infantry']=0;u['cavalry']=30
    mounted=page.evaluate(TO_REVIEW,page.evaluate(TO_FRONT,{'seed':mounted,'policy':0,'travel':0}))
    return reviews,mounted

RUN=r"""profiles=>{
 const compact=clone(profiles);for(const s of Object.values(compact))for(const h of s.history)h.body='';
 const a=save,b=render,c=scrollTopNow;save=()=>{};render=()=>{};scrollTopNow=()=>{};const rows=[];let example=null,started=null,ordered=null;
 const step=i=>{const sc=SCENES[state.scene];state.pageIndex=paginateStory(sc.body(state)).length-1;choose(i);if(sc.id===state.scene||!validSave(state))throw Error('General route blocked '+sc.id+':'+banner);};
 try{for(const branch of ['Infantry','Cavalry'])for(let address=0;address<3;address++)for(let plan=0;plan<3;plan++)for(let response=0;response<3;response++)for(let lesson=0;lesson<3;lesson++){
  state=clone(compact[branch]);activeTab='story';
  if(auh5fOffer(state)?.rank!=='General')throw Error('General offer missing '+branch);step(0);if(state.scene!=='m3_222_after_review'||!auh5hCurrent(state)||auh5hEvidence(state))throw Error('Acceptance not witnessed');
  const before=clone(state);step(0);if(state.scene!=='m3_222_standard'||!auh5hStarted(state))throw Error('Acknowledgement entry');started=clone(state);
  step(address);step(plan);ordered=clone(state);if(state.scene!=='m3_222_rider_at_the_bend'||state.militaryCareer.fieldPosition.proof!=='m3_5h:general_assumption222'||!state.militaryCareer.fieldPosition.active)throw Error('Actual order not active');
  step(response);if(auh5hEvidence(state)||!state.militaryCareer.fieldPosition.active)throw Error('Return closed before receiving');step(lesson);
  if(state.scene!=='ch11_p60_07_meeting_222'||!auh5hEvidence(state)||state.storyClock.year!==222||state.age!==before.age||state.militaryCareer.fieldPosition.active)throw Error('Receiving account/calendar');
  const m=clone(state.militaryCareer),old=clone(before.militaryCareer);delete m.fieldPosition;delete old.fieldPosition;delete m.commandAssumption222;if(JSON.stringify(m)!==JSON.stringify(old))throw Error('Rank/muster/commission/staff changed');
  for(const k of ['coins','items','innerCircle','dragonGenerals','civicCareer','relationships','health','age','storyClock'])if(JSON.stringify(state[k])!==JSON.stringify(before[k]))throw Error('Unchosen grant/change '+k);
  if(state.militaryCareer.legendaryGroup||auh79Emperor(state)||auh65Crowned(state))throw Error('Legendary/crown grant');
  const frozen=JSON.stringify(state);militaryPanel();npcMemories('hansheng');npcMemories('xuwen');auh63SocialPosition(state);auh5hRecord(state,'listen');auh5hPosition(state,true);if(JSON.stringify(state)!==frozen)throw Error('Views/replay changed state');
  if(!SCENES.ch11_p60_07_meeting_222.body(state).includes('first movement account')||!auh63SocialPosition(state).position.startsWith('General / '))throw Error('Callback/Character');
  const loaded=resolve(JSON.parse(JSON.stringify(state)));if(!validSave(loaded)||!auh5hEvidence(loaded))throw Error('JSON/resolve receipt lost');
  rows.push({branch,address,plan,response,lesson,account:state.militaryCareer.commandAssumption222.account});example=clone(state);
 }return {rows,example,started,ordered};}finally{save=a;render=b;scrollTopNow=c;}
}"""


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--report',type=Path);args=parser.parse_args()
    with fixture(BASELINE) as (browser,url,result):
        base=browser.new_page();base.goto(url+'/baseline.html');reviews,mounted=organic_reviews(base);ids=base.evaluate('Object.keys(SCENES)');base.close()
        for width in (390,1280):
            context=browser.new_context(viewport={'width':width,'height':900});p=context.new_page();errors=[];p.on('pageerror',lambda e:errors.append(str(e)));p.goto(url+'/active.html')
            current=set(p.evaluate('Object.keys(SCENES)'));assert set(ids)<=current and current-set(ids) in (NEW,NEW|HANZHONG_219_SCENES,NEW|HANZHONG_219_SCENES|COURT_224_SCENES,NEW|HANZHONG_219_SCENES|COURT_224_SCENES|DESIGNATION_221_SCENES,NEW|HANZHONG_219_SCENES|COURT_224_SCENES|DESIGNATION_221_SCENES|SHU_ACCESSION_225_SCENES,NEW|HANZHONG_219_SCENES|COURT_224_SCENES|DESIGNATION_221_SCENES|SHU_ACCESSION_225_SCENES|DRAGON_NOMINATION_227_SCENES,NEW|HANZHONG_219_SCENES|COURT_224_SCENES|DESIGNATION_221_SCENES|SHU_ACCESSION_225_SCENES|DRAGON_NOMINATION_227_SCENES|HAN_DRAGON_229_SCENES)
            run=p.evaluate(RUN,{'Infantry':reviews[7],'Cavalry':mounted});assert len(run['rows'])==162 and len({x['account'] for x in run['rows']})==9
            old=context.new_page();old.goto(url+'/baseline.html')
            parity=r"""s=>({offer:auh5fOffer(s),body:SCENES.m3_222_field_review.body(s),choices:SCENES.m3_222_field_review.choices(s).map(o=>{const x=clone(s);o.effect(x);return {label:o.label,next:o.next,state:x};})})"""
            for i,seed in enumerate(reviews):
                actual=p.evaluate(parity,seed);expected=old.evaluate(parity,seed)
                assert actual['choices']==expected['choices'] and actual['offer']==expected['offer']
                if i!=7:assert actual['body']==expected['body']
                after=r"""cfg=>SCENES.m3_222_field_review.choices(cfg.s).map(o=>{const x=clone(cfg.s);o.effect(x);x.history.push({sceneId:'m3_222_field_review'});x.visited.push('m3_222_field_review');x.scene='m3_222_after_review';return {body:SCENES.m3_222_after_review.body(x),choices:SCENES.m3_222_after_review.choices(x).map(c=>({label:c.label,next:c.next}))};})"""
                actual_after=p.evaluate(after,{'s':seed});expected_after=old.evaluate(after,{'s':seed})
                for j,(x,y) in enumerate(zip(actual_after,expected_after)):
                    if i==7 and j==0:
                        assert [c['label'] for c in x['choices']]==[c['label'] for c in y['choices']]
                    else:assert x==y,(i,j)
            tail=r"""s=>SCENES.ch11_p60_07_meeting_222.body(s).split('<p>The first movement account')[0]"""
            assert p.evaluate(tail,run['example'])==old.evaluate(tail,run['example']);old.close()
            p.evaluate(r"""cfg=>{
             const e=cfg.example;
             const hist=clone(e);hist.visited=[];if(!auh5hEvidence(hist))throw Error('History-only proof');
             const flags=clone(e);flags.visited=[];flags.history=[];if(auh5hEvidence(flags)||auh5hCommission(flags))throw Error('Flag-only proof');
             for(const field of ['account','rank','appointmentProof']){const bad=clone(e);bad.militaryCareer.commandAssumption222[field]='invented';if(auh5hEvidence(bad))throw Error('Invalid '+field);}
             const bad=clone(e);bad.militaryCareer.commandAssumption222.units[1].id=bad.militaryCareer.commandAssumption222.units[0].id;if(auh5hEvidence(bad))throw Error('Duplicate receiving roll');
             const later=clone(cfg.ordered);later.militaryCareer.fieldPosition={year:224,active:true,proof:'later:kept'};const frozen=JSON.stringify(later);auh5hPosition(later,false);auh5hMark(later,'m3_222_first_response','inspect','m3_222_rider_at_the_bend',['inspect']);if(JSON.stringify(later)!==frozen||auh5hCurrent(later))throw Error('Later post overwritten');
             const sameYear=clone(cfg.ordered);sameYear.militaryCareer.fieldPosition={year:222,active:true,proof:'later:independent_post'};const sameFrozen=JSON.stringify(sameYear);auh5hPosition(sameYear,false);if(auh5hCurrent(sameYear)||JSON.stringify(sameYear)!==sameFrozen)throw Error('Other 222 post overwritten');
             const unknown=clone(cfg.started);unknown.militaryCareer.units.find(u=>u.active!==false).source='unknown';if(auh5hCurrent(unknown))throw Error('Unknown formation');
             const noEncounter=clone(e);noEncounter.visited=noEncounter.visited.filter(id=>id!=='preparation');noEncounter.history=noEncounter.history.filter(h=>h.sceneId!=='preparation');state=noEncounter;if(auh5hPresent(state,'hansheng')||npcMemories('hansheng').some(t=>t.includes('honest objection was part')))throw Error('Unmet comrade memory');
             const legacy=resolve(clone(e));delete legacy.militaryCareer.commandAssumption222;for(const k of Object.keys(legacy.flags))if(k.startsWith('m3_222_first_')||k==='m3_222_command_started')delete legacy.flags[k];state=legacy;const prior=JSON.stringify(state);militaryPanel();npcMemories('hansheng');if(auh5hEvidence(state)||JSON.stringify(state)!==prior)throw Error('Legacy backfill');
             const gov=clone(e);gov.civicCareer.appointed=true;gov.civicCareer.office='Governor';gov.civicCareer.territory='Existing district';state=gov;if(!civicPanel().includes('Governor')||!auhMcCivicOffice(state))throw Error('Governor erased');
            }""",run)
            # Full-history organic General acceptance and first command using DOM.
            p.evaluate('s=>{state=clone(s);activeTab="story";render();}',reviews[7]);clicks=0
            for index in (0,0,1,2,2,1):
                p.evaluate('()=>{state.pageIndex=paginateStory(SCENES[state.scene].body(state)).length-1;render();}')
                p.locator(f'[data-choice="{index}"]' if index else '[data-choice="0"], [data-action="next-scene"]').click();clicks+=1
            assert p.evaluate('state.scene==="ch11_p60_07_meeting_222"&&auh5hEvidence(state)&&auhStoryUIRecordedUnits(state).reduce((n,u)=>n+u[1]+u[2]+u[3],0)===720')
            p.reload();assert p.evaluate('auh5hEvidence(state)&&validSave(state)')
            p.locator('#menuToggle').click();p.locator('#gameMenu [data-nav="military"]').click();assert p.locator('[aria-label="First General command in 222"]').is_visible()
            assert p.evaluate('document.documentElement.scrollWidth<=innerWidth')
            # Continue from this played first command into the actual 223 handover.
            extra=p.evaluate(r"""()=>{const a=save,b=render,c=scrollTopNow;save=()=>{};render=()=>{};scrollTopNow=()=>{};let steps=0;try{activeTab='story';for(;steps<65&&state.scene!=='m3_223_rolls';steps++){const sc=SCENES[state.scene];state.pageIndex=paginateStory(sc.body(state)).length-1;const direct=sc.choices(state).findIndex(o=>o.next==='ch11_p60_08_turn_223');choose(direct>=0?direct:0);if(state.scene===sc.id)throw Error('223 continuation blocked '+sc.id+':'+banner);}if(state.scene!=='m3_223_rolls')throw Error('Receiving roll missing');for(const i of [1,1,0]){const sc=SCENES[state.scene];state.pageIndex=paginateStory(sc.body(state)).length-1;choose(i);}if(state.scene!=='ch12_01'||!auh5hEvidence(state)||!auh5gHandover(state)||!auh5gEvidence(state)||auhStoryUIRecordedUnits(state).length||state.militaryCareer.rank!=='General')throw Error('Historical command lost on handover');return steps;}finally{save=a;render=b;scrollTopNow=c;save();render();}}""")
            p.reload();assert p.evaluate('auh5hEvidence(state)&&auh5gHandover(state)&&state.storyClock.year===224')
            assert not errors,errors
            result['checks'].append({'width':width,'routes_organic_major_review_two_current_branch_variants_full_four_local_choices':162,'nine_first_command_results':'PASS','all_nine_prior_profiles_offer_effects_and_non_general_refusal_defer_parity':'PASS','grade_720_muster_staff_inventory_civic_relationships_unchanged':'PASS','order_active_and_received_retired_once':'PASS','chronicle_people_military_character_and_223_handover_history':'PASS','provenance_unknown_roll_duplicate_later_post_no_backfill':'PASS','json_resolve_and_http_reload':'PASS','general_acceptance_and_four_scene_dom_clicks':clicks,'continuation_223_handler_steps':extra,'page_errors':errors});context.close()
    result['limits']='General seed reached organically through Baxi/Jing/222. Current Cavalry service/muster variant and Governor/later-post comparators synthetic. All 3^4 new local choices on both branch variants; nine earlier organic profiles test unchanged offers/refusal/defer. Matrix suppresses paint/storage and compacts historical bodies; six DOM clicks use full history. 223 continuation uses handlers. No Sixth Tiger, Shu enthronement, Dragon investiture, all prior world/relationship products or real-device file:// certification.'
    write_report(result,args.report)
if __name__=='__main__':main()
