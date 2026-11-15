# Development progress — Codex handoff initialization

## Baseline
- Active: v0.4.99.5d; baseline awal terverifikasi v0.4.99.4m.
- Status: gate M2 dan checkpoint fungsional VIII–IX bertarget; batch crossing 210, charter 211–213 dan dinas Baxi 215–216 terimplementasi/teruji. M3 sedang berjalan pada Chapter X; M3–M11 dan objective penuh belum selesai.
- Goal mode status: AKTIF atas perintah eksplisit pengguna dalam percakapan ini. Objektif: Prologue–Chapter XIX dan Epilogue sesuai M0–M11; belum selesai.

## Evidence already in repository
- `docs/QA_RECEIPT_v0.4.99.4m.md` — scope and limits of previous targeted QA.
- `docs/CHANGELOG_v0.4.99.4m.md` — last baseline change.

## Next work
- Struktur VIII/IX/X mengikuti roadmap pada 5a. Kelompok hearing–crossing 210 sudah direvisi pada 5b dan charter 211–213 pada 5c; rotasi ke Yi/Baxi dan river screen 215–217 terintegrasi pada 5d. Berikutnya Hanzhong/Jingzhou 218–219, mandat/muster dan kesinambungan NPC/relasi. Jangan menganggap label bab atau batch 210 sebagai kelulusan seluruh X.
- Node Xu Shu awal serta sesudah Changban sudah menjadi pembacaan bersumber; pertahankan perbedaan laporan/pertemuan serta outcome Red Cliffs ketika melanjutkan dunia 210–223.
- Tawaran Captain 209 kini eksplisit dan mengembalikan watch yang sesuai pada jalur baru. Tetap audit milestone karier berikutnya di X–XI, dengan penerimaan, muster dan jabatan yang benar-benar tercatat.
- XII–XIX/Epilogue: adaptasi pemerintahan dan suksesi Shu-Han serta perluas struktur legacy; belum dikerjakan atau disertifikasi. Registry baseline tidak mempunyai tag Chapter XIII–XIX, sehingga konten akhir legacy tidak boleh diklaim setara dengan delapan chapter Emperor Saga.
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

## Checkpoint batch I–VII — v0.4.99.4t
- Tiga scene pada 201 mengubah warrant Sergeant yang diterima menjadi pengalaman komando terbatas road watch. Cabang memerlukan Infantry, warrant dan unit yang benar; Cavalry, penolakan, permintaan independent authority, tahun lebih akhir dan record yang tidak konsisten tetap pada jalur lama.
- Tidak ada promosi baru dari arc: komisi lama yang diterima secara eksplisit tetap satu-satunya sumber rank Sergeant dan 20 personel road watch. Pertempuran mempertahankan unit itu, memperlihatkan batas kewenangan, koreksi dari veteran, biaya dan laporan yang harus ditandatangani. Tidak ada assistant atau Special Staff otomatis.
- Seluruh 27 kombinasi lokal per viewport lulus. VII: 18 scene baseline, tiga tambahan, 44 edge lama identik pada input sama (kecuali route insert yang disengaja), sembilan edge baru; acceptance/decline, empat bypass negatif, duplikasi unit, no-grant, recall, HTTP reload dan UI Military lulus.
- Regression checkpoint: smoke 8/8 dan tujuh suite browser (`qa_chapter1`, `qa_chapter2`, `qa_m1`, `qa_chapter4`, `qa_chapter5`, `qa_chapter6`, `qa_chapter7`) semuanya lulus pada HTML 4t yang sama, di 390/1280 px; page error 0. Bukti terstruktur: `docs/qa/CHECKPOINT_4t.json`; rincian: `docs/QA_CHECKPOINT_v0.4.99.4t.md`.
- Registry 642: seluruh 630 ID baseline dipertahankan + 12 scene baru. Semua 35 data URI portrait identik; lima Special Staff dan threshold tetap. Rollback formal kini v0.4.99.4s; tidak membuat ZIP baru.
- Sesi berhenti pada batas sumber daya konteks setelah checkpoint terverifikasi ini. Objective tetap tercatat dan belum selesai; jangan mengklaim daemon latar atau pengembangan otomatis berlangsung ketika tidak ada eksekusi. Tidak ada biaya, push, perubahan locked decisions atau permintaan persetujuan baru dalam batch ini.

