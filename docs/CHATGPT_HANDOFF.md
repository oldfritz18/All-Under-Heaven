# Melanjutkan All Under Heaven melalui ChatGPT

Paket transfer disiapkan atas permintaan pemilik16November2026. File game, dokumentasi dan riwayat yang diperlukan dapat dibaca tanpa bergantung pada konteks percakapan lama. Gunakan ChatGPT yang mendukung unggahan ZIP dan pengolahan file/kode untuk menghasilkan HTML berikutnya.

## Cara memakai

1. Unggah ZIP handoff ke percakapan ChatGPT yang baru, lalu berikan `PROMPT_LANJUT_CHATGPT.txt` di dalam paket.
2. Minta ChatGPT mengekstrak paket, membaca instruksi dan memverifikasi `TRANSFER_MANIFEST_SHA256.txt`. Jangan mulai dari ZIPstarter4m atau membuat game baru.
3. Acuan playable terakhir: `GAME/ACTIVE_BUILD.txt`, versi5n/The Standard He Chose, SHA-256 `15e85e566f259e9e253536f83710c00be4729ae7e69474c54451cb9e1eb9050d`, commit game `5f306bf46646c85203615cf4aff94c2745d91f29`. Build ini sudah dipush. Semua35gambar tertanam di HTML; tidak memerlukan folder portrait eksternal.
4. Baca dan lanjutkan pekerjaan yang disimpan di `WORK_IN_PROGRESS/5o/README.md`. Itu draf, bukan checkpoint yang sudah lulusQA. Rekonstruksi/review/targetedQA terlebih dahulu; pertahankan5n sebagai acuan valid sampai candidate layak dipromosikan.
5. Hasil tiap batch: HTML versi berikutnya yang dapat diunduh, catatan perubahan, hasil tes nyata beserta batasnya, dan PROGRESS yang diperbarui. Sertakan patch/source bila aksesGit tidak tersedia. Commit/push hanya dapat dilakukan bila sesi baru mempunyai aksesGitHub yang sah; fileZIP sendiri tidak memberikan autentikasiGitHub.

## Urutan membaca untuk sesi baru

`AGENTS.md` → `docs/START_HERE.md` → `GAME/ACTIVE_BUILD.txt` → `docs/PROGRESS.md` → `GOAL_MODE_PROMPT.md` → locked/approved design decisions → `ROADMAP/06_EMPEROR_DRAGONS_UNIFICATION_ARC.md` → WorldBible/MasterGDD dan rules sesuai pekerjaan. Snapshot Issue1/2 beserta komentar tersedia di `docs/issue_snapshots/`; bilaGitHub tersedia, periksa perubahan setelah waktu snapshot.

Mandat terbaru sudah disetujui: succession luar biasa tanpa adoption, termasuk new post223 mandate dengan actualLiuShan/court consent; Emperor tetap dapat langsung bertempur; paraDragon otonom; konsekuensi lintas UI/ending; maksimal5Dragon opsional, terpisah dari5SpecialStaff existing. Jangan meminta ulang keputusan tersebut, mengarang hidden testament atau memberi title/troops dari dokumen. Prosa/UI Inggris; laporan Indonesia tanpa spoiler.

## Keadaan implementasi

General222, jalur SixthTiger, lawful Shu accession/first decree, nominasi227 dan satu personal Dragon arc Han Sheng tersedia pada scope QA masing-masing.5n menambahkan actual receiving mission228(field/delegate), optional earnedGeneral/Dragon229, command handover dan aftermath/callback. Tetap ada jalur tanpa appointment. Ini **belum** fullM4/all0–5/collective, majorM5–M7/settlementsWei&Wu, XIX/Epilogue atau M8–M11. Issue1/2 tetapOPEN. Goal adalah instruksi berkelanjutan dalam sesi aktif, bukan proses latar ketika chat berhenti.

## Tes dan riwayatGit

`python3 scripts/smoke.py` adalah pemeriksaan statis8bagian. TargetedQA terbaru: `scripts/qa_han_dragon229.py`, `scripts/qa_dragon_nominations227.py`; bukti di `docs/qa/BATCH_5n.json`. Tes browser memakai PythonPlaywright, Chromium, Node dan baselineGit; ketersediaannya perlu diperiksa di sesi baru. Jangan menyatakan browser/physical-device`file://`lulus bila hanya static check yang dapat dijalankan. Jika tool belum tersedia, catat secara tepat dan lakukan pemeriksaan lain yang memang bisa dilakukan.

Paket lengkap menyertakan `REPOSITORY_HISTORY.bundle`, yaitu historyGit tanpa localconfig atau credentials. Untuk menjalankan comparatorGit di lingkungan baru, clone bundle ke **direktori baru**, misalnya `git clone --branch main REPOSITORY_HISTORY.bundle All-Under-Heaven-history`, lalu kerjakan pengujian di clone itu. Jangan clone atau checkout di atas proyek yang sudah berisi perubahan. Paket juga memiliki ordinary sourcefiles agar dapat dibaca tanpaGit. Bundle tidak memuat draft yang belum disimpan dalam commit; folderWIP yang disertakan merupakan acuan eksplisit untuk draft.

Tidak ada personal player save yang diberikan dalam sesi ini. Save/schema/QA import-export yang ada tetap harus dipertahankan. ZIPstarter awal ada dalam historyGit; tidak perlu menduplikasinya dalam working snapshot transfer. `INITIAL_MANIFEST_SHA256.txt` adalah bukti paket awal, sedangkan `TRANSFER_MANIFEST_SHA256.txt` memverifikasi paket transfer terkini.
