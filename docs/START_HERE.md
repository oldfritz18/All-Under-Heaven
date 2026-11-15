# All Under Heaven — Codex Goal Mode handoff

## Baseline dan build aktif
- File playable saat ini selalu ditentukan oleh `GAME/ACTIVE_BUILD.txt`. Lihat `docs/PROGRESS.md` untuk versi aktif dan hasil QA batch terbaru.
- Baseline handoff asli yang diverifikasi: `v0.4.99.4m`, disalin identik dari build chat; tersedia dalam ZIP starter dan commit inisialisasi `76f5684a8e191a5833bafdb8052de3597b952c04`.
- Perubahan berikutnya adalah penerus in-place dari engine tersebut. Git menyimpan setiap batch; `ROLLBACK/` menyimpan checkpoint terdahulu dan diperbarui pada milestone formal.
- Last known state from handoff: Chapter I rework in progress; prior chapters preserved. Reported 630 registered scenes, 46 historical NPC IDs, and 35 embedded pictures. The local smoke script performs static checks; it does NOT establish dynamic counts.
- Project coverage: Part I (190–223 CE), Prologue–Chapter XI; Part II (223–250 CE), Chapter XII–XIX and Epilogue. Historical ROTK route + meaningful alternate history.

## Required initial sequence
1. Read `AGENTS.md` and locked decisions, then relevant GDD/World Bible and roadmap sections. Do not load all giant texts indiscriminately if targeted references are enough.
2. Run `python3 scripts/smoke.py` and inspect existing game scene registry, branching, ranks and saves.
3. Audit only actual blockers before declaring Chapter I ready; stop polishing already-correct scenes endlessly.
4. Implement the next largest coherent narrative/gameplay group, preserve all existing functionality, and verify with actual tests.
5. Update `docs/PROGRESS.md` and `GAME/ACTIVE_BUILD.txt` as appropriate, commit to Git, continue toward the persistent Goal.

## Locked-decision precedence
The `LOCKED_DESIGN_DECISIONS_2026-11-15.md` file was written when v0.4.99.4i was active. Its design decisions are still binding, but its *baseline filename* is historical. v0.4.99.4m above is the later executable baseline.

## Review checkpoints
- After Chapter I rework is cohesively playable, proceed to Chapter II and beyond with the same quality standard.
- Record playable scenes, historical NPC participation, battlefield positions, career milestones, emotional/romantic/comedy threads and systems synchronized.
- If a test or user approval blocks the work, report a precise blocker. Do not claim work continued when it has stopped.