## M2 — v0.4.99.4u, gate fungsional/coverage bertarget
- W08: empat scene penugasan, tekanan, penarikan dan aftermath pada 200 ditambahkan antara exit VI dan pembukaan VII. Semua tiga preferensi exit lama dipertahankan; combat branch dan warrant tidak berubah. Kekalahan strategis tidak diubah menjadi kemenangan personal.
- W10: tiga scene wing action/report dan satu pertemuan opsional Xu Shu pada 207 ditambahkan sebelum VIII. Pembacaan nasihat tertanggal pada node legacy 208 tidak lagi menghadirkan Xu Shu atau memberi acquaintance baru. Save lama yang sudah memiliki acquaintance tetap dipertahankan.
- W07/Xiapi diklasifikasi sebagai laporan dunia bersumber pada rute ini, bukan partisipasi retroaktif. Ledger lengkap dan kondisi W01–W10: `docs/M2_CAMPAIGN_COVERAGE.md`.
- `campaignEvidence` opsional menyimpan fakta aksi ketika exit nyata dipilih. Military, People dan recall membutuhkan sumber/aksi yang cocok serta visit/history; tidak dibuat ketika render, migrasi, atau hanya melihat tahun/flag.
- Seluruh 642 ID sebelumnya dipertahankan + delapan scene baru = 650. Portrait tetap 35 data URI identik, schema save utama dan lima Special Staff tetap.
- `qa_m2_continuity.py`: 108 rute pairwise W08 dan 144 kombinasi lokal W10 per viewport 390/1280; seed Sergeant dan Private diperoleh lewat keputusan organik baseline, Cavalry memakai fixture legacy. No-grant, consent pertemuan, timeline, field position, legacy acquaintance, flag-only, idempotence, history-only dan reload/UI lulus.
- Smoke 8/8 dan delapan suite browser pada source 4u yang sama lulus; page error 0. Rincian: `docs/QA_M2_v0.4.99.4u.md`, data: `docs/qa/CHECKPOINT_4u.json`. Gate bukan sertifikasi seluruh kombinasi novel, biografi lengkap atau perangkat nyata. Rollback formal: 4t.


## Pembuka VIII — v0.4.99.4v, selesai pada cakupan bertarget
- Delapan scene Bowang/Xinye dan review/aftermath ditambahkan sebelum dewan Jing legacy. Tugas, formasi, officer, signal, recall, pengetahuan terbatas, biaya lokal, humor serta kehidupan setelah kontak ditulis sebagai prosa Inggris orisinal.
- Komisi baru memerlukan dua laporan dinas yang terbukti dan penerimaan eksplisit. Private dapat menerima Sergeant/20; Sergeant dengan road watch valid dapat menerima Captain/60 Infantry atau 30 Cavalry. Watch lama dikembalikan saat Captain diterima, tanpa duplikasi; refusal/defer mempertahankan pangkat dan muster. Angka adalah penugasan fiktif yang dibacakan dalam scene. Tidak ada staff/recruit/resource gratis.
- Pembuka, dewan dan compact awal sekarang membedakan penugasan company dari pasukan/otoritas independen pada rank Private–Captain. Legacy command lebih tinggi dipertahankan; beberapa scene retreat/Red Cliffs berikutnya masih perlu perbaikan terpisah. Belum menandai VIII atau M3 tuntas.
- Registry 658; seluruh 650 ID 4u dan 35 embedded images dipertahankan. Bukti dinas baru tersimpan opsional dan dibaca Military/People dengan source serta visit/history.
- Smoke 8/8; `qa_chapter8.py` 324 variasi per viewport 390/1280 + 11 klik DOM nyata, reload, acceptance/refusal/defer, provenance, no-grant dan legacy Major parity lulus. `qa_m2_continuity.py` kembali lulus 108 W08 + 144 W10 rute per viewport pada hash yang sama. Tidak ada page error.
- Bukti: `docs/qa/BATCH_4v.json`; batas dan sumber: `docs/QA_CHAPTER_VIII_v0.4.99.4v.md`. Rollback formal tetap 4t; 4u tersedia dalam Git. Tidak membuat ZIP atau push.


