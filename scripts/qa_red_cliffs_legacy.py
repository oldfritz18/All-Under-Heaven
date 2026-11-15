#!/usr/bin/env python3
"""Unchanged higher-command bodies and effects across the fire/settlement arc."""
import argparse
from pathlib import Path
from qa_support import fixture, write_report
from qa_m2_continuity import START
from qa_changban import ADVANCE
from qa_river_councils import TO_HANJIN
from qa_river_patrol import TO_FLOTILLA
from qa_red_cliffs import BASELINE, TO_ANCHORS

PROJECT=r"""s=>[
 'ch08_rc54_anchors','ch08_rc54_huanggai','ch08_rc54_letters','ch08_rc54_ruse','ch08_rc54_camp',
 'ch08_rc54_wind','ch08_rc54_silent_oars','ch08_player_river_battle','ch08_rc54_fire_rain','ch08_rc54_collision',
 'ch08_shu56_zhaoyun_flameline','ch08_rc54_choice_of_fire','ch08_rc54_north_bank','ch08_rc54_pursuit',
 'ch08_rc54_morning','ch08_rc54_winners','ch08_shu56_liubei_settlement','ch08_player_battle_result','ch08_alliance_afterfire','ch08_06'
].map(id=>({id,body:SCENES[id].body(s),choices:SCENES[id].choices(s).map(o=>{const x=clone(s);o.effect(x);return {label:o.label,next:o.next,state:x};})}))"""

def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--report',type=Path);args=parser.parse_args()
    with fixture(BASELINE) as (browser,url,result):
        base=browser.new_page();base.goto(url+'/baseline.html')
        seed=base.evaluate(START,False)['snapshots']['ch08_pb55_xushu']
        for transform,arg in [(ADVANCE,{'seed':seed,'decision':0})]:seed=base.evaluate(transform,arg)
        seed=base.evaluate(TO_HANJIN,seed);seed=base.evaluate(TO_FLOTILLA,seed);seed=base.evaluate(TO_ANCHORS,{'seed':seed,'weak':False})
        # A synthetic higher-command import, not a claim that Major was earned
        # by this default route. Keep real visit/clock metadata, compact bodies.
        seed['militaryCareer']['rank']='Major'
        for history in seed['history']:history['body']=''
        expected=base.evaluate(PROJECT,seed);base.close()
        for width in (390,1280):
            page=browser.new_page(viewport={'width':width,'height':900});errors=[];page.on('pageerror',lambda e:errors.append(str(e)));page.goto(url+'/active.html')
            assert page.evaluate(PROJECT,seed)==expected
            assert not errors,errors
            result['checks'].append({'width':width,'higher_command_scene_body_label_destination_effect_parity':20,'page_errors':errors});page.close()
    result['limits']='Synthetic Major import parity only; no organic proof of earning Major or certification of legacy strategic fiction.'
    write_report(result,args.report)
if __name__=='__main__':main()
