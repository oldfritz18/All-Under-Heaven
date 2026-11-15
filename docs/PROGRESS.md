# Development progress — Codex handoff initialization

## Baseline
- Active: v0.4.99.4o; baseline awal terverifikasi v0.4.99.4m.
- Status: batch Chapter I dan Chapter II selesai pada cakupan review/QA yang dicatat. Pengembangan berikutnya: Chapter III dan checkpoint M1, lalu IV dan seterusnya secara berurutan.
- Goal mode status: AKTIF atas perintah eksplisit pengguna dalam percakapan ini. Objektif: Prologue–Chapter XIX dan Epilogue sesuai M0–M11; belum selesai.

## Evidence already in repository
- `docs/QA_RECEIPT_v0.4.99.4m.md` — scope and limits of previous targeted QA.
- `docs/CHANGELOG_v0.4.99.4m.md` — last baseline change.

## Next work
- Chapter III: tinjau pemulihan, relasi, penilaian layanan dan integrasi state sebelum checkpoint M1.
- Lanjutkan IV–XIX dan Epilogue sesuai roadmap. Jangan menyamakan hasil QA sampel dengan kelulusan editorial seluruh cabang atau rilis M11.

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

## Batch Chapter I — v0.4.99.4n, selesai
- Empat adegan perkenalan Wei Zhen, Han Sheng, dan Xu Wen diperluas dengan dialog, keterbatasan pengetahuan, koreksi yang diterima NPC, pilihan menolak kedekatan, dan konteks tugas infanteri.
- Jawaban kepada Wei Zhen mendapat flag eksplisit baru yang opsional; gate, People dan Chronicle mencerminkan jawaban aktual. Ingatan baru memerlukan bukti visit/history; tidak diisi otomatis pada save lama.
- Tidak ada ID scene, label/tujuan pilihan lama, relasi/stat lama, rank, pasukan, portrait, atau schema save yang dihapus atau diganti. Jumlah registry tetap 630; 35 gambar tertanam identik.
- Bukti: `python3 scripts/smoke.py` 8/8; `python3 scripts/qa_chapter1.py --report /workspace/work/chapter1_qa.json` lulus 262 edge pada 93 scene sampel per viewport 390/1280, parity state lama, JSON save/reload HTTP, migrasi save baseline, provenance visit/history, pagination/pilihan/menu DOM, tanpa page error.
- Catatan QA dan batas: `docs/QA_CHAPTER_I_v0.4.99.4n.md`. Gate ini mengizinkan kelanjutan berurutan ke II; bukan klaim seluruh kombinasi pilihan, editorial M10, Android/file://, atau rilis M11 telah lulus.

## Batch Chapter II — v0.4.99.4o, selesai
- Tujuh scene Pan River dan scene surat antarpasukan diperluas dengan ketidakpastian medan, perintah yang benar-benar terdengar, formasi dan rekan terdekat, risiko pilihan, tindakan mandiri pihak lain, serta aftermath personal.
- Bug terbukti: baseline masih menyimpan `fieldPosition.active=true` ketika pemain sudah sampai di laporan sore. Penarikan yang dipilih kini menutup posisi tersebut sebelum laporan; Military dan People mengingat gerakan yang benar-benar dipilih, Chronicle mencatatnya sekali.
- Migrasi hanya mematikan posisi Pan yang cocok dengan proof, pilihan, branch Infantry, tahun 191, scene laporan dan bukti visit/history. Tidak ada penugasan, reward atau ingatan baru yang dibuat untuk flag-only, cavalry, proof lain atau scene lain.
- Smoke 8/8; `scripts/qa_chapter2.py` lulus 70 edge pada 43 scene sampel dan 27 rute taktis lengkap per viewport 390/1280. Rute mencakup seluruh pasangan keputusan dari enam pilihan tiga-arah; bukan seluruh kombinasi. Dua kasus migrasi positif dan empat negatif per viewport, save/reload HTTP serta Military/People/Chronicle lulus, page error 0.
- Semua ID, label/tujuan pilihan, portrait dan state lama identik selain perbaikan status posisi yang disengaja beserta satu catatan Chronicle baru. Detail: `docs/QA_CHAPTER_II_v0.4.99.4o.md`.