## Retreat–Changban–Hanjin — v0.4.99.4w
- Sembilan node lama direvisi tanpa menghapus ID/arah keputusan/enum. Private tetap berada di bawah section leader; Sergeant/Captain hanya mengarahkan active muster. Prosa memperjelas formasi, officer, sektor, tekanan, pilihan hold/counterstroke/river approach, recall dan akibat lokal. Zhao Yun serta Zhang Fei memilih tugas dan memimpin pasukan sendiri.
- Xu Shu pada node sesudah Changban kini berupa dispatch/laporan terdahulu pada semua rank, bukan pertemuan yang salah waktu. Acquaintance legacy dipertahankan; inquiry/forwarding/verification tidak menjadi rescue atau penugasan pasukan gratis.
- Bukti dinas Changban baru hanya dicatat ketika exit crossing yang dimainkan benar-benar dipilih. Military, People dan callback mengikuti sumber/aksi/visit/history; flag-only tidak memberi credit. Semua rank, unit, staff, coins/items dan circle tetap. Posisi retired pada recall, tanpa menimpa penugasan tahun lebih akhir.
- Registry 658, 35 embedded images identik. Smoke 8/8, `qa_changban.py` 216 rute pairwise + sembilan klik DOM per viewport 390/1280 lulus; regresi `qa_chapter8.py` kembali lulus 324 rute + 11 klik DOM per viewport pada hash 4w yang sama. Page error 0.
- Bukti dan batas: `docs/QA_CHANGBAN_v0.4.99.4w.md`, `docs/qa/BATCH_4w.json`. M3 masih berjalan; dewan sungai/Red Cliffs, komisi 209 serta relabeling chapter menjadi prioritas berikutnya. Rollback formal tetap 4t; tidak membuat ZIP atau push.


## Dewan sungai — v0.4.99.4x
- Lima belas node lama diperluas/dikoreksi untuk Private–Captain tanpa menghapus ID atau handler efek lama. Proposal, custody dokumen dan rekomendasi loading/signal tidak lagi menjadi kedaulatan, kapal atau staf pribadi. Guan Yu, Liu Qi, Lu Su, Zhuge Liang, pilots serta komandan company tetap memiliki kewajiban masing-masing.
- Pilihan river council sekarang memberi tugas tempur terbatas dengan muster aktif; Private menjalankannya di dalam section. Character dan Military tidak menyebutnya pemilik contingent/fleet. Tidak ada grant pangkat/unit/staff/ship/goods/recruit. Posisi baru ditutup pada laporan pagi yang dimainkan, hanya bila proof dan attendance cocok.
- Registry 658, portrait 35 identik. Smoke 8/8; `qa_river_councils.py` 216 rute dan 17 klik DOM per viewport 390/1280 lulus, termasuk semua pasangan sebelas kelompok pilihan, military no-grant, UI scope, legacy Major parity, reload dan penutupan posisi sampai 209. Regresi Changban 216 rute + sembilan klik DOM per viewport juga lulus pada hash 4x yang sama. Page error 0.
- Bukti: `docs/QA_RIVER_COUNCILS_v0.4.99.4x.md`, `docs/qa/BATCH_4x.json`. Battle/settlement Red Cliffs, komisi 209, relabeling dan milestone M3 tetap belum selesai. Rollback formal tetap 4t; tidak membuat ZIP atau push.


## Persiapan dan patroli Red Cliffs — v0.4.99.4y
- Sembilan node flotilla–twilight diperluas dengan embarkation, perintah deck/company, crew navigation, signal drill, patroli terbatas, kontak, biaya, shore coordination dan konflik perintah. Cavalry serving dismounted tetap pada branch aslinya; tidak menjadi Support atau pemilik armada.
- Handler/enum/score/relasi/tujuan lama dipertahankan; prosa dan Chronicle kini mengikuti active muster. Tiga tujuan patroli memberi laporan berbeda dan keterbatasan nyata, tersimpan hanya setelah embarkation/kontak yang terbukti. Military dan People membaca bukti yang sama; replay tidak menggandakan record.
- Registry 658, portrait 35 identik. Smoke 8/8; `qa_river_patrol.py` 216 rute + sembilan klik DOM per viewport 390/1280 lulus, termasuk parity efek lama dan legacy Major, no-grant, cavalry dismounted, provenance, idempotence serta reload. Regresi councils 216 rute + 17 klik DOM per viewport kembali lulus, termasuk posisi retired pada laporan pagi 209. Page error 0.
- Bukti dan batas: `docs/QA_RIVER_PATROL_v0.4.99.4y.md`, `docs/qa/BATCH_4y.json`. Fire assault/settlement, komisi 209, pemetaan VIII–X dan objective M3–M11 tetap belum selesai. Tidak ada biaya, ZIP, push atau perubahan locked decisions.


