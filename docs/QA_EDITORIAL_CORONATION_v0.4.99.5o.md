# M4-B Coronation Editorial — The Oath They Heard (5o)

**Implementation source:** `scripts/apply_coronation_5o.py` patches the existing 5n active HTML in place by creating a versioned 5o successor; it never rebuilds the engine. Scenes: m4_225_chamber, m4_225_liushan, m4_225_objections, m4_225_vigil, m4_225_investiture, m4_225_proclamation, m4_225_private, m4_225_decree.

Adds 23 English prose paragraphs in eight already-playable scenes: lawful succession, Liu Shan's independent answer, court objections, solemn vigil/seal ceremony, public proclamation, private aftermath, and first policy. All prior story choices, effects, state, save/import/export, assets and UI remain unchanged after exact source recovery. Chapters XIII–XIX remain unfinished.

**Status:** editorial patch authored; automated GitHub build workflow attempts to construct active 5o on this branch. This document does not claim browser QA, device testing or Codex Cloud completion. Source auditor requires the exact 5n SHA256, recovers 5n byte-for-byte by removing all new `data-auh5o` paragraphs and restoring version tags, and compares 35 portrait payloads. Run `python3 scripts/smoke.py` and `python3 scripts/qa_enthronement225.py` and `python3 scripts/qa_han_dragon229.py` (localhost Chromium) after generation, plus mobile long-page pagination and human editorial proofread, before merging.

Issues #1/#2 stay OPEN. Do not regard roadmap or prose completion as entire M4 completion.
