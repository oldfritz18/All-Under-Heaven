# Checkpoint fungsional VIII–XI — v0.4.99.5g

Build: `GAME/ALL_UNDER_HEAVEN_v0.4.99.5g_THE_ROLLS_AND_THE_CHAIR.html`.

SHA-256: `b99e47c031893e991d0b83ceed425715e4e0df540cce8802ff6f49e1c0fac56c`. Receipt gabungan: `docs/qa/CHECKPOINT_5g.json`.

## Perubahan 223 dan bridge 224

Enam node assembly/oath/courier replies direvisi agar pilihan politik tidak otomatis mengalihkan tentara field formation. Tiga scene baru mengisi military account, ratification dan aftermath setelah keputusan final XI. Seluruh 669 ID 5f, valid optional branches, personal/marriage/family prose dan efek skor lama tetap; registry 672.

Player memilih kelanjutan duty, penyerahan kembali formasi yang disebut, atau pemisahan military reporting line dari household mandate. Handover hanya tersedia untuk assignment yang dapat diverifikasi, dengan later-post guard. Ia menonaktifkan record unit aktif tersebut tanpa menghapus atau menggandakan record. General dapat menyerahkan 720 prajurit sambil mempertahankan grade dan historical commission; personal release tetap permohonan tersendiri. Private/0 meminta release tanpa mengklaim formasi yang tidak dimiliki. Branch/combat history, staff, superior, appointment history, grade proof dan commission authority tidak diubah secara otomatis.

Chair dapat diterima, didelegasikan atau disaksikan tanpa menerima office. Pilihan 223 merupakan kesempatan baru: penolakan charter 213 tidak diubah menjadi acceptance retroaktif. `civicCareer.settlement223`, optional `militaryCareer.handover223`, serta `worldNotices.western223` dicatat dari actual choices/source/history; view/load tidak membuatnya. Household duty bukan Governor/crown/imperial ministry. Public passage yang diterima satu officer tidak menjadi whole interstate alliance. Civic/Character/Military/People/Chronicle memakai status yang sama.

Original final XI choice tetap menjalankan seluruh efek lamanya. Advance ke 224 ditahan pada jalur baru sampai local account selesai: 223/49 di ketiga scene baru, lalu XII/224/50. Older starting-age fixture tetap relatif. Save legacy yang sudah melewati arc tidak dipaksa kembali; higher/crowned authority yang sah tetap pada prose/effect lamanya.

Pembuka XII memperoleh bridge Part II dengan current court claim dan kewajiban yang benar-benar dibawa dari river. Kalimat premature final-years diganti pada jalur baru tanpa menghapus sisa prose. Kesunyian setelah public assembly, kawan lama, kerugian karena handing back command, humor landing/stool/bowl serta optional adult personal life tetap mendapat tempat.

## Sejarah dan batas pengetahuan