## Fire assault–settlement — v0.4.99.4z
- Dua puluh node sampai exit 209 diperluas/dikoreksi sebagai engagement yang dapat diputuskan pemain dalam assigned combat file. Briefing, intel, signal, api, tiga aksi, shore report, objective, pursuit, loss review dan hearing tersambung; Huang Gai/Zhou Yu/awak tetap otonom. Adegan core/romance 208 yang valid dipertahankan.
- Perhitungan lama dan empat hasil perang tetap. Tindakan company dibedakan dari laporan koalisi; tidak mengubah kemenangan menjadi kepemilikan armada/provinsi. Receipt W14 baru memerlukan order proof dan kunjungan nyata; Military/People/Character/Chronicle serta callback memakai scope yang sama. Posisi retired sebelum 209.
- Komisi Captain 209 kini eksplisit dan hanya diterima pada field choice. Watch terkait dikembalikan pada jalur baru; Captain 208 tidak dipromosikan lagi, Private tidak dipromosikan otomatis. Save 4y dan older-order resume yang mempunyai warrant/watch sah mempertahankan tawaran lama tanpa receipt dinas retroaktif. Tidak ada staff/ship/goods/recruit gratis.
- Registry 658, portrait 35 identik. Smoke 8/8; `qa_red_cliffs.py` 324 rute pairwise dan 20 klik DOM per viewport 390/1280 lulus; semua empat outcome dan dua matriks parity hasil lama lulus. Regresi patroli 216 rute + sembilan klik DOM per viewport serta 20 node legacy Major body/label/effect parity lulus. Reload dan provenance/idempotence lulus; page error 0.
- Bukti/hash dan batas: `docs/QA_RED_CLIFFS_v0.4.99.4z.md`, `docs/qa/BATCH_4z.json`. Pemetaan VIII–X, kampanye 209–223, milestone M3 dan objective XIX/Epilogue tetap belum tuntas. Rollback formal tetap 4t; tidak ada ZIP, biaya atau push.


## Checkpoint VIII–IX dan struktur VIII–X — v0.4.99.5a
- Pembagian tampil kini sesuai roadmap: VIII 10 scene pembuka/Bowang/Xinye; IX 61 scene retreat–Changban–Red Cliffs; X 84 scene settlement 209 serta legacy 210–219. 503 scene lainnya tetap. Internal IDs/acts/tabel calendar dan history save lama dipertahankan; tidak ada perubahan reward, pilihan atau timeline dari relabeling.
- Heading VIII/IX/X tampil sekali pada jalur baru dan benar pada direct legacy entry. Inspector memakai display chapter aktif tanpa membuat fixture/riwayat baru. Parity prosa lama mengabaikan hanya heading H2 yang kini diuji tersendiri; paragraf, pilihan dan efek lainnya tetap dibandingkan.
- Delapan suite Chromium 390/1280 serta smoke 8/8 PASS pada hash identik: map, VIII, Changban, councils, patrol, fire/settlement, legacy Major dan boundary M2. Map membandingkan rute/state organik Captain dan Private sampai 214; seluruh route-state identik selain teks heading history. Tidak ada page error. Registry 658; portrait tetap 35 identik.
- Bukti/hash/cakupan: `docs/QA_CHAPTER_MAP_v0.4.99.5a.md`, `docs/qa/CHECKPOINT_5a.json`. Rollback formal diperbarui ke 4z dari Git dengan hash cocok; riwayat versi lain tetap di Git. Tidak membuat ZIP, push atau biaya.
- Audit awal X: 70 kunjungan/64 ID default sampai entry XI/220, Captain/60 masih tetap. Mandat 210, charter 211–213, ketepatan tahun entry western messenger serta pengalaman Yi/Hanzhong/Jingzhou perlu integrasi berikutnya; jangan memberi rank, attendance, kapal atau jabatan otomatis. Rincian dan bukti: `docs/CHAPTER_X_AUDIT_v0.4.99.5a.md`, `docs/qa/AUDIT_X_5a.json`.
- Gate ini bersifat fungsional/targeted untuk VIII–IX, bukan M3 sampai XI, editorial semua cabang, Chapter X selesai atau objective XIX/Epilogue tuntas. Android/perangkat nyata/file:// dan M11 masih terbuka.


