
/* v0.4.99.5o — Xu Wen: an independent, witnessed reconnaissance case.
 * This is service/relationship groundwork, NOT a General or Dragon appointment.
 * The inspected detachment is existing and returns to prior custody at closure.
 */
const AUH5O_IDS=['m4_230_xu_hearing','m4_230_xu_terms','m4_230_xu_order','m4_230_xu_muster','m4_231_xu_road','m4_231_xu_contact','m4_231_xu_return','m4_231_xu_review','m4_231_xu_close'];
const AUH5O_RESULTS={
 verified:'The two measured approaches resolved into one viable lower road. The opposing scout captain kept the upper ridge, and no territory was transferred.',
 sheltered:'The guarded family wagons passed by the checked lower approach. The longer route consumed the promised day, while the rival captain kept his own screen.',
 exposed:'An unsupported push reached the rain-cut interval and was recalled when the rival captain shifted his screen. The lost ground and wounded were entered without false victory.'
};
function auh5oParent(s){
 const m=s?.militaryCareer,units=m?.units||[],han=m?.hanMuster228;
 const hanLive=han?.unit?.id&&units.some(u=>u.id===han.unit.id&&u.active!==false);
 const candidates=units.filter(u=>auh5nSource(s,u)&&(!hanLive||u.id!==han.parent?.id)&&
   (u.active!==false||(auh5gHandover(s)&&m.handover223.units.some(h=>h.id===u.id&&h.source===u.source))));
 const u=candidates[0];
 return u?{id:u.id,source:u.source,infantry:200,cavalry:40,archers:0,wasActive:u.active!==false}:null;
}
function auh5oEntry(s){
 const p=s?.militaryCareer?.fieldPosition,n=s?.civicCareer?.dragonNominations227?.xuwen;
 return !!(s?.scene==='ch12_c62_06_personal_230'&&s.storyClock?.year===230&&auh5nLiving(s)&&auh5lShu(s)&&
   auh5mNomination(s,'xuwen')&&n?.status==='conditional_interest'&&!auh5mWithdrawn(s,'xuwen')&&
   !s.flags?.m4_xu_case&&!s.militaryCareer?.xuRecon231&&!s.npcMilitaryCareers?.xuwen&&
   (!p||!p.active&&p.year<=230)&&auh5oParent(s));
}
function auh5oStarted(s){
 return !!(auh5lShu(s)&&s.flags?.m4_xu_case==='service_review'&&auh5mNomination(s,'xuwen')&&
  s.civicCareer.dragonNominations227.xuwen.status==='conditional_interest'&&!auh5mWithdrawn(s,'xuwen')&&
  auh4nSeen(s,'ch12_c62_06_personal_230'));
}
function auh5oCurrent(s,year){
 const p=s?.militaryCareer?.fieldPosition;
 return !!(auh5nLiving(s)&&auh5oStarted(s)&&s.storyClock?.year===year&&!s.flags.m4_xu_closed&&
   (!p||p.year<=year)&&(!p?.active||(s.scene==='m4_231_xu_contact'&&p.proof==='m4_5o:measured_road231')));
}
function auh5oOptions(s,list,year){
 return auh5oCurrent(s,year)?list:[opt('Close the unsupported review without creating an appointment.','m4_231_xu_close')];
}
function auh5oMark(s,scene,key,value,allowed,year,prior){
 if(s.scene!==scene||!auh5oCurrent(s,year)||s.flags[key]!==undefined||
   !allowed.includes(value)||(prior&&!auh4nSeen(s,prior)))return false;
 flag(s,key,value);return true;
}
function auh5oOrder(s,presence){
 if(!['field','delegate'].includes(presence)||!auh5oCurrent(s,230)||!auh5oParent(s)||
   !['bounded','audited'].includes(s.flags?.m4_xu_terms))return;
 if(!auh5oMark(s,'m4_230_xu_order','m4_xu_presence',presence,['field','delegate'],230,'m4_230_xu_terms'))return;
 s.militaryCareer.xuOrder230={schema:1,source:s.scene,year:230,missionYear:231,presence,
   parent:auh5oParent(s),scope:s.flags.m4_xu_terms,authority:'Shu receiving command, bounded scout inquiry'};
 note(s,'The Order for a Question, 230',presence==='field'?
  'You accepted an absence from court with named coverage, to attend an inspected field reconnaissance. No personal force has yet been transferred.':
  'You remained at court while Xu Wen and the receiving officers planned the inspected reconnaissance. A courier report cannot become your battlefield memory.');
}
function auh5oOrderProof(s){
 const e=s?.militaryCareer?.xuOrder230;
 return !!(e?.schema===1&&e.source==='m4_230_xu_order'&&e.year===230&&e.missionYear===231&&
   ['field','delegate'].includes(e.presence)&&e.presence===s.flags?.m4_xu_presence&&
   e.authority==='Shu receiving command, bounded scout inquiry'&&
   ['bounded','audited'].includes(e.scope)&&e.scope===s.flags?.m4_xu_terms&&
   auh5nSource(s,e.parent)&&typeof e.parent.wasActive==='boolean'&&auh5oStarted(s)&&auh4nSeen(s,e.source));
}
function auh5oMuster(s){
 const m=s.militaryCareer,e=m.xuOrder230,p=m.fieldPosition;
 if(s.scene!=='m4_230_xu_muster'||!auh5oCurrent(s,230)||!auh5oOrderProof(s)||m.xuMuster230||p?.active)return;
 const parent=m.units.find(u=>u.id===e.parent.id&&u.source===e.parent.source);
 const available=auh5oParent(s);
 if(!parent||!available||available.id!==parent.id||!auh5nSource(s,parent)||
   (parent.active!==false)!==e.parent.wasActive)return;
 const id='m4-230-xu-screen-'+parent.id;if(m.units.some(u=>u.id===id))return;
 parent.active=false;
 const unit={id,source:'m4_230_xu_muster:inspected',name:'Xu Wen — Measured Road Screen',active:true,
   commander:'xuwen',rank:'Acting Commander',infantry:200,cavalry:40,archers:0,morale:'—',discipline:'—'};
 m.units.push(unit);
 m.xuMuster230={schema:1,source:s.scene,year:230,proof:'m4_5o:physical_muster230',
   parent:clone(e.parent),unit:{id,source:unit.source,infantry:200,cavalry:40,archers:0},inspection:true};
 flag(s,'m4_xu_muster',true);chapterSixAdvanceYear(s,231,'m4_231_xu_road');
 note(s,'The Screen Actually Counted','One existing 200-infantry/40-cavalry detachment was inspected and temporarily transferred. Its parent roll was closed. Han Sheng’s command and the other parent rolls were untouched.');
}
function auh5oMusterProof(s){
 const e=s?.militaryCareer?.xuMuster230,o=s?.militaryCareer?.xuOrder230;
 return !!(e?.schema===1&&e.source==='m4_230_xu_muster'&&e.year===230&&e.inspection===true&&
   e.proof==='m4_5o:physical_muster230'&&e.unit?.id==='m4-230-xu-screen-'+e.parent?.id&&
   e.unit.source==='m4_230_xu_muster:inspected'&&e.unit.infantry===200&&e.unit.cavalry===40&&e.unit.archers===0&&
   JSON.stringify(e.parent)===JSON.stringify(o?.parent)&&auh5nSource(s,e.parent)&&
   s.flags?.m4_xu_muster===true&&auh5oOrderProof(s)&&auh4nSeen(s,e.source));
}
function auh5oLiveUnit(s){
 if(!auh5oMusterProof(s))return null;
 const unit=s.militaryCareer.xuMuster230.unit;
 const found=(s.militaryCareer.units||[]).filter(u=>u.id===unit.id&&u.source===unit.source&&u.active!==false);
 return found.length===1&&found[0].infantry===200&&found[0].cavalry===40&&found[0].archers===0?found[0]:null;
}
function auh5oDeploy(s,plan){
 if(!auh5oLiveUnit(s)||!auh5oMark(s,'m4_231_xu_road','m4_xu_plan',plan,['trace','shelter','probe'],231,'m4_230_xu_muster'))return;
 if(s.flags.m4_xu_presence==='field')s.militaryCareer.fieldPosition={
   year:231,proof:'m4_5o:measured_road231',active:true,
   formation:'Inspected field screen: 200 infantry, 40 cavalry and the original receiving officers',
   sector:'Western Shu road below a rain-cut ridge and civilian detour',
   commander:'You hold the bounded task; Xu Wen may contradict unsupported estimates',
   objective:'Verify bearings, protect counted carts and return within the marked interval'};
}
function auh5oOutcome(s,response){
 const field=s.flags.m4_xu_presence==='field',plan=s.flags.m4_xu_plan;
 return field&&plan==='probe'&&response==='press'||!field&&plan==='probe'?'exposed':
   plan==='shelter'?'sheltered':'verified';
}
function auh5oContact(s,response){
 const field=s.flags.m4_xu_presence==='field',p=s.militaryCareer.fieldPosition;
 if(s.scene!=='m4_231_xu_contact'||!auh5oCurrent(s,231)||!auh5oLiveUnit(s)||
   s.militaryCareer.xuService231||!auh4nSeen(s,'m4_231_xu_road')||
   !['hold','verify','press'].includes(response)||!['trace','shelter','probe'].includes(s.flags.m4_xu_plan)||
   (field&&(!p?.active||p.proof!=='m4_5o:measured_road231')))return;
 const result=auh5oOutcome(s,response),wound=field&&result==='exposed'?'strained_knee':null;
 const opponent=result==='exposed'?'The rival scout captain independently occupied the changed ridge and forced the bounded recall.':
   'The rival scout captain withdrew his screen toward its own ridge and retained the disputed upper ground.';
 s.militaryCareer.xuService231={schema:1,source:s.scene,year:231,unitId:s.militaryCareer.xuMuster230.unit.id,
   presence:field?'field':'court',plan:s.flags.m4_xu_plan,response,result,wound,opponent};
 flag(s,'m4_xu_response',response);
 if(field){
   s.militaryCareer.fieldPosition={...p,active:false,objective:'Contact ended; receiving line and witnessed report remain'};
   if(wound)flag(s,'m4_xu_knee_strain',true);
 }
 note(s,'The Measured Road, 231',AUH5O_RESULTS[result]+' '+opponent+
   (field?' You attended the real unit.':' You remained in court; no personal combat or sight was awarded.')+
   (wound?' The exposed movement strained your knee.':''));
}
function auh5oService(s){
 const e=s?.militaryCareer?.xuService231;
 if(!e||!auh5oMusterProof(s)||e.schema!==1||e.source!=='m4_231_xu_contact'||e.year!==231||
   e.unitId!==s.militaryCareer.xuMuster230.unit.id||!['trace','shelter','probe'].includes(e.plan)||
   e.plan!==s.flags?.m4_xu_plan||!['hold','verify','press'].includes(e.response)||e.response!==s.flags?.m4_xu_response||
   e.presence!==(s.flags.m4_xu_presence==='field'?'field':'court')||
   e.result!==auh5oOutcome(s,e.response)||e.wound!==(e.presence==='field'&&e.result==='exposed'?'strained_knee':null)||
   !auh4nSeen(s,'m4_231_xu_road')||!auh4nSeen(s,e.source))return false;
 return e.opponent===(e.result==='exposed'?'The rival scout captain independently occupied the changed ridge and forced the bounded recall.':
   'The rival scout captain withdrew his screen toward its own ridge and retained the disputed upper ground.');
}
function auh5oReturn(s,answer){
 if(!auh5oService(s)||!auh5oMark(s,'m4_231_xu_return','m4_xu_report',answer,['checked','shared','claim'],231,'m4_231_xu_contact'))return;
 note(s,'The Account Neither Ruler Could Improve',answer==='claim'?
   'You attempted to claim all credit. Xu Wen retained the independent copy, and it did not become a military qualification.':
   'The corrected bearings, households and rival screen remained in the public record. Xu Wen could disagree without losing the actual service he had performed.');
}
function auh5oReview(s,answer){
 if(s.scene!=='m4_231_xu_review'||!auh5oCurrent(s,231)||s.flags.m4_xu_review||
   !['recognized','deferred','declined'].includes(answer)||!auh5oService(s)||!auh4nSeen(s,'m4_231_xu_return'))return;
 if(answer==='recognized'&&!['checked','shared'].includes(s.flags.m4_xu_report))return;
 flag(s,'m4_xu_review',answer);
 s.militaryCareer.xuRecon231={schema:1,source:s.scene,year:231,answer,
  result:s.militaryCareer.xuService231.result,report:s.flags.m4_xu_report,
  status:answer==='recognized'?'witnessed_service_only':'no_qualifying_appointment'};
 note(s,'The Reconnaissance Service Review',answer==='recognized'?
   'An independent, witnessed service qualification was recorded. General grade, Dragon commission, a permanent command and additional troops were expressly NOT conferred.':
   'The hearing closed without a qualifying commission. A refused or deferred review cannot be converted to General rank by year or relationship.');
}
function auh5oReviewProof(s){
 const e=s?.militaryCareer?.xuRecon231;
 return !!(e?.schema===1&&e.source==='m4_231_xu_review'&&e.year===231&&
   ['recognized','deferred','declined'].includes(e.answer)&&e.answer===s.flags?.m4_xu_review&&
   e.result===s.militaryCareer?.xuService231?.result&&e.report===s.flags.m4_xu_report&&
   e.status===(e.answer==='recognized'?'witnessed_service_only':'no_qualifying_appointment')&&
   auh5oService(s)&&auh4nSeen(s,e.source));
}
function auh5oClose(s){
 if(s.scene!=='m4_231_xu_close'||!auh5oStarted(s)||s.flags.m4_xu_closed)return false;
 const p=s.militaryCareer?.fieldPosition;
 if(p?.active||p?.year>(s.storyClock?.year||0))return false;
 if(auh5oMusterProof(s)){
   const unit=auh5oLiveUnit(s),e=s.militaryCareer.xuMuster230;
   const parent=s.militaryCareer.units.find(u=>u.id===e.parent.id&&u.source===e.parent.source);
   if(!unit||!parent||parent.active!==false)return false;
   unit.active=false;parent.active=e.parent.wasActive;
   flag(s,'m4_xu_unit_returned',true);
 }
 flag(s,'m4_xu_closed',true);
 note(s,'The Boundaries of Service','The inspected temporary formation was returned to its actual source; the new reconnaissance service remains a separately witnessed account, not a grant of General, Dragon, territory, staff or new forces.');
 return true;
}
const auh5oOldPersonalChoices=SCENES.ch12_c62_06_personal_230.choices;
SCENES.ch12_c62_06_personal_230.choices=s=>[...auh5oOldPersonalChoices(s),
 ...(auh5oEntry(s)?[opt('Open Xu Wen’s separate, witnessed scout service inquiry.','m4_230_xu_hearing',x=>flag(x,'m4_xu_case','service_review'))]:[])];
