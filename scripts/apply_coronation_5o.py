#!/usr/bin/env python3
"""Apply the approved M4 coronation editorial expansion to the existing 5n HTML.
Never reconstruct the game engine. Idempotent, exact-recovery source audit.
Run from repo root: python3 scripts/apply_coronation_5o.py --write
"""
import argparse, hashlib, re
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
GAME=ROOT/"GAME"
OLD="ALL_UNDER_HEAVEN_v0.4.99.5n_THE_STANDARD_HE_CHOSE.html"
NEW="ALL_UNDER_HEAVEN_v0.4.99.5o_THE_OATH_THEY_HEARD.html"
OLD_HASH="15e85e566f259e9e253536f83710c00be4729ae7e69474c54451cb9e1eb9050d"
DATA=[
  [
    "m4_225_chamber",
    "<p>You can present the service",
    [
      "The hearing is not arranged like a battlefield council. Nobody lays a sword across a map and waits for the loudest voice to claim it. A clerk brings forward two cases, each tied with a different cord. One contains the warrants by which soldiers have followed you; the other contains petitions from families who have never seen your face. When an officer reaches for the military case first, the agricultural representative asks whether the order of reading is already a verdict. The clerk unties neither cord until the Chancellor says that both will be heard.",
      "An old campaign witness stands at the edge of the officials. He can attest to a retreat but has no office from which to speak about succession. His account is neither an endorsement of a crown nor an accusation against you. He describes rain, a rear file counted twice and a subordinate's warning that spared a column an avoidable loss. It is easier to admire courage when one has not been asked what authority it should purchase. Zhuge Liang asks the officers to enter military service and succession law in separate columns. If all your battlefield honors were set aside, what would remain to persuade a living court and a living household? The recording brush pauses. You know the answer cannot be given by advancing a formation."
    ]
  ],
  [
    "m4_225_liushan",
    "<p>You can propose protected independent terms",
    [
      "The household answer receives the same space on the table as the military return. An official tries to reduce the guarantees to a single courteous phrase. The receiving clerk asks precisely which words should be removed from the copy sent back to the household. Nobody volunteers a deletion. For the first time the debate feels less like a distant legal arrangement and more like a promise that someone may someday need the courage to invoke against an angry ruler.",
      "You remember how Liu Bei's name once traveled ahead of his column. To some it promised shelter; to others another army requiring grain. His heir inherited that contradiction as surely as he inherited a title. You have no right to declare that the willingness to consider a transfer means he feels no grief, resentment or apprehension. Your ambition cannot write the interior of another man's mind. The protected terms must keep his disagreement lawful after the witnesses leave."
    ]
  ],
  [
    "m4_225_objections",
    "<p>You can bind the proposed reign",
    [
      "As daylight moves toward the door, another petition is opened. Its author wants a record corrected: three days of transport duty were counted as four, and the fourth has become a debt against his household. A junior officer says the discrepancy may be settled after the succession. The petitioner asks what a new government is worth if the old government's error passes into its ledgers under a new seal. The court is quiet enough that the scratch of the recording brush can be heard from across the room.",
      "The Chancellor has the disputed figure marked rather than erased. He looks first toward those who fear an undefended frontier, then toward those who have learned that a demand called urgent may consume an entire planting season. Neither side has the luxury of an unthreatened country. Nor may danger make an imprecise order sacred. You discover that the legitimacy of a realm may be tested by a single numeral if the person beneath it has nowhere else to take a complaint."
    ]
  ],
  [
    "m4_225_vigil",
    "<p>The public oath has not yet been sworn.",
    [
      "Night settles on Chengdu without suspending the work at its gates. Watchmen exchange passwords, a cart with a broken axle is hauled out of a narrow lane, and the men who will stand solemnly beneath banners in the morning now sit without their shoes, binding fresh cord around the ends of their standards. For years you learned to tell approaching horsemen from an overloaded wagon by sound alone. Tonight those noises belong to people who will rise before dawn regardless of your answer.",
      "A keeper lays out the ceremonial garments. He brushes dust from the outer fold and says that his father once carried government records through a season of flight. He does not ask you to promise there will never be another flight. Such a promise would insult the memory of the one they survived. He asks only that, when a messenger arrives with bad news, the man wearing these robes permit him to finish reading it. You cannot decide whether the request is bold or ordinary. You know it should not require boldness.",
      "After the attendants leave, you try to remember the weight of the first weapon entrusted to you and the first officer who corrected your footing. None of those moments promised you this chamber. They taught you instead that men carry orders with their bodies rather than the confidence of whoever gives them. If authority passes to you, the reach of your decisions will extend farther than you can walk. Somewhere beyond the wall a child is comforted; you do not know the family and do not turn its private life into an omen. The oath must be your own answer, not a story imposed on strangers."
    ]
  ],
  [
    "m4_225_investiture",
    "<p>${AUH5L_VOWS[s.flags.m4_225_vigil]",
    [
      "An officer calls the ranks to order and the movement passes down the hall in a succession of sleeves and leather. Military witnesses stand beside officials whose authority is written in tablets, registers and carefully assigned places. A mistake in their arrangement is noticed and corrected without sending anyone away in disgrace. You are grateful. The reign about to begin will need people who can repair an error before it becomes a test of loyalty.",
      "The keeper approaches the imperial seal with both hands. He will not lift it before the instrument is read and the witnesses acknowledge its conditions. In the pause you hear cloth shifting as those who have stood through the long proceedings settle their weight upon tired knees. In another life you would have measured silence by the possibility of ambush. Here the danger is that ceremony may cause you to forget how many people are being asked to trust words they cannot enforce with weapons.",
      "Your memory of Liu Bei is not the figure sewn into a banner. It is a man who chose between imperfect roads, listened to counsel that contradicted his hopes and carried losses he could not repair by giving them grander names. There is no voice from the dead to confer a blessing the living have not given. Others here knew him differently. Some knew him only through the demands of government. You cannot inherit an invented agreement or borrow absolution from grief.",
      "Beyond the near doors the proclamation bearers rehearse the first words under their breath. One stumbles and begins again. Somewhere in the crowd will be soldiers who remember an order they obeyed and families who remember one they questioned. The ceremony cannot require the same feeling of them all. Its dignity must leave room for both. The seal of Shu-Han cannot make you the sovereign of the northern plains or eastern rivers by touch; it can only place the visible duties of this government into your hands.",
      "The keeper brings the prepared cloth nearer. He waits rather than anticipating your answer. A rank once seemed a height that could be climbed. This is a weight that can only be taken up. Between the seal and your hands there remains an unoccupied space, and nobody, not even the most persuasive courtier, can cross it for you."
    ]
  ],
  [
    "m4_225_proclamation",
    "<p>When the last words reach the outer court",
    [
      "The first herald speaks for the near court. Another takes the words at the gate; a third waits in the street where vendors, wheels and hurried footsteps contest his voice. Each begins only after receiving the final clause of the undertaking. The proclamation travels as a series of careful breaths rather than a single triumphant cry. Those nearest the doors see the seal. Those farther away see only the faces of people who heard the terms before them.",
      "A veteran bows without lifting his eyes. Beside him a young porter remains standing because the load against his shoulder makes kneeling difficult. Neither is reproved. A woman whose household supplied transport animals asks whether the receiving office will preserve its old ledgers. A clerk replies that it must, or nobody will know which debt belongs to which day. This practical exchange continues while the crowd takes up your imperial title. What little you hear of it is more useful than applause.",
      "Some voices offer congratulations so fierce that they seem to challenge the people around them to equal the noise. Others are quiet. You recognize the danger of believing the loudest people are all the people. Above the witnesses, standards turn in the wind, their colors brilliant against the roofs. The sight is magnificent and terrible: every banner required hands to weave and carry it, and every regiment contains people who must return from future campaigns or be mourned.",
      "The court will preserve the formal moment of accession. Beyond these steps, the country will remember a less orderly day: an interrupted market, a delayed petition, a soldier whose comrade could not attend, a family wondering whether a promise spoken here can reach its village. Their different memories do not diminish the ceremony; they are the measure of its reach. A public acclamation does not end the argument about how a country should be governed. It begins the answers a ruler will owe."
    ]
  ],
  [
    "m4_225_private",
    "<p>You may write the private truth",
    [
      "The ceremonial robe is set aside without fanfare. Dust has gathered at its hem and you stare at it longer than the moment deserves. An attendant is counting the cups used by the officials. His tally keeps slipping because two men departed early and another returned after the first count. You almost offer to help, then realize that even a harmless task may become difficult if the Emperor insists on being useful where someone else has been entrusted with the work. The distance between a person and an office has begun before sunset.",
      "You try to speak Liu Bei's name without the formal titles that now accompany it. What remains is neither a flawless founder nor an excuse for your ascent. He was someone who sought counsel, lost men, made promises and left the living to decide what those promises required. Grief refuses the neat order of the proclamation. You may honor his legacy without pretending the court has settled every doubt he might have carried.",
      "The first message to someone who knows you well is harder than the oath. You could describe the banners and omit the weight, report the seal without admitting how your hands shook, or write the true sentence and risk being answered by someone who remembers your old mistakes. You find that you want that answer. The palace has acquired a sovereign, but it must not make every older friendship into a petition."
    ]
  ],
  [
    "m4_225_decree",
    "<p>You can suspend the first disputed call",
    [
      "The transport officer spreads a narrow map upon the table. He points to a bridge requiring timber and a storehouse from which the timber might be taken. The agricultural witness sets her return beside it: if the teams are summoned now, fields will wait through the better part of the remaining weather. A military clerk calculates the risk of a late convoy; another counts how many men have already been absent for service. Neither calculation is a lie. Both become lies if the people omitted from the other sheet are treated as though they do not exist.",
      "You remember the silence before the seal and now hear the unmistakable sound of disagreement. There is relief in it. Nobody has mistaken your new title for a solution to a flooded road. The petitioner asks whether the order will be reviewed after its first consequences are known. You ask the clerk to enter that question into the decision record. It will not spare anyone the cost of your choice. It will let them bring that cost back to where it may be counted, disputed and answered."
    ]
  ]
]
MARKER="data-auh5o"
def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true", help="create the successor and advance ACTIVE_BUILD")
    args=parser.parse_args()
    original=(GAME/OLD).read_text(encoding="utf-8")
    assert hashlib.sha256(original.encode("utf-8")).hexdigest()==OLD_HASH, "5n source hash mismatch; abort"
    changed=original
    added=[]
    for scene_id, anchor, paras in DATA:
        mark="scene('"+scene_id+"'"
        start=changed.find(mark)
        assert start>=0, ("missing existing scene", scene_id)
        end=changed.find("\nscene('", start+len(mark))
        assert end>=0, ("missing next-scene anchor", scene_id)
        body=changed[start:end]
        assert body.count(anchor)==1, ("nonunique prose anchor", scene_id)
        ins="".join('<p data-auh5o="'+scene_id+'-'+str(i)+'">'+paragraph+'</p>\n' for i,paragraph in enumerate(paras,1))
        assert MARKER not in body, ("scene already modified",scene_id)
        changed=changed[:start]+body.replace(anchor,ins+anchor,1)+changed[end:]
        added.append(ins)
    title_old="<title>All Under Heaven — v0.4.99.5n The Standard He Chose</title>"
    title_new="<title>All Under Heaven — v0.4.99.5o The Oath They Heard</title>"
    meta_old='<meta name="auh-build" content="v0.4.99.5n">'
    meta_new='<meta name="auh-build" content="v0.4.99.5o">'
    assert changed.count(title_old)==1 and changed.count(meta_old)==1
    changed=changed.replace(title_old,title_new,1).replace(meta_old,meta_new,1)
    restored=changed.replace(title_new,title_old,1).replace(meta_new,meta_old,1)
    for section in added:
        assert restored.count(section)==1
        restored=restored.replace(section,"",1)
    assert restored==original, "engine/scene/choice/save diff outside added prose"
    assert len(re.findall(r"\bscene\(['\"]",original))==len(re.findall(r"\bscene\(['\"]",changed))
    images=lambda s:re.findall(r"data:image/(?:png|jpeg|webp);base64,[A-Za-z0-9+/=]+",s)
    assert len(images(original))==35 and images(original)==images(changed), "portrait parity failure"
    n=sum(len(p) for _,_,p in DATA)
    print(f"PASS: {len(DATA)} existing coronation scenes, {n} paragraphs; 35 portraits and all legacy source unchanged")
    print(f"Bytes: {len(changed.encode('utf-8'))}; source parity: exact after removing editorial paragraphs/version metadata")
    if args.write:
        target=GAME/NEW
        if target.exists():
            assert target.read_text("utf-8")==changed, "Existing successor differs; abort"
        else:
            target.write_text(changed,encoding="utf-8")
        (GAME/"ACTIVE_BUILD.txt").write_text(NEW+"\n",encoding="utf-8")
        print("WROTE",target)
if __name__=="__main__":
    main()
