# Development progress — Codex handoff initialization

## Baseline
- Active: v0.4.99.4s; baseline awal terverifikasi v0.4.99.4m.
- Status: checkpoint fungsional M1 (I–III) dan batch IV–VI selesai pada cakupan review/QA yang dicatat. M2 berlanjut ke VII; M3–M11 belum selesai.
- Goal mode status: AKTIF atas perintah eksplisit pengguna dalam percakapan ini. Objektif: Prologue–Chapter XIX dan Epilogue sesuai M0–M11; belum selesai.

## Evidence already in repository
- `docs/QA_RECEIPT_v0.4.99.4m.md` — scope and limits of previous targeted QA.
- `docs/CHANGELOG_v0.4.99.4m.md` — last baseline change.

## Next work
- Chapter VII: audit Runan/Jingzhou, promosi yang diterima/ditolak, kepemilikan unit, konsekuensi relasi dan posisi tempur sebelum checkpoint M2. W07/Xiapi tetap cakupan laporan dunia; W08 dan kampanye berikutnya perlu rekonsiliasi terhadap timeline aktual.
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

## Checkpoint M1 — v0.4.99.4p, selesai pada cakupan bertarget
- Dua scene opsional pada 192 ditambahkan setelah `ch03_02`, dengan jalur Continue lama tetap tersedia. Wei Zhen, driver dan Han Sheng dapat saling mengoreksi; protagonis tidak mengeluarkan perintah perjalanan.
- Jalur perkenalan 191 + pemeriksaan bersama 192 + persetujuan eksplisit kini dapat membuka kesempatan personal adviser pada 193 meskipun 190 dilewatkan. Baru bertemu pada 192 tidak cukup; menolak pada 192 dihormati; tawaran asli 190 + 191 tetap ada.
- Keanggotaan tetap membutuhkan pilihan menerima pada 193. Tidak ada Special Staff, pangkat atau unit baru dari hubungan personal. Efek baru idempotent; People/Chronicle dan recall menghormati visit/history.
- Registry 632: seluruh 630 ID lama dipertahankan, ditambah dua scene opsional. Semua 35 gambar dan lima role/threshold Special Staff tetap identik.
- `scripts/qa_m1.py`: 14 scene III, 28 edge lama identik dan tujuh edge opsional baru; tujuh rute Prologue–193 per viewport 390/1280, masing-masing 146–148 pilihan. Accept/refuse, peluang kedua, pertemuan terlambat, save/reload, efek berulang, history-only, flag-only, bypass Pan Cavalry/tahun lebih akhir, dan UI People lulus; page error 0.
- Checkpoint juga menjalankan ulang `qa_chapter1.py` dan `qa_chapter2.py` pada build 4p: seluruh hasil bertarget lulus. Batas full-combination, editorial seluruh novel dan perangkat nyata tetap terbuka; tidak mengklaim M8–M11 selesai.
- Rollback milestone: v0.4.99.4o. Rincian dan hash: `docs/QA_M1_v0.4.99.4p.md`.

## Batch Chapter IV — v0.4.99.4q, selesai
- Tujuh scene diperluas: komitmen sahabat, Yao Qing, Pei Liang, teh Lin Yue, serta kontak Beihai, kabar Xu Province dan defence orchard. NPC memiliki tugas dan pilihan sendiri; relasi tidak mengganti kewenangan formal.
- Bug terbukti: saat bertempur di Beihai/Xuzhou 194, Military masih menunjukkan posisi Pan River 191. Lima event pilihan kini mencatat posisi, objective, section leader, proof dan status aktif/terakhir; branch, unit, pangkat dan Special Staff dipertahankan.
- Migrasi memerlukan scene tujuan yang cocok, pilihan valid, branch yang sudah tercatat serta visit/history aktual. Tidak menimpa posisi lebih baru, penugasan 194 lain yang sah, atau membuat branch dari flags/tahun saja. Marker event mencegah replay menimpa posisi setelahnya.
- Kronologi Lin Yue dikoreksi: perkenalan pada III sekarang berada di 192, sehingga rujukan pasti dua tahun pada IV 193 tidak lagi digunakan. Kalimat kepemilikan/komando atas bridge party diganti dengan tindakan prajurit di bawah section leader.
- `scripts/qa_chapter4.py`: 20 scene, 53 edge; 54 rute kampanye per viewport 390/1280 (27 Infantry, 27 fixture Cavalry), seluruh pasangan delapan pilihan tercakup; 10 migrasi positif, enam negatif, replay, date/age gate, HTTP save/reload aktif/terakhir dan UI Military lulus; page error 0. Rincian: `docs/QA_CHAPTER_IV_v0.4.99.4q.md`.