scene('m4_230_xu_hearing',16,'The Map He Would Not Sign',s=>[
 '<p>Xu Wen’s checked reply from the council of 227 has rested in a clerk’s packet longer than either of you wished. Conditional interest was all it promised. He is not a General, and no one has put his hand upon a Dragon standard. He has sent a second packet, this one containing two versions of the same road.</p>',
 '<p>The first is neat. Its hills keep their shape, the ford is a thin line, and the distances are perfect. The second was folded in the rain. A smear of ink conceals an old marker; a civilian guide has written a correction below it. Xu has refused to sign the tidy copy.</p>',
 '<p>You remember the early camp and the campaigns in which he corrected confident estimates, but shared history does not exempt him from the obligations of today. His own receiving officers must confirm what he can leave behind. A formation must be available without borrowing the soldiers presently commanded by another man.</p>',
 '<p>'+ (auh5nActive(s,'hansheng')?'Han Sheng’s separate command remains on its lawful roll. You do not bring his men into this hearing by writing a friend’s name twice.':'The earlier Dragon inquiries and unfilled places remain separate from the service now proposed.')+'</p>',
 '<p>Xu’s note ends with a sketch of a horse standing motionless beside a boundary stone. Beneath it he has written that the horse has not confirmed the bearing. A clerk asks whether this is a joke. You say it is, and ask him to bring the other map.</p>'
].join('\n'),s=>auh5oOptions(s,[
 opt('Hear the terms on which an independent reconnaissance can be judged.','m4_230_xu_terms'),
 opt('Leave the conditional inquiry without any military commission.','m4_231_xu_close')
],230),'Chapter XIV · The unsigned map');
scene('m4_230_xu_terms',16,'Two Distances for the Same Road',s=>[
 '<p>Xu Wen sends a second receiving copy, with the wet correction still visible. He will lead a bounded inspection only if its present officers retain the right to contradict him, the civilian carts receive a separate return line, and the command is permitted to report failure without finding a scapegoat to replace the missing distance.</p>',
 '<p>In the receiving office, one commander proposes that the scouts count wagons and cavalry as if they could occupy the same space at the same hour. The next officer objects before the words are finished. Xu asks which of them will tell a driver to move his cart through a horse. Their laughter has an edge; they have all seen orders less absurd carried into battle.</p>',
 '<p>You may order two independent measurements with household capacity checked, or preserve a shorter task within a marked recall line. Both cost something. The first loses time. The second may return knowing less. Neither creates a General or a future Dragon by asserting that such titles would be useful.</p>',
 '<p>He does not ask you to be infallible. He asks whether he will still be allowed to tell you that the road on your favorite map does not exist.</p>'
].join('\n'),s=>auh5oOptions(s,[
 opt('Require two witnessed bearings and separate household capacity returns.','m4_230_xu_order',x=>auh5oMark(x,'m4_230_xu_terms','m4_xu_terms','audited',['audited','bounded'],230,'m4_230_xu_hearing')),
 opt('Authorize a bounded reconnaissance under an explicit recall marker.','m4_230_xu_order',x=>auh5oMark(x,'m4_230_xu_terms','m4_xu_terms','bounded',['audited','bounded'],230,'m4_230_xu_hearing')),
 opt('Reject the service proposal without altering Xu Wen’s earlier work.','m4_231_xu_close')
],230),'Chapter XIV · Two measurements');
scene('m4_230_xu_order',16,'An Emperor Cannot See Through a Courier',s=>[
 '<p>The relevant ministers and existing officers have their own duties. A journey by the Emperor requires those responsibilities to be covered rather than abandoned under a grand phrase. You ask who will answer the petitions while you are away. A clerk provides an unwelcome list.</p>',
 '<p>If you travel, the real formation will have to be inspected before you can lead it into danger. You will stand among soldiers who cannot understand an order until their officers repeat it, and the other captain will decide his own movement. If you stay, Xu Wen will have to judge a field you cannot see and bring back a report which may contradict your plan.</p>',
 '<p>The court offers both courses. Neither licenses a fictitious army or personal battle credit for someone who remained beside the seal.</p>',
 '<p>Outside, the horse on the disputed map has been copied onto a second sheet. Someone has given it a rather more heroic expression. The original clerk is accused of knowing the animal personally.</p>'
].join('\n'),s=>auh5oOptions(s,[
 opt('Cover my court duties and accompany the real inspected formation.','m4_230_xu_muster',x=>auh5oOrder(x,'field')),
 opt('Keep the court watch; let Xu Wen and his officers conduct the inspection.','m4_230_xu_muster',x=>auh5oOrder(x,'delegate')),
 opt('Do not authorize the field assignment.','m4_231_xu_close')
],230),'Chapter XIV · Actual authority');
scene('m4_230_xu_muster',16,'The Men Behind the Bearings',s=>[
 '<p>The receiving officers count the proposed screen by actual parent roll: two hundred infantry and forty cavalry. Their duties and officers are not erased when the detachment moves. A man under treatment is entered on the roll even though he cannot stand at the inspection table.</p>',
 '<p>'+(s.militaryCareer?.xuOrder230?.parent?.wasActive?'The detachment will move from an active formation. Its previous entry must be closed before another can open.':'The earlier handover of 223 established the receiving custody. A new release must be inspected and expressly accepted; an archived return is not a free army.')+'</p>',
 '<p>The household road has its own requirements. Xu refuses the suggestion that a mounted patrol should also pull the wagons through the flooded bend. A company officer writes the two duties in separate columns and makes the error visible rather than merely apologizing for it.</p>',
 '<p>'+(s.flags.m4_xu_presence==='field'?'You are present at the count and can see the waiting soldiers. One asks which road they are being told to believe. You answer that they will follow the one their scouts can actually prove.':'Both copies reach the court. You are not an eyewitness simply because a messenger brings back a precise number.')+'</p>',
 '<p>The temporary detachment can be released for this service alone, or the proposal can end. It will return to its previous lawful formation or custody at the conclusion unless a separate, actually accepted command is established later.</p>'
].join('\n'),s=>auh5oOptions(s,[
 ...(auh5oOrderProof(s)?[opt('Accept the inspected, temporary transfer; proceed to the road in 231.','m4_231_xu_road',auh5oMuster)]:[]),
 opt('Refuse this transfer and issue no soldiers.','m4_231_xu_close')
],230),'Chapter XIV · Inspected service');
scene('m4_231_xu_road',16,'A Road With Two Names',s=>[
 '<p><em>231 CE.</em> At the westward approach the valley narrows into wet reed beds. The lower lane can carry family carts, but the upper path runs close to a rival captain’s scouts. The enemy has a reason to keep the hill: their own line of messages runs across it, and a Shu seal is not a reason to surrender.</p>',
 '<p>'+(s.flags.m4_xu_presence==='field'?'You travel with the assigned infantry and cavalry. The infantry keep the lower road, the mounted screen its checked interval. Xu Wen directs the reporting pairs under their original officers; he is entitled to disagree when your estimated distance fails their witnesses.':'At court you receive the bounded task and a dated first return. Xu Wen has gone with the inspected screen; neither his eyes nor his danger are yours by narration.')+'</p>',
 '<p>A marker has fallen from the ridge. One guide measures from the old tree; another measures from the stone now lying in the ditch. An officer who wants to move before the light fails begins to grow impatient. Xu says he would also prefer to be home before dark, but would rather not arrive by an invented shortcut.</p>',
 '<p>You can trace the disputed bearings, shield the household route or test the exposed slope within the recall boundary. Each gives up time, ground or information; none automatically conquers the enemy position.</p>'
].join('\n'),s=>auh5oOptions(s,auh5oLiveUnit(s)?[
 opt('Send two reporting pairs to verify the actual lower bearing.','m4_231_xu_contact',x=>auh5oDeploy(x,'trace')),
 opt('Protect the household carts and accept a slower arrival.','m4_231_xu_contact',x=>auh5oDeploy(x,'shelter')),
 opt('Test the exposed upper slope within the return boundary.','m4_231_xu_contact',x=>auh5oDeploy(x,'probe'))
]:[opt('Close the unsupported field request.','m4_231_xu_close')],231),'Chapter XIV · The missing marker');
scene('m4_231_xu_contact',16,'The Captain on the Other Hill',s=>[
 s.flags.m4_xu_presence==='field'?
 '<p>Enemy scouts appear on the upper track at the same moment that one reporting pair gives its corrected signal. You stand with a real infantry file, a company officer within hearing and cavalry on the firm slope. The other captain has made his own decision and is shortening your time to act.</p>':
 '<p>The first dated report reaches court. Xu Wen has not won a distant campaign on your behalf. The opposing captain changed his screen, the lower witnesses disagreed and the checked unit continued under its own officers. You may answer the report, but cannot issue a tactical order into yesterday.</p>',
 '<p>'+(s.flags.m4_xu_plan==='probe'?'The higher route is narrower than the chart claimed. One scout turns his horse across the path and warns that there is no room to pass a cart.':'The nearer lane is covered, but the second bearing has not yet been delivered. A driver keeps asking whether the men in the upper reeds are friends.')+'</p>',
 '<p>Xu Wen sends an honest correction to the plan. The officer receiving it looks toward you without trying to make the disagreement disappear. The immediate choice is not whether to become legendary. It is whether the living men can return by the route the map has finally admitted exists.</p>'
].join('\n'),s=>auh5oOptions(s,auh5oLiveUnit(s)?(s.flags.m4_xu_presence==='field'?[
 opt('Hold the return marker and cover the approaching pairs.','m4_231_xu_return',x=>auh5oContact(x,'hold')),
 opt('Verify the new bearing and correct the marching order.','m4_231_xu_return',x=>auh5oContact(x,'verify')),
 opt('Press personally toward the disputed interval before the screen closes.','m4_231_xu_return',x=>auh5oContact(x,'press'))
]:[
 opt('Accept the independent report without claiming personal combat.','m4_231_xu_return',x=>auh5oContact(x,'hold')),
 opt('Require the second witness copy before judging the result.','m4_231_xu_return',x=>auh5oContact(x,'verify')),
 opt('Record that the proposed upper route was too dangerous.','m4_231_xu_return',x=>auh5oContact(x,'press'))
]):[opt('Close an unsupported scout report.','m4_231_xu_close')],231),'Chapter XIV · The rival screen');
scene('m4_231_xu_return',16,'The Map He Finally Signed',s=>[
 '<p>'+(auh5oService(s)?AUH5O_RESULTS[s.militaryCareer.xuService231.result]:'No operation can be credited without its witnessed return.')+'</p>',
 '<p>'+(s.flags.m4_xu_presence==='field'?'You hear the accounts among the returning soldiers. The rival captain has held his own ground; the men beside you know the exact weight of being told to leave a dangerous place rather than call a retreat an advance.':'You read the field report at court. The officers’ decisions remain theirs. A dated letter cannot give you the memory of a battle you did not attend.')+'</p>',
 '<p>'+(s.militaryCareer?.xuService231?.wound?'The exposed movement strained your knee on the broken bank. A soldier steadies you on the return path. Xu Wen asks whether you now believe the witness who said it was too steep. You are angry enough to laugh and sore enough to say yes.':'Xu Wen returns with the corrected drawings and refuses to make the missing ridge into a captured banner. Two soldiers have taken turns keeping a rain-soaked chart dry beneath their tunics.')+'</p>',
 '<p>The account names the independent enemy movement, the delay to the household carts and the real duty of the inspected unit. The cart driver who supplied a disputed distance has signed beneath the military officer. Xu calls him the most useful man on the page. The driver says he would rather be useful somewhere with a better road.</p>',
 '<p>You can preserve the unflattering measurement, share the named witnesses or attempt to claim a personal triumph. The last does not erase the original return, but it will prevent an independent service qualification from being entered under your name.</p>'
].join('\n'),s=>auh5oOptions(s,[
 ...(auh5oService(s)?[
 opt('Preserve the disputed distances exactly as witnessed.','m4_231_xu_review',x=>auh5oReturn(x,'checked')),
 opt('Sign with the scouts, receiving officers and civilian witnesses.','m4_231_xu_review',x=>auh5oReturn(x,'shared')),
 opt('Claim the whole operation as my personal triumph.','m4_231_xu_review',x=>auh5oReturn(x,'claim'))
 ]:[]),opt('Close the case without entering a false report.','m4_231_xu_close')
],231),'Chapter XIV · An honest return');
scene('m4_231_xu_review',16,'Service Is Not Yet a Standard',s=>[
 '<p>The court reads both returns before discussing honors. Xu Wen’s work is not made smaller by the absence of a victory. He found the real route, accepted the correction of people without titles, and kept his own officers accountable when the rival captain moved.</p>',
 '<p>He wants the testimony left in the record even if no larger command follows. The General and Dragon positions discussed in 227 require demonstrated rank, continuing duty, a distinct service hearing, freely accepted appointment and actual command. They will not be granted today. The inspected scouts have completed a temporary service, not a permanent military transfer.</p>',
 '<p>When the testimony is read, the junior clerk has finally worked out the note about the horse. He asks whether the animal ought to appear in the witness list. Xu says it has already provided more reliable evidence than an officer who reported a ford without looking at it.</p>',
 '<p>Recognize the witnessed reconnaissance as one qualification for a later independent military hearing, defer judgment, or decline to use this result. Every path preserves the service and its cost without granting General, Grand General, troops or a Dragon seat from the calendar.</p>'
].join('\n'),s=>auh5oOptions(s,[
 ...(auh5oService(s)&&['checked','shared'].includes(s.flags.m4_xu_report)?[
 opt('Record the verified service only; a later General hearing will require separate proof.','m4_231_xu_close',x=>auh5oReview(x,'recognized'))
 ]:[]),
 opt('Defer the qualification while preserving the original witness account.','m4_231_xu_close',x=>auh5oReview(x,'deferred')),
 opt('Decline to use this reconnaissance as a higher command qualification.','m4_231_xu_close',x=>auh5oReview(x,'declined'))
],231),'Chapter XIV · Not a promotion');
scene('m4_231_xu_close',16,'A Blank Place Kept Honest',s=>[
 '<p><em>'+String(s.storyClock?.year||230)+' CE.</em> '+(auh5oReviewProof(s)&&s.flags.m4_xu_review==='recognized'?'Xu Wen has an independently witnessed reconnaissance on the military return. The qualifications of a future command remain to be tested.':'No General or legendary qualification is inferred from a reply, an unfinished mission or a refused hearing.')+'</p>',
 '<p>'+(auh5oService(s)?AUH5O_RESULTS[s.militaryCareer.xuService231.result]:'No completed reconnaissance or victory is invented.')+' The other Dragon nominees retain their own conditions; their answers have not been rewritten to accommodate a story about Xu Wen.</p>',
 '<p>There will be time to learn whether he desires a wider command, and whether the state can issue one without taking another commander’s soldiers. For now the working maps go back to the people who will use them, and the proposed future standards remain as empty as the appointments actually made.</p>'
].join('\n'),s=>[
 ...(s.storyClock?.year===230?[opt('Close the inquiry and return to the original 230 personal interval.','ch12_c62_06_personal_230',auh5oClose)]:[]),
 opt('Close the temporary assignment and carry the record into the court of 232.','ch12_c62_07_council_232',x=>{
   if(auh5oClose(x))chapterSixAdvanceYear(x,232,'ch12_c62_07_council_232');
 })
],'Chapter XIV · The next hearing');
for(const id of AUH5O_IDS)SCENES[id].displayChapter=14;
const auh5oOldPortrait=auhPortraitDirectBattle;
auhPortraitDirectBattle=function(s){
 if(s?.storyClock?.year===231&&s.flags?.m4_xu_presence==='field'&&s.scene==='m4_231_xu_contact'&&
   auh5oLiveUnit(s)&&s.militaryCareer?.fieldPosition?.active&&s.militaryCareer.fieldPosition.proof==='m4_5o:measured_road231')
   return ['trace','probe'].includes(s.flags.m4_xu_plan);
 return auh5oOldPortrait(s);
};
const auh5oOldMemories=npcMemories;
npcMemories=function(id){
 const list=auh5oOldMemories(id);
 if(state&&id==='xuwen'&&auh5oService(state))list.push('Xu Wen personally corrected the reconnaissance of 231; the opposing captain kept his own ridge. '+(state.flags.m4_xu_presence==='field'?'You served with the inspected formation.':'You heard the dated account from court, not as a battlefield eyewitness.'));
 if(state&&id==='xuwen'&&auh5oReviewProof(state))list.push(state.flags.m4_xu_review==='recognized'?
   'His 231 service was recorded as an independently witnessed qualification for later review; no General or Dragon commission was awarded.':
   'The reconnaissance hearing was closed without a new military rank or legendary appointment.');
 return list;
};
const auh5oOldUnits=auhStoryUIRecordedUnits;
auhStoryUIRecordedUnits=function(s){
 const units=s?.militaryCareer?.units;
 if(!Array.isArray(units)||!units.some(u=>u?.source==='m4_230_xu_muster:inspected'))return auh5oOldUnits(s);
 const ok=auh5oMusterProof(s),id=s.militaryCareer.xuMuster230?.unit.id;
 const projected=units.map(u=>u.source==='m4_230_xu_muster:inspected'?
   ok&&u.id===id&&Number.isSafeInteger(u.infantry)&&u.infantry>=0&&u.infantry<=200&&
   Number.isSafeInteger(u.cavalry)&&u.cavalry>=0&&u.cavalry<=40&&u.archers===0?
   {...u,rank:'Acting Commander'}:{...u,active:false}:u);
 return auh5oOldUnits({...s,militaryCareer:{...s.militaryCareer,units:projected}});
};
const auh5oOldMilitary=militaryPanel;
militaryPanel=function(){
 const html=auh5oOldMilitary();
 if(!state||!auh5oMusterProof(state))return html;
 return html+'<section class="panel mc-panel" aria-label="Xu Wen scout screen"><h3>Xu Wen · Measured Road Service</h3><p>One existing 200-infantry/40-cavalry detachment was temporarily transferred after inspection. '+
 (state.flags.m4_xu_unit_returned?'Its assignment was closed to the former roll or receiving custody.':'The temporary receiving assignment is still open on its actual roll.')+
 '</p><p>'+(state.flags.m4_xu_presence==='field'?'You attended the actual field movement.':'You delegated the field movement and retained court obligations.')+
 '</p>'+(auh5oService(state)?'<p>'+esc(AUH5O_RESULTS[state.militaryCareer.xuService231.result])+'</p>':'')+
 '<p>No General, Grand General or Dragon commission was created in this service batch.</p></section>';
};
const auh5oOldCivic=civicPanel;
civicPanel=function(){
 return auh5oOldCivic()+(state&&auh5oStarted(state)?
 '<section class="panel mc-panel" aria-label="Xu Wen service inquiry"><h3>Independent Scout Review · 230–231</h3><p>'+
 (auh5oReviewProof(state)&&state.flags.m4_xu_review==='recognized'?
 'Verified reconnaissance has been recorded for a future lawful qualification hearing.':
 'No accepted higher command or legendary appointment has been entered from the proposal.')+
 '</p></section>':'');
};
const auh5oOldHealth=characterPanel;
characterPanel=function(){
 let html=auh5oOldHealth();
 if(state&&characterTab==='health'&&auh5oService(state)&&state.militaryCareer.xuService231.wound){
   html=html.replace('No lasting injuries are recorded in your chronicle.','The scout-screen injury below remains part of your chronicle.');
   html+='<section class="panel" aria-label="Scout screen knee injury"><h3>Measured Road · 231</h3><p>'+
    (state.storyClock.year>=232?'The knee strain recovered after the return, though long marches can recall the fall.':'The strained knee needs treatment and rest before further marching.')+'</p></section>';
 }
 return html;
};
const auh5oOldCouncil=SCENES.ch12_c62_07_council_232.body;
SCENES.ch12_c62_07_council_232.body=s=>auh5oOldCouncil(s)+(auh5oService(s)?
 '<p>The independent reconnaissance of 231 remains in the next court account: '+esc(AUH5O_RESULTS[s.militaryCareer.xuService231.result])+
 (auh5oReviewProof(s)&&s.flags.m4_xu_review==='recognized'?' Xu Wen has witnessed service for a future hearing, not a new legendary commission.':' No military title was inferred from the report.')+'</p>':'');