## Review workspace dan persiapan push — 15 November 2026
- Root/tracking enam komponen wajib diverifikasi lagi; tidak ada folder pembungkus starter yang menjadi satu-satunya lokasi proyek. ZIP asli utuh (`ZipFile.testzip`), inisialisasi sudah ada dalam riwayat Git. Tidak perlu ekstraksi ulang atau empty initialization commit.
- Checkpoint aktif 5a / commit `300ebb3` bersih dan 15 commit mendahului remote sebelum review ini. Hash HTML cocok dengan delapan suite checkpoint; smoke 8/8 dan suite map organik 207–214 pada 390/1280 dijalankan ulang dan PASS. Bukti: `docs/qa/REVIEW_2026-11-15.json`.
- Pengguna sekarang memberi izin eksplisit commit/push struktur ke GitHub. Review dicatat tanpa mengubah executable atau gameplay. Push memakai fast-forward branch main dan mempertahankan seluruh riwayat development; hasil remote diverifikasi sesudah pengiriman.
- Goal tetap aktif sebagai instruksi persisten dalam percakapan ini. Tidak ada bukti atau API untuk menyatakan scheduler eksternal/daemon berjalan. Pekerjaan berikutnya tetap mengikuti audit Chapter X, bukan restart dari starter.


## Batch pertama Chapter X — v0.4.99.5b
- Sembilan node hearing–crossing–reply 210 diperluas dengan laporan bertanggal, empat proposal, perintah company, tiga tindakan lokal, relief, balasan yang dapat ditolak dan aftermath. Rekomendasi tidak menjadi kepemilikan kapal/pasukan atau jabatan; NPC dan perwira mempertahankan kewenangan masing-masing. Optional letter dan seluruh ID/route/enum/efek lama dipertahankan.
- Delapan hasil lama tetap dihitung dengan rumus yang sama. Receipt crossing baru membutuhkan order dan visit/history; Military/Character/People/Chronicle mengikuti scope dan bukti yang sama. Tidak ada rank/muster/staff/goods/recruit/Civic office gratis; posisi tugas retired setelah relief, tanpa menimpa posting lebih akhir.
- Smoke 8/8 dan tiga suite pada hash 5b identik PASS di 390/1280: `qa_crossing210.py` 504 rute/11 klik DOM; regresi Red Cliffs 324 rute/20 klik DOM; dua route map Captain/Private sampai 214. Crossing menguji seluruh pilihan lokal pada tujuh seed karier/world, delapan replies, parity efek, sembilan node Major, no-grant, reload, idempotence, legacy no-backfill dan later-post guard. Page error 0.
- Bukti dan batas: `docs/QA_CROSSING_210_v0.4.99.5b.md`, `docs/qa/BATCH_5b.json`. Milestone formal terakhir tetap 5a (VIII–IX); rollback formal tetap 4z dan semua build lain ada dalam Git. Berikutnya charter 211–213, kalender messenger 214/215, Yi/Hanzhong/Jing serta karier berikutnya. M3 sampai XI dan XIX/Epilogue belum selesai.

## Hasil push pada review ini
- Review commit `10f50c4` tersimpan, tetapi push normal dan helper resmi gh sama-sama ditolak GitHub HTTP 403. Read/fetch berhasil; remote main masih `a82952a6fb9d32c05ba2cf4d96df19329031cafb`. Struktur dan seluruh perkembangan tetap lokal; jangan menyatakan sudah dipush.
- Status jaringan environment current/enforced menunjukkan unrestricted. Akun terlihat memiliki hak repo, tetapi kredensial sesi tidak berhasil menulis. Akses tulis/Contents ke repo ini perlu diperbarui melalui koneksi/kredensial GitHub; bukan permission untuk merombak game atau alasan menghapus/rebase riwayat. Detail: `docs/GITHUB_PUSH_BLOCKER_2026-11-15.md`.
- Goal tetap aktif sebagai instruksi kerja thread. Tidak ada bukti scheduler eksternal/daemon berjalan. Pengembangan lokal dilanjutkan dari checkpoint 5a sampai batch 5b yang teruji sambil bagian push terblokir; tidak ada restart, ekstraksi ulang, biaya atau perubahan locked decisions.


