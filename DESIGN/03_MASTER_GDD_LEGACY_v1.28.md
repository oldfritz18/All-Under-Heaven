**Approved Shu succession (16 Nov 2026):** `DESIGN/APPROVED_SHU_SUCCESSION_2026-11-16.md` governs exceptional outsider succession without adoption and new post-223 mandate with actual Liu Shan/court consent. Supersedes earlier unresolved mechanism notes; no retroactive testament or automatic crown. Follow current PROGRESS/QA for implementation.

# Approved quality requirement — Issue #1, 16 November 2026

`DESIGN/APPROVED_EPIC_ELEVATIONS_ISSUE_1.md` is binding alongside locked decisions. [Issue #1](https://github.com/oldfritz18/All-Under-Heaven/issues/1) requires meaningful General recognition/assumption of command, a separate earned Sixth Tiger climax within Liu Bei's plausible shared-life window, multi-scene Shu enthronement with contested legitimacy/acceptance/public ceremony/private aftermath/first consequential imperial decision, and personalized Dragon nominations/consent/investitures/actual handovers plus collective recognition only after five valid appointments. Preserve 0–5 Dragon seats, historical autonomy, all five Special Staff, legacy saves and portraits. Shu accession is separate from China-wide unification; no free troops, ministers, treasury or silently selected dynastic law. Implementation/QA gates remain open in `docs/ISSUE_1_IMPLEMENTATION_PLAN.md` and `docs/PROGRESS.md`; active source is `GAME/ACTIVE_BUILD.txt`, not historical filenames below.

# Addendum — v0.4.99.2l (INTERNAL)

**Non-negotiable correction:** the one signature Great Glaive, new white-silver armor and one white companion must be **obtainable before General** through genuine decisions and earned relationships. General rank does not unlock or grant these items. Neither item is mandatory for progression or any ending. Earlier scenes are optional, and later preexisting acquisition routes remain only for unclaimed items, with the same IDs and save checks. Portraits must not display unowned equipment. Source implementation is the v0.4.99.2l HTML, not the older 230s-only chronology contained in some preceding addenda.

---

# ADDENDUM — All Under Heaven v0.4.99.2k: Narrative-Earned 8-Stage Portrait System

**Authoritative executable:** `ALL_UNDER_HEAVEN_v0.4.99.2k_DEV_EARNED_PORTRAITS.html`  
**SHA-256:** `4464bc3b041340f099b42037e189b80f5b126f1c57ab571fc9ade19b21356747`  
**Based on:** `v0.4.99.2j`, SHA-256 `7559e01a28ab3bd96d37be1dd33feb03a416c7b9fd27ca2a9f4b293adadb5ba7`  
**Status:** DEVELOPMENT; NOT BETA; preserves original narrative and state format.

This checkpoint expands the earlier five-stage concept preview to eight approved standalone visual identities: **Nobody, Soldier, Officer, General, King, King at War, Emperor, Emperor at War**. Protagonist remains male, clean-shaven, consistent Face Master Option C. No story scenes, romance paths, item IDs, save keys, rank claims or relationship mechanics were changed. Portrait is a read-only projection from current story state and does not grant titles, equipment, or a win.

**Stage gates:** Nobody until actual service; Soldier on accepted early service; Officer only after an explicitly accepted limited appointment; General only where existing social-position logic and explicit field command agree; King/Emperor only when current fully ratified titles remain active; battle variants only in explicitly enumerated personal-command sequences. Simply reaching a date or chapter does not unlock a higher stage. Counsels, delegated missions and abdication do not imply personal combat or retained sovereignty.

**Critical equipment chronology:** The approved images for General and the two sovereign battle variants visibly show three unique legendary pieces that have voluntary independent in-game acquisition gates. They are therefore displayed **only after all three are recorded as owned**; until then a NON-FINAL standard-gear field image prevents spoilers/unearned gear. This ninth embedded image is a provisional display fallback, not an approved ninth stage. All eight approved full-sized source PNGs are retained in the handoff, with optimized WebP images embedded offline in the HTML. The full-image modal preserves native proportions, while responsive thumbnails use object-fit:contain rather than crop.

**Current narrative gap:** The active story does not contain a directly controlled battlefield encounter after the valid imperial enthronement. Emperor at War is wired for future earned war contexts, **not automatically unlocked** in current scenes. New story content and QA are needed before it can appear via real gameplay. Independent-political/faction routes still need contextual background art review. Abdicated/retired appearance requires future bespoke art, not unearned old crowns.

**QA:** JS syntax PASS; 176 responsive/feature/checkpoint assertions across 320/390/768/1280 px PASS; 558 × 2 sampled scene body/choices renders PASS (1,116); nine images decoded in browser PASS; old `v0.4.99.2j` save PASS in simulated storage; 13 dev checkpoints exercised per viewport. Physical local-file close/reopen could NOT be verified: sandbox Chromium blocked file:// by administrator policy. Manual exhaustive editorial branch and physical mobile performance still pending.

---

# INHERITED MASTER GDD CONTENT — v1.28 FAST / 0.4.99.2j, retained verbatim after this addendum

# ADDENDUM — v0.4.99.2j / Dynamic Protagonist Portraits

**Active game:** `ALL_UNDER_HEAVEN_v0.4.99.2j_DEV_DYNAMIC_PROTAGONIST_PORTRAITS.html`  
**SHA-256:** `7559e01a28ab3bd96d37be1dd33feb03a416c7b9fd27ca2a9f4b293adadb5ba7`  
**Parent HTML:** v0.4.99.2i, SHA-256 `de73dcc711ca1769f6c24374f664593a0a13d9b56835da4a2c3570977cd30089`  
**Status:** DEVELOPMENT — not beta.

New implementation is a **presentation-only pilot**. The male protagonist's current visual tier is derived from earned, presently held game authority and evidence, not chapter number or age alone: Nobody, Soldier, General (command-tier visual), King, Emperor. Rank transitions use existing history and sovereignty predicates; this feature does not grant rank. Do not display the King/Emperor portrait on an unratified title. A peaceful abdication must not imply present imperial/royal office.

**Identity and continuity:** same face throughout, clean-shaven, hair may follow office and dress, physical maturation from age sixteen until adulthood; Timeless Heroes life rules remain unchanged. Contextual backgrounds, in-game inventory-accurate armor/robes, injury variants, and individually redrawn portrait detail remain *future art work*; the current five images are **crops of the approved 5-stage concept sheet**, not final character art. Stage I presently may look older than sixteen. On-screen captions explicitly say *Portrait preview*.

**UI:** Character page shows a clickable portrait on desktop and mobile; the existing full-image modal now accepts the protagonist as well as encountered NPCs. Zoom buttons (+/−), Escape, backdrop click and close button work. Previously unencountered NPC portrait security unchanged. All portrait images are embedded as WebP in the standalone HTML; no new save keys or relationship data.

**QA:** 4 viewports; 64 passed checks including stage gates, zoom, modal behavior and hidden NPC portrait; 1,116 scene renders over two sampled states with valid choice destinations; five images decoded; 13 developer checkpoint enter/exit checks left stored save bytes identical; old v0.4.99.2i save loaded in simulated storage. Physical `file://` close/reopen not verified because Chromium here blocks local navigation. Full manual branch editorial and on-device performance remain open.

---

# Inherited Master GDD FAST v1.28 — v0.4.99.2i (unaltered)

# MASTER GDD — CURRENT FIRST / v0.4.99.2i · People Menu Filtering

**Active file:** `ALL_UNDER_HEAVEN_v0.4.99.2i_DEV_PEOPLE_GENDER_RELATIONSHIP_AUDIT.html`. SHA-256 `de73dcc711ca1769f6c24374f664593a0a13d9b56835da4a2c3570977cd30089`. INTERNAL / POSSIBLY SPOILER-BEARING.

## Approved UI decision
- People is divided by **Male** and **Female** first. Under Male show **Friends / Neutral / Enemies**. Under Female show **Acquaintances / Friends / Lovers**.
- Keep the established hamburger navigation (desktop and mobile), English-only title, historical heroic art, and player-visible knowledge gating. Existing People portrait cards are reused, no new art assets required for this checkpoint.
- `auhFemaleRelationshipCategory` evaluates direct knowledge and real confirmed relationship choices; no love flag is set because the UI is opened. Romantic interest alone does not qualify as Lovers. A later explicitly chosen friendship or separation can supersede an earlier romantic event; marriage is treated as a partner relation unless future game rules explicitly change that status.
- Female NPCs can still be adversaries, neutrals or independent actors in the internal story even though the user chose a more personal female UI grouping. Never coerce those states to friendship or romance.
- Display groups are client-side and not saved as campaign choices. Names not yet encountered remain masked. No change to data of unencountered historical characters.

## Status and QA
53 people / 39 historical / 14 original; seven female roster IDs; 558 scenes, 12 chapters, 14 portraits. Four widths PASS; 13 preview checkpoints PASS; legacy save PASS using simulated storage; 1,116 selected-state scene render checks PASS. See `ALL_UNDER_HEAVEN_QA_RECEIPT_v0.4.99.2i.md` and `ALL_UNDER_HEAVEN_PEOPLE_RELATIONSHIP_AUDIT_v0.4.99.2i_INTERNAL.md`. Full editorial audit and `file://` browser close/reopen remain open; **NOT BETA**.

---

# MASTER GDD — CURRENT FIRST / v0.4.99.2h

**ACTIVE HTML:** `ALL_UNDER_HEAVEN_v0.4.99.2h_DEV_CHRONOLOGY_CAST_VISUAL_PILOT.html` · SHA-256 `14d318fbbc61e1eaa4138b3987436b8df3b9958b7d15212b2edbdde99a859b8f`. INTERNAL / MAY CONTAIN SPOILERS.

## HC05 design and QA contract

1. Historical casting is the intersection of **39 historical IDs** and **player-witnessed knowledge gates**. An archivist's report or debug roster does not signify personal acquaintance. Historical baseline notes must never force a death or rank change, given the game's divergence model.
2. In Developer Tools only, **Historical Audit** lists each ID, game-context date, provisional historic-year annotation (12 total), missing dates (27 pending) and portrait presence. Audit warnings are read-only. Do not expose that ledger in player-facing People or Chronicle.
3. 214/220 optional archive choices now require the actual year plus all inherited source flags. All old choices remain in place. No new story or save schema is introduced.
4. The first visual batch comprises **six original 400×400 WebP portraits** with historical-heroic color and garments; exact files and SHA are in `art/hc05/HC05_ART_MANIFEST.json`. Original eight portraits retained. The normal People screen continues to hide non-encountered identities and art. 14/53 portraits now present.
5. Keep narrative-first Parchment/Ink aesthetic, hamburger menu in both desktop/mobile, English-only title, and Developer Tools explicitly opt-in. No sound until portrait design and device performance are tested.
6. Source references are *research pointers*, not completed certifications. Continue full biography checks for 27 pending, editorial reachability and save durability. NOT BETA.

---

# MASTER GDD — CURRENT FIRST HC04 / v0.4.99.2g

**Active executable:** `ALL_UNDER_HEAVEN_v0.4.99.2g_DEV_HISTORICAL_CHRONOLOGY_QA.html` · SHA-256 `b470660d4f220526b080ba7508deb70a70e59902eed6921da22624b50d1ca912`. Internal reference; spoiler-bearing material remains below.

## HC04 — Design contracts and implementation

- **Temporal provenance:** NPC rank, office and personality remain known only when learned. Role information taken from a document must carry its recorded year; do not silently imply perpetual rank, survival or alliance.
- **Agency and counterfactual history:** historical baseline years inform developer QA, not deterministic in-game deaths. The historical baseline audit entries are incomplete and must not be treated as a whole-cast chronology certification. Player choices may change recorded history, subject to earned consequences.
- **New interludes:** `ch10_hc04_01_dated_offices` (214 CE) and `ch11_hc04_02_letters_outlast_seals` (220 CE) are optional, conditional follow-ups to the 200 CE northern dispatch. All original choices remain on the parent story screen. Completing interludes changes only bounded archive flags and Chronicle notes, never other rulers' choices or personal acquaintance flags.
- **QA:** `hc04ContinuityWarnings` and `HC04_BASELINE_YEAR` are private developer tools, never ordinary narrative UI. Existing HC03 independent southern officers and remembered 208/210 relationship logic remain untouched.
- **Counts:** 53 characters, 558 scenes, 12 chapters. Offline single-file HTML; save keys and narrative IDs inherited. QA has succeeded only on named sampled paths, not all endings. Art unchanged: 8/53 character portraits.
- **Next:** follow source-based lifespan and geography checks for the remaining uncertain roster, then Visual Enhancement batch of remaining portraits. Audio after visual QA; beta blocked on device file save and full editorial checks.

---

# MASTER GDD — CURRENT-FIRST HC03 UPDATE / v0.4.99.2f

**Active executable:** `ALL_UNDER_HEAVEN_v0.4.99.2f_DEV_LIVING_HISTORICAL_CHARACTERS.html` · SHA-256 `d3f34f7dea24643cc1bda4cf47180c05d9dd9074af687c70830c9748dfaca63b`. Historical ensemble 53 People (39 historical / 14 original); scene count 556; 12 chapters. This header supersedes older implementation counts below without deleting existing GDD systems. Internal reference, may contain spoilers.

## HC03 Design Decisions — Verified in source

- **Historical actors must remember only real experience.** A past report does not create an introduction; an earlier interview does not force a later reunion, military command or political allegiance. A later second meeting requires prior actual eyewitness flags and an affirmative choice.
- **Agency:** non-player commands maintain their own schedules. Even when a player returns two years later, staff and commanders may refuse the player's authority. NPC advancement remains independent of player romance, popularity or heroic equipment.
- **Timeline:** 208 (prior encounter) → 210 (optional renewed office records) → 214 and 220 (indirect archival echoes). The latter are documents, not implied proof of officers still holding the same historical office. No claims about historical lifespan are introduced as settled evidence in the player-facing UI.
- **Incremental implementation:** three optional scene registrations, 210 gate attached to `ch09_01`, readback appended to `ch10_01` and `ch11_01`, known-info extensions for already-met officers. No old option or scene was removed. Save schema/key unchanged; no visual or audio payload changed.
- **QA:** Chapter VIII source-legal passage through a HC02 river encounter into an optional HC03 210 follow-up completed; 16 variant cases, older baseline regression, 3,336 dynamic context checks, 13 chapter preview state isolation and old-save migration. Device `file://` close/reopen and comprehensive historical lifespan audit remain unverified. Not beta.
- **Art backlog:** embedded portraits presently cover 8/53 People. Developer index lists all 53, ordinary People is knowledge-gated; art production follows NPC-depth QA.

---

# MASTER GDD — CURRENT-FIRST UPDATE HC02 / v0.4.99.2e

**Executable authority:** `ALL_UNDER_HEAVEN_v0.4.99.2e_DEV_HISTORICAL_CAST_BATCH_02.html` / SHA-256 `4a77213c814ec812e8c3f5c5f9d32572d0cd7a997274ffa3e79ac5f75ef5eaf6`. This update extends implementation metadata only; do not treat old roster counts elsewhere in this file as current. Internal document may contain spoilers.

## HC02 design acceptance

- Historical casting milestone updated: 41 → 53 unique People; 545 → 553 scenes; 12 chapters unchanged, late-Han 190 opening intact. 12 new historical profiles, plus additional optional appearances for two already registered historical figures. 39 historical / 14 original total.
- Optional scenes must pass **agency gate**: a courier or a register may mention someone, but `hasWitnessed(id)` is true only when a player-selected direct meeting occurs. Unknown players see no privileged NPC facts. Reports stay offstage and distinguish uncertain claims from witnessed observations.
- Three physical/time-window anchors: Chapter VI 199 CE; Chapter VII 200 CE; Chapter VIII 208 CE. Report-only historical references never create late-year live encounters with period-inappropriate people.
- Preserve all old options at three entry scenes; explicit no-intervention choices can bypass or close the new incident; no mandatory NPC meeting, faction switch, promotion, personal bonus or forced alliance. Consequences are modest journal flags, observed distinctions, and branch-specific callback text.
- Existing portraits, English-only masthead, one hamburger drawer with vertical labels on desktop/mobile, visual theme, opt-in Developer Tools, Chapter fixtures, and original save schema remain. Art/audio integration remains after HC03, per user priority.
- QA: two viewport branch suites (10 positive subcases); four negative false-meeting cases; source-v0.4.99.2d legacy JSON restored and validated; 13/13 chapter preview save-isolation; 553 scene bodies × six contexts = 3,318 dynamic render/choice inspections, zero missing targets/errors in tested contexts; one bounded 190 legal route to an inherited early terminal path. Physical file:// close/reopen and complete editorial/dynamic-life review still open; no beta claim.

---

# MASTER GDD FAST — HC01 HISTORICAL NPC BATCH (v0.4.99.2d)

**This appendix records implementation status, not a change to approved GDD v1.28 core systems.** Historical casting pool remains the approved 100–120 possible figures, not a mandatory content quota. See GDD-04 (history/knowledge/geography/divergence), GDD-07 (agency), and spoiler-safe QA rules. Old GDD preserved below.

- Implemented 12 additional historical identities into the existing People registry (41 total: 27 historical, 14 original) and six optional early-campaign scene records (545 total; 12 chapters unchanged).
- This is HC01: coalition-era reports/limited personal encounters. Historic offices and remote names are introduced through guarded records, not an automatic camp-wide reunion. Player may skip the optional material while remaining the central decision maker.
- Five **potential**, individually choice-gated, direct historical meetings; seven other new figures currently remain report-only. Not all five can be met in one run of the three mutually exclusive 190 coalition errands. The optional Chapter II courier reports are source-tagged, not personal meetings.
- Living-world behavior is bounded scripted independence: distant officers have their own logistical priorities and can disagree, but this build does NOT implement deep multi-decade individual agency, individual mortality simulation or 12 complete interpersonal paths.
- Protected invariants: legacy save keys/format, `validSave`, history/NPC memory, six adult romance candidates, Inner Circle/earned generals, earned sovereignty, independent historical NPCs, optional one white horse and three legendary gear categories, household agency, eight preserved manuscript endings and three main new ending families, 16-year-old start, title-only English masthead, responsive hamburger UI.
- Stop/go: complete historical NPC expansion and timeline/editorial checks before the next visual polish sprint. Do not represent incomplete images as complete portraits; do not force meetings or expose hidden characters in normal People navigation.

---

# ACTIVE MASTER GDD v1.28 FAST — v0.4.99.1 READER UX POLISH

**Executable:** `ALL_UNDER_HEAVEN_v0.4.99.1_DEV_READER_UX_POLISH.html` (SHA-256 `d2e60b3d31cfe4fe0654b9981d3f522346a25b0f1feeed78f55d6cf11fcb5483`). This update is incremental and *non-narrative*. All 539 scenes, 29 People, 12 chapters, archives, decisions and version-1 save keys remain in place.

## UI/UX implementation delta

| Area | v0.4.99.1 implementation | Backward compatibility |
|---|---|---|
| Reader column | Settings: Focused (620px), Comfortable (695px default), Wide Desktop (810px); mobile always fits screen | Optional `prefs.readerWidth`; old save receives standard without mutation until changed |
| Small screens | Safe-area-aware margins, compact 320px layouts, touch targets, stronger focus visibility, content wrapping | CSS-only; no screen or scene rerouting |
| Keyboard dialogs | Portrait close restores focus to original thumbnail; Tab remains in dialog; Escape closes | Existing portraits unchanged |
| Navigation | Heading focus on panel change; selected subtabs retain keyboard focus | No NPC/relationship/equipment changes |
| Save display | Existing v0.4.98 verified storage and import safeguards kept; reading preferences saved in the existing slot | Same save keys, storage format and save validation |
| Spoiler protection | Developer QA Jump hidden by default; explicit `?devqa=1` query enables preview menu | QA fixture data preserved; actual previews remain unsaved |
| Technical metadata | Corrected document title and active build metadata | No runtime network dependency |

## Regression evidence and outstanding gates

- Syntax PASS. Inherited 1,779 save assertions and 1,767 editorial-preservation assertions. Six inherited feature QA groups pass (713, 813, 584, 715, 1,422, 1,104 checks).
- 539 × 33 synthetic context fragment checks (17,787) show no markup errors; 120 legal randomized complete journeys (34,103 decisions), two lawful guided journeys (420 / 422 decisions) pass with current engine.
- Browser stand-in UI checks: 198 assertions over 6 responsive/theme combinations (320, 390, 768 and 1280px; both dark/light), zero detected JS errors. Inherited simulated save/import regression also passed 45 checks at 390/1280px.
- NOT verified: physical unrestricted `file://` save persistence across browser close/relaunch; full human read-through and independent manual sign-off for 539 scenes / remaining conditional cases. Beta blocked.
- Next milestones after continuing editorial QA: v0.4.99.2 curated visuals, v0.4.99.3 optional sound/ambience, v0.4.99.4 integrated audio/visual/save QA; all subject to regression and physical origin gates.

---

## Prior GDD v1.28 FAST — v0.4.99 overlay (preserved)

# ACTIVE MASTER GDD v1.28 FAST — v0.4.99 EDITORIAL / BRANCH QA

**Executable:** `ALL_UNDER_HEAVEN_v0.4.99_DEV_EDITORIAL_BRANCH_QA.html` (SHA-256 `229c4cc273af355c4272658ba5c979549a649ab667403e54acdbbecddc8addd3`). Retain the design rules of v1.28 FAST; this overlay only updates QA status and non-structural editorial improvements. **539 scenes / 29 People / 12 chapters.**

## Canon and editorial constraints

- The player begins as an unknown 16-year-old in 190 CE and shapes their own history; historical people retain independent choice and agency. Rankings, kingdoms, military victories, spouses, children and legacies are earned, never automatically granted by a title.
- Six romance paths, voluntary 18+ consensual non-graphic adult intimacy and family decisions, young/adult children's independent ambitions, enduring Inner Circle and merit-appointed generals remain. Do not expose private gauges or hidden causes in the UI.
- Exactly one earned great glaive, one earned new white-silver armor set and one earned, player-named exceptional white horse; hidden names and acquisition events stay internal, as do narrative surprises and major loyalty/death conditions.
- Coins support housing, land, facility choices only; no added commodity markets or mandatory taxes. War can be fought personally or directed, but always with costs, logistics, witnesses and the possibility of failure.
- English interface/narrative; Indonesian spoiler-free progress reports. Save slot names and version-1 save schema stay compatible, with extra safeguards against corrupt imports.


## Implementation delta

| Area | Verified v0.4.99 change | No-regression constraint |
|---|---|---|
| Early manuscript typography | Three unclosed paragraphs repaired | Do not change manuscript wording, triggers or effects |
| Late dynamic narrative HTML | Two nested paragraph expressions corrected | No change in narrative copy or choice routing |
| Witness voice continuity | One term corrected to remain consistent with the character described | No change in historical outcome |
| Legacy/deep-linked family scene | Missing family-visit year now invokes existing safe continuity notice | Valid 18+ voluntary household paths are preserved verbatim |
| Branch QA | 539-scene render/choice matrix, 120 deterministic legal routes and guided 420/422-decision paths | Do not misclassify gated optional scenes as unreachable merely because random walks miss them |
| Save/UX | Inherited v0.4.98 transactional import, protected corrupt slot, keyboard/mobile affordances | Save keys, schema and content mechanics unchanged |

## Verification and unresolved gate

- 17,787 fragment checks / zero markup findings after fixes, 1,767 targeted preservation assertions, 278,674 random route invariants, 34,103 executed decisions and 0 failures. 539 scene IDs, 29 People and 8 archived endings retained.
- Six inherited suites, two long guided journeys and Playwright simulated-storage/viewport tests passed. Full per-branch human literary sign-off remains open, as does unrestricted physical file-protocol persistence after browser process close.
- See QA receipt and per-scene matrix for exact coverage and limits. v0.5.0 beta not authorized.

---

## Historical GDD v1.28 FAST v0.4.98 overlay — preserved verbatim

# ACTIVE MASTER GDD v1.28 FAST — v0.4.98 OFFLINE STABILITY & UX

**Executable:** `ALL_UNDER_HEAVEN_v0.4.98_DEV_OFFLINE_STABILITY_UX.html` · SHA-256 `b2068ec5883984b9b7a9f17e9ab832ec8b8e8700fa8ce3cc71babc106e992d4e`. This first overlay is authoritative; the v0.4.97 and older overlays below remain as historical provenance. No new narrative scene, NPC, portrait, ending family, item grant or property subsystem was introduced. **539 scene IDs / 29 People / 12 chapters.**

## Implementation delta — v0.4.98

| Subsystem | Applied changes | Guardrails |
|---|---|---|
| Save/write feedback | Readback-verifies `localStorage.setItem`; visible status, fail-safe on quota/permission errors | Existing save keys and data version are unchanged |
| Autosave lifecycle | Existing decision, page and settings saves retained; adds safe `pagehide` and document `visibilitychange` checkpoints | No write from developer QA previews or invalid state |
| Corruption handling | Detect unreadable current save/sandbox; preserve raw bytes, offer recovery-copy download and warning | Older valid fallback cannot silently overwrite unreadable slot via background autosave |
| Import transaction | 8 MB guard, JSON/schema validation + normalization, overwrite confirmation, no active-state switch on failed storage persistence | Separate original and sandbox copies preserved; old saves normalized by original `resolve` |
| UX / accessibility | Save status near reading header; visible focus ring, 44 px menu/close targets; menu initial focus, Escape restore and Tab wrap; 360–1280 px browser interaction QA | No rewriting story prose/choices or exposing hidden relationship gauges |
| Offline packaging | Single HTML with inline CSS/JS and embedded illustrations; no detected remote script/stylesheet/fetch dependency | Native unrestricted `file://` storage/relaunch still pending |

## QA / acceptance

- `node --check qa/engine.js`, `node qa/qa_offline_stability_0498.js` (1,779 assertions, 32 legal stored snapshot decisions and complete 539-scene body/choice source equality); six inherited regression families pass.
- Fresh source-legal 190–250 CE journeys: 420 and 422 valid decisions on land and house+paid stable alternatives. Four v0.4.97 optional meetings remain usable.
- Chromium DOM tests with **simulated/injected** storage: 73 new browser scenario checks at 360, 390, 768, 1280; 8 inherited directed clicks at 390, 1280. No page errors or detected horizontal overflow. Direct native browser `file://` testing blocked by administrator and not certified.
- No exhaustive editorial alternate-branch sign-off. Beta gate is still closed. See `qa/ALL_UNDER_HEAVEN_QA_RECEIPT_v0.4.98.md`.

## Next v0.4.99

Complete manual spoiler-protected read-through of all 539 scenes and every meaningful alternate branch, chronological/age consent checks, independent NPC decisions, earned family/royal state, property, war and singular item proofs. Follow with unrestricted desktop and Android file-origin close/relaunch verification before a beta decision.

---

## Historical Master GDD v1.28 FAST checkpoint overlays — preserved unchanged

# ACTIVE MASTER GDD FAST — v0.4.97 / GENERATIONAL & REPUTATION LEGACY

**Authoritative HTML:** `ALL_UNDER_HEAVEN_v0.4.97_DEV_THE_LIVES_THEY_CHOOSE.html` · SHA-256 `cfc012a1c3e1cd4bcc94be4026db7d2c8a7acc255fc98a3c57e90d4426cc5e8f`. **539 scenes** (535 retained + 4 optional), 29 People, 12 chapters, three ending families. This first overlay is authoritative; earlier overlays below remain as history.

## Implementation

- `p97_230_an_evening_not_bought`: an optional, one-time seasonal meeting; married-adult characters with actual household see a tender, sustained and non-graphic romantic conversation, with no automatic intimacy contract or pregnancy. No spouse: complete friendship scene.
- `p97_234_voices_in_the_records`: public reputation is conveyed through independent witnesses drawn conservatively from earned historical flags (earlier civic, property, diplomatic or defeat record). No visible reputation statistic or guaranteed praise.
- `p97_234_questions_without_orders`: youth scene permitted only after an authentic family entry and for a child still under 18; child has no imposed career or inheritance.
- `p97_249_their_own_road`: permitted only with genuinely adult child age >=18 in story year, before the final coastal hearing; an adult can express independent wishes without automatic throne, office, military service, or bypassing `i84_heir_*` scrutiny.
- Every new option returns to its original scene and becomes unavailable once chosen (`p97_*_done`, `p97_*_answer` flags). Three active ending families may conditionally echo earned choices. All 535 old scene IDs and eight manuscript blocks remain; old save keys unchanged.
- Equipment spoilers do not belong in player-facing status. All three singular legendary-equipment design principles and the earned white horse remain unchanged.

## QA

Feature test 713 assertions; four new meetings reached via fresh 190–250 legal story, with both actual independently obtained land and home+paid stable variants (420 and 422 valid choices); 8 real browser clicks on 390/1280 px without script errors or overflow. Inherited combat/equipment 813, property 584, NPC memory 715, romance 1,422 and endings 1,104 pass. Organic no-horse 401, foster succession 402, and northern failure 383 also pass. Verified JSON resolve/roundtrip for new flags; local native physical `file://` storage remains unverified. See QA receipt.

## Next phase

v0.4.98 Offline & UX: actual physical `file://` save/reload, keyboard/mobile accessibility, regression, corrupt import and no-data-loss check. v0.4.99 exhaustive narrative editorial & branch QA. Beta and stable only upon release gates.

---

# ACTIVE MASTER GDD FAST — v0.4.96 / LIVING HOME & ESTATE

**Authoritative game:** `ALL_UNDER_HEAVEN_v0.4.96_DEV_WHAT_THE_HOUSE_REMEMBERS.html` · SHA-256 `f099347a2893a94077e52e6ae5bf6a9994126b626825ebc77d58de3e6e2868d7`. Current-first development specification; 535 scene IDs / 29 People / 12 chapters. Older checkpoint overlays follow for historic context.

## Implemented

- Three new one-time narrative nodes (`p96_225_the_room_with_light`, `p96_225_the_fields_that_speak`, `p96_230_the_open_stable`) wrap existing source choices without deleting/replacing them. All three return to original source scene after the choice; new visit flags prevent looping. Eligibility uses canonical saved date and earned ownership/relationship proof; stable additionally requires named-or-unnamed earned horse plus paid stable. The horse need not be named to be owned.
- Eight previously available purchased property improvements now have **distinct text echoes**, not power increments: Family Rooms, Reading Room, Courtyard Garden, Courtyard Stable, Irrigation Channel, Village Granary, Field Road, Village School. Only completed upgrades are described. No projected rent or daily tick.
- Three meaningful player options each record one `p96_house_choice`, `p96_land_choice`, `p96_stable_choice` plus heard flags and journal text. Conditional brief memories surface in later homeland/war scenes and all three ending families only after the meeting actually occurred. **No** new wife, child, purchased asset, horse, army, political title, dragon appointment, war victory or equipment grant.
- Compatible with older saves, `auh92NormalizeProperty`, the original property UI, original one-off Coins deduction, unique companion name, existing journal, and save validation. Old save keys unchanged.
- No spoiler content in player-facing development report: unique legendary-gear names and donor identities, actual gift narratives, hidden prerequisites, and surprising events remain in executable source only.

## QA receipt summary

**697 feature assertions**, fresh 190–250 house+stable and land alternative histories (414/412 choices), 10 real UI clicks at mobile/desktop sizes including one actual Coins-paid property commission, 813 inherited combat/gear checks, 584 property, 715 NPC, 1,422 romance and 1,100 ending checks. Fresh no-horse, regional failure, biological/foster heir routes passed. Physical `file://` persistent reload and exhaustive human editorial pass not yet certified. See `qa/ALL_UNDER_HEAVEN_QA_RECEIPT_v0.4.96.md`.

## Follow-up: v0.4.97 — Generational & Reputation Legacy

Careful adult children/autonomy, reputation through NPC behavior and selected seasonal personal memories; preserve optional family/no-family paths. Do not add character stat readouts or an economy simulator. Before beta, certify real physical offline save behavior and review full branch prose.

---

# ACTIVE MASTER GDD FAST — v0.4.95 / WAR CONSEQUENCES & LEGACY

**Source of truth:** `ALL_UNDER_HEAVEN_v0.4.95_DEV_THE_WEIGHT_OF_THE_UNRETURNED.html`, SHA-256 `699abeb694bd5eb3c28c78ec2f9105c02c5f888c1dfd632a84a3ef97dea366e4`; 532 scenes, 29 People. Current-first contract; historical checkpoint overlays retained below.

## Implemented this batch (player-facing spoiler-free)

- 5 optional new story scene IDs added to the existing 527, without rewriting old scenes: 3 campaign defeat aftermaths, 2 separate signature-equipment conversations.
- Contested fronts retain their failure state, original territorial limitations, royal status and three ending-family logic. Choices set one `p95_loss_<front>` consequence flag and journal entry, with conditional regional/ending callbacks; they do not create artificial conquest.
- Separate legacy equipment moments use existing verified multi-year character decisions, no new gauge/quest engine. Accepted equipment is added to the existing `items` array only once after an explicit choice; refusal grants nothing, prevents an identical one-time meeting from replaying, and preserves the story.
- One Great Glaive and one newly made white/silver armor; no generic loot roll, shop, craft timer, armor recolor, gold expense or duplicated copies. Added optional tactical responses only on an already valid King/field campaign route; existing `w83NorthDecision` and `w83WestDecision` still resolve with the full supply and prior-service prerequisites. No automatic victory.
- **Spoiler lock:** actual artifact titles, donor identities, trigger choices and surprise prose live only inside the executable, never in player-readable handoff summaries. A future editor should inspect the source privately without quoting spoilers in reports.
- The original white named horse, timeless-but-vulnerable companion, house/land upgrades, 29 People, old saves/scene IDs/manuscripts, original three endings and family/adult abdication remain.

## State and QA

Item IDs are unique; `validSave` additionally rejects duplicates or gear claims lacking a grant flag, retaining the prior shape validation. Unknown old saves are not retroactively awarded equipment. Frontier failures require exact 240/245/249 CE and earned crown proof. 813 tests of new logic, 10 UI clicks, 4 separate source-legal paths (one full campaign plus three failed-front alternatives), and older 190–250 regressions PASS. Physical `file://` storage under an unrestricted browser remains unverified, as does an editorial reading of every optional path.

---

# ACTIVE MASTER GDD FAST IMPLEMENTATION CHECKPOINT — v0.4.94

**Authoritative executable:** `ALL_UNDER_HEAVEN_v0.4.94_DEV_COURTS_BEYOND_THE_BANNER.html` · SHA-256 `078d37c818aeaf97a114dfbc72daa9351ddb2d8b123fb04757dc6d0ed13a7e28`. 527 scenes, 29 People. Current-first overlay, with previous FAST GDD entries preserved beneath.

## Added: Historical NPC Autonomy and Living World

- `AUH94_AUDIENCES`, `p94Allowed`, `p94Remember`, `p94Options`, `p94OtherCourt`, `p94WestNews`, and `p94EastReply` inserted near executable script bottom before the original state boot. No new data engine, duplicate save keys, stat gauges, automatic relationships or daily economy.
- Three optional scenes at 220, 244 and 248 with nine choices and one-time flags, returning to the *same* original source scene. Source choices remain untouched. Year guards and royal proof applied at front campaigns; false chronology and corrupt-state invitations hidden. The third-party political action itself occurs regardless of whether player attends; responding only records the user's handling of those events.
- Dynamic narrative only: earlier 220 exchange affects western court's reaction at 244, 244 affects eastern response in 248, and selected earned replies can be referenced in inherited 245, 249 and all three epilogue families. Responses do not alter the existing outcome conditions of western or eastern fronts or forcibly annex a faction.
- Companions speak only if truly earned: `p88Here(s,'weizhen')`, `w83Commander(s,'peiliang')`, `w83Commander(s,'dengyu')`. Named horse only if `horseCompanion` exists, using escaped label. Spoiler-free inherited rules unchanged.

## Acceptance summary

`qa_autonomy_0494.js` **676 PASS**; inherited letters **1,212**, property **584**, NPC interactions **715**, romance **1,422**, endings **1,092** PASS. Organic 190–250 **406 legitimate decisions** with all 3 v0.4.94 scenes plus five Dragon Generals and peaceful adult-heir abdication. Horse-declined and foster/biological offspring routes also pass. Six browser clicks at 390/1280 px. **Real unrestricted physical `file://` persistence and complete editorial read remain unverified**.

---

# ACTIVE MASTER GDD FAST IMPLEMENTATION CHECKPOINT v0.4.93

**Source of executable truth:** `ALL_UNDER_HEAVEN_v0.4.93_DEV_LETTERS_FROM_OTHER_ROADS.html` · SHA-256 `b8dcc009ec0c91c2041aea2d624d1e65ce07f929d45a6db7ce07ef54e579ed60`. Current-first implementation overlay; historical versions follow below. 524 scenes, 29 People, 12 chapters, three ending families, eight legacy manuscript sources preserved.

## Scope this batch

- Quality-first **v0.4.93 NPC Memory / Living World** increment: three real narrative encounters, nine responses. Direct 210→223→239 callback dependencies are recorded as optional flags and visible Journal notes. The script checks historical officers' earned involvement, not implied lifelong allegiance.
- `AUH93_MEETINGS`, `p93Allowed`, `p93Remember`, `p93Rejoin`, `p93Choices`, `p93OwnedLetter` are defined near the bottom of existing HTML, after prior scenes, before saved state boot. This avoids the need for a standalone new engine or incompatible save schema.
- The 239 encounter is limited to 239 with earned King proof. Original source choices, military outcomes, all existing flags and save slot keys are preserved. No new attributes, daily money, auto family, auto NPC membership, auto horse, old-age death, future legendary item names, or forced endings.
- Four existing narrative callbacks: 225 household, 240 northern reports, 249 final river, and the three active ending bridges. This is *not* a complete 12-chapter editorial audit; the full audit remains a release gate.

## Acceptance evidence

QA scripts: `qa/qa_letters_0493.js` 1,209 PASS, `qa/organic_letters_0493.js` 400 source-legal steps PASS, `qa/browser_letters_0493.py` six real UI clicks at mobile and desktop PASS, inherited property/horse 584, NPC 715, romance 1,422, ending 1,089 PASS, independent horse-declined and family routes PASS. JSON roundtrip PASS. Physical `file://` browser restart tests still blocked by environment restrictions.

## Spoiler-free contract remains binding

Coins develop earned property and never purchase secret signature gear. One emotionally earned signature weapon, one **new** white/silver armor, and one white, named, long-lived horse whose bond is earned after starting the game with none. The last is already implemented; secret weapon/armor event reveals remain future work, hidden from public user reports. Only adult consensual, non-graphic romance; independent historic rivals; player may choose a non-royal path or King before optional Emperor and peaceful verified adult-child abdication.

---

# MASTER GDD FAST — CURRENT IMPLEMENTED CONTRACT v0.4.92

**Authoritative HTML:** `ALL_UNDER_HEAVEN_v0.4.92_DEV_THE_HOUSE_AND_THE_WHITE_COMPANION.html` · SHA-256 `a72df119811ce47d5399ca493f2e8c790b060b0d6a263a46ad07c2a338cd7ec3`. **521 scenes, 29 People, 3 active ending families**; 8 untouched archive manuscript blocks. This overlay supersedes older versions below.

### Lightweight Coins, Home & Estate v1 (implemented)

Coins stay a simple personal integer in *Possessions*. No equipment shop or daily income simulation. Existing introductory social/charity spending is retained; five earned Coins are documented for verified 191 CE service. Only the `ch10_06` story choice can open either the **house** branch (`house`) or the **land** branch (`restore`) in this batch; choosing public service opens neither. In *Possessions → Property*, 8 priced one-time improvements are available when relevant and affordable. Each purchase checks ownership, sufficient Coins, and duplicate completion server-side in the game logic, spends Coins once, records a journal note and persists in JSON/localStorage. Existing old-save decisions restore legitimate ownership without creating new land or a house from nothing.

### Single white companion mount (implemented phase 1)

Fresh start 190 CE has **no owned horse**. An optional scene can be reached later through an earned existing journey; player care/support and independent keeper consent matter, and acceptance can be declined. After accepting, player names the same horse through *Possessions → Horse*. The horse can be recognized through later personal choices, or remain private, with no mandatory legendary outcome. Dedicated aging exemption means the single horse does not die of old age alone, but narrative peril remains. No horse stamina, gear turnover, replacement, passive skill multiplier, automatic battle victory, or loot table. Names/plot acquisition triggers must remain spoiler-free in dev progress.

### Signature weapon & armor (approved design, NOT code in this milestone)

One emotionally-earned signature Great Glaive-type polearm, one **new** white/silver suit of armor acquired after ordinary starting attire, and the single evolving white horse. All signature names, sources, exact conditions and reveal moments must remain hidden from player-facing docs until experienced. No legendary item purchasable with Coins. Never force legendary acquisition or require it for ending. Equipment earned from different decisive emotional moments, without using preexisting copyrighted plot or direct character events.

### QA / continuity

All old 517 scene IDs, 29 People, 8 legacy ending manuscript sources, three current ending families, 190–250 time, legal King/Empire proof, Inner Circle, 5 Dragon Generals, independent historical NPC allegiance, adult non-graphic consent-driven romance/family/abdication and `auh-v047-draft-*` storage keys survive intact. 584 targeted assertions, 715 NPC, 1,422 romance, 1,086 ending, accepted and declined fresh organic routes, mobile/desktop UI (14 clicks) passed. Standalone file URL persistence and full editorial branch coverage remain open.

---

# MASTER GDD FAST — ACTIVE IMPLEMENTED CONTRACT v0.4.91 / THE RIVER AND THE THREE FRONTS

Source of executable truth: `ALL_UNDER_HEAVEN_v0.4.91_DEV_THE_RIVER_AND_THE_THREE_FRONTS.html` · SHA-256 `1d1e19e9e174f39546f891b154579c6e5d7ce51c8c8722adf1403f346bb2e2c1` · World Bible v1.91 FAST. All 517 older scene IDs, 29 People and eight archive manuscripts retained. No new scene registrations, forced crown/romance, save version or storage-key changes.

**Defect resolution:** (1) three differently labelled 208 encounter choices now enter the already-existing Zhuge Liang/Lu Su diplomatic sequence and legitimate river command path; their original effect functions remain intact. (2) The Cai Zhen after-war continuation no longer re-enters the completed Red Cliffs battle; the witnessed casualty flag distinguishes pre-battle vs post-battle transitions. (3) Absent optional Inner Circle companions are no longer asserted present in eight restored 208–209 scenes; ordinary officers replace them without forged identity or appointment.

**Military legitimacy is unchanged:** northern Han Sheng + Xu Wen, western Pei Liang + Lin Shuo, eastern Deng Yu + Xu Wen decisions still require earned kingship, actually appointed pairs, valid 208/229/233 proof, proper annual theater orders and provisioning, and exactly the same resolution/cost machinery as the original tactics. No guaranteed victory or new automatic promotions. All three **source-legal from fresh 190** pairing actions proven in one 390-choice 190–250 trace. Old treaty-led victory and no-King/fatal paths also passed.

**QA:** 603 new assertions PASS; 679 Dragon baseline, 715 NPC, 1,422 romance, 1,076 ending regressions PASS; 8 clicks in Chromium at 390/1280px PASS; save JSON in-memory roundtrip PASS. **Open release gates:** physical standalone `file://` save/reopen blocked by Chromium host policy, all-branch human editorial pass and wider real-device/browser matrix. Do not mark this as final release.

---

# CURRENT IMPLEMENTATION — ALL UNDER HEAVEN v0.4.90 / CHARACTER DEPTH

**Current executable:** `ALL_UNDER_HEAVEN_v0.4.90_DEV_THE_PEOPLE_WHO_CARRY_THE_STANDARDS.html` with SHA-256 `50806f152c2b5048be9dcdf49df2d943d4888eb9a18108692ee11deaff30157b`. 517 registered scenes, 29 People, 12 chapters, 3 active ending families, 8 unchanged archived manuscripts. Latest section below takes precedence over older chronological records retained in full.

## Design-to-code changes

1. 210 CE `lc81_210_shared_table` includes optional one-time encounter `p90_210_the_letter_not_sent`, a human story with presence, aid, and nonintervention outcomes. The Han Sheng/Wei Zhen correction now depends on actual roster status. Joining no friend is required for the human story; anyone absent stays absent.
2. 230 CE `d82_230_merit_register` adds optional `p90_230_the_standard_at_rest`, separating compassion and front-line drill from the unrelated later appointment merits of Lin Shuo. All three replies return to the existing open/partial/delegated audit choices. No royal commission is created.
3. Chapter XII war councils add distinct appointed-Dragon voices for Han Sheng (frontline shield), Xu Wen (withdrawal/civilian screen), Deng Yu (paid convoy and ferries), Pei Liang (drill/engineering), and Lin Shuo (rear guard/refugees); no generic banner is allowed to substitute for unearned officers.
4. Joint Dragon alternatives on three front counterstrokes use existing outcomes `hold_pass`, `hold_depot`, `landings`, respectively. Existing prerequisites and expenditure logic apply unmodified; choice only changes tactical accountability and later dialogue/epilogue memory. These alternatives require exact dual appointments and compatible 239/244/248 conditions.
5. New flags optional; no save-version increment or old scene ID replacement. Existing romance, Inner Circle, King/Emperor naming, three ending families, optional lawful heir and archive manuscripts are retained.

## Test boundaries and next improvement

`qa/qa_character_depth_0490.js` 679 assertions; `qa/organic_depth_0490.js` 353-click source-legal walk; `qa/browser_depth_0490.py` 14 real UI clicks; current versions of romance/people/imperial QA 1,422 / 715 / 1,076 assertions, respectively, all PASS. `file://` blocked in sandbox; physical save persistence and all-branch human editorial reading not certified. Further editorial work should examine alternate-history battle outcomes and **organic front-commander alternatives**, not just scripted state fixtures. Avoid running the Prologue for each small fix.

---

# CURRENT CHECKPOINT — ALL UNDER HEAVEN v0.4.89 / THE DEBTS THAT FOLLOW AN ARMY

**Executable authority:** `ALL_UNDER_HEAVEN_v0.4.89_DEV_THE_DEBTS_THAT_FOLLOW_AN_ARMY.html`. **SHA-256:** `cf7f8cd9559ae58304ac682778101f455ac83da2dd50404891d9f0a6b178a49f`. **515 registered scenes, 29 People, 12 chapters, 3 active ending families, 8 archived ending manuscripts unchanged.** This v0.4.89 checkpoint supersedes older version headers below; older sections are archived continuity evidence, not current source status.

## Implemented in HTML v0.4.89 — war continuity, not more disconnected scenes

- Four existing campaign scenes received **conditional paragraphs** responding to documented earlier choices: 235 royal council listens to 196 ration witnesses and 210 civilian debts; 239 northern supply reflects the 223 disputed-office response; 244 western countermove acknowledges the winter council's real 244 choice; 248 Jiangdong reconnaissance respects the 223 records and any historically established Lu Su encounter without moving him or his allegiance into the present.
- Two **earned optional choices** were added without removing any previous choice. At `w83_240_war_council`, a joint garrison audit is available only with the genuine 196 shared-ration decision, earned kingship, settled north and correct year 240. At `w83_245_river_orders`, an independently witnessed ferry charter requires the actual 210 civilian passage settlement plus the 223 renewal-of-seals choice, earned kingship, settled western front and correct year 245. These actions follow the old time/scene progression, record distinct flags, and NEVER automatically settle another territory.
- New save-state keys (optional, absence is fully compatible): `w89_north_audit='witnessed'`, `w89_ferry_charter='joint_witnesses'`; existing `w83_north_aftermath` and `w83_east_preparations` are set to supported values only after taking the respective choice. The new narrative echoes are conditional; all three active epilogues can remember the evidence, but none grants a wife, heir, ally, crown, Dragon, or victory.
- Zero new registered scenes; original 515 scene IDs and all previous options remain, with only 2 optional additions. Eight archived ending manuscripts remain identical to v0.4.88. Save schema version and keys unchanged.

## Verification and open issues

- `node --check`: PASS; `qa_war_continuity_0489.js`: **596 assertions PASS** (old IDs/manuscripts, per-choice variants, blocked cases, valid save flags, no undeserved promotions or crown). V0.4.88 optional NPC meeting regression **715 PASS**; v0.4.87 romance regression **1,422 PASS**; imperial regression **1,074 PASS**.
- Full source-legal 190–250 journey visited previous choices and **both new war-council options**, ending with earned union and lawful biological-heir abdication; JSON roundtrip PASS. Independent foster-heir abdication, fatal route and base organic routes still PASS.
- Chromium with in-memory `set_content` and real buttons: both choices selected at mobile **390 px** and desktop **1280 px** (4 clicks); **zero JavaScript errors or horizontal overflow**.
- **NOT CERTIFIED:** actual standalone `file://` persistence across browser restarts, all-branch human narrative review, all devices, or full manual 12-chapter playthrough. Not final release.

## Binding design decisions — unchanged

Start 190 CE, protagonist 16; Timeless Heroes = chronological ages advance, children's growth continues, adult appearance stabilizes. Max 7 **earned** Inner Circle, one optional original Grand Strategist Wei Zhen; up to 5 merit-earned Dragon Generals only after becoming King. Kingdom can be named; King first, optional genuine unification to Emperor and separately chosen empire name. Three active ending families with eight retained archive manuscripts; peaceful voluntary abdication to an independently verified worthy adult child, with no succession feud. Six distinct romance candidates, adult consent required and non-graphic continuous intimacy; one principal wife and up to five independently consenting concubines. Historical NPCs pursue independent faction priorities. Game text/UI English, development reports Indonesian and spoiler-safe. War scale may draw inspiration from Kingdom manga but scenes/characters remain original.

---

# CURRENT CHECKPOINT — ALL UNDER HEAVEN v0.4.88 / THE PEOPLE BEHIND THE BANNERS

**Active executable authority:** `ALL_UNDER_HEAVEN_v0.4.88_DEV_THE_PEOPLE_BEHIND_THE_BANNERS.html` SHA-256 `69b46021f7711dd5b15bdab933fcbb669c85d9642c421a6a2f5c69838669a245`. This v0.4.88 header overrides older checkpoint headings below, which remain archived for continuity. **515 registered scenes, 29 People, 12 chapters, 3 active ending families, eight legacy ending manuscripts preserved.** Not a final release.

## New implemented content

- Five optional, playable, one-time human-scale meetings at **196, 210, 223, 244, 249 CE**, reachable through existing scene-choice hooks. They explore early companionship, unpaid civilian promises, independent historical court authority, winter campaign disagreement and the final encampment. Every encounter returns to its **original** scene. Old choices and effects remain intact. The 244 and 249 visits require an actually earned King; state-only invalid visits safely return to original content.
- Inner Circle commentary is conditional on earned membership; Wei Zhen can acknowledge strategic error, Xu Wen and Han Sheng can disagree, Qin Rui and Deng Yu retain autonomous responsibilities, and Dragon Generals appear only if appointed. Historical encounters with Zhao Yun or Lu Su are referenced as **past witnessed records** only if the actual campaign flags support them; neither is teleported or recruited.
- Decisions create `p88_<year>_done` and `_decision` only after choosing one of three distinct responses; appropriate public-duty / command / supply accounting may change. No automatic NPC admission, Dragon appointment, romantic bond, child, regional sovereignty, empire, or historic fates. Conditional epilogue echoes appear only for established choices; eight archival ending manuscripts stay unchanged.
- Source anchors: `lc81_196_pei`, `ch09_04`, `ch11_p60_08_turn_223`, `w83_244_western_supply`, `ch12_c79_07_the_final_river_249`. New scene IDs: `p88_196_the_shared_bench`, `p88_210_the_unpaid_words`, `p88_223_no_borrowed_loyalties`, `p88_244_a_winter_council`, `p88_249_banners_at_dusk`.

## QA and limitations

- JavaScript syntax PASS. 715 new assertions, 1,422 v0.4.87 adult romance regression assertions, 1,074 imperial/ending assertions PASS. Five new scenes visited in **one source-legal 190–250 CE mechanical journey**, including marriage, biological adult heir and voluntary peaceful abdication. Several independent pre-existing organic war, fatal, non-King, foster and biological heir paths also pass; see QA receipt.
- Real UI browser testing: 20 actual clicks at **390 px** and **1280 px** across the five new encounters, no detected JS error or horizontal overflow. JSON save/resolve on organic abdication trace PASS.
- **NOT CERTIFIED:** physical standalone `file://` save persistence across browser restart (restricted environment); full human reading of all branches; exhaustive cross-device restore. Do not claim those passed.

## Binding decisions preserved

English in-game text and UI; Indonesian spoiler-free developer reports. Protagonist begins 16 in 190 CE. Timeless Heroes means chronological aging and children's maturation continue while adult appearance stabilizes. Max seven earned Inner Circle members, one attainable original Grand Strategist, max five merited Dragon Generals only after becoming King, then optional genuine unification to Emperor by around 250 CE. User-named kingdom and empire, three main ending families with eight archived old ending scripts, consent-based romances, optional established family, independently proven adult heir for voluntary peaceful abdication without succession conflict. Historical NPCs have agency and factional duties, never recruited by fiat. War staging may take high-level inspiration from *Kingdom* but narration and choices are original.

---

# CURRENT CHECKPOINT — ALL UNDER HEAVEN v0.4.87 / THE WORDS KEPT AT HOME

**Executable source:** `ALL_UNDER_HEAVEN_v0.4.87_DEV_THE_WORDS_KEPT_AT_HOME.html`; SHA-256 `50db0310b3f4bcbf464feb1d607a6b3c29085937c625b54819df7c8f25613796`. **510 registered scenes, 29 People, 12 chapters, 3 current ending families, eight historical ending manuscript/bridge IDs retained.** This heading supersedes older checkpoint status records that follow; those are archival continuity evidence.

## Binding romance direction, implemented in this batch

- **Continuous Intimate Romance:** adult, freely chosen in-person romantic scenes that preserve dialogue, emotion and physical affection without an abrupt generic fade-to-black. Intimate sexual activity is not graphically depicted; no scene grants bodily access, marriage or pregnancy as an entitlement. Everyone involved must be at least 18 chronologically. The six established romance characters and their individual age rules remain binding.
- Five new optional scenes: **218** (unmarried, prior in-person affection); **223** (unmarried, personally earned closer meeting); **225**, **230**, **234** (already married, actual shared household). Distinct character voices for Shen Lian, Lin Yue, He Qing, Cai Zhen, Lan and Song Wan; no seventh candidate.
- New flags `p87_218_done`, `p87_223_done`, `p87_225_done`, `p87_230_done`, `p87_234_done`, their `_tone` and `_person` companions, **only after choosing a scene response**. Consent and precondition failures return safely to the existing story; episodes cannot repeat unintentionally. Never infer new marriage, concubine, pregnancy, child, rank, historical loyalty or territory.
- Existing wedding and intimate snippets were edited to replace several abrupt lamp/curtain cuts with continued on-page conversation, without introducing graphic description. A verified biological or foster child in the family is acknowledged; absent children are not invented.
- Three current epilogues receive a short memory only if a new, genuine spouse-scene choice happened. Eight legacy ending manuscript blocks remain byte-for-byte logically identical to v0.4.86.

## Verification summary

- New `qa_romance_0487.js`: **1,422 checks PASS** across all 6 romance characters × 5 visit-year arrangements; **60 legal choice effects**, **120 blocked/invalid combinations**, save shape, no repeated grants, 510 scenes, 29 People, 8 legacy manuscripts unchanged.
- `browser_romance_0487.py`: **20 real UI clicks** across five scenes on 390px and 1280px; no JavaScript error or horizontal overflow.
- `organic_romance_0487.js`: single fresh-190-CE playthrough legally visited romance scenes in **218, 225, 230** and completed 250 CE biological-child abdication; no state or partner injected. **223 and 234 not proven organically** in this batch but were tested by direct state/choice/browser checks.
- `qa_imperial_0487.js`: **1,069** regression assertions, including current three ending families and archived eight manuscripts. Other source-legal organic war, fatal, foster/biological abdication scripts run PASS after patch. `node --check` PASS.
- Browser's unrestricted physical `file://` save/reload persistence remains **UNVERIFIED**. Entire 510-scene, all-state human narrative editorial certification still **NOT DONE**. This is a development checkpoint, not final release certification.

## Locks to carry to next chat

Start year 190 at chronological age 16; Timeless Heroes stabilizes adult appearance but does not freeze ages or children's growth. Max 7 optional earned Inner Circle members; Wei Zhen an original earned Grand Strategist; up to 5 appointed Five Dragon Generals only after becoming King. King before optional Emperor after true unification, optional kingdom/dynasty naming. Three current ending families, eight retained old scripts, peaceful optional abdication to an independently proven-worthy adult child. Historical NPC autonomous. War scale inspired by *Kingdom* but original plot/text. One principal wife, up to five independently consenting concubines among the six romance candidates; family/children never automatically assigned. English game narration/UI, Indonesian user-facing spoiler-free QA notes.

---

# CURRENT DEVELOPMENT CHECKPOINT — v0.4.86 THE BANNERS KEEP THEIR WORD (11 NOV 2026)

**Active executable authority:** `ALL_UNDER_HEAVEN_v0.4.86_DEV_THE_BANNERS_KEEP_THEIR_WORD.html` SHA-256 `7c3740c88861248db775d58f00cbe0061d250812a90ab7fd8ccafd9355d6e50f`. **505 scenes, 29 registered People, three current ending families, eight protected legacy ending manuscripts/IDs, 12 chapters.** This block supersedes earlier CHECKPOINT / NEWEST headings below; old sections remain historical audit evidence, not current active source. **Targeted QA only, not final release certification.**

**New actual HTML content:** Five optional chronologically grounded, playable scenes (208, 223, 239, 244, 248 CE): `p86_208_pilots_and_seals`, `p86_223_separate_obligations`, `p86_239_northern_witnesses`, `p86_244_western_witnesses`, `p86_248_jiangdong_witnesses`. Source-choice effects stay intact, with only a forward detour for eligible old destinations. The 223 detour is available only when the earlier 221 disputed-office path was actually played. The 208 encounter depends on its existing Lu Su negotiation route. Old save scene IDs remain valid without replaying inserted scenes.

**Narrative rules:** Jiangdong, the northern command, western officials and prior historical NPCs remain autonomous, tied to recorded interests. None is forcibly reassigned, confirmed dead or guaranteed alive on an alternate-history branch. Wei Zhen and appointed Dragon Generals comment only if earned; fallback scenes work with no council members or Dragons. Three later war hearings record 15 possible civilian-account / command choices as flags, give actual costs or care where appropriate, and feed evidence-dependent prose in the three new epilogues. They never automatically grant territory, rank, wife, child, NPC membership or an ending. Original 208/223 evidence can be referenced decades later without inventing future speech from Lu Su or other historical actors.

**QA evidence on final code:** `node --check` PASS; 669 focused checks including all 15 new decisions, 505 scene registry, 29 People, 500 previous IDs, all eight legacy manuscripts; 393 continuity-regression checks; 1,064 imperial/ending-regression checks; two King-to-Emperor 190–250 organic mechanical routes (with five or zero Dragon Generals); five other legitimate existing family routes, fatal route, and two independent 190–250 biological/foster abdication routes PASS. Browser actual UI 390/1280 px, 20 clicks across the five new arcs, zero JS errors / overflow. JSON serializable flags and old-save guard preserved. Physical `file://` persistent save across browser restart **UNVERIFIED**, all-branch human editorial certification NOT done.

**Locked design preserved:** 190 CE protagonist age 16, Timeless Heroes chronic age / adult visual stability, 7 optional earned Inner Circle, one attainable Grand Strategist, 5 King-only Dragon Generals, King before optional united Emperor, user-named kingdom/dynasty, explicit lawful proof for voluntary peaceful adult-child abdication, 3 new ending families + 8 archived legacy endings, no forced marital or historical assignments. English game UI/narration; Indonesian ordinary reports spoiler-safe. Normal ending by c.245–250 CE. No 280 CE extension required.

**Next:** Continue NPC autonomy across alternative-history war branches and reduce repetitive war-account phrasing; perform full-branch narrative continuity reading; certify local physical-file browser persistence on an unrestricted machine. Do not claim release ready until this work is done.

---

# MASTER GDD FAST — ACTIVE QA ADDENDUM v0.4.85.1 (11 NOV 2026)

**Source of executable truth:** `ALL_UNDER_HEAVEN_v0.4.85.1_DEV_CONTINUITY_GUARD.html` · SHA-256 `4dfe1cd51e469267548484a25ceba42b1ceee5cb8b2b08f7bc6bacd8fcc73ed1` · World Bible v1.85 FAST. **Scope:** continuity and malformed-save hardening only; no new narrative or design authority, no migration of ending family logic. The v0.4.85 and earlier paragraphs below serve as provenance. Three ending families and all eight preserved older ending scenes are unchanged.

**Implemented:** named family scenes no longer crash when an imported old/inconsistent save lacks its required spouse/offer record. Such scenes display one non-spoiler recovery option leading to an existing public-scene checkpoint; no relationship is implied or granted. For genuine lawful routes, the original scene body/options remain. `validSave()` now also rejects malformed nested save payloads and arrays in place of records, while retaining older saves with no optional `innerCircle`, `dragonGenerals`, or `realmNames` fields. The storage keys and chapter-calendar guards are unchanged.

**QA / release gate:** Matrix 4,000 body + 4,000 choice evaluations, zero exceptions; 393 focused checks, 1,049 guarded-build imperial checks, eight organic journeys, two full organic abdication paths and browser UI/JSON file-picker tests pass. **Still open:** physical `file://` persistent storage across browser restarts, complete human editorial review, historical-autonomy and multi-device old-save matrix. Do not label this final release. All locks on Inner Circle, Dragons, King/Emperor, Timeless Heroes, non-automatic family and peaceful verified successor are preserved.

---

# v0.4.85 QA CHECKPOINT — THE WITNESSED PATHS

**Development type:** integrated verification and build-identity correction; **no new scene, story choice, crown requirement, romance requirement, or save key.** Primary source is HTML v0.4.85 built directly on v0.4.84. This is a QA checkpoint, **NOT** full offline-release certification.

**Verified:** 500 registered scenes, 29 People, three new ending families, all eight legacy manuscript families preserved, and existing royal/dynasty naming and early council mechanics retained. First organic 190 CE to 250 CE **peaceful imperial abdication** proven twice from actual player choices: (A) voluntary marriage + fostered child + adulthood + civil and military witnessed merit (339 choice transitions); (B) voluntary marriage + biological child with separate family planning and birth choices + adulthood + same merit proof (329 choice transitions). Both passed chronology checks and JSON save/resolve roundtrips. Source-legal checkpoints were also clicked through in a real browser viewport at 390 px and 1280 px (62 UI choices total) without JavaScript errors or horizontal overflow. Focused old-version regression: 1,105 assertions, eight representative 190-to-terminal ending-family runs. These are automated checks, **not** eight full human editorial readings.

**Unverified blocker:** Chromium here rejects direct navigation to the physical HTML via `file://` with `ERR_BLOCKED_BY_ADMINISTRATOR`; a separate attempt at a synthetic HTTP(S) navigation is likewise blocked. Therefore physical-origin persistent save/reload across browser restarts has **NOT** passed. Reader must test on a permitted local environment. The broad artificial cross-scene matrix generated 56 content-render exceptions only when family-only scenes were entered without required spouse or offer state; those are invalid deep-link fixtures rather than demonstrated legitimate player routes, but malformed external saves need a later hardening pass. Full 500-scene editorial and deep historical counterfactual audit remain open.

**Carry-forward locks:** 12 chapters, 190 CE start at age 16; official calendar ages progress, adults retain youthful appearance (Timeless Heroes), children grow; consent-driven family and partnership; seven optional Inner Circle members with an early original Grand Strategist, up to five merit-based Five Dragon Generals **after becoming King**; King → optional Emperor after true unification; named kingdom and empire; no forced loyalty, heir, pregnancy, abdication or succession civil war; three new ending families, eight legacy manuscripts retained for save compatibility, broad *Kingdom* inspiration without copying source narrative. Normal target ending c.245–250 CE, not 280. All game text English, regular development reports Indonesian and spoiler-safe.

# MASTER GDD FAST — CURRENT IMPLEMENTED CONTRACT v0.4.84 (11 NOV 2026)

**Game:** `ALL_UNDER_HEAVEN_v0.4.84_DEV_IMPERIAL_LEGACY.html` · SHA-256 `32f321be7789fc1171c64aeb83a053ee2b9c41e2310aee6ba5ebb6f9ac1ead65`. **World Bible companion:** `ALL_UNDER_HEAVEN_World_Bible_v1.83_FAST_INTERNAL.md`. **500 scenes / 29 People / three new ending families / eight preserved legacy ending manuscript sources.** This CURRENT block overrides prior planned-status text and historic release-gate passages referring to eight *active* endings; the eight original ending manuscripts remain archived and playable through legacy scene IDs for old save continuity. Existing twelve chapters, 190 CE start, Timeless Heroes, seven Inner Circle slots, five King-only Dragon commissions, and lawful imperial union constraints remain binding.

## The three active ending families

1. **The Sovereign:** requires genuinely earned regional King proof. An earned Emperor may remain in office or, optionally, retire after selecting an adult child who has separately demonstrated civic judgment and frontier stewardship before independent public witnesses. Regional rule does not imply imperial union. The approved abdication is peaceful and voluntary; no contested succession/civil war. Old E01/E04 scripts are retained as archive and variant material rather than additional ending families.
2. **The Legendary General:** a source-legal non-sovereign survivor; military service and evidence are required before the prose calls the player a general. Non-command retirement, administrative/service and family variations render explicitly as *A Life Beyond War* rather than fabricating a military rank. The old E02/E03/E05/E06/E07 sources remain available for older saves.
3. **The Final Legacy:** triggered only by an actual fatal event, not high risk/score alone. Earlier E08 manuscript and old bridge remain accessible in pre-existing saves.

**Runtime migration:** fresh completed games route to `i84_bridge_<family>` and then `i84_lifetime_<family>`. `flags.i84_ending_family`, `flags.i84_legacy_source`, and optional `flags.i84_*` reign/heir evidence are additive. Existing `LIFETIME_DRAFT.endingBlocks`, eight original bridge/lifetime scene IDs, old save keys, crowns, marriage, Inner Circle, Dragon roster and realm names are unmodified. Previously saved players already at old manuscript scenes are not forcibly remapped or replayed. Character label switches to Retired Emperor only after abdication, while imperial unification remains a proven historical achievement.

**Adulthood / successor definition:** a child must exist under earlier player-earned `auh69_child` fostered-guardianship or `auh70_bio_children` biological records, be >=18 at the current narrative year, and have a verified family relationship. A mature child is **not automatically competent**. Selection by the player initiates an optional, transparent, two-part assessment (civil records and a limited military supply duty); direct appointment without verification fails. The player can always keep ruling, even after an assessment passes. No automatic pregnancy, adoption, choice of eldest child or family rivalries.

**QA receipt:** Node/parser PASS; 1,105 new assertions PASS; 8 source-legal mechanical 190-to-terminal traversal variants PASS including fatal, regional King, civilian/general and Emperor; UI clicks at 390/1280 px PASS. Abdication-specific tests use correctly constructed qualifying **checkpoint fixtures**, not a complete organic 190-to-abdication run. Physical file-origin save/reload, broad story prose audit, full historical NPC progression and multi-session persistence remain **NOT VERIFIED**. Next milestone v0.4.85.

---

# ACTIVE CHECKPOINT — v0.4.83: THE ROADS OF UNIFICATION

**Source executable:** `ALL_UNDER_HEAVEN_v0.4.83_DEV_THE_ROADS_OF_UNIFICATION.html`, SHA-256 `cd9046197b76e0b0afa209ca65bdffa7fa7a68b3230572771c116f576314aeb3`. **486 scenes, 29 People; eight original E01–E08 ending sources preserved.** This FAST GDD is a cumulative planning/continuity file; **v1.28** remains the underlying Master GDD identity.

**Implemented milestone v0.4.83 (targeted):** Nine new Chapter XII scenes integrate operation planning, supply, rear-guard relief, rival independent countermoves, mountain-pass protection and Jiangdong fleet responses into the old post-234 optional royal branch. Campaign choices are consequential: adequate provision plus suitable military / treaty choices are required for regional unification in addition to *existing* earned earlier proof; bad logistical choices can prevent further conquest. Ordinary officers suffice, while optional commissioned Dragon Generals and the actually recruited Grand Strategist have distinct contributions without automatic victories. The protagonist may personally lead military actions and may remain King rather than become Emperor. A 235 field council preserves the 239 Five Dragon muster/review. Kingdom/empire naming from v0.4.82.1 and family/adulthood conventions are unchanged. Retains 12 chapters and English game UI.

**Technical continuity:** Append-only scene definitions and targeted `.choices` wrappers for the existing royal campaign. Campaign records are optional `state.flags.w83_*`; save-key names unchanged; `realmNames`, `innerCircle`, `dragonGenerals` untouched. Later original scene IDs remain available to legacy saves. Dynamic E01 epilogue addition states costs and specifically recorded military assignments only. Avoid presuming historic NPC faction transfer or the existence of a player-created family.

**Acceptance evidence and limitations:** Node syntax PASS, 618 focused checks PASS; 5 original v0.4.82 organic journeys PASS; 2 additional choice-legal journeys from 190 to imperial naming/ending, including with zero Dragon Generals; UI 390/1280 px 19 war choices + naming PASS; no JavaScript errors or overflow. v0.4.83 is a **meaningful campaign-depth batch**, not a fully quantified combat simulator; casualty trajectories, individual historical-officer careers, physical offline persistence, comprehensive eight endings and v0.4.84 peaceful abdication remain open.

**Next locked step:** v0.4.84 THREE main ending families (Sovereign / Legendary General / Final Legacy), with voluntary abdication only after a valid Emperor reign to the player's selected adult child proven fit to rule, **NO succession struggle**; preserve original eight sources and saves throughout migration. v0.4.85 end-to-end QA follows.

---

# MASTER GDD FAST — v0.4.82.1 NAMING ADDENDUM (11 NOV 2026)

**Executable baseline:** `ALL_UNDER_HEAVEN_v0.4.82.1_DEV_THE_NAMES_OF_THE_REALM.html` · SHA-256 `13a83678a7720dc771d3e82da2d0cec63f7f557eb6d834fa00b7fd719ec2fba2`. A targeted revision above v0.4.82. Current playable structure: **477 scenes, 29 unique People, eight original ending manuscripts retained**.

## Kingdom and empire names — implemented

1. Players can name their earned **regional kingdom after the 233 CE King ceremony**: suggested River Marches / Han / Liang / Yan, or custom text.
2. Players can separately name their earned **imperial dynasty after the 250 CE unification oath**: inherited Great [Kingdom] or suggestions Great Han / Great Liang / Great Yan, or custom text. Royal and imperial names are independent and persist via optional `realmNames.kingdom` and `.empire` fields. Latin/CJK letters, numbers, spaces, hyphens, apostrophes and periods allowed, 2–32 characters, with escaping for display.
3. Naming does not grant or override title, territory, military merit, Inner Circle, Five Dragon Generals, or imperial ratification. Never permit names when King/Emperor proof missing. Players may leave the defaults. Existing save JSON remains valid and old save keys are unchanged. Names appear in Character, sovereignty rank/affiliation, and conditional E01 epilogue.
4. The older **eight master ending manuscripts** remain preserved until tested v0.4.84 conversion to the **three approved ending families**: Sovereign / Legendary General / Final Legacy. Peaceful voluntary abdication only to an adult child with documented merit, no succession war, remains future work.

## Test evidence / limitations

PASS parser, 540 state+structural checks, real browser clicks at 390/1280px, and five legal mechanical journeys from 190 to terminal. **Not certified:** physical offline `file://` save persistence or full manually narrated endings. Continue v0.4.83 War of Unification, then v0.4.84 and v0.4.85. Keep all prior constraints and preserve existing codes.

---

# NEWEST CHECKPOINT — v0.4.82 THE FIVE DRAGON STANDARDS (11 NOV 2026)

**Source of truth:** `ALL_UNDER_HEAVEN_v0.4.82_DEV_THE_FIVE_DRAGON_STANDARDS.html` (SHA-256 `edc53d79d1e55a71a05cadf908542e3183cc5883deb811bdc084aac8fa4a8cbf`). **476 registered scenes / 29 unique People entries / 8 original ending manuscripts unchanged**. Incremental patch directly over v0.4.81 HTML, NOT a replacement game. Milestone v0.4.82 **core King-to-Five-Dragons loop implemented and target-tested**, not comprehensive release certification.

**Implemented:** the pre-existing regional kingship remains an earned, ratified 233 CE state. A **230 CE witnessed military ledger** introduces original field captain **Lin Shuo**; it may be audited, only partially credited, or passed to independent officers. At the King's 234 CE council, the player may optionally establish **Five Dragon Generals (五龍將)**; founding alone appoints **zero** generals. Five possible personally appointed commanders require distinct witnessed service: Han Sheng (veteran discipline), Xu Wen (field infantry), Deng Yu (convoy logistics), Pei Liang (trained reserves), Lin Shuo (audited rear guard). Roster may remain 0–5, officers may be individually relieved and later reconsidered, and the King may first found/review the standards during the optional 239 CE northern campaign. A service-unproven Lin Shuo refuses an unsupported royal rank. Five Dragon Generals are **separate from the seven-person Inner Circle**, yet members may overlap. Royal mandates do not grant another faction's allegiance, force victories, turn Wei Zhen into a military general, or bar protagonist frontline service. People UI displays only a formally founded and earned roster. The seven Inner Circle slots and Grand Strategist are unaffected.

**Source-legal organic QA from 190:** 5 independent mechanically traversed directed routes: King with 5 standards; King with 2; King with zero; King declining founding; non-King denied the military order. The played 5-standard route reaches the already-existing 250 CE E01 epilogue through **307 choices**, with no injected title, personnel, or territory. This test is **choice-engine simulation, not a full manual UI readthrough**. Additional source-consistent 234 fixtures check 0–5 appointments, independent refusal, 239 late founding, release, legacy save normalization and permission. Chromium UI click tests at 390px/1280px passed. 8 original ending manuscripts retained.

**QA evidence:** 1,312 focused v0.4.82 checks; 6,284 legacy v0.4.81 checks; 518 structural checks; syntax PASS; five legal 190-to-terminal route variants; 390/1280 browser clicks PASS. **NOT certified:** literal `file://` persistent save/reload, manual read of every ending, long-term historical recruitability, full independent-NPC career and potential on-screen battle casualties, three-ending migration or imperial abdication. Major multi-stage Kingdom-inspired war belongs to v0.4.83, not claimed finished here.

**Roadmap preserved:** v0.4.80 / 0.4.81 prior work -> **v0.4.82 core implemented** -> v0.4.83 War of Unification -> v0.4.84 3 ending families and peaceful worthy adult-child succession, NO civil war -> v0.4.85 full story QA. English gameplay / Indonesian dev reports. Timeless Heroes unchanged. No spoilers in ordinary user-facing reports.

---

# LATEST DEVELOPMENT CHECKPOINT — v0.4.81, THE LIVING COMPANIONS

**Active game:** `ALL_UNDER_HEAVEN_v0.4.81_DEV_THE_LIVING_COMPANIONS.html` · SHA-256 `c9837c9af6e39bc4c5be199b9370d47e6f51f0e4a367e9801772ae80335f9b4f` · **470 scenes / 28 unique People entries / eight retained legacy ending bridges**. This is a targeted development checkpoint, not final release certification. **Roadmap v0.4.80–0.4.85 remains locked**, with v0.4.80 complete at its prior tested scope and v0.4.81 substantially implemented but deeper historical recruiting and full NPC career simulation still open.

**Changes implemented:** Nine new optional scenes in 193, 196, 208, 210, and 220 CE; two original candidate NPCs Yao Qing (diplomatic courier) and Pei Liang (developing field officer). Earlier four original companions Qin Rui, Deng Yu, Han Sheng, Xu Wen and Grand Strategist Wei Zhen keep continuity; eleven intended candidates are tracked (four baseline originals, three newer originals, four historical). Four additional original characters can receive earned 196 invitations (Qin Rui, Deng Yu, Yao Qing, Pei Liang). Up to seven total may form an actual circle by 196 CE through valid choices from 190 CE, while a player may refuse everyone. Historic Zhao Yun, Xu Shu, Mi Zhu and Lu Su retain their separate factions/duties; none is made an automatic retainer. Reports about each are encountered conditionally. Account disagreements in 210 CE may lead to an earned departure in 220 CE, preserving independent character agency.

**Universal Timeless Heroes, stage 1 implemented:** protagonist remains 16 in 190, children mature, calendar/chronological ages still increment, outward appearance stabilizes from adulthood, and technical age-100 caps on calendar advances are removed; existing adult-romance gating and biological/adoptive child timelines stay unchanged. The People and Character UI mention the convention without guessing specific NPC birth years or erasing pre-existing appearances. No immunity to battle, illness, injury or event-based death. The game does NOT currently simulate a separate full age database for every NPC, and no complete war-to-250 narrative appearance audit has yet been completed.

**QA:** `node --check` PASS; **6,284 new logic assertions** PASS; **491 legacy structural and ending bridge checks** PASS; two source-legal journeys from 190 to 196 (accept route: 95 choices, seven earned companions; decline route: 94 choices, zero companions) PASS; Playwright Chromium real UI click checks at 390/1280px PASS with no page errors or horizontal overflow. Character physical stage, People disclosure, serializer/legacy save normalization, 208–220 agenda/departure combinatorics checked. **Physical `file://` save persistence, complete manual eight endings, and historical NPC recruitment remain unverified / unfinished.**

**Next milestone:** v0.4.82 — King-only Five Dragon Generals, earned offices and appointments; continue strengthening candidate and independent faction follow-ups as needed before claims of complete v0.4.81 depth. Three-ending migration and peaceful abdication remain later v0.4.84 tasks. No spoilers in ordinary user reports.

---

# LATEST DEVELOPMENT CHECKPOINT — v0.4.80, THE CIRCLE BEFORE THE CROWN

**Status: implemented and targeted QA passed; NOT final.** Executable source is `ALL_UNDER_HEAVEN_v0.4.80_DEV_THE_CIRCLE_BEFORE_THE_CROWN.html` (SHA-256: `3e11e4c1aa06cdb94cc360649b4012fb1aa11f9447fa72af88e4eb438c1b4583`). Current counts: 461 scenes (eight added), 26 People entries (Wei Zhen added). The legacy eight ending manuscripts and save keys remain.

**Changed:** Original candidate **Wei Zhen** appears in an optional recorded encounter at Chenliu in 190 CE; can be met or declined. Han Sheng and Xu Wen gain optional personal trust scenes through their existing 190 CE patrol. A 191 CE relay encounter tests Wei Zhen's fallible tactical judgment and friendship with the two others. A 193 CE earned invitation lets the player ask Wei Zhen to become a **primary Grand Strategist** and invite Xu Wen and Han Sheng into a personal Inner Circle. Everyone may decline/part; there is a legal no-join path. A separate `innerCircle` save object stores up to seven active members and a single strategist reference. People panel shows only player-earned members, not hidden personality dossiers. Older saves receive an empty roster, never retroactive followers. The player remains the protagonist and all rank awards are still earned separately.

**Test evidence:** Node JS compile PASS; 3,099 engine assertions across path combinations and legacy-save normalization PASS; two source-legal 190→193 automatic traversals (accept: 83 scenes, 3 earned members; reject: 82 scenes, zero members) PASS; Playwright clicks on 390px and 1280px (state checkpoints for unchanged intermediate chapters, genuine choice handlers for new scenes and opening, no page error or horizontal overflow) PASS. This is NOT certification of all eight endings or physical `file://` save/reload. No NPC art was created in this batch.

**Next work:** v0.4.81: all 11 candidate concepts, NPC autonomy / cross-relations, and Timeless Heroes implementation. Maintain the 7 active cap and one Grand Strategist. Do not recreate from scratch or erase eight legacy ending scripts until v0.4.84 migration is validated.

---

# ALL UNDER HEAVEN — MASTER GDD v1.28 — FAST INTERNAL

**Type:** Optimized AI-reading edition of the **approved Master GDD v1.28**. **No new source GDD version; the FAST working edition incorporates the latest binding user ruling (10 Nov 2026): the playable protagonist is the central historical actor, and Romance of the Three Kingdoms is inspiration, NOT an inviolable canon.** Prepared 10 November 2026, with current build pointers refreshed 11 November 2026 after v0.4.79. This is the working GDD reading file; the full unchanged v1.28 is preserved in the archive named below. Its source identity remains **v1.28**, while World Bible v1.77 FAST is the active continuity reference. 

**Approved source:** `ALL_UNDER_HEAVEN_Master_GDD_v1.28_INTERNAL.md`, SHA-256 `2892547229687bcded95395f787d4db05d277547460924a556d341162d9de081`.
**Full source archive:** `ALL_UNDER_HEAVEN_Master_GDD_v1.28_FULL_ARCHIVE.zip` — consult only for verbatim historical wording, superseded decisions, detailed research leads or old QA evidence. The archive is not an everyday fourth active project file.
**Active companion:** `ALL_UNDER_HEAVEN_World_Bible_v1.77_FAST_INTERNAL.md` (early Inner Circle formation locked as future design). **Current playable baseline:** `ALL_UNDER_HEAVEN_v0.4.79_DEV_MANDATE_OF_UNIFICATION.html`, SHA-256 `e180056c0af6f795996822653e28b3cfbf2a2f4bcb232e7ed86bf916f419d650`.
**Disclosure:** INTERNAL SPOILERS may be retained here and in the World Bible. Player-facing game and ordinary chat must not reveal undiscovered characters, endings, motivations, affinity, hidden conditions or other story secrets. Game prose and interface: **English**; production discussions: **Indonesian**.

---


## ACTIVE SIX-MILESTONE DEVELOPMENT ROADMAP — USER LOCKED 11 NOVEMBER 2026

**Must survive chat transfers; authoritative checklist packaged as `ALL_UNDER_HEAVEN_ROADMAP_v0.4.80_TO_v0.4.85_LOCKED.md`.** In order: **0.4.80** early Inner Circle incl. Xu Wen, Han Sheng and original Grand Strategist; **0.4.81** all 11 candidates, independent NPC arcs and universal Timeless Heroes; **0.4.82** King status and optional founding of five Five Dragon Generals; **0.4.83** deep, multi-operation, *Kingdom*-inspired war for China with direct protagonist combat; **0.4.84** tested migration to 3 ending families, optional earned peaceful abdication to a worthy adult child without succession conflict; **0.4.85** end-to-end narrative, state, QA and offline-save checks. Start with **0.4.80**. Milestone numbers denote target sequence, NOT implementation or test claims. All old eight ending code paths must remain until explicit, tested migration. Carry forward v0.4.79 executable unchanged; full acceptance gates are in the separate roadmap file.

## LATEST USER-APPROVED ENDING & PEACEFUL SUCCESSION DECISION — 11 NOVEMBER 2026

**Authority / status: LOCKED FUTURE DESIGN. NOT YET CODED.** This section supersedes earlier proposals for eight separate *future* endings, five grouped endings, contested heirs, and 280 CE as a required finish. It does **not** delete or override anything already executable in HTML v0.4.79. Preserve all eight original E01–E08 manuscripts, ending conditions, save IDs and existing option routes until a separately tested migration exists. This is an approved **target architecture**, not a claim that the game now has three endings.

- **THREE main ending families (target):** (1) **The Sovereign** — become King, possibly unite China and become Emperor; branches include remain King, reign as Emperor, or voluntarily abdicate *after* successful unification and a meaningful (non-obligatory) reign. (2) **The Legendary General** — heroic military legacy without needing a sovereign throne; can continue command, retire peacefully, or hand over command. (3) **The Final Legacy** — premature death / fatal consequences of meaningful choices; a serious potential outcome, never forced merely for variety. Past government/reform, independent domain, personal/family, and peaceful retirement conclusions become **conditional epilogue variants**, not additional major ending families. Diplomacy and civil administration remain substantial gameplay.
- **PEACEFUL ABDICATION IS A VOLUNTARY E01 VARIANT, NOT AN EXTRA ENDING.** It requires that the protagonist *actually* became Emperor of unified China and has an **adult, demonstrably capable, eligible child chosen by the player**, not just the firstborn or a hidden automatic successor. Biological or legally recognized adopted children may be eligible when game relationship and legal context supports it. A credible successor should have earned preparation/experience, demonstrated judgment and public-administrative responsibility; the selection and abdication are explicit player decisions. If no appropriate adult child exists, this specific abdication-to-child option is unavailable; never conjure a spouse, child or heir to unlock it. Timeless Heroes applies: neither abdication nor successor readiness requires an aging/illness decline.
- **NO SUCCESSION CONFLICT.** Explicit user veto: **do not write inheritance fights, sibling contests, throne-grabbing intrigues, rival heir civil war, a disputed designated heir or a compulsory succession crisis** as the price of the abdication route. The selected heir is genuinely worthy; succession is deliberate, respected and peaceful. Appropriate challenges of *governance*, reconstruction and leadership after abdication may remain, without secretly reintroducing an heir dispute. Other children retain agency and dignified lives, not automatic antagonists.
- **PLAYER AGENCY & PACING:** Do not force Emperor, abdication, marriage, children, or any single ending. Prefer a focused conclusion around 245–250 CE as an authoring target, not a hard calendar gate; King-before-optional Five Dragon Generals-before-optional Emperor order persists. Allow strong military play throughout and no mandatory long retirement arc. The 12-chapter structure is retained; Chapter XII may contain several optional late campaign phases.
- **QA/migration pending:** design a mapping of existing E01–E08 runtime outcomes to three target families without deleting prose, losing route flavor or breaking saves. Validate earned family/adult heir, childless emperor, regional King, continuing Emperor, Legendary General, fatal branches, age/calendar and UI before claiming the migration complete. Never claim this addendum proves executable abdication or three-ending architecture.

### POST-v0.4.79 — APPROVED NEXT-DEVELOPMENT DESIGN, NOT IMPLEMENTED (11 Nov 2026)

## LOCKED USER DESIGN DECISIONS — 11 NOVEMBER 2026 — IMPLEMENTATION PENDING

**Status = APPROVED_DESIGN, NOT_IMPLEMENTED in HTML v0.4.79.** These are explicit decisions made after the v0.4.79 executable checkpoint, not functions/flags/scenes already in that build. Later chats MUST read this section before changing the age system, NPC cast, ruler path, military honors or family timeline. User-facing updates must not claim QA or implementation until code is changed and tested. English playable narration/UI; Indonesian development reports. The player remains the protagonist and sole decision-maker of their life.

### A. UNIVERSAL TIMELESS HEROES / YOUTHFUL APPEARANCE (user confirmed)

- **Intent:** the protagonist and beloved/favorite NPCs should visibly remain young throughout the campaign, including the long campaign to unify China. To avoid an arbitrary favored-only exception, **apply the same fictional life-course rule to all humans in the world**, historical and original, men and women; this is a literary convention, not a supernatural power, scientific proposition or new claim about actual Three Kingdoms history.
- **Clock stays real:** world calendar, elapsed years, birthdays and **chronological ages** keep advancing. New protagonist starts at **16 in 190 CE** (unchanged), is 60 in 234, and may be 76 in 250; do NOT freeze the stored age, reset age on scene entry, break year/age sync, or rewrite saved character age. Real historical birth-year chronology, relative seniority, rank, meeting feasibility, and known deadlines remain meaningful. Existing saves preserve old data.
- **Growth and youth:** children and adolescents develop normally until adult maturity. Once an individual reaches their established **adult appearance**, age-related visible aging and routine physiological decline cease; adults retain youthful adult looks despite increasing chronological age. No fixed numeric maturation threshold is invented for every person; preserve the individual age, visual state, and the romance-specific anchors below. Individuals already elderly when introduced are **not** retroactively rejuvenated. Facial expressions, scars, injuries, illness, disability, style and the consequences of lived experience can still change.
- **Mortality remains:** injury, battle, disease, murder and consequential story events can kill characters. Mere old chronological age should NOT automatically trigger a death, mandatory retirement or weakened combat ability under the new system. No invulnerability, forced resurrection, immortality or plot armor; senior advisors and veteran generals remain autonomous. This rule still needs a focused audit of existing age-driven scenes, character descriptions, mortality gates, and ending prose before code implementation.
- **Family consistency:** children still grow to adulthood and can develop independence, adult careers and optional succession stories. Parenthood/pregnancy/adoption remain elective with recorded consent and actual played decisions; never auto-award spouses, heirs or property. The protagonist's youth does not entitle them to romantic access to anyone.
- **Adult-romance preservation:** Six fictional adult romance candidates retain their v0.4.70 **stable adult age anchors**: Shen Lian 29; Lin Yue 26; He Qing 28; Cai Zhen 27; Lan 25; Song Wan 30. These were already deliberately non-aging **for the six candidates only**. Universal youth extends adult visual preservation to the rest of the cast but MUST NOT alter the six approved anchor ages, eligibility, mutually consenting adult-only romance or marriage constraints. No intimate/romantic content involving minors; adults age 18+ only. Treat historical NPC recorded birth years separately as chronological facts, not frozen identity ages.
- **Presentation:** avoid continual lines about miraculous anti-aging or characters being frail due only to calendar age. Experienced characters can acquire gravitas, scars, changing habits and political judgment while remaining physically youthful adults. Keep occasional birthday events and aging-related respect in social terms, without describing physical decrepitude based on chronological years alone.

### B. PLAYER-BUILT INNER CIRCLE (user confirmed)

- **Max 7 active trusted Inner Circle members**, separate from the potentially very large wider military/civil court and distinct from friendship count. Membership is earned and changeable, never automatically filled. A person need not hold a formal office to be close to the protagonist. The seven desired functional contributions are: closest companion, grand marshal, grand strategist, elite general, chancellor, logistics commander, and diplomat/intelligence chief. **Roles are descriptive, not seven mandatory exclusive slots or automatic rank awards.**
- **11 principal candidates planned:** four existing original NPCs **Han Sheng, Xu Wen, Qin Rui, Deng Yu**; **three new original candidates not yet named or designed in code** (strategist, diplomatic/intelligence talent, rising field officer); four higher-priority historical possibilities **Zhao Yun, Xu Shu, Mi Zhu, Lu Su**. These are design candidates, NOT currently recruited/guaranteed, and their whereabouts, dates, oaths, lives and loyalties must be respected. 3–4 opportunities for substantial lifelong friendship. Other historical figures, including Liu Bei's celebrated retainers, may become credible alternative-history allies only if hard-earned; do not steal loyalists by fiat.
- Every member has independent beliefs, friends, rivals, ambitions, possible family, refusal/departure/betrayal/death and world actions. Members have relationships **with one another**, not only with the protagonist. Avoid spoiler/exposed hidden personalities. Reward actual shared history, not just combat rank or hidden score.

### B0. EARLY INNER CIRCLE GENESIS — 190 CE ONWARD (explicit user decision, 11 Nov 2026)

**MANDATORY START:** The *formation process* of the player's future Inner Circle **must begin in the opening 190 CE playable story (Prologue / earliest Chapter I)**, while the protagonist is age 16 and before receiving a lordship, army, royal crown, or formal council. This overrides any earlier shorthand suggesting council recruitment begins only when the protagonist becomes a ruler. It **does not** mean seven preselected companions or a court exist on the first screen.

- **Immediately encounter possible lifelong companions** through location-plausible shared work, journeys, military service or crises. Author real choices to help, trust, disagree with, distance from, or lose the earliest people; a first meeting may be just an acquaintance. An initial circle of **0–2 organically trusted people** is a pacing target, not a free grant, forced minimum, or automatic entourage. Entry can happen when warranted after shared action, even before any formal title.
- **Reuse established early-character continuity where feasible** (especially Han Sheng and Xu Wen if the actual source route, place, and timeline permit). Qin Rui and Deng Yu can join later based on genuine witnessed meetings, not forced 190 appearance. Do not retroactively add historical figures who were elsewhere, alive at different stages, or loyal to other patrons. Existing NPC identities and discoveries remain untouched until played.
- **The original Grand Strategist candidate must have an early, meaningful introduction and an attainable friendship/recruitment pathway beginning in Act I (190–192), or as soon as local travel/story feasibility genuinely allows—not hidden until kingship or late empire.** Early candidate may be a young scholar/learner with notable judgment, *not* magically fully accomplished at the first encounter; earned counsel, mentoring, mistakes and accomplishments support later formal appointment. If the early encounter is declined, provide conditional later re-encounter(s) rather than compulsory recruitment. Preserve exactly one primary Grand Strategist at a time, a possible empty seat, and historically plausible optional alternatives.
- **Development stages**: 190–192 acquaintance and first trusts → 193–199 repeated companionship, disagreement and first earned stable fellowship → 200 onward earned military/political responsibilities, personal change and potential departures → regional rule, kingship and a larger court, with no automatic seven-member completion → Five Dragon Generals only *after becoming King* and separately from Inner Circle → potential imperial unification without rewriting early relationships.
- **Show long-memory callbacks** in choices, visits, council debates, frontline missions and family life: longstanding bonds affect later offers and reactions without replacing player agency. Members may retain friendships after dismissal, be close without holding office, or accept high office without being personally close. Also author inter-member connections, jealousies and loyalties. Player can choose solitude or refuse candidates; the game still progresses.
- **Do not conflate with starting power**: protagonist at 16 in 190 CE has no free permanent entourage, no Grand Strategist already in post, no Five Dragon honors, no royal authority. Formative closeness is *personal*, not an early government cabinet. Maintain privacy of NPC personality/hidden gauges.
- **Implementation/QA NOT YET DONE in v0.4.79 HTML**: inspect actual Prologue/Chapter I inbound choices and NPC chronology; insert small optional encounter/choice arcs, preserve existing choice effects and one-time flags; ensure age/time, no retroactive historical discovery, save compatibility, refuse/leave/rejoin alternatives, later council callbacks, no softlock and no forced seven members. Run targeted early and late regressions, including early Grand Strategist introduction and an optional zero-Inner-Circle path. Do NOT claim this is already playable merely because World Bible specifies it.

### B1. GUARANTEED GRAND STRATEGIST OPPORTUNITY / PRIMARY STRATEGIST (user confirmed, 11 Nov 2026)

- **Binding narrative requirement:** among the protagonist's maximum **seven Inner Circle members**, the intended functioning council **must have one named primary Grand Strategist**: a genuine strategic mind of a caliber comparable in *narrative importance and versatility* to **Zhuge Liang or Sima Yi**, not a literal copy or a character with guaranteed foresight. This is an additional explicit player decision, taking priority over the earlier statement that all seven role descriptions are optional. **Exactly one primary strategic adviser at a time** may hold this council responsibility; another adviser may exist outside the Inner Circle. Do not expand the seven-member cap.
- **Do not auto-recruit.** Make at least one credible **original Grand Strategist candidate** available through story-grounded encounters and choices, independent of the survival/recruitability of any historical figure. Recruitability must be a real playable opportunity (not merely a codex mention), and advancement into the Inner Circle should require mutual trust, demonstrated competence, and willing acceptance. If the player repeatedly rejects every candidate or the strategist leaves/dies, the role may temporarily or permanently remain vacant by player consequence. Hence guarantee **an attainable opportunity**, not guaranteed companionship against the player's decisions.
- **Strong distinct character:** independent ideas, limitations, human motives and substantial relationships with the protagonist and other NPCs. Can propose multiyear grand strategy, assess military logistics, predict reasonable opponent moves, coordinate battlefield operations with the Five Dragon Generals, conduct diplomacy and institutional reform, and **challenge the protagonist's plans** when warranted. Avoid infallible clairvoyance or NPC usurping the player's leadership. Meaningful disagreement, mistakes, loyalty strain and rivalries have lasting outcomes.
- **Recruitment alternatives:** a historically plausible alternate-history **Xu Shu** may compete for the primary adviser role if legitimately recruited; **Zhuge Liang** or **Sima Yi** may only be recruited through exceptional, historically coherent alternative-history branches that respect existing obligations, age, place, factions and relationship history. No historically famous adviser is automatically reassigned to the protagonist. A candidate's arrival must never retcon a prior NPC's loyalty.
- **King → Emperor continuity:** if the protagonist establishes a kingdom, the primary Grand Strategist should be a true actor in strategic deliberations **before** the unification campaign and during it, able to disagree with the five independently selected Dragon Generals. After unification, retain independent statesmanship, fallibility, and political risk. The protagonist makes the final player choice and can personally lead armies.
- **Coding and QA obligation:** implement original candidate introduction and organic recruitment, show one clear primary Grand Strategist assignment, unique seat validation, vacancies/replacements, and callbacks into military/political decisions; test early successful recruitment, deliberate refusal, death/departure, eligible historical alternate, and coexistence with the seven-person limit and five Dragon Generals. **NOT IMPLEMENTED in v0.4.79 HTML.**

### C. KING → FIVE DRAGON GENERALS → UNIFICATION → EMPEROR (user confirmed)

- **Progression is optional and earned:** young protagonist → independent regional ruler → **King** → option to formally establish **Five Dragon Generals** (*Five Dragon Generals*, fictional `五龍將`, Wǔ Lóng Jiàng) **while already King, BEFORE becoming Emperor** → actual military/diplomatic multi-region unification → optional imperial oath/coronation as **Emperor of a unified China**. May stay King, fail at unity, refuse emperor title or pursue other ending paths. The v0.4.79 HTML **already implements an earned regional crown and earned imperial unification variant of E01**, but DOES NOT YET implement Five Dragon Generals or the fuller Inner Circle system.
- **Max 5 Dragon Generals, not required to fill all five.** Award to meritorious original or historical serving commanders via credible kingly authority, player approval and a meaningful ceremony. Titles should recognize different strengths (large-force leadership, valor, tactical command, defense, independent campaign) without pigeonholing permanent abilities. The cohort is a fictional honour, **not** the historical office or a rename of Liu Bei's literary Five Tigers. The earlier suggestion **Five Pillars of the Realm is superseded** by the user's chosen name **Five Dragon Generals**.
- Dragon membership and 7-person Inner Circle are **independent, overlapping sets**: a commander may be on both; Dragon status alone does not mean private friendship or automatic obedience. Appointments have social consequences for selected/unselected officers. Resignations, deaths, unworthiness or defection may leave vacancies; fame and accomplishments affect later campaigns. The protagonist still personally leads battles if chosen and credible. After imperial unification, surviving Dragons can retain honor and obtain new earned responsibilities without being auto-promoted.
- This king-founded Dragon institution is **distinct from** the older optional 'Six Tiger Generals' honor proposed for an exceptional Liu Bei/Shu-aligned literary alternate-history route; do not conflate the two, do not make the Five Tigers historically official, and do not award either by default.

### D. KINGDOM MANGA AS HIGH-LEVEL CREATIVE REFERENCE — UNIFICATION (USER APPROVED 11 NOV 2026; NOT YET IMPLEMENTED)

**Goal:** Build the *feeling of an epic, sustained, personally costly unification campaign* after the protagonist has earned the title of King and has the option to found Five Dragon Generals. Inspired by the scope, rival armies, political struggles, rising commanders, and tactical/strategic reversals associated with Yasuhisa Hara's *Kingdom* (Qin/Warring States), **without copying its specific plot, lines, designs, military-unit names or character archetypes wholesale**. *All Under Heaven* remains a 190 CE Three Kingdoms alternate-history story and preserves *Romance of the Three Kingdoms* inspiration. General references only: https://www.viz.com/kingdom and https://kingdom-anime.com/story/ .

**Design constraints (binding):**
1. Player: 16 in 190 → earn friends and command → become regional ruler → **King** → optionally create and appoint **up to five earned Five Dragon Generals** → wage connected Northern/Western/Jiangdong campaigns → govern settled regions → optionally become **Emperor of unified China**. Remain King, fight and lose, negotiate peacefully, refuse the Emperor title or select other endings; keep all eight main ending slots unchanged.
2. Inner Circle max 7, with one available/recruitable original Grand Strategist introduced meaningfully from Act I, capable of sophisticated but **fallible** counsel. Dragon Generals may overlap the circle. Their battlefield initiative and consequences depend on trust, command, supply, experience, service and actual decisions; their lives and choices remain their own.
3. Campaign depth: multi-step sieges, supply lines, terrain, weather, reinforcements, fatigue, intel, morale, opposing generals' independent countermoves, diplomacy, temporary retreats and civilians; avoid 'one choice captures a kingdom'. Each theater's actions should impact later theaters and reconciliation. Let protagonist directly lead and fight without replacing the strategist or generals; never make protagonist a spectator while NPCs monopolize all decisive turns.
4. Winning does not erase local institutions. After military/diplomatic settlement, require credible sovereign transfer, governance, tax/legal protections, and civilian legitimacy before asserting a unified empire. Treat regional lordship and universal empire as distinct. No fiat-dead historical figures, no forced historical defeat, no guaranteed outcome.
5. Keep established 12 chapters: optional campaign beyond 234 remains integrated as Chapter XII-tagged late life, as in v0.4.79. Red Cliffs remains a principal earlier climax, not a scene invalidated by later wars. No mandatory linear conquest track or ninth ending. Universal Timeless Heroes, family agency, adult-romance anchors and offspring chronology remain intact.

**Implementation/QA acceptance later:** Verify the v0.4.79 235–250 ten-scene contract first; extend it with coherent campaign decisions and earned NPC appointments (not a ground-up rewrite); unit test King-only founding, zero/fewer-than-five Dragon seats, historical NPC refusal, adviser-departure alternatives, 3-theater state, campaign victory/retreat/failure, rank and age, imperial-gate denial and earned coronation, all 8 ending branches, legacy save/import/export. Sample source-legal 190→250 journeys plus real click tests. Physical `file://` storage remains an independent unverified release gate. **This addendum updates design docs only and is NOT an executable gameplay implementation or QA pass.**

### IMPLEMENTATION / TEST PLAN (REQUIRED LATER, NOT CLAIMED DONE)

1. Source-of-truth age audit: `state.age`, date advancement, save/load/validSave, per-NPC age/birth year anchors, AI/narrative descriptions, health/mortality and ending text. Implement visual/biological-age presentation separately from chronological age; preserve old saves and 16-year-old start; test across 190–250 and minors growing into adults.
2. Start organic Inner Circle formation in the 190 CE Prologue / earliest Chapter I, including early candidate encounters and an early original Grand Strategist introduction; never hand out an already assembled council. Follow with earned role/office separation, mutual NPC relations and exit consequences, without automatic entry for historical figures. Respect map, age, rank, loyalty and discovery.
3. After earned King title, offer founding and appointment scenes for Five Dragon Generals (0–5), record recipient identities, consent/acceptance, eligibility and independent missions; provide wartime callbacks through imperial unification, voluntary no-Dragons and remain-King routes.
4. Regression tests: eight endings, adult romance/consent, family children and succession, protagonist frontline freedom, NPC ages/meeting/social etiquette, independence and late-period deaths; actual offline `file://` persistent save/reload remains **UNVERIFIED** in v0.4.79 and must not be claimed otherwise.

---

### v0.4.79 — THE MANDATE OF UNIFICATION / EARNED EMPEROR ENDING (11 Nov 2026; IMPLEMENTED / TARGETED_AND_ORGANIC_QA_PASS)

**New binding user decision:** An ending as **Emperor who has unified China** MUST be genuinely available. Earlier v0.4.78 constraining E01 to regional kingship was correct only for the then-existing earned territory, not a permanent limit on protagonist destiny. The approved narrative's eight ending categories remain, with E01 now supporting a **regional king** outcome or a true **emperor of unified China** outcome, conditional on territorial proof. Do not award imperial rank from ambition alone, skip three independent regional institutions, or erase the kingdom-only and failed-unification alternatives.

**Implemented:** Ten new optional post-234 scenes tagged Chapter XII (235–250 CE), launching only from an earned 233 crown at the existing 234 council. Rival northern, western and Jiangdong administrations maintain interests, defensive capacity, separate registers and the ability to refuse. The protagonist may personally command expeditions or establish a negotiated league; both routes require prior source decisions and actual regional settlements, then a 249 whole-realm congress and chosen 250 imperial oath. The campaign can fail and E01 remains regional in that case. Complete imperial status is tested by `auh79Emperor(s)`, not an invented ending slot. Narrated/People UI reacts to the earned title; original eight `LIFETIME_DRAFT.endingBlocks` are unchanged; v0.4.78 E01 regional narrowing is applied only to non-imperial records. No forced romance, spouse, heir or famous NPC survival. Original save key and schema unchanged; year 250 is supported by `validSave` without migration.

**QA:** Runtime Node syntax PASS; **179 targeted assertions** PASS incl. both military and negotiated prepared-state routes plus denied false imperial title, regional failed route, old-save compatibility and E01 vocabulary. Chromium actual 12-click diplomacy route at each 390px/1280px viewport PASS, no JS page errors or overflow. Inherited 8,295 + 4,852 + 7,083 assertions PASS against final HTML. Directed **24 mechanistically legal 190 CE searches**: 13 terminals, 11 steps capped; **11 terminal E01 imperial outcomes** with all choices applied, one more emperor before step cap. This is not 11 manually read UI playthroughs, nor exhaustive gameplay, nor certification of genuine browser-origin persistent `file://` save. Mock storage export/import PASS. Post-234 campaign/late-century historical institutional responses and full imperial-family prose require editorial and deeper QA in later batches.

**Pointers:** Active HTML `ALL_UNDER_HEAVEN_v0.4.79_DEV_MANDATE_OF_UNIFICATION.html` SHA-256 `e180056c0af6f795996822653e28b3cfbf2a2f4bcb232e7ed86bf916f419d650`; active World Bible v1.71 FAST; this FAST GDD continues approved master GDD v1.28 without renumbering source.

---

### v0.4.78 — THE EIGHT WITNESSED LEGACIES / ENDING LITERARY CONTINUITY AUDIT (11 Nov 2026; IMPLEMENTED / TARGETED_QA_PASS)

**Scope:** v0.4.77→v0.4.78 HTML source patch, 443 scenes and 25 People unchanged. Eight original source ending manuscript blocks, arbitration, character-family rules, flags, persistent save key and calendar untouched. The player-visible epilogue renderer receives 29 bounded prose substitutions: an earned *regional* crown is not the whole empire; past command does not guarantee all soldiers survived; clerical influence is confined to willing jurisdictions; independence does not compel a city to mourn; administration does not silently grant a canal; retirement does not automatically grant an estate; and a fatal battlefield injury does not teleport a spouse or physician into a private room. Previously hardened E06 family/estate prose is preserved. This is editorial/continuity QA, not eight new endings or a new asset batch.

**Evidence:** 639+639 targeted checks across nine fixture scenarios × eight ending manuscripts (mobile/desktop) PASS, zero browser errors or overflow. Inherited state matrices 8,295 + 4,852 + 7,083 checks all PASS; eight bridge-to-ending real UI interactions at both sizes (16/16 clicks) PASS; v0.4.77 river UI 11/9 clicks PASS. 220 mechanically source-legal start-190 trajectories reconfirmed four E06 wife+child+family cases. Source master block JSON unchanged. **Mocked storage only**: same-page save/load plus real browser JSON export and FileReader import PASS, but HTTP localhost and native file origin are browser-policy blocked and native persistent offline reload remains UNVERIFIED. Do not confuse mocked storage with persistent file-origin QA, or targeted editorial QA with eight complete human readthroughs.

**Active triad:** `ALL_UNDER_HEAVEN_v0.4.78_DEV_THE_EIGHT_WITNESSED_LEGACIES.html` SHA-256 `17f5856385ef19163ee818a06b323feb002752cb74030356e145b1dfc1ef0af3`, `ALL_UNDER_HEAVEN_World_Bible_v1.70_FAST_INTERNAL.md` and this FAST GDD (approved GDD source **v1.28**, unchanged). Next highest release gate: real physical device/local-file persistence and multi-route NPC/ending editorial review.

---

### v0.4.77 — THE NAMES THE RIVER KEEPS / EARNED FAMILY-ENDING QA & CIVILIAN ACCOUNTABILITY (11 Nov 2026; IMPLEMENTED / TARGETED_QA_PASS)

**Implementation:** HTML code extended **v0.4.76 → v0.4.77** with four opt-in scenes for 230, 232 and 234 CE (443 total, +4; People 25; 15 historical). New late-river civilian petition follows the already-played regional-office events; mutually disputed reports preserve historical uncertainty and independent neighboring power centers. Actual witness claims, family situation and authority limits govern prose and options. Choices at 230 have bounded civic/administrative effects; 232 public appeals or independent review and 234 ledger succession yield eight individually authored conditional epilogue afterwords. The original eight `LIFETIME_DRAFT.endingBlocks`, eight bridge destinations and `auh64DecideEnding`/sovereignty arbitration remain unchanged; neither marriage, kinship, birth, child, office nor an ending is awarded by this addition.

**QA:** Node syntax PASS. New **8,295** assertions / 216 combinations PASS; inherited 4,852 assertions / 135 combinations PASS and 7,083 family assertions / 216 combinations PASS. Chromium prepared-state UI actual clicks: 11 mobile / 9 desktop for new arc, 16/16 inherited witness arc and 26/25 inherited household arc, no errors/overflow. **220 source-legal lifetime mechanical attempts** from initial 190 state resulted in **four** E06 instances with earned wife and child (no forced family flags, no ending override). 167 terminated, 53 reached step cap. These are not real manual playthroughs; `file://` persistence still untested due environment blocking local-file origins. The former open reachability question is resolved for mechanical source routes, but full manual eight-epilogue reading and native offline save remain open.

**Active artifact:** `ALL_UNDER_HEAVEN_v0.4.77_DEV_THE_NAMES_THE_RIVER_KEEPS.html` SHA-256 `e479aca4e88cb108b326e1ee072f7a32793d6f4a7fd9fad1fa1dac12285d5d24`. World Bible FAST v1.69 WB-01N records exact gates and uncertainty limits. Next: native offline persistence on permissive local device and editorial review of all eight outcomes.

---

### v0.4.76 — THE WITNESS BOOK AND THE HOME / HISTORICAL EVIDENCE & RESPONSIBLE E06 RENDERING (11 Nov 2026; IMPLEMENTED / TARGETED_QA_PASS)

**Implementation:** Source HTML v0.4.75 extended to **439 registered scenes** (+6), without recreating the engine, modifying original story choices, or changing legacy save keys. Two voluntary 230 witness/register conversations separate the player's personally observed 208–210 encounters and 223 independent regional-office reports; two voluntary 232 hearings allow rival offices to disagree while restricting the protagonist to jurisdiction and evidence actually acquired; a voluntary 234 account refuses fabricated certainty about the distant campaign. Another optional 234 home agreement follows only from verified wife+child and earned v0.4.75 home hearing; care, property and the child's freedom remain negotiated, not inherited by decree. See World Bible WB-01M for the exact additive flags and scene identifiers. An E06-specific **render-time** epilogue adjustment removes false unconditional child, estate, servants/fortune/property assumptions for old and childfree saves. The original eight `LIFETIME_DRAFT.endingBlocks` JSON manuscripts, ending arbitration, original romance cast, all original options, sovereignty/frontline and chronology rules are preserved. This is a *display reconciliation*, not a change in the approved underlying GDD ending manuscripts or an award of new wealth/land/children.

**QA and boundaries:** JavaScript syntax PASS; **4,852 branch/state checks** (135 structured witness/family combinations) and **7,083 inherited household checks** (216 combinations) PASS. Real UI **16 / 16 new clicks** at 390/1280 px, with inherited family UI **26 / 25 clicks** also PASS; no page errors or overflow. Sampled 140 legitimate 190→ending mechanical trajectories, 105 natural terminals and 35 step caps: one E06 route observed, but **E06 with organically earned spouse and child did not appear in these 140**, so combined E06+family editorial route is still unverified. Prepared married/child fixtures confirm E06 displayed text correctness, not source-legal end-to-end eligibility. Browser `file://` navigation remains denied by administrator policy; real native offline storage/reload/export/import remains untested. No release-final claim. Approved GDD source remains **v1.28**; this FAST file only updates active pointers and the implementation ledger.

---

### v0.4.75 — THE MEASURE OF A HOME / CHRONOLOGICAL FIRST VISIT & FAMILY ACCOUNTABILITY (11 Nov 2026; IMPLEMENTED / TARGETED_AND_ORGANIC_FAMILY_QA_PASS)

**Current HTML:** 433 scenes (+6), 25 People (15 historical), and eight unchanged lifetime ending manuscripts with original arbitration. Six original household characters / six candidate romance ages, one principal wife, up to five separately consenting concubines, and voluntary biological/foster-child paths remain governed by older GDD and World Bible contracts. A discovered chronology mismatch made the first 225 CE family visit invisible during a normal game: the inherited public council displays 225 content while its `storyClock` is still 224, then moves to 227 through its own choice effects. v0.4.75 offers a voluntary 224→225 household detour with correct real calendar advancement when a valid wife/home is present, then returns to the **same council and original public effects**. A new 227 two-scene witnessed refuge follow-up preserves original source decision effects; 230, 232 (two scenes) and 234 add optional, guarded, in-person household accountability. Family privacy, the wife’s chosen homemaker role, each concubine’s autonomy, children’s kin ties and the protagonist’s ability to lead government and personally fight remain intact. Distinct, conditional memories in the eight existing ending bridges require an actual 234 household conversation; no forced epilogue type or grant of marriage, title or child. The existing save key/schema and all inherited scenes/options remain present. Read World Bible WB-01L for exact IDs and flags.

**QA:** Node `--check` PASS; Chromium **7,083 assertions / 216 structured combinations PASS (0 failed)** including six wife IDs, varied family compositions, 224→225 on-ramp with preserved original 225 political effects, old-save bypass, original 227 home decision effects, 230–234 voluntary follow-through, chronology, child state and all eight bridge echoes. Real browser UI **26 clicks at 390 px** and **25 at 1280 px** PASS, no JavaScript exceptions or horizontal overflow, using prepared married-household states. **80 automated, source-legal 190→lifetime probes** additionally yielded 18 earned marriages (no direct status inject), at least 11 of those with earned children (foster and/or biological) and 12 with an earned 234 home account; this is a purposive test sample, not an exhaustive all-choices sample, and NOT a full browser UI playthrough of these 80 trajectories. v0.4.74's eight mechanically earned ending types remain earlier evidence, **not** a full new eight-ending certification. Physical native `file://` storage/reload and import/export, all spousal paths into specifically E06, comprehensive narrative and historical-NPC review remain UNVERIFIED. No final-release claim.

---

### v0.4.74 — OFFICES WITH THEIR OWN ORDERS / AUTONOMOUS RIVAL RESPONSES (11 Nov 2026; IMPLEMENTED / TARGETED_AND_ORGANIC_QA_PASS)

**Active HTML:** 427 scenes (+6), 25 People (15 historical), eight intact ending manuscripts and original arbitrator. Source approved GDD v1.28 and naming/romance requirements remain unchanged. Two 221 CE scenes respond to the already-earned original decision by distinguishing independent northern inspectors, western stores and Jiangdong ferries; two 223 CE scenes preserve the inherited assembly result but give those three neighboring offices non-player-controlled, sometimes costly reactions. Optional 232/234 CE local hearings revisit inherited military and civilian obligations. The protagonist can still choose personally to inspect posts or place bounded tasks with delegates while retaining responsibility. For disputed Red Cliffs or alternate succession branches, these are source-bounded military agents, not fabricated personal reports certifying historical leaders' deaths or ascensions. Existing aged, timed relationship, crown and household gates remain authoritative. The 223 office register may color all eight existing bridge texts but never forces an outcome or confers sovereign title. See WB-01K for precise states, scene IDs and continuity restrictions.

**QA:** Node syntax PASS. Chromium-state matrix **13,627 checks PASS across 486 variations, 0 failures**, testing intact source choice effects and exits, gated records, delayed responses, older saves, distinct resulting offices, conditional household language, date/age and eight bridge callbacks. Chromium real-click UI **15/15 at 390 and 1280 px**, no page exceptions or overflow; fixtures start at chapter checkpoints. Automated **source-legal 190 CE age-16 → lifetime** sequences additionally found a route to **each of the eight ending manuscript types** through actual offered choice effects and end-state arbitration with **no injected ending or crown flags**. Sovereignty was earned through existing 225–233 requirements; household-focused ending was observed but **not** with proven spouse/child. Source-legal traversal is not the same as an exhaustive browser UI playthrough, content coherence audit or native offline save test. `file://` and local network navigation can be blocked by Chromium policy here, and native-origin persistence remains UNVERIFIED. Next: strengthen marriage/children organic traversal and editorials; strengthen individual historical NPC agency when verified data and timeline permit; perform real-device file-origin save/import QA. No final-release claim.

---

### v0.4.73 — THE UNSETTLED SEALS / ALTERNATIVE SUCCESSION & CHRONOLOGICAL OBLIGATIONS (11 Nov 2026; IMPLEMENTED / TARGETED_QA_PASS)

**Active game:** 421 registered scenes (seven new 219–234 CE scenes), 25 People including 15 historical, eight unchanged original ending manuscripts and eight intact bridge-to-lifetime routes. Chapter X's already-earned 219 frontier order receives a two-scene local intelligence and witness follow-up. Chapter XI's original 220 dynastic policy still executes before a two-scene historical courier dispute, and the 223 river assembly can face an independent local accountability decision. Optional 232 and 234 hearings revisit the real social cost of earlier decisions, with one legitimate home option only for a spouse/home that already exists. 220, 221 and 223 historic-successor statements are **conditionally qualified** if the preceding Red Cliffs campaign was contested or yielded northern footholds; new text never asserts an unseen general's death, survival, exile or accession as certain. The protagonist's action is political and military at the authority/roads already earned, with competing officials allowed independent response. Both name/source GDD v1.28 authority and six adult romance rules unchanged; no new marriage, child, kingship or death created. Eight ending bridges receive distinct earned memories; ending algorithm and manuscripts untouched.

**QA and boundaries:** `node --check` PASS, **16,084** prepared-state branch and history conditions PASS (0 failures), **15 actual UI clicks at 390 px and 15 at 1280 px** PASS (0 page errors, no overflow), eight separately prepared eligible final-state fixtures reached their corresponding `bridge_E01`–`bridge_E08` and `lifetime_E01`–`lifetime_E08` IDs. These fixtures do **not** certify eight Prologue-origin legal ending paths. Localhost browser navigation blocked under Chromium's administrator policy (as previously observed on `file://`); native offline origin saving, export/import and physical mobile browser roundtrip **NOT VERIFIED**. Better historical faction-state modeling and organic earned-path QA remain open. Read WB-01J / WB-02 / WB-05 / WB-08 before next changes.

---

### v0.4.72 — TWO LIVING WITNESSES / GEOGRAPHICALLY BOUNDED DIRECT ENCOUNTERS (11 Nov 2026; IMPLEMENTED / TARGETED_QA_PASS)

**Active HTML:** 414 scene registrations, 25 People including 15 historical, and eight untouched original ending manuscripts. Five scenes extend **already present** 208 CE Guan Yu Hanjin / Lu Su lower-quay encounters and supply a conditional 210 CE hearing with participants under the protagonist's own local authority. Military reserves, ferry families, pilots, provisional rival-court terms and debt/appeals now have distinct player-resolved costs; Guan Yu and Lu Su retain separate institutional responsibilities. Actual Guan Yu meeting additionally qualifies for People discovery; Lu Su's previous discovery effect is preserved. Recurring X–XII records and eight different ending-bridge memories activate only after those lived encounters, not for old saves that skipped them. Original military authority, 233 earned kingdom, mortal choices, romance and family rules, old save keys and original game routes remain intact; no king, spouse, child or historical future outcome is automatically created.

**QA:** Node syntax PASS; 4,738 prepared-state assertions PASS / zero errors across 162 branch combinations; 15 real UI clicks per 390/1280px path PASS; original choices and registered endpoints retained. `file://` browser navigation explicitly blocked by environment, so actual offline save/reload/export/import **NOT verified**, nor full organic traversal to eight endings or comprehensive counterfactual 219–234 continuity. Approved GDD v1.28 design unchanged; this FAST implementation ledger and World Bible v1.64 are updated. Consult WB-01I / WB-03 / WB-05 / WB-08.

---

### v0.4.71 — THREE COURTS / ACCOUNTABILITY / CHAPTER XII CONTINUITY (11 Nov 2026; IMPLEMENTED / TARGETED_QA_PASS)

**Current file:** `ALL_UNDER_HEAVEN_v0.4.71_DEV_THREE_COURTS_ACCOUNTABILITY.html` (SHA-256 `f60860c294228e79166cc2ceb2e8d5ee59f70940af31ca0a6c268320c184c9a7`), **409 SCENES, 25 PEOPLE (15 historical), eight retained ending manuscripts**. The approved original Master GDD **v1.28 remains unchanged**; only this FAST working edition is updated. Seven added scenes allow an optional 232 CE hearing concerning separate western, northern and Jiangdong interests, with honest courier geography, prior 208–209 historical NPC memory, four substantive dispositions, and a 234 CE follow-up about resource costs. Personal frontline inspection stays possible for any authority level. Household consultation is available only after an earned principal-wife home; existing child records influence lived safety concerns but never create pregnancies or heirs automatically. Each of eight original end-bridge manuscripts gains a distinct conditional callback; no new ending or unearned crowning is implemented.

**Risk discipline:** Do not count named leaders in dispatches as physical NPC meetings, deaths or new People discoveries. Existing v0.4.65 regional sovereignty, v0.4.64 mortality, romance consent, 190 CE age-16 start and save schema remain intact. **Targeted QA:** `node --check` PASS; 1,781 state/choice assertions PASS; two actual Chromium click paths (390 and 1280 px, 15 clicks each) PASS with zero exceptions/overflow. Entire 190–234 chronological route, **all eight ending reachability**, native browser `file://` persistence and exhaustive mixed-household migration tests remain **UNVERIFIED**. Consult WB v1.63 WB-01H for conditional flags and QA boundaries.

---

### v0.4.70 — FIXED ADULT ROMANCE AGES; OPTIONAL BIOLOGICAL PARENTHOOD (11 Nov 2026; IMPLEMENTED / TARGETED_QA_PASS)

**Latest binding user correction:** The original six potential romance women use stable **non-aging fictional adult age assumptions** (Shen 29, Lin Yue 26, He Qing 28, Cai Zhen 27, Lan 25, Song Wan 30) so biological pregnancy is an available story possibility. This intentionally departs from calendar realism for these **six fictional romance candidates only**, without freezing the protagonist’s age (16 in 190 CE), historical characters, careers, geopolitical consequences or consent requirements. Treat this as a creative storytelling concession, **not a medical claim about fertility**. Do not change their listed ages per scene or secretly assign biological children to preexisting saves.

**Private adult romance:** Distinct optional in-person scenes for the wife or any previously consenting concubine at 225 and 230 CE. They may choose affectionate privacy with no family plan, explicitly discuss the possibility of a biological child, or remain close without a private evening. The user requests graphic sexual acts, but actual production remains **sensual, mature, metaphorical, non-graphic**, with explicit agency and fade-to-black. All events occur long after the protagonist is 18+. A birth is never an automatic consequence of the intimate scene, is offered at a separate 227/232 family event, and then the family continues to care for that child. The 229 voluntary fostering/kin-supported route is preserved. One principal wife, up to five consent-based concubines, unchanged six romance identities and eight ending manuscripts.

**Implemented scope and QA:** `ALL_UNDER_HEAVEN_v0.4.70_DEV_FIXED_ROMANCE_AGE_BIOLOGICAL_FAMILY.html`, SHA-256 `8c9e49f85c69c0f27620f46435a6c7a7ed512510d3ceb3b3ddeff84482d8ee28`, **402 SCENES / 25 PEOPLE (15 historical) / 8 manuscript endings**. 14 new scenes; targeted Node syntax test; 36 prepared-state wife-and-concubine cases; no-wife/minor/no-unearned-pregnancy checks; mobile/desktop live-click route and two-mother later-birth condition passed. End-to-end full story, real offline-save behavior, fixed-age narrative coherence review and all eight ending attainability remain **NOT VERIFIED**. See WB v1.62 WB-01G.

---

### v0.4.69 — LIVED FAMILY AND NON-AUTOMATIC PARENTHOOD (11 Nov 2026; IMPLEMENTED / TARGETED_QA_PASS)

**Binding direction maintained:** One principal wife and up to five **voluntarily accepting** concubines, chosen only from the six existing adult female romance candidates; each maintains personal boundaries, privacy and a distinguishable domestic life. The protagonist may remain single, child-free, a frontline fighter, a commander or a ruler. Household scenes must respect historical geography, economic obligations and what the protagonist can actually witness, and must not turn wives or concubines into collectible tokens or forced carers. Mature private intimacy remains consent-based, evocative and non-graphic.

**New implementation:** `ALL_UNDER_HEAVEN_v0.4.69_DEV_LIVED_HOUSEHOLD_FIRST_CHILD.html` SHA-256 `e60baf678fda24e745bc490eb511f46f5b56c7ddc57dd11d3dea5728dc7681d7` adds **eight voluntary Chapter XII family scenes** across 225, 227, 229, 230 and 232 CE. The wife and protagonist discuss parenthood together; **no child follows from marriage or hope alone**. Because candidate ages/birth dates are not adequately established for universal late-life pregnancy, the first earned option is to **take a displaced four-year-old into the household with surviving kin's consent**, or provide protection without changing the child's household. Actual chosen guardianship only then records a child born 225 and welcomed 229, with years tracked through 234 and child memory reflected in Character / ending bridges. This is fostering, **not** biological birth or automatic dynastic inheritance. All existing war, politics, historical NPCs, eight manuscript endings, and previous save key are intact. **388 registered SCENES, 25 PEOPLE, eight ending blocks.**

**QA scope:** Node inline JS syntax PASS, **46 Chromium prepared-state household scenarios** PASS (six wife variants, one 5-concubine household, no-wife/no-child cases), six actual mobile clicks and six actual desktop clicks PASS. **Not** complete lifetime/ending QA or verified native offline storage. See World Bible v1.61 WB-01F and actual HTML. Do not assert biological childbirth or automatic heir succession.

---

### Latest user correction — ONE principal wife; additional consenting CONCUBINES, not wives (11 Nov 2026; IMPLEMENTED in v0.4.68 with targeted QA)

**Binding:** The protagonist may marry **exactly zero or one principal wife** through the previously written 218/223 CE romance route. Among the **same six original female adult romance candidates**, any other eligible woman may freely choose the distinct status of **concubine** after a separate in-person household conversation. No second or coequal wife; **five is a possible maximum, NOT a goal or guarantee**. This newer user ruling explicitly supersedes the interrupted prototype idea of a second wife. Respect the principal wife’s informed agreement, each prospective concubine’s autonomous consent, adulthood, earned emotional ties, specific social obligations, privacy, property and ability to refuse. No automatic child, family bliss, sexual entitlement or extra character. Intimate prose may be adult, evocative and metaphorical with discreet fade-to-black, **not explicit graphic sexual acts**. Newly joined homemakers have individually authored professional transitions; the protagonist remains responsible for household security while free to govern and fight.

**Implementation:** `ALL_UNDER_HEAVEN_v0.4.68_DEV_ONE_WIFE_CONCUBINES.html`, SHA-256 `6f0a46c7d6f8383f65f026d777995ee22d02a8706935839359d7503e32731388`. **380 scenes; 25 People; eight existing ending manuscripts**, one unchanged wife field `auh66_spouse`, new `auh68_concubines` array (max five), separate voluntary covenant dates and household roles. Six windows 223/225/227/229/230/232 CE are gated by wife, earned romance and relationship choices; at most one new concubine per window. Character/People and ending bridges distinguish wife from concubines. Older saves remain intact and are not silently reassigned. **Not** a fully simulated Han legal hierarchy or complete household novel; ongoing historical validation and full route QA remain necessary.

**QA:** Node JS check PASS; 30 distinct wife/concubine pairings and one wife + five sequentially gated concubines PASS in Chromium model state tests; negative tests for child age, prior friend-only path, absent relationship, absent wife, lack of household care, existing-save compatibility, additional sixth, and eight ending registrations PASS. Actual Chromium 390/1280 px UI trails each 8 clicks PASS. Native offline persistent saves and organic Prologue-to-multiple-household/ending path remain **NOT VERIFIED**. See World Bible v1.60 WB-01E for exact evidence.

---

### Latest user decision — married wife focuses on homemaking (11 Nov 2026; IMPLEMENTED in v0.4.67 with targeted QA)

**Binding, superseding v0.4.66 for NEW marital arrangements:** After a reciprocally chosen marriage, the wife **withdraws from outside paid/public work** to focus on the family home and, if later present, care for children. This preference should be authored through credible individual negotiation and professional handover, not an unexplained personality erasure or a husband's unilateral decree. The spouse has her own voice, memory, property/belongings and power to say yes/no to the marriage; she must not be depicted as a professional employee after leaving that work. Unmarried romance candidates continue independent professions. Marriage alone never generates pregnancy, children, land, a public office or exclusive claim over a spouse's body. The husband remains accountable for provisioning, security and time, and may retain his war/political career and frontline combat choices.

**Implementation:** `ALL_UNDER_HEAVEN_v0.4.67_DEV_HOUSEHOLD_LIFE_AFTER_MARRIAGE.html`, **338 registered scenes, 25 People, eight ending manuscripts**. Six revised distinct marriage agreements and rites, six 218 household-transition scenes, six 223 equivalents with correct chapter markers, 219 and 224 in-person household visits, two optional older-save renegotiations, current marriage role displayed in Character/People, 222/230 in-person married reunion prose rewritten so wife is found at home, not back at work. Flags `auh67_home_role='homemaker'` / `auh66_household='wife_at_home'` for new weddings; family intent is a discussion, not a child. **Old v0.4.66 already-married saves keep earlier outside-work vows until an explicit in-game mutual change**, preserving previous save history. Existing save key/schema, chapter/ending IDs and main campaigns unchanged.

**QA:** Node inline JS syntax PASS; 12 conditional 218/223 wedding routes PASS; older pact and alternative child-plan/no-marriage flags checked, 224 and 230 conditional prose and all eight ending manuscript identifiers preserved; three actual Chromium 390px / 1280px UI trails (218 Lin Yue twice, 223 He Qing once), five clicks apiece, reached original chapter return with valid state and no page error or overflow. No complete organic six-romance life route or native `file://` persistence certified. See World Bible **v1.59 WB-01D** for current truth.

### Previous implementation note — v0.4.66 (11 Nov 2026; SUPERSEDED HOME ROLE FOR NEW MARRIAGES)


**NEW BINDING USER DECISION — MARRIAGE BEFORE THE FINAL CHAPTER:** Six established romance candidates now have individually written, mutually consensual, non-graphic wedding opportunities on **218 CE / Chapter X** for sufficiently developed relationships and **223 CE / Chapter XI** for later-earned commitments, while the main military, political and domestic story continues. **Eight authored scenes plus eight Chapter XI scene aliases**; 322 registered scenes / 25 People; no altered ending IDs, age of 16 at start, NPC roster or save key. A meeting and earned prior history are prerequisites; no automatic marriage from a single romantic choice or age/office. Deferring and declining marriage do not obstruct the campaign. The spouse retains independent work, choices and property obligations, and marriage alone never grants children, titles or an estate. A one-spouse protection gate prevents false claims of multi-party consent; optional plural partnership remains approved design but not comprehensively implemented.

**Targeted QA:** JS syntax PASS; 36 marriage/defer/decline state routes PASS; seven negative gates PASS; real Chromium UI four clicks each for 218 marriage on 390px mobile and 223 marriage on 1280px desktop PASS with no errors/overflow; character overview displays spouse; ten pre-existing kingdom scenarios regressed PASS. Full six-route organic playthroughs, native offline save persistence, married lifetime arcs and all eight endings are still unverified. See WB v1.58 WB-01C for evidence boundaries.

### Previous implementation note — v0.4.65 (11 Nov 2026)

**IMPLEMENTED with DEEP-targeted QA:** Ten connected scenes spanning 225–233 CE with 234 callbacks now allow the protagonist to **earn a regional sovereign crown**, not an empire. Preconditions require actual earlier-independent territorial footing, a 225 assembly petition, a 229 territorial success (military or credible local treaty), 232 consent and public charter, a 233 secured border, and the protagonist's explicit acceptance of a witnessed title. **E01** becomes reachable from qualifying tested midgame state; neither a local district nor a high ambition score grants kingship. Failed expansion, forced claims, voluntary rejection and later abdication do not silently grant E01. Crowned character rank and status show the actual title; E08 remains available only after a causal death event and takes priority. Prior war options, six optional adult romances, 230 direct meetings, NPC historical casting, age 16 start, eight ending manuscripts and save schema remain unchanged. **306 scenes, 25 registered People (15 historical).**

**QA:** JS syntax PASS; 10 deliberately varied 225–234 conditional route scenarios PASS (see WB v1.57 WB-01B); mobile and desktop Chromium actual UI-click routes (25 interactions each) PASS; failure/abdication/legacy no-op tests PASS. Not a whole-game 190-to-234 route proof, not a claim of completed alternate-geopolitical world simulation or native offline file persistence. An imperial throne over all China is a **separate unimplemented undertaking** from this smaller witnessed kingdom.

### Previous implementation note — v0.4.64 (11 Nov 2026)

**Implemented, tested within a bounded Chapter XII checkpoint:** Seven new original 234 CE last-council scenes, direct military confrontation even when already a ruler/commander, witnessed governance and household stewardship choices, and a mortal last stand with explicit consequence. **Seven non-crown thematic endings** can now be selected through evidence-conditioned logic and were each tested using controlled valid-state fixtures; **eight existing ending manuscripts remain in source**. The crowned E01 endpoint remains intentionally gated until a credible actual sovereignty and ratification sequence is written, not given away for ambition points or a small charter. Mortality E08 now requires an actual death event instead of risk-score ranking. New age/rank-sensitive paragraphs appear in five existing scenes. 296 scenes; 25 People, 15 historical. No changes to base game save key, existing romance opportunities, registered historical NPCs, or existing bridge/ending manuscripts.

**QA truth:** Inline JS parser PASS; six bounded 234 campaign fixture families with branch/`validSave` checks PASS; seven ending-category artificial-state fixtures (E02–E08) plus blocked unearned-crown case PASS; 390 px Chromium actual-click fatal route PASS; past-age fixture 69 rendered correctly. Complete organic early-to-ending pathways, file-origin storage/export and E01 earned-sovereignty route **NOT VERIFIED / NOT IMPLEMENTED** as described above; see WB v1.56 WB-01A.

## GDD-00 — READ FIRST: ACTIVE RULES AND AI NAVIGATION

### Authority and truth hierarchy
1. The latest explicit user decision overrides a conflicting older instruction. **This optimized document does not independently amend approved design.** The unmodified v1.28 archive supplies exact source wording when needed; where a later user ruling exists, such as occasional birthdays or the 4–8-scene batch preference, follow the newer ruling recorded in World Bible v1.54 / conversation.
2. **Master GDD v1.28 = binding design.** **World Bible v1.61 = current entities, chronology, chapter cards, relationships, research status, risks and QA checkpoint.** **Actual HTML v0.4.69 = current observed implementation**, not proof that every design rule is implemented. Do not mistake a proposed scene/character/reward for live gameplay.
3. Old GDD headers, build hashes, handoff instructions, source indexes and QA results referring to v0.4.7–v0.4.24 and WB v1.1–v1.26 are **ARCHIVE_ONLY**, regardless of whether their paragraph says “CURRENT” or “LATEST”. Use this post-v0.4.79 design addendum plus World Bible WB-01Q for new binding design, and WB-01P for v0.4.79 implementation evidence. This fast-edition handoff was refreshed after v0.4.62; the latest user direction clarifies romance presentation without changing the frozen ending/chapter scope.
4. Never claim a feature exists solely because it is designed, or a branch works because a static choice appears in HTML. Use `LOCKED_DESIGN`, `IMPLEMENTED`, `TARGETED_QA_PASS`, `PARTIAL`, `PROPOSED`, `NOT_VERIFIED` or `ARCHIVE_ONLY` explicitly.
5. **Exactly three routine active files:** this GDD FAST reading edition, World Bible v1.73 FAST, and the latest tested HTML (currently v0.4.79). Archive files are source preservation, not routine input. When publishing a newer build or Bible, update the small status pointer first; do not append another chronological “latest” block.

### Read-on-demand navigation
| Work item | Read here | Read in World Bible | Code scope |
|---|---|---|---|
| Any new work / cross-chat handoff | GDD-00, GDD-01 | WB-00, WB-01 | Verify active HTML and hash |
| Scene prose, war, politics | GDD-02, GDD-04 | WB-02, WB-05 specific chapter, WB-07 | Affected scene + neighboring entry/exit |
| Historical NPC / title / alternative history | GDD-04, GDD-05, GDD-07 | WB-02, WB-03, WB-07, WB-08 | Encounter/office/knowledge flags |
| Romance, friendship, social scene | GDD-02, GDD-05, GDD-06 | WB-04, relevant WB-05/06 | Choices, NPC discovery, state callbacks |
| Estate, possessions, household | GDD-06, GDD-08 | WB-06, relevant chapter card | Ownership, inventory and economic consequences |
| Interface, character stats, portraits | GDD-03, GDD-09 | WB-03, WB-08 | Relevant UI or asset only |
| Calendar, save, state, endpoints | GDD-03, GDD-04, GDD-09–11 | WB-01, WB-02, WB-08 | DEEP tests: clock, import/export, legal fixtures |
| New chapter batch / production checkpoint | GDD-10–11 | WB-05 specific chapter, WB-08 | Current batch + flagged downstream |
| Verbatim historical decision / complete old QA | Original v1.28 archive | World Bible v1.35 archive | Consult only if necessary |

**Fast rule:** Read headings and index first, then the **one or two relevant GDD sections**, the relevant World Bible cards and exact scene spans. Never load all three full files merely to fix one choice. Cite exact versions when reporting QA; no automatic Prologue replay for every revision.

## GDD-01 — ACTIVE PROJECT CONTRACT AND IMPLEMENTATION TRUTH

### Non-negotiable design scope (LOCKED_DESIGN)
- **One Lifetime:** prologue, **12 chapters**, **8 distinct main endings** and contextual lifetime epilogues. Starting year **190 CE**; historical milestone planning through **224–234+**, no forced death or survival at a fixed year, no playable heir/successor.
- **The protagonist is the central actor and possible history-maker, never a permanent assistant to famous NPCs.** *Romance of the Three Kingdoms* and the films *Red Cliff* I–II provide literary/epic inspiration and historical characters, **not immutable story outcomes, character hierarchies or a canon the player must preserve**. Verifiable history supplies the starting world, dates and institutions; earned protagonist decisions, NPC initiatives and alternative outcomes take precedence once the story diverges.
- **Six substantive possible adult-female romances:** **S0 Shen Lian + R1–R5 = six candidates total**: Shen plus five **OTHER** independent adult women. These are optional opportunities, not collectible guaranteed partners. **3–4 meaningful lifelong friendship arcs** as a planning target. Additional adult-venue supporting women are **separate** from the six romance candidates.
- **100–120 historical figures = campaign casting pool, not mandatory 100–120 detailed biographies or portrait purchases**. Research and register significant actors just in time; respect their independence, presence, chronology, sources and local knowledge.
- Four shared, non-exclusive service/story lanes: **field command, civic administration, diplomacy/politics, independent/private**. These are editorial perspectives, *not* new class menus or exposed stats. Branch/rejoin with persistent world and relationship consequences rather than writing four separate novels.
- Story-first relationships, mature **non-graphic consensual** adult intimacy, meaningful social life, nuanced war/politics, attainable earned recognition, optional plural-partner households, event-based property/estate decisions. No sprawling new subsystem before core story/QA. The player may choose solitude, no romance, civilian life or refusing office without being punished by the design.
- Offline-first single self-contained HTML release; possible Android WebView/APK later. Mobile reading experience first, desktop also usable. Original portrait assets as needed, all disclosure-gated.

### Binding protagonist-primacy amendment — 10 November 2026 (newer user authority)
**The campaign belongs to the player character, not to the novel's heroes.** Historical persons are major supporting, allied or opposing *characters in the protagonist's story*; none has narrative ownership over a famous battle, political outcome, or crown. The protagonist may independently lead armies, invent a decisive strategy, prevent or cause a historical victory, take rulership, defy Liu Bei/Cao Cao/Sun Quan, forge different coalitions, or live privately with consequences. All routes must allow **player-led action** matching earned ability, opportunity, legitimacy, followers, travel, and information. The protagonist may be better than famous historical heroes. Historical NPCs retain realistic interests, competence and ability to resist; their *automatic historical wins, plot armor and superiority are not protected*.

**All twelve chapter rule:** Each must contain a consequential central action controlled by the protagonist (command, diplomacy, governance, independent initiative, family/community protection) and track the resulting world reaction. A player may decline office, romance or war without being relegated to scenery. Historical events and chapter chronology are *opening conditions*, not mandatory replay. Red Cliffs must offer command of a decisive engagement and lasting recognition/complications; do not steal that leadership back with a later retcon. **Implementation in v0.4.52:** 3 new command/battle/result scenes in Chapter VIII, revised subsidiary envoy-council prose, revised text in nine major decision scenes, and conditional long-range memories in IX–XII; **not yet** a complete all-chapter structural rewrite, war outcome matrix or verified independent-sovereignty ending.

### Leadership does not prohibit personal combat — 11 November 2026 (newer user decision, binding ALL chapters)
**Military, political and imperial status must not automatically force a player into remote command.** An earned warlord, governor, independent ruler, monarch, commander, or claimant retains the option to fight in person, join the frontline, challenge a credible opposing officer, or lead a dangerous breakthrough where geography, age, health, presence and military context permit. Equally legitimate alternatives include delegating battlefield command, commanding from a protected position, protecting civilians, and refusing war. **No permanent class/office lock** removes personal combat. Personal participation has meaningful tactical effects and risk of injury, defeat, capture or loss of followers; high rank is neither invulnerability nor a mandatory punishment. Named historical figures need not appear or accept a duel without plausible location and motive. The player's personal courage and wider army leadership should both be recognized and remembered.

**Implemented locally in v0.4.61:** Three conditional Chapter XI 222 CE scenes after choosing to lead a strike, offering three physically present battlefield roles, two tactical decisions, distinct aftermath and Chapter XII memory. This proves one case, **not** full coverage across all chapters; cross-chapter leader/frontline flexibility remains an authoring/QA obligation.

### Fixed age 16 and age/rank-sensitive NPC behavior — 11 November 2026 (newer user decision, ALL chapters)
**LOCKED_DESIGN:** New protagonists begin at **16 in 190 CE**; remove the starting-age picker. Do not change existing valid older saves to age 16 retroactively; exported saves keep their historical starting age and current progress, while Restart begins a new age-16 life. Ages approximate from fictional elapsed years (17 in 191, 19 in 193, 34 in 208, 46 in 220, 60 in 234), no invented exact birthday. The protagonist has **no automatic commission at sixteen**. How historical and original NPCs address, invite, train, test, respect or oppose the character depends on age, witnessed competence, **actual office/rank**, troops, factional ties and local power. Neither celebrity nor seniority automatically prevents an earned protagonist from giving orders later. Distinguish military command, civic leadership, provisional recognition and formal sovereign title; do not award titles on hidden ambition points. High status does not preclude front-line fighting. Under-18 relationships may be formative friendship but not adult romantic intimacy or sexual contact; age-18+ mutual-consent restrictions continue. **v0.4.63 IMPLEMENTED / TARGETED_QA_PASS:** Fixed UI age 16; 14 adapted existing scene interactions/early Shen choices; dynamic character Position/Command/Affiliation/Basis of Authority from genuine flags; first-known NPC positions not falsely presented as permanent; old-save ages unchanged. Node tests and new-game desktop/mobile form UI passed. This is **PARTIAL** coverage of the broader all-chapter social protocol; full organic scene/ending and native save QA not completed. See World Bible v1.55 WB-01 / WB-08.

### Current implementation snapshot (11 Nov 2026; consult WB-01 for exact evidence)

**Active override:** v0.4.75 / 433 registered scenes, 25 People, eight preserved ending manuscripts. Historical lower-version feature counts in this FAST file are dated implementation evidence; WB v1.67 and current HTML take precedence for code facts.

- **HTML v0.4.64, DEVELOPMENT DRAFT**, not a complete, polished or eight-ending verified game. Opening 190 CE; **VI 198**, **VII 200**, **XII 224**; `storyClock` tracks **year precision**, birth month/day unknown and age across time skips approximate. Existing legacy-save age is protected on migration. **Do not repeat older GDD assertion that VI is still 197 or XII still 222.**
- World Bible v1.53 records **25 People IDs: 15 historical + 10 original including six possible romance candidates**; IDs and presence in registry are **not proof of actual player discovery**. Full six lifetime romance paths and all historical profiles are not certified.
- Later chapter draft scene coverage and eight thematic ending blocks exist; **the original six 200 CE Chapter VII scenes now continue through seven new 201–207 first-pass scenes; this remains incomplete relative to the full novel-scale quality target**. Ending reachability remains unverified.
- v0.4.44 calendar-focused QA recorded 18/18 calendar/state checks and sampled Chapter V branches into VI/VII; real file-origin persistence/native downloads and comprehensive alternate routes remain unverified. Read WB-01/WB-08 for caveats; do not inflate past test claims.
- **Birthdays — NEWER USER DECISION, 10 Nov 2026:** Celebrate only at **occasional meaningful narrative moments**, never annually by default. Chronological age continues; do not invent dates of birth. No exact-date birthday subsystem is required now. This is a scoped clarification, not a claim of code implementation.
- **v0.4.45 prior Chapter VII batch:** `ch07_07`–`ch07_13` give Chapter VII a scene for each year 201–207, with 3 additional strategic decisions; see WB-01/WB-05 for source/event map and targeted browser checks. **v0.4.46:** Chapter VI adds four 198–199 scenes and two consequential choice groups, with indirect historical contacts and follow-through into Chapters VII and VIII. Chapter VI decision labels/flags and old save schema remain intact. No engine, save-key, existing 20 choice-group or ending-block edits. Choice consequences also appear in Chapter VIII and IX without changing those chapters’ choice effects. **v0.4.47:** Cai Zhen R3 gains an opt-in court-family intrigue interlude with one new conditional scene and three choices; see WB-04 and the live HTML. No seventh romance and no change to the v1.28 design contract. **v0.4.48:** Four additional gated R3 scenes in Chapter VIII–IX with two consequential civic/personal choices and one delayed Chapter X reply; original six romance identities and historical-family boundaries preserved. See WB-04; these are not completed romance endings.
- **v0.4.49–v0.4.50:** six romance windows across six women (two scenes per woman), with opt-in private tenderness, opt-out choices and humor; original ending blocks unchanged and whole-life route completion not certified. See WB-04/WB-08 for verified scope.  **v0.4.51:** two historical NPCs introduced through realistic 208 river-diplomacy source anchors (Zhuge Liang and Lu Su), five witness-ledger scenes and 210 callbacks; source framing is reviewed, personal meeting is fictional, with targeted discovery/save/18-route/UI checks. See WB-03/WB-08. **Production batch size — NEWER USER DECISION, 10 Nov 2026:** Favor **4–8 connected scenes when coherent**, with risk-tiered QA. The original §10A’s “2–4 scenes” remains in the archived source as an older operating preference, not the current default; do not pad a batch to reach a quota.

**v0.4.52 implementation milestone:** Red Cliffs command choices and their consequences are now protagonist-led in Chapter VIII; Chapter III–XII decision framing was selectively revised. Full player-led history outcomes across twelve chapters, late canonical assumptions and all eight ending gates still require separate authoring and DEEP QA. See WB-01, WB-05 and WB-08.

**v0.4.53 implementation checkpoint (10 Nov 2026):** Chapter IX now has five new protagonist-led scenes and three decisions across 211–213 CE to establish local military, civilian or independent authority, confront a rival garrison, and choose political settlement. The year-precision clock advances 210→211→212→213→214 without losing the original Chapter IX effects. Six local outcomes produce conditional Chapter X–XII callbacks, and an earned independent charter unlocks a possible league proposal in Chapter XI. These are local political changes, not an implemented independent kingdom, imperial title, or complete alternative dynastic history; eight ending gates remain unverified and unchanged. See World Bible WB-01/05/08. Older saves after IX do not replay the new route. Original Master GDD source version remains **v1.28**.

**v0.4.54 Red Cliffs expansion (10 Nov 2026):** Chapter VIII now adds **21 original prose scenes**, major protagonist-led campaign decisions and four contingent war results; historical Zhou Yu and Huang Gai become encounter-gated People records. The existing coalition and romance routes remain in place. Three scene phases connect earned command → campaign councils/shore reconnaissance/coalition dispute → deception/wind/fire assault → battlefield choices and 209 settlement. Results echo in Chapters IX–XII; no automatic historical victory. This is a large **authored climax expansion with targeted QA**, *not* a full dynamic geography/province engine or all-eight-ending reachability proof. **Keep 12 chapters and eight endings**. See World Bible v1.46 WB-01/WB-05/WB-08. No changes to original approved GDD source v1.28.


**v0.4.62 — THE YEARS THAT REMAIN (11 November 2026; IMPLEMENTED / TARGETED_QA_PASS):** Chapter XII gains fifteen new scenes over 225–234 CE: earned-only independent/civic/compact authority, 228 field/treaty/civilian mission, leadership-compatible direct shield fighting or captain confrontation (also rear command), meaningful tactical consequences and 232 council policy before the old closing scenes. Six individual female romance routes offer a **single optional actual 230 face-to-face visit** based on previously earned relationship, distance and consent, with an immediate response (closer/friendship/parting) and no magic travel or automatic property/marriage. Historical Zhuge Liang reference is contextual and optional personal consultation is gated by prior meeting/western alignment. Older saves already beyond `ch12_01` naturally bypass this extension. QA: 153 game VM political/war combinations, 18 candidate-stance variants, declined/underage/independent negative checks; 17 mobile and 15 desktop real UI clicks passed. 289 SCENES, 25 People, six romance candidates, eight ending drafts, same save key. Full ending feasibility, local file persistence and organic chapter-to-chapter romance histories remain **NOT VERIFIED**. See WB-01/05/08.

**v0.4.61 — A RULER TAKES THE FIELD (11 Nov 2026; IMPLEMENTED / TARGETED_QA_PASS):** Adds 3 scenes in the 222 Chapter XI raid route; political allegiance/local authority cannot block fighting personally. The protagonist can meet the rival vanguard from the shield line, confront an opposing captain, or issue frontline orders under fire, then hold to evacuate wounded or risk a costly counterstroke. Six tactical variants × three existing political postures tested (18); both non-raid options unchanged, 390/1280px Chromium click routes PASS (6 clicks each), no JavaScript exceptions/overflow. Existing save key, NPC roster, six romance routes, 8 ending manuscripts unchanged. **Not** evidence that rulers can duel personally in every chapter yet or that full ending feasibility is tested. See WB-01/05/08.

**v0.4.60 — THE CONTESTED MANDATE (11 Nov 2026; IMPLEMENTED / TARGETED QA):** Adds 15 Chapter XI scenes, nine linked political-war beats (220–223 CE) and six distinct, opt-in, face-to-face romance meetings at a plausible neutral exchange in 222. Lu Xun joins the historical People registry only if actually met in a fictional guarded parley. Political choices alter local command, civilian oversight, contested sovereignty and successor diplomacy; 223 results echo into Chapter XII, but **no imperial sovereignty is awarded by score**. The 220 Wei succession, 221 western Han claim, 222 Yiling confrontation and 223 Liu Bei succession are researched baseline anchors, not immutable history after major protagonist divergence. Original XI choice effects, old-save format, six romance identities and eight ending drafts preserved. Targeted QA: parser PASS, 243 VM politics combinations plus six romance cases and consent/age/meeting checks, 27 real clicks at 390px and 25 at 1280px through Chromium `set_content`, no JS errors/overflow. Native file-origin persistence and comprehensive eight-ending reachability remain unverified; see WB-01/WB-08. **All source GDD v1.28 binding principles remain unchanged.**

**v0.4.59 — IN-PERSON ROMANCE FIRST (11 November 2026; newer user decision / IMPLEMENTED with targeted QA):** Romantic continuity should rely on **real meetings, shared tasks, spoken disagreement, humor, freely chosen affection and emotional aftermath**, not repeated exchanges of letters. 217 Chapter X now supports a plausible seasonal river market visit, eight new authored scenes (two setup/selection + six distinct job-grounded encounters for eligible Shen Lian, Lin Yue, He Qing, Cai Zhen, Lan or Song Wan), **at most one personal meeting in the visit**, or skip and remain single. The 218 memory recognizes the actual interaction; each has closeness/friendship/parting, with relationship consent and independent livelihoods intact. Cai Zhen's meeting additionally requires credible prior court status/approvals and an escorted, neutral household-exchange reason, not sudden presence in the camp. Ordinary 217–218 private correspondence is **superseded on new routes**, but the old scene IDs remain accessible for **loaded v0.4.58 saves mid-letter**. v0.4.58 historical/political campaign and five outcomes unchanged, old chapter choices and save key unchanged. **256 scenes; 24 People (14 historical); 8 ending manuscripts**. STANDARD targeted QA: 127 valid scene-fixture paths, eight new scene IDs reached, six relationship candidates with three emotional outcomes, age/refusal/unknown/old-save gates, five war results, correct age/year, Node syntax and 51 actual UI clicks *per viewport* at 390px and 1280px, no errors/overflow. This is NOT completion of lifetime romances, legal full-start route audit or native disk-save QA; see World Bible v1.51 WB-01/WB-04/WB-08. Approved source GDD stays v1.28.

**v0.4.58 — Western Frontier / Living Ties (11 November 2026; IMPLEMENTED / TARGETED_QA_PASS):** Eight new linked Chapter X scenes cover 215–219, giving the protagonist further command over frontier commitments, actual armed/witnessed/civilian tactics and a consequential 219 border order conditioned on Red Cliffs' different results; **five bounded late-219 local outcomes**, not automatic control of Jing/Yi or imperial authority. Historical actors Liu Bei, Guan Yu, Zhuge Liang, Zhang Fei and Zhao Yun influence the story through geographically plausible messengers, offices and reports; no false discovery/automatic private meetings. In parallel, the player's established adult relationships can yield one of six distinctive optional, consent-respecting 217–218 letter exchanges, or none; six romance lifetime routes remain partial. Original ch10_05 effect, ch10_06, existing Song Wan/Lan/Cai Zhen windows, save format, eight ending records and 24 People unchanged. **248 total scene IDs; STANDARD QA:** 114 fixture traversals (108 political/military combinations and six correspondence fixtures), five outcome states, correct 214→219 clock/age; 15 real mobile UI clicks and 15 desktop, no errors/overflow, earlier three romance detours verified. Not full start-to-ending or browser persistence QA; see WB v1.50. Source GDD remains v1.28.

**v0.4.57 — The Three Seals (11 November 2026; IMPLEMENTED / TARGETED_QA_PASS):** Nine Chapter IX scenes in 210 CE turn four possible Red Cliffs outcomes into distinct postwar negotiations with envoys from Liu Bei's circle, Jiangdong, northern authorities and river households. The protagonist chooses how to report the battle, seeks his own military/civic/independent settlement or a limited northern ceasefire, and commands the defended crossing, negotiation or evacuation. Eight local political resolutions, remembered in Chapters IX–XII, are conditional rather than royal titles or canonical guarantees. Old Chapter IX choice effects, six romance candidates, fourteen historical People slots, eight main ending records and offline save schema remain. **240 scenes, 24 People**. STANDARD targeted QA: 144 210 CE fixture combinations pass body/effects/save validation, eight settlement result types; 15 real UI clicks each on mobile/desktop, no errors/overflow. Not a legal 190–234 full route test, province-level political engine, native `file://` persistence, or complete ending QA; see World Bible v1.49 WB-01/05/08. Underlying GDD v1.28 unchanged.

**v0.4.56 — Four Voices at Red Cliffs (10 November 2026):** Eight new Chapter VIII scenes deepen Liu Bei, Zhang Fei, Zhao Yun and Zhuge Liang as independently motivated later-Shu-associated officers around Jing’s collapse, Changban, the 208 river war and 209 settlement. The protagonist negotiates direct political/military decisions, may cooperate or diverge, and retains primacy. Tactical decisions feed an earned bounded leverage modifier and conditional Chapter IX–XI memories. All four figures were already registered; People roster remains 24 (14 historical). New scene registry 231. Targeted QA 243 chapter-level state/choice permutations, 12 real UI interactions on each of 390px and 1280px, JavaScript syntax and save-validity PASS; native file persistence, complete chapter origin paths and all 8 ending reachability UNVERIFIED. Keep 12 chapters, eight ending drafts and six romance candidates. In 208 this is Liu Bei’s circle, **not yet the Shu Han state**. See World Bible v1.48 WB-01/03/08. No amendment to underlying GDD v1.28.

**v0.4.55 — historical Shu-circle buildup (10 November 2026):** Fourteen new Chapter VIII opening scenes now run from the late-Jing crisis through Liu Bei's retreat, protagonist-led Changban decisions, the Hanjin boat crossing and Liu Qi's Jiangxia political compact, before the v0.4.54 Red Cliffs climax. Xu Shu and Liu Qi join the historical People roster with encounter-gated discovery; Liu Bei, Guan Yu, Zhang Fei, Zhao Yun, Zhuge Liang, Mi Zhu, Sun Qian and Jian Yong have contextual roles. The state of Shu **does not exist yet in 208 CE**; these are later Shu-associated figures and the independent Liu Qi of Jing. Four three-way groups plus Xu Shu's three responses give 243 sampled combinations with valid save/state; 16 actual mobile UI steps and the 208→209 war transition tested. First-pass historical fiction, not finished whole-game QA. The protagonist commands troops and can change the course of war; historical generals retain independent agency. Eight ending drafts and six romance candidates unchanged. See World Bible v1.47 WB-03, WB-05 and WB-08. No amendment to the approved full source GDD v1.28.

## GDD-02 — EDITORIAL NORTH STAR / FIVE LITERARY PILLARS

**LOCKED standard:** The player should experience a novel, not a sequence of short menu prompts. The 12 chapter structure does not justify thin prose or constant exposition. Target total authored text (including alternatives) **~180,000–240,000 words** / **15,000–20,000 per chapter as a planning band, never a padding quota**. One playthrough naturally reads fewer words. Pace for drama and meaningful silence; do not force every chapter to include each pillar equally.

1. **Epic-novel prose:** Original literary English, textured environment, memorable dialogue and voices, gradual revelation, uncertainty, morally complicated decision-making, real stakes, textured aftermath. Vary rhythm; avoid repetitive recaps, appearance inventories, redundant emotional summaries, purple padding, technical page labels and visible game mechanics in prose.
2. **Emotionally credible romance:** Build anticipation, chemistry, tenderness, joy, vulnerability, silence, playful humor and heartbreak from shared history, gestures, conversation, distance, uncertain interest and reciprocity. Characters may say no, initiate, have their own ambitions or choose friendship. Positive romance deserves as much weight as tragedy. No instant devotion for a single favor or hidden affinity score as a substitute for writing.
3. **Tense, believable war and politics:** Battles obey geography, formations, weather, information, command limits, morale, exhausted people, supplies, physical wounds, casualties and aftermath. Political maneuvering includes legitimacy, distrust, negotiation, patronage, intelligence delays, leverage and institutional cost. Historical figures retain credible intelligence, resources and independent agency, but **they can be outmaneuvered, surpassed, allied with or defeated by the protagonist**. The player does not gain effortless victory from stats or a famous meeting; they can earn true strategic command and reshape a whole campaign.
4. **Mature but non-graphic consensual intimacy:** All involved **18+**, with informed free consent. Write charged atmosphere, desire, gestures, tenderness, and emotional/social aftermath without pornographic descriptions of anatomy/sexual acts; use discreet transition/fade-to-black. No sexual access as reward for command, money, coercion or rescue.
5. **Human-scale life and situational comedy:** Meals, chores, friends teasing each other, warmth, festivals, letters, homes, children when applicable, reunions and celebrations. Humor should follow character and context, not modern slang or constant jokes. Avoid making each joyful event immediately turn tragic; let genuinely earned happiness land.

**Scene gate:** Is this continuous original fiction? Are location, era, NPC knowledge and agency consistent? Does choice produce traceable future consequence? Does romance earn reciprocity and consent? Does war/politics earn its outcome? Does the scene contribute rhythm, including relief or joy? Review at targeted scene level; assess full-act pacing at milestones.

## GDD-03 — PROTAGONIST, TIME, LIFE AND MORTALITY

- **Latest binding age decision (11 Nov 2026) overrides v1.28's adult/custom starting-age language:** every **new** protagonist is an unaffiliated **male, age 16 in 190 CE**, with player-chosen name and two chosen talents, initially close to the milieu that may lead toward Liu Bei's circle; later political independence and other careers are possible. This wording mirrors the v1.28 design; do not infer a new gender mechanic from older drafts without verifying the actual build and obtaining a new ruling. Player's words and choices—not a preassigned personality—define character.
- **Six approved abilities:** Leadership, Prowess, Intellect, Stewardship, Charisma, Intrigue. **Exceptional Prodigy**: select **two distinct 92/100** attributes; remaining **four at 83/100**. No XP grind, perk tree or level ladder. Skills are not an additional redundant exposed menu. Growth comes from credible milestones, not repeated stat purchases.
- NPCs cannot see hidden stats; **Natural Revelation** means competence becomes known only through witnessed acts and reports. Reputation, authority, rank and trust remain distinct from raw ability. Even exceptional talent faces timing, authority, unfamiliar terrain, conflicting aims and real human cost.
- Event-based story clock: advances minutes through years only when scenes require, not realtime. A chapter is not one year. Respect age, known injuries, recovery, households, marriage, kinship, personal possessions, responsibilities and changed political control at time skips. Unknown birth date remains unknown; occasional birthday events only when narratively justified and the known timing allows.
- Risk can be fatal when fairly signaled and causally earned; no arbitrary death, compulsory death age, invulnerable protagonist or protagonist control of children after death. End a lifetime with coherent epilogue even when the player dies earlier than the later historical chapters.

### Ratified chapter-year envelopes (DESIGN; verify actual route/year separately)
| Segment | Approved CE years | Key instruction |
|---|---|---|
| Prologue + I | 190 | Opening and first stakes |
| II | 190–191 | Elapsed time and early consequences |
| III | 191–192 | Early loyalties and constraints |
| IV | 193–195 | Rival warlords and civilian life |
| V | 196–197 | Court legitimacy and political shifts |
| VI | **198–199** | Responsible command and regional changes |
| VII | **200–207** | Several dated arcs and years of rising stakes |
| VIII | 208–209 | Large-scale conflict/alliances |
| IX | 210–213 | Political, civic and household consolidation |
| X | 214–219 | Long-term war and personal consequences |
| XI | 220–223 | Political reconfiguration, survival/office gates |
| XII | 224–234+ | Flexible lifetime resolution, no mandated survival |
| Epilogue | Actual life | Depends on protagonist's earned life, not one fixed year |

These are planning envelopes, not forced battle quotas, scene timestamps or guarantees that a celebrity historical NPC is physically present. Check in-game source and World Bible history map before placing an actor. Where canonical prerequisites fail, adapt later scenes; do not force later canonical events. Test clock-save migration separately from prose.

## GDD-04 — HISTORICAL NPC CANON, GEOGRAPHY, KNOWLEDGE AND DIVERGENCE (LOCKED)

**Higher-priority user correction (10 Nov 2026):** Use this section for historical plausibility at the beginning of each route, NOT a reason to reserve key victories and leadership for historical men. When player agency and literary-history replication conflict, allow the protagonist to cause plausible divergence, recompute faction and NPC state, and rewrite subsequent events. No fixed historical victor is guaranteed after its causal prerequisites change. Protect *causality* and *NPC agency*, not predetermined canon.


**Canon priority:** *Romance of the Three Kingdoms* shapes recognized character portrayals, legendary strengths, iconic conflicts and narrative baseline. *Records of the Three Kingdoms*, Later Han scholarship and responsible historical sources contextualize institutions, office titles, geography, military organization and chronology. If accounts differ, explicitly identify **NOVEL_CANON**, **HISTORICAL_CONTEXT**, **EDITORIAL_FICTION** or **TO_VERIFY** in internal notes; never call a fictional meeting a verified historical event. Dialogue and dramatic prose must be original, not copied from novel/translation.

**Rules for every historical actor and major event:**
1. Preserve recognizable novel-grounded talents, flaws, personal loyalties, strategic/dueling ability and personal voice. High player stats do not overpower historically formidable figures or override chain of command.
2. Give historical NPCs **independent scripted lives**: loyalties, plans, alliances, ambitions, duties and offstage movement. This does not require a separate autonomous AI-agent simulation. Refusal, loss, friendship and allegiance changes must follow credible causation.
3. **Knowledge is bounded:** firsthand evidence, witness statements, letters, intelligence, spies, roads and real message delays. NPCs do not know offscreen private player choices, future events or remote news instantly. The player only sees what their character reasonably learns.
4. **Geography and chronology:** actor alive and of feasible age, rank, faction, office, proximity and travel resources. Travel, couriers, armies, rumors and summons take time; weather, escorts, road control and war matter. No cameo teleportation or future office prematurely granted.
5. **Alternate history is allowed only through a causal chain:** source event/choice → viable action/resources/timing → witnesses and institutions → durable world/player/NPC flags → consequences to later battles, survival, alliances, offices and historical encounter eligibility. Recompute later canon when its prerequisites no longer hold.
6. **No absolute plot armor:** historical people may be injured, die, lose office, survive against the baseline or change allegiance when earned by the world state; neither arbitrarily kill nor artificially preserve them to force a future plot.
7. Titles and court power must match the actual date and political authority; English display, internal Hanzi/Pinyin for research. A literary collective honor, formal office, nicknames and property grants are never interchangeable.
8. **Progressive Discovery:** NPC enters the People screen only after legitimate encounter; do not reveal hidden personalities, motives, feelings, enemies or portraits prematurely. Internally track discovery/knowledge separately from omniscient author notes.
9. QA on NPC scenes includes identity/ability, era/presence, source/status, knowledge, motives, alternate-world chain, independence, knowledge-gated UI, legal choices, valid save/import and later callbacks. Check actual world faction and local jurisdiction, not simply a famous scene's year.

**Detailed live cast/historical flags and source notes:** World Bible **WB-02/03/07/08**; archived GDD §§6A, 7B/7C hold original long-form wording and research leads. Verify notable facts before declaring canonical historical accuracy.

## GDD-05 — HISTORICAL CAST, NPC DISCOVERY AND RELATIONSHIPS

- **Campaign historical planning target:** 100–120 persons, roughly **20–25 major** (deep source linked life/voice/location and long-term impact), **35–45 supporting** (credible portrayal and continuity) and **45–50 background** (brief source-verified reference only). This is **casting capacity**, not required 100 portraits or 120 NPC biographies before continuing the novel. Fictional and historical actors may share narrative relevance; ensure no double-counting when changing tiers.
- **People categories:** Neutral / Friends / Enemies, reflecting *observed* relationship and allowed to evolve; no spoilers of concealed hostility. Hide unknown fields, do not display birthplace, mechanical debug notices, invented descriptions, or full personality until earned. Known profile may have name, age, rank, political office, brief verified appearance/portrait, observed character and shared history; do not repeatedly narrate appearance in scene bodies.
- **Hidden relationship state:** trust, respect, attraction, promises, commitments, remembered deeds, witness and knowledge flags. Display qualitatively, not internal percentage gauges. Every consequential NPC can initiate, refuse, respond, remember, leave or act elsewhere. Important friendships can remain non-romantic and be as deep as love.
- **Assets:** portrait art is original semi-realistic painting, consistent with period and character. People portraits are optional until original art exists, and gated by actual discovery; registration alone is not display permission. Do not substitute unverified portraits or reveal future profiles.
- Research and populate an NPC only when its scene/relationship depends on it. Record stable ID, source/fiction status, period, affiliation, known appearance, relevant role, locality, first legitimate encounter, independent goal, prior commitments, assets, discovery flag, reachable scene/choice dependencies and later memory. Maintain original source references and uncertainty in the World Bible, not huge rosters in this GDD.

## GDD-06 — SIX ROMANCES, FRIENDSHIPS, ADULT SOCIAL LIFE AND HOUSEHOLDS

### Six optional substantial romance arcs (LOCKED_DESIGN, ongoing implementation)
**Six women total = S0 Shen Lian plus R1–R5 *five other distinct adult women*.** The present editorial casting is **R1 Lin Yue** (river/transport), **R2 He Qing** (healing/community), **R3 Cai Zhen** (private correspondence/political network), **R4 Lan** (pleasure-house performer with individual aspirations), **R5 Song Wan** (property/trade/household). These are original fictional identities and subject to chronology and scene validity; World Bible WB-04 and actual HTML govern current introduction/discovery status. Their full life-long routes are **not** all complete.

**For each substantive candidate, require:** stable ID; distinct voice, work, desires, friends and agency; optional first encounter in plausible adult period/location; attraction or no attraction based on actions; at least meaningful choice/response, follow-up and independent initiative; real relationship development or refusal/platonic continuation; reunion/absence/correspondence obeying distance; downstream career/household/world effects; conditional late-life/ending recognition; relevant targeted QA. Do not write equal repetitive courtship templates, force all six in one playthrough, or assume any person is obtainable by status/wealth. A venue supporting character is **not** one of the six merely because intimacy or a recurring scene occurs; only a deliberate R-slot assignment with long-form treatment counts.

**Historical women:** current R1–R5 are original characters, not claims about historical figures. Any proposed substitution with a documented historical woman must verify family/marriage, age, timeline, loyalties, geography and plausible divergence, rather than retconning earlier canon. No automatic romantic rights over subordinates. Every adult participant must be 18+ with freely given consent.

**NEWER CREATIVE RULE — 11 Nov 2026:** Prefer face-to-face meetings and actual personal participation over letters. Let correspondence carry brief practical information when geography prevents a credible visit. Do not use remote letters to simulate a full romance, invent travel, summon NPCs by rank, or override a declined invitation. The v0.4.59 Chapter X reunion windows are first-pass implementation only.

### Intimacy and levity — latest user direction (10 Nov 2026; DESIGN, PARTIAL IMPLEMENTATION)
Each of the **six optional romance routes** must eventually offer at least one *distinct, earned, adult and mutually chosen intimate moment* as part of a multi-chapter relationship, with meaningful tenderness, attraction, metaphor, a discreet fade-to-black and emotional/social aftermath. Do **not** require the moment for progression, imply entitlement, or write graphic anatomy/sexual acts. Existing geography, age, knowledge, commitment and free consent continue to govern eligibility; intimacy is not interchangeable copy or a prize. Platonic, distance and no-romance paths remain complete. Comedy belongs in everyday meals, officerly mistakes, comradeship and private banter without undercutting casualties or solemn political moments. **Implementation:** v0.4.49 introduced first optional scenes for S0 Shen, R1 Lin Yue and R4 Lan; **v0.4.50** adds first optional scenes for R2 He Qing, R3 Cai Zhen and R5 Song Wan. Thus **6/6** have private opportunity scenes and meaningful refusal alternatives, but **none** has a fully authored and QA-certified lifetime arc; chronological/court safety, friendship and ending epilogues still require development.

### Deep friendship (APPROVED BLUEPRINT)
Aim for **3–4** substantial potential friendships with mutual vulnerability, humor, shared chores and risk, initiative, distance, disagreements, reconciliation, deaths/partings where earned and memories that persist across Acts. NPCs remain whole people without player attention. Do not force every friendship to form; no superficial instant “best friend” unlock after one deed. Private affection and loyalty need not mean political agreement.

### Adult social life and celebration (APPROVED DIRECTION)
Depict credible late-Han **campfire meals, markets, wine houses, feasts, homecomings, family celebrations, village weddings, performances, poetry, banquets, entertainments, ancestral rituals and community gatherings** when era, class, city, hosting and cost make sense. Celebrations can be genuinely joyful, bittersweet, politically risky, or simply ordinary; not every visit requires a visible choice or penalty. **Birthdays are occasional meaningful narrative events, not annual events.** Invitations may be refused; knowledge, arrival time, class norms and expenses matter. No modern club/dating concepts disguised as Han life.

**Adult venues:** pleasure houses/brothels/performers, hosts, managers and workers are distinct people, not automatic sexual services or collectibles. Attendance is optional, access/plausibility researched, consent never inferred from profession or payment; consequences for promises, resources, privacy, reputation and relationships are contextual, not moralistic or forced. Supporting women may recur separately from the six routes. Keep scenes emotionally grounded and non-graphic.

**Marriage timing — NEWER USER DECISION (11 November 2026):** Courtship and formal marriage may occur mid-lifetime in ordinary chapters as soon as credible multi-scene relationship, age, mutual consent, time and social duties permit. Do not defer every marriage to Chapter XII or endings. Show the wedding and married life as actual narrative events, and preserve each woman’s agency, personal history and agreed domestic role; new v0.4.67 marriages have voluntary handovers from outside employment. Initial implementation v0.4.66 offers gated 218/223 CE marriage for all six candidates; longer household arcs and plural-consent rules remain incomplete.


### Optional plural-partner households (APPROVED DIRECTION, not a separate engine mode)
The protagonist may form multiple concurrent adult romantic/household ties **only when every participant consents** and each has independent boundaries, priorities and ability to refuse or leave. Monogamy, non-cohabiting relationships, remaining single, and no romance are equally complete choices. Verify historical distinction among marriage, concubinage, private partnerships, kinship and palace institutions, never assume “everyone becomes equal wives” or guaranteed status. Resources, housing, dependence, children, inheritance, promises, social and political standing, jealousies/harmony and absences create context-specific consequences; no compulsory harem or collection screen. Offscreen household members act in ways consistent with known goals and communication delays.

**Writing tone:** vivid adult feeling and plausible flirtation, optional playful metaphors/euphemism only if voice/context appropriate, never a workaround for graphic sexual content. Do not treat coerced romance, harassment or exploitative authority as a desired reward.

## GDD-07 — CAREERS, PERIOD OFFICES, RECOGNITION AND SIX TIGERS

### Earned recognition and emotional payoff (APPROVED DIRECTION)
Promotions, grants, gifts, honorary titles and sincere gratitude are **earned** by consequential acts, witnesses and legitimate authorities, never guaranteed chapter rewards or raw-stat conversions. Build anticipation and an actual human payoff: the deed, corroboration, nomination, deliberation, credible conferral, personal/friend/family reactions, celebrations where appropriate, and subsequent new duties and reputation. Do not undercut every triumph immediately. Independent, civic, administrative and diplomatic heroism can receive equally meaningful acknowledgement even when a ruler withholds an office. Allow a player to refuse promotion and respect its consequences. A personal epithet, office, courtesy name, literary honor and property gift are different things.

**Office categories:** (1) actual military appointments/command; (2) civil offices with jurisdiction, e.g. `太守` Commandery Administrator and `刺史` Inspector, period-dependent; (3) noble/court honors, including posthumous designations *only after death*; (4) informal sobriquets or novel/literary groupings. Use clear **English** in game; Hanzi/Pinyin in internal source review. A directional style like “General of the East” is ambiguous: `征東將軍` (campaigns east), `鎮東將軍` (guards/pacifies east), `平東將軍`, `安東將軍` are distinct and **not interchangeable or universally ranked**. Similarly `前將軍`, `左將軍`, `右將軍`, `後將軍`, `車騎將軍`, `大將軍` need scene-specific verification and a grantor with real authority.

**Credible below-general field responsibilities, not one ladder:** `屯長` *Tunzhang* (unit leader), `軍候` *Junhou* (field captain), `軍司馬` *Jun Sima* (military officer), `別部司馬` *Biebu Sima* (independent detachment commander), `校尉` *Xiaowei* (colonel/command role), context-dependent `都尉` *Duwei* (commandant) and `中郎將` *Zhonglangjiang* (General of the Household, title not automatically a full general). `偏將軍` *Pianjiangjun* and `裨將軍` *Pijiangjun* are **junior general-titled** designations, not below-general rank slots. Numbers, command structure, salary, factional legitimacy and translation require local source checks. Advancement, appointment, reassignment, demotion, civil transfer and refusal follow era/office geography and who can actually grant it; never a fixed XP ladder.

### Optional “Six Tiger Generals” (APPROVED CONDITIONAL ALTERNATE-HISTORY DESIGN, NOT HISTORICAL FACT)
The *novel's* **Five Tiger Generals** are Guan Yu, Zhang Fei, Zhao Yun, Ma Chao and Huang Zhong. They are a literary cohort, **not a historical government office**. On a causally justified **Shu/Liu Bei-aligned divergent** route, the protagonist might be honored as a **sixth member**, `六虎將` (Six Tiger Generals), with the original five represented, living/viable, a credible later-period patron/government able to grant recognition, exceptional *earned* military merit, actual ceremony and player acceptance. **Never** declare the original novel had six or automatically grant a vacant slot. If the historical five-person cohort becomes impossible, invent a **differently named** earned honour where appropriate rather than falsifying canon. Other careers/factions may earn equally satisfying independent distinctions. Cohort honour does not confer an unearned formal military office.

**Authoring/QA records:** grantor, source, year/place, eligibility, deed, verifiable witness, communication delay, proclamation and whether public, acceptance/refusal, office vs sobriquet, duties, real unit/jurisdiction, item/ownership, relationships, state flags, future callbacks and historical deviation. Verify eligibility and ineligibility, original-five survival, non-Shu, pre-late-era timing, office/rank display, save compatibility and downstream dialogue. The original v1.28 §§7A–7C and World Bible research section retain detailed lead references; don't assume these shorthand titles have all been individually fact-checked.

## GDD-08 — POSSESSIONS, PERSONAL PROPERTY AND NARRATIVE ESTATES

**Meaningful possessions**: weapons/armor, horses, keepsakes, funds, dwellings, trade stakes and military-assigned resources, each with ownership, provenance, description and story relevance rather than crafting trees or meaningless stat bonuses. Named horses carry memories, character and physical condition but do not require daily-feed minigames.

**Narrative estate blueprint inspired in structure by *Lords of Infinity*, NOT copied or assumed historically accurate for Han China.** Estate/property access must be earned via wages, purchase, inheritance, family, marriage, grant, service, trade or political authority; protagonist does not begin automatically a landed gentry owner. Keep these ownership classifications distinct:
- `PERSONAL`: transferable/spendable assets owned by protagonist;
- `FAMILY/HOUSEHOLD`: joint/kin-linked property and obligations;
- `TRUSTED/MANAGED`: assets managed for other owners;
- `OFFICE/FACTION`: state, court, army or assignment stores/funds, **not** personal income;
- `DISPUTED`: contested claims requiring evidence and consequences.

Relevant **milestone decisions**, not daily taxation spreadsheet: tenant wellbeing versus revenue, seasonal stock, debt/pledge and creditors, upkeep/repairs, irrigation/market/workshop/road investment, domestic obligations, fraud, floods, war requisition, evacuation, confiscation, trusted manager autonomy, distant messages and delayed human consequences. No one-click estate ownership from rank, no automatic riches, no flat numerical Han rent/tax model without sources, no mandatory management for a soldier or solitary traveler.

Game-facing Possessions may show a brief qualitative asset/debt/estate description based on what is actually acquired. Internally record only flags with authored downstream consequences; do not duplicate existing meters or add standalone economy/harem/venue simulators. Track valid owners across gifts, campaign resources, household decisions, refusal, and war-related losses. Check cost/unit plausibility, soft locks, scene affordances and save migration when implemented. Original game supplies and property ownership must be inspected before each patch; old GDD snapshot values are not runtime assertions.

## GDD-09 — READING UI, STATE SCHEMA, OFFLINE BUILD

### Display and interaction (LOCKED)
- Original reading-first mobile UI, desktop readable; **All Under Heaven** literary serif title, no old subtitle. Parchment & Ink light, high-contrast dark, Follow Device. Offline-safe fonts and original visuals.
- One compact **Game Menu**: Story, Character, People, Possessions, Journal, Settings. No duplicate desktop navigation and no always-on mobile bottom bar. Settings: theme, font size, spacing, Save/Load/Export/Import; autosave. Maintain scroll/reading position when closing menu, mobile touch targets and accessibility contrast.
- Character: name, age, relevant rank/affiliation, wealth, reputation, **six attribute bars**, health/traits. **No redundant Skills submenu** or mechanical prose/explanatory status labels (“Hidden Prodigy,” “Original Campaign” etc.). Hide internal numerical relationship states and developer widgets in normal mode.
- Ordinary story pages: continuous prose and occasional meaningful choices or **Next**; no frequent scene IDs, page numbers, repeated year/location ribbons, or boilerplate. A simple chapter title is acceptable at opening.
- People portrait: original semi-realistic painted, period-consistent visual; thumbnail and enlarge-on-tap after true discovery. No copying copyrighted faces/poses/costumes/art, no pre-discovery face/biography leak.

### Runtime and saves (design plus verified-source warning)
- Developer-facing separation of story/engine/state/assets is permitted, but **distribution remains one offline HTML**; Android packaging only later if justified.
- Core save domains: character identity/age/health/attributes/rank/affiliation/reputation; world year, geography and divergence; NPC discovery, memories, attitudes and commitments; equipment/mounts/funds/property ownership; scene cursor, decisions, eligibility and mode flags; **reader settings separately**.
- Preserve existing scene IDs, choice keys, import/export serialization and legacy save keys unless explicitly versioned/migrated. Never fabricate QA save states: use legal gameplay traversal and verified checkpoint export/import. A static scene/JSON presence does not certify route reachability or valid post-load navigation.
- Player-only modes Heaven's Favor / God Mode optional off by default; do not leak spoilers in default UI. Free/offline tooling first; paid subscription or service requires user approval.

## GDD-10 — EFFICIENT DEVELOPMENT WORKFLOW / CHANGE CONTROL

**Working invariant:** **Read only what changed. Edit only what is needed. Test everything affected.** This is intended to reduce redundant work, **not** reduce literary/historical rigor.

1. **Verify active triad**, current filename/hash, WB-01 risks and real scene identifiers. Read applicable GDD section and local World Bible cards only; do not read all previous chats or the full archive by default. The older §0.5 “open GDD v1.17 / WB v1.15 / HTML v0.4.8” is **superseded and must never be used as a handoff**.
2. Select a **coherent 4–8-scene batch when appropriate**, with required inbound/outbound dependencies and memory callbacks. Preserve strong prose. Smaller patches are fine for actual bugs; don't artificially split every small change into a separate file/version. Research actors, period office, geography and possessions **just in time**, not 120 biographies first.
3. Write English literary scenes, integrate war/politics, friendship, independent female arcs, household/civic life when earned, and sensible time transitions. Keep names, travel, spoken claims, knowledge, timeline, romance status and agency consistent. Use branch-and-rejoin **without erasing flags, previous refusals or permanent consequences**. No forced player presence at every famous historical event.
4. Patch only required HTML sections, preserving unrelated scene IDs, choice strings/keys, links, save/import contracts, discovered-only People and asset IDs. Record exact changed scene IDs, data/flags and dependent downstream scenes. Changes to calendar/schema/ending gates trigger DEEP checks. Never reuse a fixture after its source version became invalid.
5. **Risk-tiered QA** (next section) before a claim of completion. Distinguish parser check, scripted handler transitions, actual browser clicks, mock-storage imports and file-origin persistent-storage checks. A valid QA fixture must originate from legal traversal, be exportable/importable, and match its build/schema.
6. Update **WB-01 status + affected topical record** at a meaningful checkpoint; amend this fast GDD only for actual approved design changes, active triad pointers or workflow policy changes. Avoid per-micro-edit GDD version proliferation and repeated historical “LATEST” paragraphs. Archive old long-form receipts separately.
7. In spoiler-safe chat, report what changed, actual test evidence, open risks and the next batch. Do not expose unrevealed endings, NPC identities, decisions or secret relationship gates unless the player requests them.

### Risk levels
| Level | Appropriate change | Minimum validation |
|---|---|---|
| **FAST** | Pure prose, nonstate images, metadata | JS/syntax or source parsing as relevant; no orphan scene/asset IDs; one genuine targeted route; quick prose/source review |
| **STANDARD** | Dialogue choice, story flags, NPC appearance/discovery, relationship callbacks | FAST + relevant alternative choices and dependent scenes; real transitions/state assertions; discovery/knowledge and chronology checks |
| **DEEP** | Calendar, state/schema, save, ending arbitration, engine, major integration | Standard + old-save migrations, legal fixtures, import/export roundtrips, broad routes/endings/desktop/mobile when affected, regression evidence and explicit untested gaps |

Never call one QA pass a full campaign certification. Comprehensive end-to-end regression remains mandatory at integrated milestones and release. Technical testing cannot replace editorial reading or credible historical research.

## GDD-11 — PRODUCTION CONTRACT, CHAPTER DELIVERY AND RELEASE GATES

**NEW P0 editorial gate:** For each chapter, verify at least one protagonist-owned consequential turn that changes a battle, regime, settlement, relationship network or durable personal destiny. Historical characters cannot monopolize the decisive actions. Audit every chapter and eight ending prerequisites for real world-state effects rather than purely narrative praise; never mark this chapter-wide gate COMPLETE on the basis of one changed sentence.


### Production architecture
- **Four Acts:** I=Chapters I–III (first stakes and loyalties); II=IV–VI (responsibility and rival demands); III=VII–IX (expanding consequences and long-term lives); IV=X–XII (legitimacy, irreversible conflicts and legacy). Prologue and lifetime epilogues frame the full story. Chapter breaks can be paced differently **while retaining twelve total chapters**.
- One connected world with four editorial service lanes; choices should matter through reputation, memory, authority, injury, relationships, assets and future world state. **3–5 meaningful decisions per major sequence as a rough editorial budget, not a hard quota**. Include prose-only Next transitions for pacing; minimize inconsequential microchoices. Avoid clone-chapters for every branch.
- **Per chapter, document locally in WB-05**: year/Act, conditional historical anchors and verification status, believable geography, 2–4 dramatic movements, social/romance/daily-life beats, military/political/civic pressure, meaningful decision(s), entry/exit state, downstream callbacks, external sources and QA warnings. These are proposals until implemented/verified; no chapter card is proof of finished prose.
- **Execution milestones:** connected skeleton ≠ complete novel; harden save/engine and schema; expand/polish chapters with targeted QA; integrate NPC/estate/career, historical divergence and art where needed; validate eight endings; full narrative/mobile/regression pass before release. Design choices may be made editorially without asking permission each scene; require user approval to alter locked 12-chapter/8-ending scope, defining mechanics or overall aesthetics.

### Release definition of done
- Complete readable prologue + 12 novel-quality chapters + 3 **actually reachable** current ending families and lifetime-sensitive variants, while preserving eight legacy manuscript sources and their old-save routes.
- Major choices, alternate-historical branches, earned honors, agency, changing relationships and known NPC availability produce consistent immediate/delayed outcomes.
- No critical softlocks, invalid transitions, unintended romance, knowledge or art leaks; known birth/age/time and travel constraints follow story state. All saved states migrate or explicitly fail safely; native offline restart/export/import and mobile controls tested.
- No graphic sexual content; adults and consent; no mandatory mature-venue, estate, family, sexual or multi-partner choices.
- All distributed art original and licensed for intended use, bundled offline; game remains readable without portraits when an asset is missing.
- Full QA and editorial pass over historical consistency, alternate-world survival/office, endings and route continuity. **Design drafts or test previews are not a public release.**

## GDD-12 — HISTORICAL VERSION CONFLICTS, SOURCE MAP AND AUDIT NOTES

### Superseded or repetitive material deliberately excluded from everyday reading
- v1.28 original header and §0 recorded **v0.4.24 / WB v1.26** as then-current; one older “current build” subsection still said **v0.4.16**, and §F/§0.5 handoff still used **v0.4.8**, GDD v1.17 and WB v1.15. These are **dated history, not active pointers**. Current truth is GDD-01/WB-01 and the actual v0.4.45 file.
- Old chronological §§0.2–0.2G and Appendices A–C contain extensive repeated Chapter III–VI deltas, test receipts, source fingerprints and historical decision ledgers. These remain in **unchanged archive** and need not be ingested to edit Chapter VII.
- Historic romance target **12–15 → 4 → 5 → clarified six (S0+R1–R5)**; only the latest six-candidate rule is active. Original §6D contained a sentence saying “approved 4 potential substantive romance NPCs”; it is superseded by v1.28's explicit six-cast correction. Maintain additional independent adult-venue NPCs separately.
- Original §10A uses **2–4-scene** default, newer 10 Nov decision uses **4–8 coherent scenes**. Neither is a quality or word-count quota; scope and risk drive QA.
- Old GDD calendar remarks about Chapter VI=197 and Chapter XII=222 describe old builds; latest v0.4.44 fixes year entries, with **exact date/birthday and comprehensive save QA still incomplete**.
- Original long-form external references are **research leads, not blanket verified scene facts**. Kept unchanged in source archive and summarized in World Bible WB-07; inspect them only when authoring that exact office, social scene or event.

### Coverage map: original v1.28 sections → FAST section
| Original long-form source | FAST authoritative reading location |
|---|---|
| §0 handoff, §1–2 scope, blueprint §§A/F | GDD-00, GDD-01, GDD-03, GDD-11 |
| §2.1 calendar / §5 age and mortality | GDD-03–04 |
| §3 / §3.1 / §3.2 literary standards | GDD-02, GDD-11 |
| §4 abilities and revelation | GDD-03 |
| §6 + §6A–6B actors/discovery/cast | GDD-04–06 |
| §6C social, §6D plural household, §6E style, §6F friends | GDD-02, GDD-06 |
| §7, §7A–7C official ranks/rewards/tigers | GDD-07 |
| §8 / §8A estates/ownership | GDD-08 |
| §9 reader UI | GDD-09 |
| §10 runtime, §10A–10B efficiency/scope, §11 modes | GDD-09–10 |
| §12 done, blueprint §§A–D, Appendix B QA | GDD-10–11 |
| §0.2 old build checkpoints, blueprint §§F–G, Appendices A–C old receipts/ledgers | **Original source archive only** (see GDD-12) |

### Archive-only source and integrity policy
The unchanged original GDD is authoritative for **source provenance or finer details** where this compressed reading edition omits illustrative examples. It must not override a later explicit user decision or a tested newer implementation. When genuine ambiguity matters, inspect the exact original section and World Bible, document the conflict, and make the smallest well-supported change. Do not quietly replace detailed canon with assumptions. The optimized GDD is a reading/workflow artifact, not a tested gameplay update or a replacement for source verification.

---
## v0.4.99.2 design overlay — Historical Heroic UI

**Decision:** apply visual design directly to a checkpointed copy of the real game, not to a parallel mock UI. Keep v0.4.99.1 unchanged as recovery baseline.

**Implemented:** an English-only masthead, embedded mountain-fortress decorative art, dark wood records-cabinet rail on wide desktop, mobile menu fallback, bordered parchment story folio, context-neutral date ribbon, illustrated existing-NPC cards, red-seal accents and historical treatment of Character, Possessions and Chronicle.

**Accessibility & privacy:** choice text remains readable and prominent; responsive navigation must work by keyboard; known-NPC gates are reused unchanged; existing portraits remain zoomable; saved story history is preserved internally; no new character biographies or art revelations can bypass discovery flags.

**Next:** review missing NPC portrait coverage and art consistency in incremental batches, then visual scene art only at narratively meaningful junctures, optional opt-in ambience/SFX in v0.4.99.3, and integrated/native device QA in v0.4.99.4. Beta remains gated by native `file://` relaunch test and full 539-scene manual editorial review.


---

## UI design decision — v0.4.99.2a (12 Nov 2026)

**Current source:** `active/ALL_UNDER_HEAVEN_v0.4.99.2a_DEV_ICON_NAV_QA_TOOLS.html`. Incremental child of v0.4.99.2; gameplay and save schema unchanged.

1. Icon-only navigation for the mobile menu and desktop records cabinet, with `aria-label` and `title` for accessible navigation. Header's hamburger control also omits its visible Menu text.
2. Remove the decorative era subtitle “A Chronicle of the Later Han” from the masthead.
3. Remove persistent successful-save messages from the Story reading surface, but continue prominent storage-error/recovery feedback and retain manual save/export controls in Settings.
4. Remove the explanatory Timeless Heroes paragraph from People. Do not modify the actual Timeless Heroes rules.
5. Developer Tools: unlock explicitly in Settings; dedicated navigable Chapter Checkpoints, All Characters, Scene Index and State Inspector. Tool access is temporary/session-local and not persisted to player saves; QA preview reuses 131 fixture entries across Prologue and 12 chapters. All-char tab intentionally bypasses normal discovery only inside developer UI; player-facing People remains spoiler-gated. Scene list is an index, **not a route reachability certification**. All QA previews return to the original in-memory campaign and never autosave.

**Remaining:** direct physical file:// persistent-storage reopen proof, full human route/editorial audit, and any potential usability feedback on icon comprehension. A new opt-in sound checkpoint may follow after review. No beta certification granted.


---
## UI checkpoint v0.4.99.2b — desktop single-nav and masthead polish

- Display breakpoint: desktop >=1001 px uses the carved-wood vertical sidebar with icons **and visible English labels**; the redundant header menu toggle is hidden.
- Below 1001 px, desktop rail is hidden; one hamburger opens a **vertical text-labeled list**. No icon grid.
- Masthead height reduced (desktop 102px; smaller on tablet/mobile), brand aligned toward the top.
- Accessibility: navigation buttons continue to expose accessible names, active-state aria-current, and keyboard interaction; existing state-aware disabling is preserved.
- No changes to all 539 scenes, 29 character registry entries, player save schema, persistent keys, developer QA fixtures, romantic content, autosave, or all three ending families.
- QA verified JS parse, six responsive viewports, 13 sample chapter previews with unchanged save storage in mocked environment. Physical browser-close/reopen file:// test remains outstanding.


---

## UI navigation amendment — v0.4.99.2c (12 November 2026)

The desktop sidebar is no longer displayed. Desktop, tablet and mobile now use one collapsible hamburger menu opening a single vertical navigation list with icons and English labels. All story, NPC, chronicle data, developer chapter fixtures and save schemas remain unchanged. For implementation source see `ALL_UNDER_HEAVEN_v0.4.99.2c_DEV_UNIFIED_HAMBURGER_MENU.html`. This appendix is presentation-only and does not supersede canonical narrative or systems rules.


---
## v0.4.99.2m — Living equipment continuity and truthful portrait captions (internal)

**Decision:** Inventory and witnessed acceptance flags are authoritative; portrait stage progression does not grant equipment or rank. The story must react to accepted and declined personal gifts, including voluntary player conduct after the gift, with immediate local consequences and selective later callbacks. No retrospective branch rewrite.

**Implemented:** two voluntary post-acquisition scenes with two exclusive conduct choices each; journal memory and targeted narrative echoes in later chapters. No new major weapons, armor sets, mounts, prices, stats, romance paths, titles or ending predicates. Old scenes and original options survive. New optional flags preserve save version=1 compatibility.

**UI contract:** Existing 8 approved portrait stages are unchanged. A partial kit may differ from the artwork. Use accurate non-spoiler captions ("Artwork depicts a representative outfit. Your earned belongings are listed in Possessions.") rather than falsely showing missing gear or listing unrevealed items. Only fully earned inventory permits art that visibly displays the three main items.

**QA/remaining:** targeted continuity checks, 562 scene registry + two-context traversal, viewport/portrait and save fixtures pass. Browser validation was in-session, not a physical close/reopen on target Android/desktop. Next editorial pass should examine optional scene flow in normal human play, especially old saves and faction-context art; don't call this beta.
