# Open Bank Charter, 211–213 — v0.4.99.5c

Build: `GAME/ALL_UNDER_HEAVEN_v0.4.99.5c_THE_OPEN_BANK_CHARTER.html`.

SHA-256: `d12a1b5f660a3a5802e31271679dd01e450f7b9da63ca0db5b55b7a60e08dbfd`. Bukti gabungan: `docs/qa/BATCH_5c.json`.

## Perubahan dan kontinuitas

Lima node legacy `ch09_charter_council` sampai `ch09_charter_aftermath` diperluas untuk jalur Private/Sergeant/Captain baru. Prosa orisinal mengembangkan fiksi lokal yang sudah ada: proposal yang belum menjadi jabatan, keberatan rumah tangga, perwira garrison dengan tuntutannya sendiri, perintah terbatas, risiko tiga respons, hearing dan ratifikasi. Ini bukan klaim partisipasi baru dalam kampanye kanonik Yi atau pertemuan tokoh sejarah.

Seluruh ID/tujuan/enum dan efek tiga pilihan lama, termasuk rumus enam hasil serta perhitungan losses, dipertahankan. Pilihan keempat pada hearing meninggalkan kepemimpinan personal kepada delegates dan mencatat penolakan itu secara eksplisit. Save lama yang sudah melewati proposal tidak dipaksa memasuki mode baru. Major dan komando legacy tetap memakai body/choice/effect sebelumnya, kecuali koreksi header agar sesuai saved year.

`civicCareer.localCharter` merupakan receipt opsional pada exit hearing aktual, dengan source/year, proposal, aksi, settlement, hasil serta accepted/delegated. Penerimaan hanya sah pada hasil yang memberikan mandat lokal; petition/disputed tetap pending. Receipt militer terpisah hanya muncul bila ada branch Infantry/Cavalry dan posisi tugas 212 yang benar-benar sudah ditutup. Saksi sipil dengan branch tidak diketahui tidak memperoleh dinas militer rekaan.

Civic membuka kartu lokal terbatas berdasarkan receipt dan visit/history yang cocok. Ia tidak menunjuk Governor, mengisi pejabat, membuat treasury atau mengubah pangkat/unit/staf. Formal office yang sudah sah tetap tampil. Character, Military, ingatan Han Sheng/Xu Wen dan Chronicle membaca batas yang sama; load/render tidak mengisi riwayat retroaktif. Proposal league kemudian membutuhkan penerimaan personal yang terbukti untuk jalur baru. Penolakan kepemimpinan dihormati.

Koreksi calendar: perintah baru membawa pemain dari 211 ke approach 212 sebelum crossing, lalu hearing final 213 dan exit 214; advance yang sudah mencapai tahun tujuan tetap idempotent. Posisi aktif ditutup sesudah respons. Save lama pada crossing 211 tetap menyimpan tahun/usia aslinya dan header menyesuaikan. Western messenger pada entry 214/215 menampilkan saved year, tanpa migrasi usia atau perubahan efek pilihan berikutnya.

## Pengujian yang dieksekusi

- `python3 scripts/smoke.py`: 8/8 PASS.
- `python3 scripts/qa_charter213.py --report /workspace/work/5c_charter.json`: 360 rute per viewport 390/1280, seluruh 3 proposal × 3 aksi × 4 keputusan hearing pada lima seed karier/world organik yang dipilih dan dua branch. Cavalry, Major dan Governor adalah fixture sintetis. Semua enam hasil terjangkau; matriks asli 27 rute per branch dan efek opsi dibandingkan dengan 5b.
- Penerimaan/penolakan/pending, local Civic tanpa office, gate league, no-grant rank/muster/staff/goods, posisi aktif/retired, clock/age 212–214, legacy 211, messenger 214/215, history-only/flag-only, enum invalid, posting lebih akhir, unknown branch, read-only/idempotence dan save/reload HTTP PASS. Empat klik DOM nyata Private mencapai aftermath 213 dan Civic; tidak ada overflow/page error.
- `python3 scripts/qa_crossing210.py --report /workspace/work/5c_crossing210.json`: regresi 504 rute dan 11 klik DOM per viewport PASS, delapan balasan, parity efek/legacy Major, no-grant dan reload.
- `python3 scripts/qa_chapter_map.py --report /workspace/work/5c_map.json`: dua perjalanan organik Captain/Private 207–214 per viewport PASS. Proyeksi hanya mengeluarkan record/scope/posisi serta teks Chronicle/history pilihan 210 dan 213 yang disengaja, dan memverifikasi perubahan entry crossing 211/37 menjadi 212/38. Field lain dibandingkan persis; suite event terpisah menguji field yang diproyeksikan.
- Python compile dan `git diff --check` PASS. Fixture memeriksa syntax JS dan 35 data URI gambar byte-identical; registry tetap 658.

Semua laporan memakai hash HTML yang sama. Matriks memanggil handler pilihan/validasi asli dengan paint/storage/scroll sementara dimatikan dan body history lama dikosongkan; rute DOM/reload memakai history penuh dan storage/render asli. Ini bukan seluruh kombinasi dunia sebelumnya, audit semua Chapter X–XI, editorial M10 atau sertifikasi Android/perangkat nyata `file://`/M11. Checkpoint formal terakhir tetap 5a VIII–IX; rollback formal tetap 4z. Tidak ada biaya, portrait baru atau perubahan locked decisions. Push tidak dicoba ulang pada batch ini sesuai arahan pengguna untuk melanjutkan development lebih dahulu.