## Batch Chapter V — v0.4.99.4r, selesai
- Tujuh scene singkat tentang Qin Rui, Deng Yu, Yao Qing, Pei Liang, pertemuan sahabat dan kuda pendamping diperluas. Kewajiban mandiri, hak menolak, koreksi dan care tetap lebih penting daripada label pendamping.
- Tiga scene kampanye W05 pada 197 ditambahkan sebelum transisi lama ke VI/198: penugasan, kontak lokal, aftermath. Pilihan field/district/both tetap tersimpan dan menentukan sektor penugasan tempur; bukan perpindahan ke support/administrasi.
- Seluruh efek lama pada exit V dipertahankan; hanya transisi waktu ditahan pada 197 sampai arc baru selesai, lalu kembali ke 198/usia 24. Save yang sudah berada pada 198 atau lebih akhir tidak dipundurkan dan tidak menerima credit baru.
- Registry 635: 630 ID baseline + dua opsional III + tiga kampanye V; 35 gambar dan sistem lama dipertahankan. Tidak ada promosi, pasukan, barang, kuda, atau anggota circle gratis dari arc baru.
- `scripts/qa_chapter5.py`: 16 scene, 33 edge lama dan delapan edge scene baru; seluruh 108 kombinasi lokal (preferensi, Infantry/fixture Cavalry, posisi, aksi, laporan) per viewport 390/1280 lulus. Parity, chronology, penutupan posisi, consent/no-grant, recall VI, idempotence, legacy 198, flag-only dan HTTP reload lulus; page error 0.
- Rincian serta sumber adaptasi historis: `docs/QA_CHAPTER_V_v0.4.99.4r.md`. Berikutnya VI–VII; objective penuh belum selesai.

## Batch Chapter VI — v0.4.99.4s, selesai pada cakupan W06
- Empat scene Xiaopei 198 ditambahkan khusus pilihan forward-service, dengan penugasan, tekanan, penarikan dan after-action. Pilihan lain tetap menuju scene lama; save yang sudah lebih akhir tidak dipundurkan.
- Tiga aksi menimbulkan konsekuensi lokal berbeda: hilangnya ransum bersama, keterlambatan demi comrade, atau rusaknya shield perusahaan. Ini bukti naratif unit yang disaksikan, bukan pengurangan/pemberian barang pribadi atau angka korban rekaan. Protagonis tidak memenangkan kampanye atau menggantikan duel komandan ROTK.
- Posisi aktif ditutup setelah file mencapai collecting point; People/Chronicle dan recall akhir 198 memakai visit/history aktual. Rank, branch, unit, circle, staff, coins dan items dipertahankan.
- Bahasa awal VI dan rekomendasi council dikoreksi agar Private menyampaikan laporan/rekomendasi, bukan memerintah clerk atau mendirikan otoritas sipil. Peran belakang garis tetap perlindungan bersenjata, bukan transfer Support.
- `scripts/qa_chapter6.py`: 12 scene lama + empat baru, 25 edge lama dibandingkan pada input identik dan 11 edge scene baru; seluruh 108 kombinasi lokal per viewport 390/1280 lulus, termasuk no-grant, posisi, bypass preference/tahun, flag-only, idempotence, save/reload serta UI Military; page error 0.
- Registry 639, seluruh ID lama dan 35 gambar dipertahankan. Rincian: `docs/QA_CHAPTER_VI_v0.4.99.4s.md`. VII dan M2 secara keseluruhan belum selesai.