Sumber diperiksa saat authoring: [ROTK 85](https://kongming.net/threekingdoms/85), [Sanguozhi 33 teks Tionghoa](https://zh.wikisource.org/wiki/三國志/卷33), dibandingkan [Liu Bei, vol. 32](https://sanguozhi.app/en/chapter/32) dan [Zhuge Liang, vol. 35](https://sanguozhi.app/en/chapter/35). Dua terjemahan terakhir menyatakan pending human review; bukan satu-satunya dasar. Riset mendukung urutan kematian Liu Bei di Yong’an, accession Liu Shan di Chengdu dan administrasi Zhuge Liang pada 223. Tidak mengubah historical testament menjadi penunjukan protagonis.

Di game fakta tersebut datang sebagai dated court report dengan relay yang diperiksa. Notice membuktikan apa yang didengar pemain, tidak mengklaim bedside witness, pertemuan pribadi dengan Liu Shan, rekrutmen NPC, atau forced death/survival dari year metadata. `npcMemories('liubei')` membedakan sumber publik ini dari pertemuan. Local assembly, handover, replies dan dialog merupakan fiksi orisinal. Liu Shan mempunyai court claim yang dapat menolak calon/permohonan; bridge XII tidak memberikan crown kepada pemain.

## Eksekusi QA pada hash identik

- Smoke 8/8 PASS; Python compile dan staged diff whitespace PASS.
- `qa_settlement223.py`: **702 rute per viewport 390/1280**, 13 keadaan karier/world/charter yang dicapai organik melalui handler lama sampai 223. Current Cavalry-service, higher legacy/Governor dan older-age pembanding sintetis; force records asli dibiarkan utuh sampai handover. Seluruh proposal × custody × mandate (27/profile/branch), semua pasangan tujuh kelompok tiga-arah, serta dua counter-field choices tercakup; bukan Cartesian product semuanya.
- Exact handover/retained units, no rank loss/no new grants, historical charter/refusal tetap, accepted/delegated/witness, public notice tanpa direct meeting, source/history/invalid record, no-backfill/read-only/replay, later posting, existing Governor dan bridge date/age PASS. Efek tujuh node lama dibandingkan dengan proyeksi hanya event fields/notice/note dan deliberate clock delay. Tujuh node higher legacy body/label/effect parity PASS.
- **22 klik DOM pilihan** memakai history penuh termasuk optional personal/neighbor paths, General/720→0, delegated chair, lalu reload HTTP dan Civic/Military archives. Tidak ada page error/overflow. Last page dituju via pagination/render asli sebelum klik pilihan.
- `qa_eastern222.py`: 3.078 rute/viewport dan 23 klik DOM, earned warrant/refusal/pending, exact mixed force, legacy/calendar/read-only PASS.
- `qa_jing219.py`: 540 rute/viewport dan delapan klik DOM, sembilan hasil lokal/lima frontier result, inquiry/property/family parity PASS.
- Sebelas regresi berturut-turut PASS: `qa_baxi216`, `qa_charter213`, `qa_crossing210`, `qa_red_cliffs`, `qa_red_cliffs_legacy`, `qa_river_patrol`, `qa_river_councils`, `qa_changban`, `qa_chapter8`, `qa_chapter_map`, `qa_m2_continuity`.
- Registry assertions pada Baxi/Jing/eastern hanya ditambah tiga ID settlement yang disengaja serta earlier IDs yang sudah didokumentasikan. Tidak mengizinkan extra IDs secara bebas. Semua fixture memeriksa JS syntax dan 35 image URI byte-identical. Laporan lengkap tiap suite tersimpan dalam receipt checkpoint.

Matriks memanggil choice handler/validasi asli dengan paint/storage/scroll sementara dimatikan dan old history bodies dikosongkan; jalur DOM memakai full history serta storage/render asli. Ini targeted functional/continuity checkpoint, bukan bukti semua prior worlds, semua relationship combinations, pembacaan editorial setiap ending atau perangkat nyata Android/`file://`.

## Milestone dan kelanjutan

Rollback formal menjadi **5f**, diambil dari `e795cd9` dan cocok SHA-256 `6ca10d652eb602746ddbffb2e6a3242e72eff9a3d1eb2399031537d6348b960e`. 4z dan versi lain tetap di Git. Tidak membuat ZIP baru atau portrait, tidak mengubah locked decisions atau biaya.

Checkpoint formal terbaru sekarang VIII–XI/5g. Gate M3 belum ditutup seluruhnya: conditional honour/cohort yang layak dan audit world/NPC/editorial lebih luas belum disertifikasi. M4–M11 serta objective XIX/Epilogue tetap terbuka. `docs/PART_II_AUDIT_v0.4.99.5g.md` mengidentifikasi actual code inventory untuk court/legitimacy Shu, Liu Shan, legacy imperial/conquest predicate dan remapping XII–XIX. Hasil audit adalah pekerjaan berikutnya, bukan klaim implementasi Part II selesai.
