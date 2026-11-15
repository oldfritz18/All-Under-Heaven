# Development progress — Codex handoff initialization

## Baseline
- Active: v0.4.99.4m, 15 Nov 2026
- Status: Chapter I rework ongoing. Later chapters in the baseline preserved but not claimed fully completed.
- Goal mode status: NOT YET ACTIVATED by user. No Codex session has been started by this package.

## Evidence already in repository
- `docs/QA_RECEIPT_v0.4.99.4m.md` — scope and limits of previous targeted QA.
- `docs/CHANGELOG_v0.4.99.4m.md` — last baseline change.

## Next work
- Confirm current active file and smoke test.
- Complete a focused Chapter I narrative and state-integration pass; verify before proceeding.
- Then implement Chapter II+ in larger story/campaign batches, prioritizing the historical cast and believable future companion/staff arcs.

## QA limitations
- Actual device `file://` persistence remains UNTESTED; do not label as passed.
- This repository package itself does not prove all branches playable or tests passed; Codex should perform its own verification.

## Inisialisasi repositori — selesai
- Struktur proyek dipindahkan dari `ALL_UNDER_HEAVEN_CODEX_GOAL_READY/` ke root repositori pada branch `main`; tidak ada file tujuan yang ditimpa. Folder pembungkus yang kosong telah dihapus.
- `AGENTS.md`, `GAME/`, `DESIGN/`, `docs/`, `scripts/`, `GOAL_MODE_PROMPT.md`, serta `ROADMAP/`, `RULES/`, dan `ROLLBACK/` tersedia di root. ZIP starter dan README yang sudah terlacak tetap dipertahankan.
- Verifikasi setelah pemindahan: seluruh 26 file tetap identik secara byte; `python3 scripts/smoke.py` lulus 8/8 pemeriksaan; `sha256sum -c INITIAL_MANIFEST_SHA256.txt` cocok untuk seluruh 25 entri sebelum catatan ini ditambahkan.
- Manifest awal tetap menjadi bukti baseline paket asli; checksum `docs/PROGRESS.md` akan berbeda karena pembaruan dokumentasi ini.
- Build aktif tetap v0.4.99.4m. HTML aktif, rollback, gameplay, dan format save tidak diubah. Goal pengembangan belum diaktifkan.
- Tidak ada pengujian gameplay interaktif atau perangkat nyata dalam inisialisasi ini; batas QA sebelumnya tetap berlaku.
