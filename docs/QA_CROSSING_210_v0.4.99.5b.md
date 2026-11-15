# Crossing terms, 210 — v0.4.99.5b

Build: `GAME/ALL_UNDER_HEAVEN_v0.4.99.5b_THE_WITNESSED_CROSSING.html`.

SHA-256: `3a3ab03daf1c775996fa862cfe6389423f398d87e680e034bff6c743b4671dff`. Bukti gabungan: `docs/qa/BATCH_5b.json`.

## Perubahan

Sembilan node legacy `ch09_p57_01_tide`–`ch09_p57_09_depart` diperluas untuk Private/Sergeant/Captain. Hearing, laporan terpisah, surat beberapa pihak, empat proposal, tugas tempur di western landing, tiga tindakan, relief, balasan dan departure kini tersambung ke perintah company dan active muster. Perwira/boatmaster/household delegates mempunyai kewenangan masing-masing; rekomendasi tidak langsung menjadi armada atau provinsi pemain.

Rangkaian ini adalah fiksi lokal yang sudah ada dalam kerangka dunia 210; prosa company baru orisinal, tanpa menambah klaim pertempuran kanonik atau pertemuan historis baru. Dialog, humor, klaim keluarga, penarikan dan keterbatasan informasi tetap menjadi bagian adegan. Optional letter detour yang valid dipertahankan.

Semua ID/tujuan/enum, formula delapan hasil negosiasi, skor/relasi serta efek lama tetap. Nama tampil hasil baru menyebut local crossing terms; nilai enum lama seperti `independent_mandate` tetap. Ini tugas/arrangement setempat, bukan promosi, rekrutmen atau territorial office. Record Civic/rank/unit/staff/goods tidak berubah; Civic tidak menampilkan Governor yang tidak ditunjuk.

`campaignEvidence.crossing210` opsional dicatat ketika reply ditandatangani, membutuhkan order proof/relief dan visit/history yang benar. `fieldPosition` aktif pada tugas dan retired pada receiving line. Military, Character serta ingatan Han Sheng/Xu Wen membaca sumber yang sama; load/render tidak menciptakan receipt. History-only valid; flag-only, enum invalid, branch tak diketahui dan tahun lebih akhir tidak memberi receipt baru. Posting tahun lebih akhir tetap utuh. Legacy Major tetap melalui body/choice/effect lama.

## Eksekusi

- `python3 scripts/smoke.py`: 8/8 PASS.
- `python3 scripts/qa_crossing210.py --report /workspace/work/5b_crossing210.json`: **504 rute per viewport 390/1280**. Seluruh pilihan lokal 3 testimony × 4 policy × 3 action, dua branch, tujuh seed karier/world yang dipilih secara organik: empat kondisi perang pada Captain, dua riwayat Sergeant berbeda, serta tetap Private. Cavalry merupakan fixture sintetis. Bukan seluruh perkalian world × semua karier.
- Delapan balasan terjangkau. Satu matriks penuh hasil identik dengan 5a; seluruh efek opsi sembilan node dibandingkan pada input sama, kecuali field/receipt/scope dan Chronicle yang disengaja. Sembilan node Major body/label/tujuan/effect parity PASS.
- Tidak ada perubahan rank/muster/staff/coins/items/circle/civic office; posisi aktif/relief, provenance, read-only/idempotence, legacy no-backfill dan posting lebih akhir PASS.
- Reload localStorage HTTP dan Military DOM PASS; **11 klik browser nyata** dengan history penuh mencapai departure dari rute Private; page error/overflow 0.

Regresi Red Cliffs (`qa_red_cliffs.py`) dan route/map 207–214 (`qa_chapter_map.py`) dijalankan pada hash sama. Suite map mengenali hanya perubahan 5b yang didokumentasikan: optional receipt/scope, posisi 210 yang menggantikan posisi retired 208, empat teks Chronicle, serta label pilihan pada history sembilan node yang direvisi. Semua field lain dan urutan/clock/rank/muster tetap dibandingkan. Posisi/receipt yang dinormalisasi tersebut diuji terpisah secara penuh oleh suite crossing, bukan diabaikan tanpa verifikasi.

Matriks memakai `choose`/validasi asli dengan paint/storage/scroll dimatikan sementara serta body history lama dikosongkan sebagai string. Jalur DOM/reload memakai render/storage asli. JS syntax dan 35 embedded images byte comparison dilakukan fixture. Registry tetap 658, save key/engine utama tetap. Rollback formal tetap 4z; 5a tersedia dalam Git.

Ini batch pertama X, bukan gate seluruh X–XI/M3, editor M10 atau rilis perangkat nyata M11. Charter 211–213, mismatch tahun messenger 214/215, Yi/Hanzhong/Jing dan karier berikutnya tetap perlu kerja. Tidak ada biaya, portrait baru atau perubahan locked decisions.

Regresi pada hash identik PASS: Red Cliffs 324 rute dan 20 klik DOM per viewport; dua perjalanan map Captain/Private 207–214 dengan proyeksi perubahan crossing yang dinyatakan di atas. Semua tiga suite pada 390/1280 tanpa page error. Batas historis pada string `limits` suite Red Cliffs menggambarkan cakupan suite tersebut; pemetaan chapter sudah diuji terpisah.