## Charter lokal dan ratifikasi — v0.4.99.5c
- Lima scene charter 211–213 diperluas: proposal sementara, batas kewenangan patroli, perintah lapangan, tiga respons di ford, hearing dan ratifikasi. Pilihan keempat mengizinkan pemain menjadi saksi tanpa menerima kepemimpinan pribadi. NPC tetap memegang pasukan/mandat masing-masing; enam hasil dan formula lama dipertahankan.
- Receipt opsional `civicCareer.localCharter` hanya dicatat pada hearing aktual. Civic menampilkan accepted/delegated/pending beserta lingkup yang terbukti; tidak memberi Governor, pejabat, treasury, rank, unit, staf atau barang. Military/People/Character/Chronicle sinkron; proposal tanpa bukti tidak membuka otoritas. Jalur league kemudian memerlukan penerimaan personal yang benar-benar tercatat pada mode baru; legacy tetap.
- Jalur baru masuk crossing pada 212/usia 38, hearing ratification 213/39 dan kembali 214/40; posisi tugas ditutup sesudah aksi. Save lama di crossing 211 tetap 211 dan tidak dituakan ulang. Header western messenger mengikuti saved year 214/215 tanpa mengubah clock/age.
- Smoke 8/8 dan tiga suite pada hash sama PASS di 390/1280: charter 360 rute per viewport, regresi crossing 504 rute/11 klik DOM, dua route organik map 207–214. Charter mencakup semua pilihan lokal pada lima seed karier/world dan dua branch, enam outcome, penerimaan/penolakan/pending, no-grant, legacy Major/parity efek, provenance, reload Civic dan empat klik DOM Private. Page error 0; registry 658, portrait 35 identik.
- Bukti/batas: `docs/QA_CHARTER_211_213_v0.4.99.5c.md`, `docs/qa/BATCH_5c.json`. Checkpoint formal terakhir tetap 5a VIII–IX; rollback tetap 4z. Tidak menyatakan Chapter X, M3 atau objective XIX/Epilogue selesai. Push ditunda sesuai arahan pengguna; penolakan GitHub 403 terakhir tetap belum teratasi.


## Rotasi barat dan dinas Baxi — v0.4.99.5d
- Tujuh scene opsional menghubungkan request dinas 215, relief lokal/perjalanan melalui gorges–Jiangzhou, tugas Baxi 216, kontak tempur, return account, review warrant serta handover kembali ke river circuit. Jalur river lama tetap tersedia; menolak rotasi atau pulang dari staging tidak menerima combat credit. Pemain tidak diubah menjadi peserta penaklukan Chengdu 214 secara retroaktif.
- Ada pertemuan aktual dengan Zhang Fei di receiving camp; gerak tentara besarnya tetap independen dan diketahui melalui laporan. Protagonis mengambil keputusan pada side valley yang benar-benar ditugaskan, dengan tiga posisi/tiga tindakan dan biaya berbeda. Household delegates tetap berwenang ketika pemain pergi; consent dan seluruh scene personal/fair 217 tetap dipertahankan.
- Review earned memerlukan perjalanan/order/contact/history, return yang checked, branch dan komisi/muster sah. Tawaran baru Private→Sergeant, Sergeant→Captain, atau Captain dengan company terbukti→Major hanya berlaku setelah penerimaan eksplisit. Captain dengan komisi 209 tetapi tanpa active company mendapat company, bukan Major. Refusal/defer/pending mempertahankan rank/muster.
- Major yang diterima memegang tiga company dengan total 180 Infantry atau 90 Cavalry pada rotasi ini; old company ditutup ke roll baru, tidak dihitung dua kali. Lima Special Staff tetap sama: eligibility saja, seluruh appointment tetap milik save. Tidak ada barang/coins/civic office/Dragon General/circle otomatis. Chain Baxi berakhir pada handover; Military mencatat posisi aktif/retired dan dua receipt terpisah untuk Baxi/river screen.
- Smoke 8/8 dan tiga suite pada hash sama PASS di 390/1280: Baxi 864 rute per viewport (delapan seed karier/world/charter organik, kedua branch), charter 360 rute, dua route map 207–214. Sembilan klik DOM organik Captain→Major sampai callback 217, save/reload HTTP, exact muster, Major legacy/effect parity, staging/refusal, old age, provenance, idempotence, later-post guard dan Military DOM PASS. Page error 0. Registry 665; seluruh 658 ID lama dan 35 portrait tetap.
- Bukti/cakupan dan sumber historis: `docs/QA_BAXI_215_216_v0.4.99.5d.md`, `docs/qa/BATCH_5d.json`. Berikutnya audit/integrasi Hanzhong–Jing 218–219 serta komisi lanjutan dan XI. Chapter X/XI, M3–M11 dan XIX/Epilogue belum tuntas; milestone formal terakhir tetap 5a VIII–IX, rollback 4z. Push tidak dicoba ulang sesuai arahan pengguna.
