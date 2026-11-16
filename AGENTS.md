# All Under Heaven — Codex repository instructions

## Source of truth and priorities
1. Read `docs/START_HERE.md`, `DESIGN/LOCKED_DESIGN_DECISIONS_2026-11-15.md`, and `DESIGN/APPROVED_EPIC_ELEVATIONS_ISSUE_1.md` FIRST. GitHub Issue #1 is explicitly approved design; its quality requirements are binding, not proof of implementation.
2. `GAME/ACTIVE_BUILD.txt` names the ONLY current active HTML. Edit it in place or create a versioned successor and update the pointer. NEVER start another game from scratch.
3. Story roadmap: `ROADMAP/01_TWO_PART_190_250_v1.3.md`, `ROADMAP/05_M0_M11_DEVELOPMENT_ROADMAP_v1.0.md`, `ROADMAP/06_EMPEROR_DRAGONS_UNIFICATION_ARC.md`, related matrices; rules in `RULES/`. Preserve the dramatic build-up from Shu enthronement through personalized Dragon arcs and their later trials to the earned unification climax; roadmap is not implementation evidence.
4. `DESIGN/02_WORLD_BIBLE_LEGACY_v1.99.2m.md` and `DESIGN/03_MASTER_GDD_LEGACY_v1.28.md` provide larger reference context. Explicit newer locked decisions take precedence where they differ.
5. Game prose/UI is in ENGLISH; development notes, checkpoints and communications to the owner are in INDONESIAN; progress reports avoid story spoilers.

## Immutable constraints absent explicit owner approval
- Chapter I, 190 CE: male protagonist aged 16, Infantry Private under Han Sheng, with NO personal troops or officer authority. Rank and calendar advance through earned, story-supported events. For any rank-and-file assignment only Infantry or Cavalry, never Support.
- Historical figures (Liu Bei, Guan Yu, Zhang Fei etc.) have independent duties and agency. Introduce knowledge by plausible hearing, witnessing or meeting; no omniscient player knowledge.
- General promotions require meaningful recognition, emotional reactions and actual assumption of command. Sixth Tiger/Grand General is a separate earned climax within a valid shared-life window with Liu Bei and available Shu generals; never assemble dead, absent or unmet figures by default.
- Emperor of Shu requires contested legitimacy, deliberate mandate acceptance, substantial multi-scene enthronement/public proclamation, private aftermath and a consequential first imperial decision. Shu enthronement and China-wide unification are separate. Follow the owner-approved exceptional outsider succession **without adoption**, including a new post-223 mandate with actual Liu Shan/court consent for saves without a witnessed Liu Bei designation: `DESIGN/APPROVED_SHU_SUCCESSION_2026-11-16.md`. Do not ask to reconfirm this approval or fabricate a retroactive testament.
- After lawful imperial accession, each optional Dragon appointment needs personalized nomination, merit, relationship, availability, consent, ceremony and actual command handover. Preserve 0–5 seats; collective recognition requires all five valid appointments. No fixed names or auto-fill; preserve valid legacy saves.
- Battlefield fiction must situate protagonist inside a real unit with formation, commanding officer, soldiers nearby, visible enemy, immediate objective, movement orders and limited information, following ROTK-inspired campaigns.
- **Part II frontline lock (owner reaffirmed 16 Nov 2026; GitHub Issue #2):** the protagonist personally goes to war even as Emperor of Shu. For each major relevant M5–M7 campaign, provide a substantively playable, chronology-legal direct-field leadership/combat route with actual unit, tactical choices, independent Dragon/opponent actions, risk and aftermath; preserve meaningful delegation/diplomacy routes. Do not turn the Emperor into a palace-only observer or let Dragons take every decisive moment. Follow `ROADMAP/06_EMPEROR_DRAGONS_UNIFICATION_ARC.md` section 5 for player agency, gating, state sync and QA.
- Five Dragon Generals are exactly five FUTURE potential legendary slots, NOT five default initial followers and NOT permanent Infantry/Cavalry general classes. Any named appointments must be explicitly earned.
- Exactly five *existing* Special Staff roles: Personal Assistant (Sergeant), Strategist and Quartermaster (Captain), Deputy Commander and Intelligence Officer (Major). Eligibility is not appointment. Preserve original IDs and thresholds; demo staff are not hired staff.
- Mature romance only between adults, consensual and non-graphic/fade-to-black, no sexualization of minors. Humor, banter, friendship, daily life and legendary companions are high priorities.
- Universal Timeless Heroes convention stays; chronological aging continues. Portrait production deferred. Preserve all valid existing embedded portraits.
- Do not auto-award rank, honors, resources, relationships, historical encounters, NPC recruitment, staff, or troops.
- Preserve all valid previous scene IDs, choice paths, save/import/export compatibility and Story–Character–People–Military–Civic–Chronicle coherence.

## Working style (Fast Development)
- Ship substantial integrated chapter sections (prose, decisions, effects, callbacks, menu sync, QA), not small cosmetic patches each turn.
- First inspect the current HTML architecture, then improve it in-place. Do not replace its code engine.
- QA ONLY new/changed paths and their contracts after each batch; wider regression at chapter/milestone completion. Start with `python3 scripts/smoke.py`; extend targeted tests with verified evidence.
- Record clear completion criteria in `docs/PROGRESS.md`, with done/in-progress/blocked and proof; do not claim simulated QA as full browser/device QA.
- Follow `docs/ISSUE_1_IMPLEMENTATION_PLAN.md` for M3–M4 integration. Keep Issue #1 open until its ceremonies, choices, authority/UI/save contracts and QA are verified. Commit/push completed batches as authorized; do not auto-close the issue for partial work.
- Update `GAME/ACTIVE_BUILD.txt` whenever replacing the active file; keep only the immediate previous build in ROLLBACK when creating a formal milestone checkpoint. Commit meaningful source changes to Git.
- Do NOT create full ZIPs every patch; make them at milestones, major migrations, or for transfer.
- No costs, paid APIs, uploads of sensitive information or changing locked design without the owner's approval.
- If context is missing, find it in the repository or report a precise blocker; NEVER fabricate an implementation or test result.
