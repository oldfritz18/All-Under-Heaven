# Rekonsiliasi VIII–IX–X — v0.4.99.5a

Build: `GAME/ALL_UNDER_HEAVEN_v0.4.99.5a_CHAPTERS_VIII_IX_X_RECONCILED.html`.

SHA-256: `518ffc85a164668f5322012fe626a19d9bcba5a7b0d6e896da59e79c415c2bc6`. Bukti gabungan: `docs/qa/CHECKPOINT_5a.json`.

## Pemetaan

| Bab tampil | Rentang / cakupan | Registry |
|---|---|---:|
| VIII | 208: packet pembuka, Bowang, Xinye, review dinas | 10 scene |
| IX | 208: dewan retreat, Changban, Hanjin, councils/patrol dan Red Cliffs sampai laporan pagi | 61 scene |
| X | 209 settlement dan rangkaian legacy 210–219 | 84 scene |

503 scene lainnya tidak direklasifikasi; total tetap 658. Ini metadata dan heading tampilan, **bukan** penggantian `ch08_*`/`ch09_*` IDs. `sceneChapter()`, tabel clock, nilai act, pilihan, efek serta history lama tetap. Save tidak diberi birthday, promosi, pasukan, kewenangan atau credit karena label bab berubah.

Jalur baru menampilkan heading VIII sekali pada foreword, IX sekali pada dewan retreat, X sekali pada awal settlement 209. Header lama di core 208/210/214 dihilangkan hanya saat entry terdahulu sudah dimainkan; direct legacy entry masih menampilkan heading yang benar. Reader tetap mempertahankan ribbon tahun dan prosa lama yang valid. Detail Campaign W11/W12 di tag pembuka menjadi nama Bowang/Xinye.

Developer fixtures dikelompokkan menurut metadata scene yang aktif. Isi fixture dan state-nya tidak ditulis ulang. Fixture legacy yang jarang tidak otomatis menjadi contoh baru VIII atau seluruh cabang IX; absennya checkpoint untuk suatu scene bukan berarti scene itu tidak bisa dimainkan melalui cerita. Tidak membuat fixture sintetis yang diklaim organik.

## Bukti awal yang telah dijalankan

`python3 scripts/qa_chapter_map.py --report /workspace/work/5a_map.json`: PASS pada 390/1280 px. Dua rute organik dari 207 sampai 214 (Captain dan tetap Private) mempertahankan seluruh rangkaian scene/act/tahun/usia/rank/muster dan **final state identik** dengan 4z kecuali teks heading di history yang sengaja dikeluarkan dari perbandingan. Semua field/metadata history lainnya tetap dibandingkan.

Heading VIII/IX/X muncul tepat sekali pada 208/208/209. Legacy direct entries dan reload 210 menjadi label X dengan clock tetap 210. Metadata/view read-only, inspector grouping serta tabel calendar inference lama PASS; page error/overflow 0. Percobaan awal menemukan helper legacy sudah menghapus heading core VIII berdasarkan flag lama; fallback direct-entry diperbaiki agar selalu menyediakan satu heading yang benar.

Normalisasi QA baru menghapus **hanya** H2 chapter-title-inline untuk perbandingan prosa legacy, karena heading kini diuji tersendiri oleh suite map. Paragraph naratif, ID, label/tujuan pilihan, flag dan state/effect lainnya tetap dibandingkan. Ini bukan pelonggaran assert outcome atau izin menghapus prosa valid.

## Batas

VIII/IX dan boundary M2 diuji pada cakupan bertarget; M3 sampai XI, editorial semua cabang, pemerintahan XII–XIX/Epilogue dan rilis M11 belum selesai. Reklasifikasi 84 scene X tidak menyatakan isi/otoritas 210–219 sudah lolos audit. `file://` perangkat nyata/Android masih belum disertifikasi. Tidak ada biaya, push atau perubahan locked decisions.

## Checkpoint gabungan, dieksekusi

Smoke 8/8 dan delapan suite pada hash identik PASS: `qa_chapter_map`, `qa_chapter8`, `qa_changban`, `qa_river_councils`, `qa_river_patrol`, `qa_red_cliffs`, `qa_red_cliffs_legacy`, `qa_m2_continuity`. Semua memakai Chromium 390/1280; tidak ada page error. Coverage masing-masing tersimpan terpisah dalam receipt; tidak dijumlahkan menjadi klaim seluruh kombinasi novel.

Perintah: `python3 scripts/<nama_suite>.py --report /workspace/work/5a_<nama_suite>.json`; suite map menggunakan `/workspace/work/5a_map.json`. Report mentah beserta stdout disimpan di direktori kerja, ringkasannya di `docs/qa/CHECKPOINT_5a.json`. Node syntax check/byte comparison 35 portrait dilakukan fixture; registry 658. Rollback formal kini 4z, yang disalin dari commit `e7293d0` dan dicocokkan SHA-256. 4t serta semua penerus tetap tersedia di Git; tidak membuat ZIP.

Audit baca lanjutan X mencatat 70 kunjungan/64 ID pada satu rute default hingga entry XI/220, dengan Captain/60 Infantry masih sama. Ini observasi batas progresi dan mandat, bukan pembuktian semua route atau permintaan promosi otomatis. Prioritas berikutnya: `docs/CHAPTER_X_AUDIT_v0.4.99.5a.md`.
