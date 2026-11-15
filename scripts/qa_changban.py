#!/usr/bin/env python3
"""Company-scale Changban, NPC autonomy, and the sourced Xu Shu report."""
import argparse
from copy import deepcopy
from pathlib import Path
from qa_support import fixture, write_report
from qa_m2_continuity import START

BASELINE = 'cb7d511:GAME/ALL_UNDER_HEAVEN_v0.4.99.4v_CHAPTER_VIII_THE_ISSUED_ROLL.html'
ADVANCE = r"""config=>{
 state=clone(config.seed);activeTab='story';
 for(let i=0;i<20;i++){
  if(state.scene==='ch08_pb55_succession')return clone(state);
  const sc=SCENES[state.scene],index=sc.id==='m3_208_service_review'?config.decision:0;
  state.pageIndex=paginateStory(sc.body(state)).length-1;choose(index);
  if(sc.id===state.scene)throw Error('Baseline entry blocked: '+banner);
 }throw Error('Did not reach retreat');
}"""
ROUTES = r"""seed=>{
 const compact=clone(seed);for(const h of compact.history)h.body='';
 const realSave=save,realRender=render,realScroll=scrollTopNow;save=()=>{};render=()=>{};scrollTopNow=()=>{};
 const rows=[];
 try{
 for(const branch of ['Infantry','Cavalry'])for(let a=0;a<3;a++)for(let b=0;b<3;b++)for(let c=0;c<3;c++){
  state=clone(compact);activeTab='story';if(branch==='Cavalry')state.militaryCareer.combatService={branch,unit:'Legacy cavalry section',commander:'Recorded officer',year:208,proof:'legacy:lawful-cavalry'};
  const before=clone(state),moves=[0,a,0,b,c,0,(a+b)%3,(b+c)%3,0];
  for(const [i,index] of moves.entries()){
   const sc=SCENES[state.scene];state.pageIndex=paginateStory(sc.body(state)).length-1;choose(index);
   if(!validSave(state)||sc.id===state.scene)throw Error('Retreat blocked at '+sc.id+':'+banner);
   if(state.storyClock.year!==208||state.age!==34)throw Error('Retreat date');
   if(i===1&&!state.militaryCareer.fieldPosition.active)throw Error('No assigned field position');
   if(i===4&&!state.militaryCareer.fieldPosition.active)throw Error('Position closed too soon');
   if(i>=6&&state.militaryCareer.fieldPosition.active)throw Error('Position active after recall');
  }
  if(state.scene!=='ch08_c72_01_guanyu_council'||!auh4wEvidence(state))throw Error('Missing crossing evidence');
  if(state.flags.auh56_zhao_road!==['search','guard','intelligence'][b]||state.flags.auh55_xushu!==['inquiry','escort','search'][(b+c)%3])throw Error('Legacy enums changed');
  for(const key of ['rank','rankProof','units','appointmentHistory','staff','superior','combatService'])if(JSON.stringify(state.militaryCareer[key])!==JSON.stringify(before.militaryCareer[key]))throw Error('Unchosen military change: '+key);
  for(const key of ['coins','items','innerCircle'])if(JSON.stringify(state[key])!==JSON.stringify(before[key]))throw Error('Goods/recruit grant');
  if(state.flags.historical_meet_xushu!==before.flags.historical_meet_xushu)throw Error('Report granted/lost acquaintance');
  if(!auh55LedgerMemory(state).includes(AUH4W_ACTIONS[['hold','screen','river'][c]])||auh55LedgerMemory(state).includes('Your boats kept'))throw Error('False grand-command callback');
  const frozen=JSON.stringify(state);militaryPanel();npcMemories('xuwen');if(JSON.stringify(state)!==frozen)throw Error('View mutation');
  const once=JSON.stringify(state.militaryCareer.campaignEvidence);auh4wRecord(state);if(JSON.stringify(state.militaryCareer.campaignEvidence)!==once)throw Error('Duplicate record');
  rows.push({rank:before.militaryCareer.rank,branch,evacuation:a,zhao:b,changban:c,bridge:(a+b)%3,report:(b+c)%3});
 }
 return {rows,example:clone(state)};
 }finally{save=realSave;render=realRender;scrollTopNow=realScroll;}
}"""

