#!/usr/bin/env python3
"""Targeted Bowang/Xinye service, commission, and bounded opening councils."""
import argparse
from copy import deepcopy
from pathlib import Path
from qa_support import fixture, write_report, normalize_chapter_headers
from qa_m2_continuity import START

BASELINE = 'a463613:GAME/ALL_UNDER_HEAVEN_v0.4.99.4u_M2_ROADS_AND_WITNESSES.html'
NEW = {'m3_208_bowang_orders', 'm3_208_bowang_pressure', 'm3_208_bowang_after',
       'm3_208_xinye_orders', 'm3_208_xinye_contact', 'm3_208_xinye_after',
       'm3_208_service_review', 'm3_208_after_review'}
ROUTES = r"""seed=>{
 const rows=[],compact=clone(seed);for(const h of compact.history)h.body="";
 // The matrix exercises choose/effects/validation without repainting or writing
 // hundreds of old novel pages per variant. Real DOM/storage checks follow.
 const realSave=save,realRender=render,realScroll=scrollTopNow;
 save=()=>{};render=()=>{};scrollTopNow=()=>{};
 try{
 for(const branch of ['Infantry','Cavalry'])for(let a=0;a<3;a++)for(let b=0;b<3;b++)for(let c=0;c<3;c++)for(let commission=0;commission<3;commission++){
  state=clone(compact);activeTab='story';if(branch==='Cavalry')state.militaryCareer.combatService={branch,unit:'Legacy mounted section',commander:'Recorded officer',year:207,proof:'legacy:lawful-cavalry'};
  const before=clone(state),step=index=>{const sc=SCENES[state.scene];state.pageIndex=paginateStory(sc.body(state)).length-1;choose(index);if(!validSave(state)||state.scene===sc.id)throw Error('Blocked '+sc.id+': '+banner);if(state.age!==34||state.storyClock.year!==208)throw Error('Date changed');};
  step(0);if(state.scene!=='m3_208_bowang_orders')throw Error('Missing entry');
  step((a+b)%3);if(!state.militaryCareer.fieldPosition.active)throw Error('No Bowang posting');
  step(a);if(state.militaryCareer.fieldPosition.active)throw Error('Bowang not retired');
  step(0);if(!auh4vEvidence(state,'bowang'))throw Error('No Bowang evidence');
  step(b);if(!state.militaryCareer.fieldPosition.active)throw Error('No Xinye posting');
  step(c);if(state.militaryCareer.fieldPosition.active)throw Error('Xinye not retired');
  step(0);if(!auh4vEligible(state)||state.scene!=='m3_208_service_review')throw Error('No earned offer');
  step(commission);
  if(commission===0){
   const expected=before.militaryCareer.rank==='Private'?'Sergeant':'Captain',count=expected==='Captain'?(branch==='Cavalry'?30:60):20;
   const u=state.militaryCareer.units.find(u=>u.id==='m3-208-issued-company');
   if(state.militaryCareer.rank!==expected||!u||u.infantry!==(branch==='Infantry'?count:0)||u.cavalry!==(branch==='Cavalry'?count:0))throw Error('Wrong accepted commission/muster');
   if(expected==='Captain'&&state.militaryCareer.units.find(u=>u.id==='road-watch-201').active!==false)throw Error('Old watch double counted');
   if(state.militaryCareer.appointmentHistory.length!==before.militaryCareer.appointmentHistory.length+1)throw Error('Wrong appointment count');
  }else for(const key of ['rank','rankProof','units','appointmentHistory','staff','superior'])if(JSON.stringify(state.militaryCareer[key])!==JSON.stringify(before.militaryCareer[key]))throw Error('Refusal/defer changed '+key);
  if(JSON.stringify(state.militaryCareer.staff)!==JSON.stringify(before.militaryCareer.staff)||state.coins!==before.coins||JSON.stringify(state.items)!==JSON.stringify(before.items)||JSON.stringify(state.innerCircle)!==JSON.stringify(before.innerCircle))throw Error('Unchosen goods/staff/recruit grant');
  const frozen=JSON.stringify(state);militaryPanel();npcMemories('hansheng');if(JSON.stringify(state)!==frozen)throw Error('View mutation');
  const once=JSON.stringify(state.militaryCareer);SCENES.m3_208_service_review.choices(state)[0].effect(state);if(JSON.stringify(state.militaryCareer)!==once)throw Error('Commission replay');
  step((a+b+c)%3);if(state.scene!=='ch08_pb55_council')throw Error('Council missing');
  if(SCENES[state.scene].body(state).includes('You set your own seal'))throw Error('Independent authority invented');
  step((a+b)%3);if(state.scene!=='ch08_shu56_liubei_compact'||state.flags.m3_208_council_scope!=='assigned')throw Error('Bounded council lost');
  step((b+c)%3);if(state.scene!=='ch08_pb55_succession'||state.flags.m3_208_compact_scope!=='company')throw Error('Bounded compact lost');
  rows.push({rank:before.militaryCareer.rank,branch,bowang:a,station:b,xinye:c,commission});
 }
 return {rows,example:clone(state)};
 }finally{save=realSave;render=realRender;scrollTopNow=realScroll;}
}"""

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--report', type=Path)
    args = parser.parse_args()
    with fixture(BASELINE) as (browser, url, result):
        base = browser.new_page(); base.goto(url + '/baseline.html')
        seeds = [base.evaluate(START, decline) for decline in (False, True)]
        base.close()
        for width in (390, 1280):
            context = browser.new_context(viewport={'width': width, 'height': 900})
            page = context.new_page(); errors = []
            page.on('pageerror', lambda error: errors.append(str(error)))
            page.goto(url + '/active.html')
            ids = set(page.evaluate('Object.keys(SCENES)'))
            assert set(seeds[0]['ids']).issubset(ids) and NEW.issubset(ids - set(seeds[0]['ids']))
            runs = [page.evaluate(ROUTES, s['snapshots']['ch08_pb55_xushu']) for s in seeds]
            assert sum(len(r['rows']) for r in runs) == 324
            page.evaluate(r"""seed=>{
             for(const [year,branch,reviewed] of [[209,'Infantry',false],[208,null,false],[208,'Infantry',true]]){
              const s=clone(seed);s.storyClock.year=year;s.flags.m3_208_reviewed=reviewed;if(!branch)delete s.militaryCareer.combatService;
              if(SCENES.ch08_pb55_xushu.choices(s)[0].next!=='ch08_pb55_council')throw Error('Unsafe replay/unknown branch');
             }
             const s=clone(seed);s.scene='m3_208_service_review';s.flags.m3_208_bowang_action='pair';s.flags.m3_208_xinye_action='return';s.flags.m3_208_bowang_complete=true;s.flags.m3_208_xinye_complete=true;
             if(auh4vEligible(s)||SCENES[s.scene].choices(s).some(o=>o.label.startsWith('Accept')))throw Error('Flag-only promotion');
             state=s;const frozen=JSON.stringify(state);militaryPanel();if(JSON.stringify(state)!==frozen)throw Error('View mutation');
            }""", seeds[0]['snapshots']['ch08_pb55_xushu'])
            # Existing higher-command saves retain their old council contracts.
            base = context.new_page(); base.goto(url + '/baseline.html')
            legacy = deepcopy(seeds[0]['snapshots']['ch08_pb55_xushu']); legacy['militaryCareer']['rank'] = 'Major'
            project = r"""s=>['ch08_pb55_council','ch08_shu56_liubei_compact'].map(id=>({id,body:SCENES[id].body(s),options:SCENES[id].choices(s).map(o=>{const x=clone(s);o.effect(x);return {label:o.label,next:o.next,state:x};})}))"""
            assert normalize_chapter_headers(page.evaluate(project, legacy)) == normalize_chapter_headers(base.evaluate(project, legacy))
            base.close()
            page.evaluate(r"""seed=>{
             state=clone(seed);const h=clone(state);h.visited=[];if(!auh4vEvidence(h,'xinye'))throw Error('History evidence lost');
             const bad=clone(state);bad.militaryCareer.campaignEvidence.xinye208.action='__proto__';if(auh4vEvidence(bad,'xinye'))throw Error('Invalid enum accepted');
             const once=JSON.stringify(state.militaryCareer.campaignEvidence);auh4vRecord(state,'xinye','m3_208_xinye_after');if(JSON.stringify(state.militaryCareer.campaignEvidence)!==once)throw Error('Duplicate service');
             localStorage.setItem(SAVE_KEY,JSON.stringify(state));handleAction('load-original');
            }""", runs[0]['example'])
            page.reload()
            assert page.evaluate('validSave(state)&&auh4vEvidence(state,"bowang")&&auh4vEvidence(state,"xinye")')
            page.locator('#menuToggle').click(); page.locator('#gameMenu [data-nav="military"]').click()
            assert page.locator('[aria-label="Bowang and Xinye witnessed service"]').is_visible()
            assert page.evaluate('document.documentElement.scrollWidth<=innerWidth')
            # Actual DOM choices along a complete new route, through council.
            page.evaluate('s=>{state=clone(s);activeTab="story";render();}', seeds[0]['snapshots']['ch08_pb55_xushu'])
            for _ in range(11):
                page.evaluate('()=>{state.pageIndex=paginateStory(SCENES[state.scene].body(state)).length-1;render();}')
                page.locator('[data-choice="0"], [data-action="next-scene"]').click()
            assert page.evaluate('state.scene==="ch08_pb55_succession"&&state.militaryCareer.rank==="Captain"')
            assert not errors, errors
            result['checks'].append({'width': width, 'pairwise_campaign_and_all_commission_routes': 324,
                'organic_private_and_sergeant_synthetic_cavalry': 'PASS', 'earned_accept_decline_defer_no_extra_grants': 'PASS',
                'bounded_council_and_compact': 'PASS', 'legacy_major_contract_parity': 'PASS',
                'late_unknown_branch_and_flag_only_negative': 'PASS', 'idempotence_readonly_reload': 'PASS',
                'dom_choice_clicks': 11, 'military_dom_overflow': False, 'page_errors': errors})
            context.close()
    result['limits'] = 'Targeted opening VIII only. Prior 208 retreat/Red Cliffs prose and IX–X relabeling remain under audit. Synthetic Cavalry/legacy Major fixtures; no physical-device file:// or full-novel certification.'
    write_report(result, args.report)

if __name__ == '__main__':
    main()
