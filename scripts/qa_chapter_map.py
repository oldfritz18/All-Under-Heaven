#!/usr/bin/env python3
"""VIII/IX/X display boundaries, exact route-state parity and legacy reload."""
import argparse
from copy import deepcopy
from pathlib import Path
from qa_support import fixture, write_report
from qa_m2_continuity import START

BASELINE='e7293d0:GAME/ALL_UNDER_HEAVEN_v0.4.99.4z_FIRE_AND_THE_RECEIVING_BANK.html'

def crossing_projection(current, previous):
    """Account only for the documented 5b/5c event records and revised text.

    All other state, flags, history metadata and choice destinations must remain
    identical. The task itself is exhaustively checked by qa_crossing210.
    """
    projected = deepcopy(current)
    has_charter = projected['flags'].get('m3_211_scope') == 'local-charter'
    charter_labels = set()
    if has_charter:
        charter = projected['civicCareer'].pop('localCharter')
        assert charter['source'] == 'ch09_charter_hearing' and charter['year'] == 213
        assert charter['accepted'] and not charter['delegated']  # default route
        position = projected['militaryCareer']['fieldPosition']
        assert position['proof'] == 'm3_5c:ford212' and position['year'] == 212 and not position['active']
        del projected['flags']['m3_211_scope']
        assert projected['flags'].pop('m3_213_delegate') is False
        charter_labels = {'The Open Bank', 'A Chain Across the Ford', 'The Open Bank Charter'}
    if projected['flags'].get('m3_210_scope') != 'company':
        return projected
    evidence = projected['militaryCareer']['campaignEvidence'].pop('crossing210')
    assert evidence['year'] == 210 and evidence['source'] == 'ch09_p57_08_council'
    position = projected['militaryCareer']['fieldPosition']
    if not has_charter:
        assert position['proof'] == 'm3_5b:western_landing' and position['year'] == 210 and not position['active']
    projected['militaryCareer']['fieldPosition'] = deepcopy(previous['militaryCareer']['fieldPosition'])
    del projected['flags']['m3_210_scope']
    labels = {'The Battle Account', 'The Three Seals', 'The Western Landing', 'Three Seals on the River'} | charter_labels
    old_notes = {entry['label']: entry['text'] for entry in previous['journal']}
    for entry in projected['journal']:
        if entry['label'] in labels:
            entry['text'] = old_notes[entry['label']]
    assert len(projected['history']) == len(previous['history'])
    for entry, old in zip(projected['history'], previous['history']):
        assert entry['sceneId'] == old['sceneId']
        if entry['sceneId'].startswith('ch09_p57_') or (has_charter and entry['sceneId'].startswith('ch09_charter_')):
            entry['choice'] = old['choice']
    return projected
TRAVERSE=r"""config=>{
 state=clone(config.seed);for(const h of state.history)h.body='';activeTab='story';
 const realSave=save,realRender=render,realScroll=scrollTopNow;save=()=>{};render=()=>{};scrollTopNow=()=>{};
 const rows=[],headings=[],snapshots={};try{
 for(let i=0;i<260;i++){
  const sc=SCENES[state.scene],body=sc.body(state);for(const match of body.matchAll(/<h2 class="chapter-title-inline">(Chapter [IVX]+)<\/h2>/g))headings.push({scene:sc.id,label:match[1]});
  if(['ch08_pb55_foreword','ch08_pb55_council','ch08_rc54_winners','ch09_01','ch10_01'].includes(sc.id))snapshots[sc.id]=clone(state);
  rows.push({id:sc.id,act:sc.act,year:state.storyClock.year,age:state.age,rank:state.militaryCareer.rank,units:clone(state.militaryCareer.units)});
  if(sc.id==='ch10_01'){const final=clone(state);for(const h of final.history)h.body='';return {rows,headings,final,snapshots};}
  const index=sc.id==='m3_208_service_review'?config.decision:0;state.pageIndex=paginateStory(body).length-1;choose(index);
  if(state.scene===sc.id||!validSave(state))throw Error('Map route blocked '+sc.id+':'+banner);
  for(const h of state.history)h.body='';
 }throw Error('214 entry not reached');
 }finally{save=realSave;render=realRender;scrollTopNow=realScroll;}
}"""