def main():
    parser = argparse.ArgumentParser(description=__doc__); parser.add_argument('--report', type=Path); args = parser.parse_args()
    with fixture(BASELINE) as (browser, url, result):
        base = browser.new_page(); base.goto(url + '/baseline.html')
        initial = [base.evaluate(START, decline) for decline in (False, True)]
        seeds = [base.evaluate(ADVANCE, {'seed': s['snapshots']['ch08_pb55_xushu'], 'decision': decision}) for s in initial for decision in (0, 1)]
        assert [s['militaryCareer']['rank'] for s in seeds] == ['Captain', 'Sergeant', 'Sergeant', 'Private']
        base.close()
        for width in (390, 1280):
            context = browser.new_context(viewport={'width': width, 'height': 900})
            page = context.new_page(); errors = []; page.on('pageerror', lambda error: errors.append(str(error))); page.goto(url + '/active.html')
            assert set(initial[0]['ids']).issubset(page.evaluate('Object.keys(SCENES)'))
            runs = [page.evaluate(ROUTES, seed) for seed in seeds]
            assert sum(len(r['rows']) for r in runs) == 216
            page.evaluate(r"""seed=>{
             state=clone(seed);const s=clone(state);s.visited=[];if(!auh4wEvidence(s))throw Error('History-only evidence lost');
             const bad=clone(state);bad.militaryCareer.campaignEvidence.changban208.action='__proto__';if(auh4wEvidence(bad))throw Error('Invalid action');
             const empty=clone(state);empty.visited=[];empty.history=[];if(auh4wEvidence(empty))throw Error('Flag-only attendance');
             delete empty.militaryCareer.campaignEvidence.changban208;auh4wRecord(empty);if(empty.militaryCareer.campaignEvidence.changban208)throw Error('Retroactive attendance');
             const late=clone(state);late.militaryCareer.fieldPosition={year:214,proof:'later-post',active:true};auh4wPosition(late,'received',false);if(late.militaryCareer.fieldPosition.proof!=='later-post'||!late.militaryCareer.fieldPosition.active)throw Error('Later posting overwritten');
             const unknown=clone(state);delete unknown.militaryCareer.combatService;delete unknown.militaryCareer.campaignEvidence.changban208;auh4wRecord(unknown);if(unknown.militaryCareer.campaignEvidence.changban208)throw Error('Unknown branch credit');
            }""", runs[0]['example'])
            # Higher-command saves keep untouched local nodes. Xu Shu's incorrect
            # sighting/report is intentionally corrected at every rank.
            legacy = deepcopy(seeds[0]); legacy['militaryCareer']['rank'] = 'Major'
            project = r"""s=>['ch08_pb55_succession','ch08_pb55_refugees','ch08_pb55_march','ch08_shu56_zhaoyun_road','ch08_pb55_cavalry','ch08_shu56_zhangfei_bridge','ch08_pb55_hanjin'].map(id=>({id,body:SCENES[id].body(s),options:SCENES[id].choices(s).map(o=>{const x=clone(s);o.effect(x);return {label:o.label,next:o.next,state:x};})}))"""
            base = context.new_page(); base.goto(url + '/baseline.html')
            assert page.evaluate(project, legacy) == base.evaluate(project, legacy); base.close()
            page.evaluate(r"""seed=>{
             state=clone(seed);state.scene='ch08_pb55_xushu_choice';state.flags.historical_meet_xushu=true;
             for(const o of SCENES[state.scene].choices(state)){const x=clone(state);o.effect(x);if(!x.flags.historical_meet_xushu)throw Error('Legacy acquaintance erased');}
             if(SCENES.ch08_pb55_changban.body(state).includes('you see Xu Shu standing')||SCENES.ch08_pb55_xushu_choice.body(state).includes('before you arrive'))throw Error('Live Xu Shu persisted');
            }""", legacy)
            page.evaluate('s=>{localStorage.setItem(SAVE_KEY,JSON.stringify(s));handleAction("load-original");}', runs[0]['example']); page.reload()
            assert page.evaluate('validSave(state)&&auh4wEvidence(state)')
            page.locator('#menuToggle').click(); page.locator('#gameMenu [data-nav="military"]').click()
            assert page.locator('[aria-label="Changban witnessed company service"]').is_visible()
            assert page.evaluate('document.documentElement.scrollWidth<=innerWidth')
            # Full-history seed, actual browser controls and storage.
            page.evaluate('s=>{state=clone(s);activeTab="story";render();}', seeds[3])
            for _ in range(9):
                page.evaluate('()=>{state.pageIndex=paginateStory(SCENES[state.scene].body(state)).length-1;render();}')
                page.locator('[data-choice="0"], [data-action="next-scene"]').click()
            assert page.evaluate('state.scene==="ch08_c72_01_guanyu_council"&&state.militaryCareer.rank==="Private"&&auh4wEvidence(state)')
            assert not errors, errors
            result['checks'].append({'width': width, 'pairwise_routes_four_organic_careers_two_branches': 216,
                'no_rank_units_staff_goods_or_recruit_grants': 'PASS', 'local_orders_retired_position': 'PASS',
                'legacy_enums_and_high_command_parity': 'PASS', 'xu_shu_report_no_new_meeting_legacy_flag_preserved': 'PASS',
                'negative_provenance_and_later_position': 'PASS', 'readonly_idempotence_reload_military_dom': 'PASS',
                'full_history_private_dom_clicks': 9, 'page_errors': errors})
            context.close()
    result['limits'] = 'Retreat through Hanjin only; pairwise five 3-way decisions. Cavalry/Major are synthetic legacy fixtures. Later river councils/Red Cliffs and chapter relabeling remain pending; no physical-device file:// certification.'
    write_report(result, args.report)

if __name__ == '__main__':
    main()
