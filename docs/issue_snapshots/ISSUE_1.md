# GitHub Issue #1 — snapshot untuk transfer

Sumber: https://github.com/oldfritz18/All-Under-Heaven/issues/1

Status saat dibaca16November2026: **OPEN**. Updated_at GitHub: 2026-11-16T03:27:23Z. Snapshot ini bukan bukti implementasi atau issue closure. Keputusan dinasti terbaru di DESIGN/APPROVED_SHU_SUCCESSION_2026-11-16.md tetap berlaku.

## M3–M4: Epic General / Sixth Tiger, Emperor enthronement & earned Five Dragon Generals ceremonies

## Approved narrative direction (16 November 2026)

The player approves making all major military and sovereign elevation milestones **memorable, novel-length narrative events with earned emotional payoff**, not mere rank/title changes. This issue is a **design and implementation requirement**; it does not mean the events are already playable.

### A. General and Sixth Tiger General (M3)
- Preserve the existing playable General field-warrant route `m3_222_field_review` / `m3_222_after_review` in v0.4.99.5f, but enrich its culmination with meaningful ceremony or acknowledgement, familiar comrades' reactions, and first real assumption of command. Avoid fictional promotions or extra units.
- The **Sixth Tiger General / Grand General** recognition must be a separate, exceptionally powerful military/relationship climax earned **during a historically plausible shared-life window with Liu Bei and the Five Tigers**, or through a story-justified alternate-history branch. Do not place deceased/unmet figures at the ceremony by default. Build-up, competing perspectives, reactions, and aftermath must respond to actual player history; do not automatically confer the distinction.

### B. Emperor of Shu enthronement (M4, c.223; one of the game's central climaxes)
- Deliver a **multi-scene epic investiture sequence** with deep, literary English prose. It must feel grand and historic: the solemn court, public anticipation, banners, imperial insignia/seal, formal proclamation, officials and military hierarchy, civilians' perspective, and the scale of duty — balanced with intimate emotion, memory of humble beginnings, Liu Bei's legacy, sacrifice and grief.
- Dramatic progression: **(1) succession legitimacy and contested political arguments; (2) final acceptance of a lawful mandate and the protagonist's deliberate commitment; (3) majestic public coronation/proclamation; (4) private aftermath and first consequential imperial decision**. Reactions from Zhuge Liang, Liu Shan, court members, companions, household, troops and populace must be conditioned on actual presence, survival, allegiance, knowledge and established relations.
- Replacing Liu Shan is an **alternate-history scenario**, not a claim of historical truth. Do not quietly resolve unclear succession law, adopt the protagonist into the Liu house, fabricate consensus, or crown from chapter/year alone. Preserve alternative outcomes if prerequisites or player commitment are missing, consistent with existing Story Bible and approved constraints.
- **Shu-Han enthronement must remain distinct from any eventual Emperor/unifier of all China**; legitimate succession does not instantly reunify Wei/Wu or grant uncontested territory, armies, ministers or treasury. Ensure appointments, public legitimacy, rank/title, political factions, governance UI and Chronicle are derived from witnessed/accepted state, not narrative decoration.
- This must be among the **major narrative climaxes** of the complete novel RPG, not an administrative shortcut or a single-click announcement.

### C. Five Dragon Generals: separate legendary investiture(s)
- After the protagonist has **lawfully become Emperor**, enable an **optional, earned Five Dragon Generals appointment arc**. The five seats are fixed as **five positions maximum**, not five fixed military-branch classes; **no automatic fill**. This follows `DESIGN/01_NARRATIVE_NPC_CONCEPT_v1.0.md` and `DESIGN/LOCKED_DESIGN_DECISIONS_2026-11-15.md`.
- Each candidate (historical or original within continuity) must have independent goals, established service, earned trust, qualification, availability, consent, proper political/command authority, and explicit acceptance of the offer. The player chooses whom to nominate; candidates can refuse, stay unavailable, leave seats vacant, or disagree with one another. No fake historical encounters.
- **Each valid appointment merits a dedicated emotionally distinct ceremonial scene**: nomination/council deliberation, public recognition, personal dialogue/vow or refusal, other generals' and officers' reactions, handover of *actual* command and responsibilities. If five members are eventually appointed, a further collective scene can deliver the peak of earned camaraderie, rivalry, humor and loyalty — not before.
- Follow the concept's **Grand General rank for actually appointed Dragon Generals**, without assigning unearned units/office. Five Dragon Generals remain separate from the protagonist's Sixth Tiger General distinction and separate from the **five pre-existing Special Staff roles**; never change the latter's eligibility or roles by implication.
- Keep possibility of 0–5 filled seats, and honor absent/dead/departed NPCs and the player's prior choices.

### Acceptance & implementation safeguards
1. Integrate new sequences organically into Chapter XI→XII–XIII (and M3 earlier if Sixth Tiger recognition needs historical timing); **avoid scene/reward resets and preserve existing playable scenes, IDs, choices, portraits, save compatibility and legacy endings**.
2. Write substantial, reading-first English prose with distinct voices and realistic court/military protocol. Avoid repetitive cutscenes; key choices change later state and narration. Moments should feel earned, monumental and personal.
3. Persist verified appointment/legitimacy events exactly once, with acceptance/refusal/defer branches, negative-state QA, Chronicle/People/Military/Civic/Character sync and legacy-save migration safety.
4. Test Emperor-without-Dragons, vacant-seats, candidate refusals, alternative succession, chronology and rank paths; no forced victory or fake consent. Record targeted QA receipts and update `docs/PROGRESS.md`.
5. Continue from `GAME/ACTIVE_BUILD.txt`, current v0.4.99.5f baseline, and the existing M0–M11 roadmap. Do **not** start over, spend money, or silently override locked decisions.

**Design sources:** `DESIGN/01_NARRATIVE_NPC_CONCEPT_v1.0.md`, `DESIGN/05_CORE_STORY_DECISIONS_LEGACY.md`, `DESIGN/LOCKED_DESIGN_DECISIONS_2026-11-15.md`, `ROADMAP/05_M0_M11_DEVELOPMENT_ROADMAP_v1.0.md`. This issue captures the user's newly approved **narrative quality bar** and does not claim these scenes are implemented.

## Komentar yang tersedia saat snapshot

### https://github.com/oldfritz18/All-Under-Heaven/issues/1#issuecomment-6906448889

Cross-milestone dependency approved 16 November 2026: [Issue #2](https://github.com/oldfritz18/All-Under-Heaven/issues/2) now tracks **playable Emperor frontline command and personal battlefield participation** across M5–M7, autonomous Five Dragon Generals, and the earned China unification climax. The owner reaffirmed that becoming Emperor must **not** turn the protagonist into a palace-only observer. See `ROADMAP/06_EMPEROR_DRAGONS_UNIFICATION_ARC.md` §5, `AGENTS.md`, `GOAL_MODE_PROMPT.md` and `docs/START_HERE.md`.

**Keep scopes separate:** Issue #1 covers General/Sixth Tiger and M4 Shu enthronement / per-Dragon investitures and associated QA; Issue #2 covers their long-term command, relationship, warfare and ending payoff. Both are **OPEN implementation requirements**; roadmap/issue updates do not certify playable scenes. Continue M3-B then M4, preserving active HTML/save/portraits and documented QA gates. (Refs #2)
