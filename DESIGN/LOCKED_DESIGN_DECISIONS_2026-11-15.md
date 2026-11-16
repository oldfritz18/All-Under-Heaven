# ALL UNDER HEAVEN — LOCKED DESIGN DECISIONS

**Date agreed:** 15 November 2026  
**Status:** APPROVED / carry forward to every future development chat  
**Current HTML baseline:** `ALL_UNDER_HEAVEN_v0.4.99.4i_CHAPTER_I_COMMAND_AND_COMRADES.html`  
**Scope:** This file is a design-decision handoff, not a save file, and does not alter the game code.

## Locked decision A — Five Dragon Generals

- The protagonist will have **exactly five signature Dragon General positions** as a future legendary command circle (the *Five Dragon Generals*).
- These are **not five rigid troop-type classes**. Do not classify a general permanently as an “Infantry General” or “Cavalry General”. Infantry/cavalry may be specialties or assignments; a general can command combined arms when entrusted with suitable authority.
- Each future Dragon General must have a distinct personality, combat doctrine, ambition, strengths, weaknesses, personal arc, autonomy, and memorable moments. Make their relationships fun and emotionally engaging, with camaraderie, rivalry, and recurring comedy, analogous in *group dynamic* (not copied story or characters) to Luffy's crew.
- Membership is **earned**, never pre-awarded: the characters must meet, develop trust, freely choose commitments, and receive appropriate military posts through the story. A candidate may be original or historical if consistent with the game's historical/canonical constraints. No five names are yet definitively assigned; do not treat prior role examples as fixed appointments.
- They do **not** serve the protagonist in Chapter I merely because of future plans.

## Locked decision B — Special Staff: preserve existing game system

**DO NOT replace or expand Special Staff by inventing a new 5–7-seat staff structure.** Continue using exactly these five roles already defined in v0.4.99.4i (`AUH_MC_SPECIAL_STAFF`):

| Existing Special Staff role | Rank at which seat becomes eligible |
|---|---|
| Personal Assistant | Sergeant |
| Strategist | Captain |
| Quartermaster | Captain |
| Deputy Commander | Major |
| Intelligence Officer | Major |

- Rank eligibility **unlocks potential access only**. The protagonist must earn the rank, and each appointment must be supported by actual game state, role availability, NPC consent/eligibility, and an explicit story decision. No auto-hire or fake promotion.
- The code also contains `AUH_MC_DEMO_STAFF` sample/demo names. **These are demonstration placeholders, not proof of live appointments.** Preserve the difference.
- Five Dragon Generals and five Special Staff roles are **separate structures**. A trusted friend need not occupy either; no NPC is guaranteed a position.

## Locked decision C — Starting situation and advancement

- In **Chapter I, year 190 CE**, the male protagonist is **16 years old**, an **ordinary Infantry Private** under Han Sheng, with no personal command or troops. Universal Timeless Heroes remains the world convention.
- Liu Bei leads his contingent; Guan Yu and Zhang Fei already possess military authority and experience. The protagonist does not start as their peer.
- Military experiences are lived within the rank and file: unit, formation, commander, surrounding soldiers, visible enemies, objective, location changes, credible information limits, and orders must be clear. While serving as a rank-and-file soldier, assignments can be Infantry or Cavalry, **not Support**.
- Promotions, honors, commands, and future generals must be **earned and felt narratively**. Recognition and relationships are not the same as appointment.

## Locked decision D — Narrative tone and companion relationships

- Prioritize (1) historical NPCs and ROTK campaigns, (2) immersive soldier-perspective warfare, (3) epic novel-like English prose, (4) character-driven comedy and recurring jokes, (5) adult life and romance paced to chronological age and consent, (6) meaningful rank progression, and (7) distinct future Dragon General and Special Staff story arcs.
- Characters retain their own dreams and agency; loyalty is developed over years and can be tested. Include daily life, banter, celebrations, emotional aftermath, mistakes, and personal triumphs.
- Any intimate adult scenes should be non-graphic / metaphorical; do not sexualize underage characters.
- Historical NPCs must be introduced only through plausible hearing, witnessing, or direct encounters; preserve spoiler-safe People records, Chronicle, Military, Civic, Character, and saves.
- Portrait work remains postponed. Reuse existing valid images and scenes.

## Locked decision E — Development workflow

- **Fast Development:** continue from the existing HTML, never recreate the game from scratch; focus on substantial integrated narrative/gameplay batches; run targeted QA; preserve old valid scenes, choices, saves, and portraits.
- A full checkpoint ZIP is **not** required for each small update. Make ZIP when a milestone is completed, before major changes, or when transferring to another chat. Provide updated HTML and brief change/QA notes as needed.
- Game language: English. Development discussion: Indonesian. User-facing progress updates should avoid story spoilers.

## Handoff instruction for future chats

Treat the sections above as approved decisions. **Do not ask the user to reconfirm Five Dragon Generals or the five existing Special Staff positions.** Before altering them, check this file and the most recent HTML/GDD, and seek a new explicit user decision if a change would contradict these locked rules.

This note does not assert that all five Dragon Generals have been implemented or assigned in the active build.

## Addendum disetujui 16 November 2026 — Issue #1

[Issue #1](https://github.com/oldfritz18/All-Under-Heaven/issues/1) menetapkan mutu pengakuan General, klimaks Sixth Tiger pada shared-life window sah, multi-scene enthronement Emperor of Shu dan personalized earned Five Dragon investitures/collective scene setelah lima appointment sah. Kontrak: [APPROVED_EPIC_ELEVATIONS_ISSUE_1.md](APPROVED_EPIC_ELEVATIONS_ISSUE_1.md), wajib dibaca bersama dokumen ini. Keputusan A–E tetap berlaku; tambahan ini tidak memilih mekanisme dinasti yang belum diselesaikan atau mengklaim implementasi selesai.