def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--report',type=Path);args=parser.parse_args()
    with fixture(BASELINE) as (browser,url,result):
        base=browser.new_page();base.goto(url+'/baseline.html')
        starts=[base.evaluate(START,decline)['snapshots']['ch07_13'] for decline in (False,True)]
        configs=[{'seed':seed,'decision':decision} for seed,decision in zip(starts,(0,1))]
        expected=[base.evaluate(TRAVERSE,c) for c in configs];base.close()
        for width in (390,1280):
            context=browser.new_context(viewport={'width':width,'height':900});page=context.new_page();errors=[];page.on('pageerror',lambda e:errors.append(str(e)));page.goto(url+'/active.html')
            counts=page.evaluate("Object.values(SCENES).reduce((a,s)=>(a[s.displayChapter||'other']=(a[s.displayChapter||'other']||0)+1,a),{})")
            assert counts['8']==10 and counts['9']>0 and counts['10']>0
            for config,old in zip(configs,expected):
                current=page.evaluate(TRAVERSE,config)
                timeline = deepcopy(current['rows'])
                for row, prior in zip(timeline, old['rows']):
                    if row['id']=='ch09_charter_crossing' and row['year']!=prior['year']:
                        assert row['year']==212 and row['age']==38 and prior['year']==211 and prior['age']==37
                        row['year']=prior['year'];row['age']=prior['age']
                assert timeline==old['rows'] and crossing_projection(current['final'],old['final'])==old['final']
                assert current['headings']==[{'scene':'ch08_pb55_foreword','label':'Chapter VIII'},{'scene':'ch08_pb55_council','label':'Chapter IX'},{'scene':'ch08_rc54_winners','label':'Chapter X'}],current['headings']
                for scene,chapter,year in [('ch08_pb55_foreword',8,208),('ch08_pb55_council',9,208),('ch08_rc54_winners',10,209),('ch09_01',10,210),('ch10_01',10,214)]:
                    saved=current['snapshots'][scene];page.evaluate('s=>{state=clone(s);activeTab="story";render();}',saved)
                    assert page.evaluate('({chapter:SCENES[state.scene].displayChapter,year:state.storyClock.year})')=={'chapter':chapter,'year':year}
                    assert page.evaluate('document.documentElement.scrollWidth<=innerWidth')
                page.evaluate('s=>{localStorage.setItem(SAVE_KEY,JSON.stringify(s));handleAction("load-original");}',current['snapshots']['ch09_01']);page.reload()
                assert page.evaluate('validSave(state)&&state.storyClock.year===210&&SCENES[state.scene].displayChapter===10')
            page.evaluate(r"""samples=>{
             for(const [id,roman] of [['ch08_01','IX'],['ch09_01','X'],['ch10_01','X']]){
              const s=clone(samples);s.scene=id;s.visited=[];s.history=[];
              if(!SCENES[id].body(s).includes('>Chapter '+roman+'</h2>'))throw Error('Legacy direct-entry heading '+id);
              const frozen=JSON.stringify(s);SCENES[id].body(s);chapterName(s);if(JSON.stringify(s)!==frozen)throw Error('Metadata view mutates save');
             }
             for(const key of DEV_QA_ORDER)for(const entry of qaChapterEntries(key))if(String(SCENES[entry.scene]?.displayChapter||entry.chapter)!==String(key))throw Error('Inspector group mismatch');
             if(sceneChapter('ch08_rc54_winners')!==8||CHAPTER_YEAR[8]!==208||CHAPTER_YEAR[9]!==210||CHAPTER_YEAR[10]!==214)throw Error('Legacy clock inference changed');
            }""",expected[0]['snapshots']['ch09_01'])
            assert not errors,errors
            result['checks'].append({'width':width,'display_chapter_counts':counts,'captain_and_private_207_to_214_state_parity_except_documented_crossing_changes':'PASS',
                'single_VIII_IX_X_heading_at_208_208_209':'PASS','legacy_direct_entry_and_210_reload':'PASS',
                'readonly_inspector_group_and_legacy_clock_tables':'PASS','page_errors':errors});context.close()
    result['limits']='Two organic 207–214 routes. Only documented 210/213 event records, task position, scope/delegation flags, revised journal/choice text and the 212 entry correction are projected; other state compares exactly. Separate event suites verify those changes. No full X–XIX or device certification.'
    write_report(result,args.report)
if __name__=='__main__':main()
