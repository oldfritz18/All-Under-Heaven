# Fire assault–settlement — v0.4.99.4z

Build: `GAME/ALL_UNDER_HEAVEN_v0.4.99.4z_FIRE_AND_THE_RECEIVING_BANK.html`.

SHA-256: `1fc2cf5a197f1c5fe0e89e20d895b47f10910b26c3639523e97f77ec798bafdb`. Bukti: `docs/qa/BATCH_4z.json`.

## Perubahan dan kontrak

Dua puluh node legacy dari anchorage sampai exit 209 dipertahankan dan direvisi untuk jalur Private/Sergeant/Captain: briefing Huang Gai, laporan intelijen, ruse, daily life, perubahan angin, kontak tempur, tiga aksi lokal, api, collision, laporan shore section, tiga objective, pursuit, pagi, hearing serta respons terhadap settlement. Pilihan tetap menentukan engagement yang membuka/menahan passage dan memengaruhi hasil perang; NPC mempertahankan rencana serta pasukannya sendiri.

Perhitungan leverage, empat outcome, enum, route dan efek lama dipertahankan. Aksi pemain dibedakan dari **laporan** kedudukan koalisi. `independent_command` lama tetap sebagai enum untuk kompatibilitas; pada jalur company artinya laporan crossing sekutu yang terpisah dan dipersengketakan, bukan grant armada/provinsi pribadi. Global world result tetap dapat berbeda karena tindakan yang dipilih; bukan kemenangan historis yang dipaksakan.

`campaignEvidence.redCliffs208` dicatat pada exit laporan pagi, membutuhkan order proof yang benar-benar diterima, sumber, kunjungan battle, aksi/branch/outcome valid. Posisi tempur retired sebelum 209. Military/People/Character/Chronicle dan callback IX–XI mengikuti scope yang sama; status/posisi lebih akhir tidak menghapus bukti dinas lama. Record dan render idempotent/read-only. Tidak ada backfill receipt ketika import/save hanya mengandung flags.

Komisi Captain 209 tetap opsional: field choice menyebut penerimaan tertulis; Sgt baru memerlukan receipt dinas atau review legacy yang sah. Watch lama yang sesuai dikembalikan pada acceptance, tanpa hadiah pasukan/staff. Captain yang sudah menerima pada 208 tidak memperoleh promosi kedua. Private tetap Private; pilihan lain tidak menerima komisi. Tawaran pada save 4y asli dipertahankan. Resume lebih tua dengan warrant/watch sah, tetapi tanpa proof order 4x/4y, dapat menjalani review sesudah kontak yang dimainkan; ini mempertahankan tawaran lama tanpa membuat receipt W14 baru.

Prosa tempur dan briefing company adalah fiksi orisinal dalam kerangka ROTK. Referensi anchor yang telah dibaca: ROTK bab 49, https://kongming.net/threekingdoms/49 (15 November 2026), terutama fire ships/angin, komando Zhou Yu–Huang Gai serta kewajiban Zhao Yun mengawal Zhuge Liang. Node shore baru memakai laporan section dan tidak memindahkan Zhao Yun langsung ke command boat pemain. Tidak menyalin terjemahan atau mengklaim pertempuran company fiktif sebagai sejarah tercatat.

## Cakupan verifikasi

`scripts/qa_red_cliffs.py` menguji per viewport 390/1280:

- 324 rute: empat karier organik, dua branch, 27 baris pairwise sembilan kelompok pilihan; tambahan dua persiapan lemah. Cavalry adalah fixture legacy sintetis. Harness mengassert seluruh pasangan lokal, bukan seluruh produk Kartesius.
- Empat hasil perang terjangkau. Dua matriks rute penuh (strong Captain, weak Private) mempunyai result, leverage, cost, rank dan kalender yang identik dengan 4y.
- Tahun/usia 208/34 → 209/35 → 210/36; acceptance/refusal dan commission count benar; watch tidak terhitung dua kali. Tidak ada staff/ship/goods/recruit grant tambahan.
- Receipt, flag-only, enum invalid, history-only, idempotence/read-only, legacy no-backfill, original legacy offer serta synthetic older-order midarc resume.
- Reload localStorage HTTP, Military DOM dan 20 klik browser nyata memakai seed Private/history penuh; tanpa page error/overflow.

`scripts/qa_red_cliffs_legacy.py`: body, label, destination dan efek **20 node** fixture Major dibandingkan dengan 4y. Ini fixture kompatibilitas sintetis, bukan bukti Major diperoleh organik atau sertifikasi fiksi strategis legacy.

Regresi `scripts/qa_river_patrol.py`: 216 rute dan sembilan klik DOM per viewport, termasuk sembilan node legacy Major dan parity efek patroli. Smoke 8/8, JS syntax/35 embedded images byte comparison melalui fixture, serta Python compile dijalankan terpisah. Matriks mematikan render/save/scroll sementara dan mengosongkan body history lama sebagai string; uji DOM terpisah memakai history penuh dan penyimpanan asli.

## Batas

Registry tetap 658; semua 650 ID 4u serta delapan pembuka VIII dipertahankan. Engine/save key dan portrait tidak diganti. Belum gate M3 sampai XI, belum editorial seluruh cabang dan belum uji perangkat nyata/Android/file://. Pemetaan label VIII–X masih perlu direkonsiliasi. Prosa/otoritas 210–223 berikutnya tetap harus diaudit, termasuk jabatan/pasukan yang sah. Tidak ada push, biaya atau perubahan locked decisions.

Eksekusi final: smoke 8/8 dan ketiga suite di atas PASS pada hash identik. Percobaan awal harness legacy mengubah rank sesudah komisi telah masuk history, sehingga fixture tidak konsisten; diperbaiki dengan snapshot asli sebelum tawaran, bukan menghapus catatan komisi. Setelah review kasus midarc, compatibility guard ditambahkan dan seluruh suite terkait dijalankan ulang.
