# ALL UNDER HEAVEN — DEVELOPMENT ROADMAP v1.0

**Tanggal:** 14 November 2026  
**Cakupan:** Prologue, Chapter I–XIX, Epilogue  
**Status:** **RENCANA IMPLEMENTASI / SPOILER-FREE**, bukan pernyataan seluruh fitur sudah selesai.  
**Baseline HTML yang tersedia:** `ALL_UNDER_HEAVEN_v0.4.99.3e_DEV_LIVE_STORY_UI_SYNC.html`  
**Baseline SHA-256:** `a93255588ebbcb709e2a061759f36c5db55ac9ad6485d0a424059bec87a144f9`  
**Konsep terkait:** `ALL_UNDER_HEAVEN_KONSEP_NARASI_NPC_TETAP_v1.0_2026-11-14.md`

## Tujuan akhir

Menghasilkan satu **novel interaktif offline lengkap dan stabil**, dengan perang, politik, persahabatan, humor, romansa dewasa non-grafis, NPC historis yang otonom, dan konsekuensi hidup yang menyatu dengan antarmuka. Protagonis meniti karier dalam pasukan Liu Bei, menjadi tokoh legendaris, lalu menghadapi tantangan sebagai Emperor of Shu; hasil penyatuan Tiongkok **tidak otomatis**.

## Status awal — fakta vs pekerjaan tertunda

| Komponen | Kondisi / tindakan berikutnya |
|---|---|
| HTML, cerita, visual | Baseline v0.4.99.3e tersedia; **preserve and patch**, jangan restart game. Inventaris kode/scene aktual perlu direkonsiliasi sebelum estimasi selesai. |
| Military/Civic | UI dan beberapa pemetaan state sudah ada; audit seluruh pangkat, jabatan, superior, satuan, roster, staf, dan pergantian era masih dibutuhkan. |
| Story–UI Sync | Sudah ada contoh penunjukan Sergeant dan Captain berbasis pilihan cerita; belum setara dengan cakupan seluruh promosi/jabatan sampai Emperor. |
| Narasi I–XI | Ada materi yang harus **dibaca, disunting dan diperluas secara bertahap**; mutu dan kesinambungan semua jalur belum dinyatakan lulus. |
| Narasi XII–XIX | Struktur baru disetujui secara konsep; konten lama yang dahulu dipadatkan pada XII perlu disortir, direvisi, dan diperluas ke delapan chapter. |
| Historical + Original NPC | Data dan interaksi lama tersedia; audit kontinuitas/otonomi lintas semua chapter belum selesai. |
| Endings | Arsitektur dan varian lama harus dipetakan ke struktur 19 chapter dan divergensi dunia yang benar-benar terbentuk. |
| Save/offline | Pengujian sintetis pernah dilakukan; uji perangkat nyata, browser reload, ekspor/impor, dan migrasi antarb versi tetap menjadi gerbang rilis. |

## A. Siklus wajib untuk **setiap chapter**

> Jangan menunda sinkronisasi UI dan audit NPC sampai seluruh novel ditulis. Jalankan satu siklus vertikal berikut pada tiap chapter/kelompok kecil scene.

| Tahap | Pekerjaan | Bukti selesai (gate) |
|---|---|---|
| **1. Narasi** | Pelajari scene lama; tulis/perluas adegan berbahasa Inggris: pembuka, relasi, rutinitas, konflik, eskalasi, klimaks, aftermath; pilihan bermakna; tetap reading-first. | Prosa terbaca runtut, emosi terasa, tidak ada pengulangan atau lompatan tak terjelaskan; adegan lama valid tetap ada. |
| **2. Choice & State** | Catat pilihan, prasyarat, event, flag, waktu, wilayah, tokoh, akibat segera dan callback masa depan. Event harus **idempotent** agar save/load tidak menggandakan hadiah. | Setiap pilihan punya tujuan scene dan kontrak konsekuensi; menolak tawaran tidak mendapat hadiah; tidak ada flag kontradiktif. |
| **3. Narasi ↔ UI** | Hubungkan state cerita dengan Character, Military, Civic, People, Possessions, Chronicle; tangani status kosong dan pengetahuan terbatas. | UI berubah tepat sesudah peristiwa nyata dan pulih persis setelah save/load. Tak ada rank, pasukan, staf, Governor, atau NPC fiktif. |
| **4. NPC Continuity** | Periksa historical cast, original cast, lokasi/tahun, faksi, tujuan, otonomi, suara dialog, interaksi antar-NPC, relasi dan memori masa lalu. | NPC tidak teleport, tahu rahasia tanpa alasan, hidup sesudah wafat, setuju otomatis, atau muncul dengan hubungan yang belum dibangun. |
| **5. History & World** | Periksa kronologi ROTK/sejarah, geografi, penguasa wilayah, berita, perjalanan, logistik, keadaan faksi dan pergeseran akibat pilihan pemain. | Peristiwa historis/logika alternate history berjalan tanpa kontradiksi; perubahan sejarah merambat ke bab selanjutnya. |
| **6. QA bertarget** | Uji pilihan setuju/tolak, berhasil/gagal, state berbeda, sebelum/sesudah scene, save migrasi, rendering mobile dan desktop, proofread prosa. | Chapter Audit Receipt P0=0; semua konsekuensi penting dapat diperlihatkan; P1 tersisa dicatat dan dijadwalkan. |

**Artefak setiap chapter:** (a) manuscript + branch notes privat, (b) chapter timeline sheet, (c) per-NPC continuity ledger, (d) state/UI event matrix, (e) QA Receipt internal, (f) laporan status **spoiler-free** kepada pemain.

## B. Tahapan produksi dari awal hingga ending

| Fase | Cakupan | Pekerjaan utama dan hasil | Gerbang kelulusan |
|---|---|---|---|
| **M0 — Baseline & planning** | Seluruh kode sekarang | Bekukan salinan v0.4.99.3e, hash, inventaris scene/choice/asset/NPC/flags; perbarui story bible ke 19 chapter; tandai konsep legacy Regional King dan 12 chapter; daftar bug P0/P1/P2. | Seluruh dependensi kritis diketahui, rollback mungkin, tidak ada scene sah yang dihapus. |
| **M1 — Narasi fondasi** | Prologue, Chapter I–III (c.190–192) | Perkuat kesetiaan kepada Liu Bei, kehidupan prajurit, humor, kawan awal, komando pertama; validasi promosi Private→Sergeant/Captain hanya jika diterima. | Rute awal dari karakter baru hingga III mulus; pangkat, atasan, pasukan, People, Chronicle sinkron. |
| **M2 — Dunia berubah** | Chapter IV–VII (c.193–207) | Xuzhou, konflik/pengungsian, aliansi dan berpindahnya Liu Bei; pertumbuhan karier dan relasi; jembatan Xu Shu/Three Visits/Longzhong sesuai pengetahuan dan waktu. | Kronologi dan NPC lintas bab konsisten; karier bukan hadiah karena melompat tahun. |
| **M3 — Perang dan legenda** | Chapter VIII–XI (c.208–223) | Changban/Red Cliffs, Yi, Hanzhong, Jingzhou, perang berdampak; perkembangan General dan Sixth Tiger/Grand General; awal jabatan Governor bila sah; foreshadow dan krisis suksesi Shu. | Pertempuran punya ketegangan, kejutan, konsekuensi dan aftermath; kehormatan/hak komando dapat dibuktikan; legitimasi 223 logis. |
| **M4 — Mahkota dan pemerintahan** | Chapter XII–XIII (c.223–229) | Ubah sisa warisan cerita Regional King menjadi Shu-Han; suksesi dengan reaksi istana; rancangan pemerintahan Emperor; Chancellor, lima Ministers, Five Dragon Generals; rumah tangga, politik dan fiskal. | Semua jabatan dan Five Dragon bergantung pada pengangkatan resmi, bukan angka bab; layar Emperor menunjukkan negara yang benar-benar ada. |
| **M5 — Konflik antarkerajaan** | Chapter XIV–XV (c.229–239) | Kampanye Wei dengan kemungkinan aliansi, pakta, atau permusuhan Wu; diplomasi, logistik, pertempuran, pemulihan negeri, relasi dan konflik dalam keluarga/istana. | Wu memiliki keputusan sendiri; kampanye tidak otomatis menang; akibat militer dan diplomasi terlihat lintas bab. |
| **M6 — Generasi dan harga kekuasaan** | Chapter XVI–XVII (c.239–249) | Pergeseran generasi, pejabat, jenderal dan loyalitas; wilayah yang bertambah/berkurang; biaya perang, krisis pangan, intrik, kehilangan dan pertumbuhan personal. | Semua NPC hidup dalam keadaan dunia terkini; keputusan lalu memberi konsekuensi terasa; state wilayah/pasukan akurat. |
| **M7 — Klimaks dan penutup** | Chapter XVIII–XIX (mulai c.249, dinamis), Epilogue | Kampanye/negosiasi terakhir sesuai state; solusi penyatuan maupun kegagalan; resolusi hubungan, hidup/kematian, pemerintahan dan warisan; revisi varian ending legacy. | Tidak ada ending dipaksakan; keadaan politik, keluarga, NPC, wilayah dan reputasi konsisten dengan perjalanan pemain. |
| **M8 — Cross-chapter NPC & history audit** | I–XIX | Audit ledger Historical NPC **per tahun dan faksi** + Original NPC; kemunculan, kehidupan di luar layar, promosi, kemampuan, luka, kematian, hubungan, pengetahuan, callback; cek semua percabangan sejarah. | Tidak ada kontradiksi karakter/kronologi kritis; semua NPC kunci punya arc/konsekuensi yang jelas. |
| **M9 — System integration audit** | Seluruh UI dan state | Uji Military, Civic, Character, People, Possessions, Chronicle, Settings dan Story; rank/superior chain, Grand General, troop unique totals, governors, Officer→Minister, Special Staff, 8 portrait, items, time/aging. | Tiap peristiwa cerita = perubahan UI tepat satu kali; UI tidak tahu lebih dari karakter; semua save valid dimigrasikan. |
| **M10 — Editorial pass** | Novel penuh | Baca beberapa playthrough organik, pengeditan bahasa Inggris, ritme, romance dewasa non-grafis, humor, adegan tenang, intensitas perang dan payoff; periksa repetisi pilihan dan durasi chapter. | Setiap perang utama punya build-up, titik balik, risiko, dan aftermath; interaksi NPC terasa manusiawi, bukan lapor-stat. |
| **M11 — Regression, offline, release** | HTML final + perangkat | Full scene graph and choice coverage, multiple ending routes, save/load/export/import, `file://` di Android & desktop, viewport, accessibility, performa, aset dan kesiapan paket rilis. | Semua P0 ditutup, P1 utama diselesaikan, rilis hanya setelah uji perangkat nyata dan pembacaan penuh disetujui. |

### Pemetaan chapter dan intensitas

| Arc | Bab | Peran utama |
|---|---|---|
| **Rise of a Soldier** | Prologue–III | Identitas, mentor, sahabat awal dan pelatihan tanggung jawab. |
| **A World in Flames** | IV–VII | Pergeseran politik, kekalahan, mobilitas tokoh, dan pendewasaan. |
| **The Sixth Tiger** | VIII–XI | Perang besar, kepemimpinan, hubungan yang teruji, dan pergantian kekuasaan. |
| **The Weight of the Crown / Court of Shu** | XII–XIII | Suksesi, legitimasi, penataan pemerintahan dan para jenderal. |
| **Northern Ambition / Between War and Peace** | XIV–XV | Wei, Wu, diplomasi, biaya perang dan kehidupan pribadi. |
| **Changing Winds / Price of Conquest** | XVI–XVII | Generasi baru, kekuasaan, kelelahan perang, intrik dan pengorbanan. |
| **Final Mandate / All Under Heaven** | XVIII–XIX | Klimaks sesuai kondisi, penyelesaian yang diperoleh, lalu Epilogue. |

**Periode adalah jendela produksi, bukan promosi otomatis atau kalender wajib.** Durasi, panjang prose, dan hasil tiap bab mengikuti kondisi permainan, bukan target tahun.

## C. Kontrak integrasi Story–UI

Minimal setiap event penting memiliki:

```text
story_event_id | scene_id | selected_choice_id | world_date
actor_id | target_npc_id (optional) | faction/territory (optional)
preconditions | consequences | evidence/source-of-authority
known_to_protagonist | mutation_version | persistence/rollback policy
```

Peta state → UI:

| Event cerita | State yang berubah | UI yang harus terpengaruh |
|---|---|---|
| Promosi/penunjukan komando yang diterima | `militaryCareer.rank`, superior bila dikenal, warrant, unit aktif/bawahan | Military, Character, Chronicle, People bila ada NPC. |
| Korban perang/pasukan beralih komando | Unit/strength/morale/discipline/assignment/status; unique unit IDs | Military, Chronicle; no double-count. |
| Pengangkatan Special Staff atau Five Dragon | NPC identity, consent, appointment provenance, term, eligibility, honor | Military, People, Chronicle. |
| Penunjukan Governor/wilayah | `civicCareer` dengan scope dan superior, governance mandate | Civic unlock, Character, Chronicle. |
| Pengangkatan/penarikan Officer atau Minister | office holder, term, allegiance, vacancy, scope, responsibility | Civic, People, Chronicle. |
| Perkenalan/perkembangan NPC | discovered/known information, memories, trust, relationship, location | People, dialogue availability, Chronicle. |
| Barang/kuda/portrait/cedera | provenance, ownership, current condition, earned portrait stage, health | Possessions, Character, Story, Chronicle. |
| Diplomasi/peta/peristiwa historis berubah | world/faction treaty status, territory, hostility, campaign | Civic (Emperor diplomacy), Military, Story and ending eligibility. |

**Golden rule:** *Story mutates state → persistent state drives UI; UI never manufactures story facts.* Gunakan pengenal event stabil dan migrasi yang menyelamatkan old saves; tombol preview bukan sumber data Actual Save.

## D. NPC audit ledger dan dunia hidup

Buat satu record per NPC dengan: `npc_id`, historical/original, source era, birth/death known, allegiance/timeline, known/public/private facts, current whereabouts, appointments, independent goals, relationships, injuries, living status, player-encounter ledger, interaction callbacks, marriage/household if relevant.

Per chapter uji minimal:

1. **Historical**: kronologi cerita sesuai novel atau divergensi yang sudah dipicu; tidak ada tokoh sejarah dengan informasi yang belum dapat diketahuinya.
2. **Original**: fungsi cerita mandiri dan masuk akal; bukan pengganti tokoh sejarah karena kurang menulis historical cast.
3. **Inter-NPC life**: relasi dua NPC berubah ketika protagonis tidak ada; penolakan/loyalitas tidak dipaksakan.
4. **Appearance/discovery**: portrait dan identitas hanya muncul setelah pengetahuan karakter mencukupi.
5. **Closure**: tokoh penting yang mati, pindah, jadi musuh, menikah, dipromosi atau dipecat punya reaksi lanjutan dan memori silang.

Untuk perang besar, audit **command decisions & reports** dari para jenderal, bukan hanya dialog protagonis. Untuk politik, audit pihak istana dengan agenda bertentangan. Untuk hubungan dewasa, cek usia, consent, kesinambungan emosi serta aftermath.

## E. Audit perang, politik, romansa, dan pilihan

**War quality gate:** kondisi sebelum perang, rencana/ketidakpastian, setidaknya satu perubahan taktik bermakna, bahaya dan biaya, peran NPC, hasil yang dipengaruhi pilihan, reaksi prajurit, laporan korban, dan aftermath personal. Kemenangan epik tidak harus berarti kemenangan mudah.

**Politics quality gate:** penunjukan punya dasar kewenangan, penolakan NPC dan legitimasi diperhatikan, pajak/grain/public order memengaruhi kelangsungan perang; aliansi Shu–Wu bukan skrip wajib dan dapat berubah.

**Relationships quality gate:** perkembangan bertahap, konsistensi ucapan/tindakan, humor dan keintiman ditempatkan sesuai emosi; tidak ada informasi atau komitmen otomatis yang belum terjadi. Interaksi seksual hanya antara karakter dewasa yang setuju, non-grafis.

**Choice quality gate:** pilihan penting berdampak bukan hanya pada satu angka; mempunyai callback, jalur penolakan/gagal, dan konsekuensi masuk akal; tidak semua halaman harus berisi pilihan.

## F. QA & manajemen risiko

### Prioritas perbaikan

- **P0 — wajib segera:** crash/softlock/scene hilang, korupsi save, kejadian mustahil, promosi atau perkawinan yang tidak terjadi, NPC mati muncul tanpa sebab, kebocoran spoiler atau narasi dewasa di bawah umur, ending yang tak cocok dengan kondisi dunia.
- **P1 — wajib sebelum release:** adegan terlalu pendek, hubungan melompat, NPC kosong tanpa agency, strategi perang tidak berpengaruh, konsekuensi terlupakan, redundansi UI, aksesibilitas utama.
- **P2 — polish:** detail grafis tambahan, transisi animasi, kosmetik, variasi dialog non-kritis.

### Pengujian efisien

- Tiap perubahan lokal: uji *affected scenes* + pilihan tetangga + state negatif + satu save lama + UI yang terkait; hindari full replay setiap revisi kecil.
- Tiap checkpoint kelompok bab (III, VII, XI, XIII, XV, XVII, XIX): **targeted multi-chapter regression** dan continuity pass.
- Saat perubahan skema save, story router, temporal logic, rank/appointments, atau ending: jalankan validasi global lebih awal.
- Sebelum release: *full scene graph* + beberapa **organic playthrough** dengan pilihan berbeda, ending divergence, portrait, dan uji perangkat sebenarnya. QA sintetik tidak menggantikan pembacaan prosa secara utuh.
- Simpan QA Receipt: versi, SHA baseline/hasil, scene/komponen diubah, pengujian, bug P0/P1/P2, status lulus/gagal, keterbatasan yang belum diverifikasi.

### Matriks pengujian minimal

| Jenis jalur | Contoh kondisi yang harus terbukti |
|---|---|
| Karier | Terima/tolak komisi; loncat bab tanpa promosi; pemimpin unit gugur; pindah penugasan, pasukan lama tidak ikut otomatis. |
| Pemerintahan | General tanpa Governor; General + Governor; Governors kehilangan wilayah; Emperor dengan posisi Menteri kosong; pengangkatan NPC menolak. |
| Hubungan | Teman/rival/pasangan dengan riwayat berbeda; perpisahan, sakit, kematian atau perubahan faksi; dewasa/non-dewasa gating. |
| Perang | Menang/seri/mundur/kalah; logistik/kematian/koordinasi Wu berbeda; kegagalan strategi berdampak di bab berikut. |
| Save | New game, legacy import, auto/manual save, export/import, reload, restart dari pembuatan karakter; `file://` Chrome Android & desktop. |
| Endings | Beragam kondisi faksi/territori/legitimasi, kematian, hubungan, dan warisan; tidak ada hardcode penyatuan. |

## G. Kriteria selesai (Definition of Done)

**Release Candidate baru layak ketika**:

- Prologue, Chapter I–XIX, dan Epilogue dapat diselesaikan tanpa softlock.
- Narasi berkualitas novel, memuat seluruh enam pilar emosi dan variasi intensitas.
- Semua promosi, jabatan, pasukan, NPC, harta, health, portrait dan diplomasi berasal dari event cerita yang valid; save setelah reload tetap cocok.
- NPC historis utama berperilaku otonom dan kronologis, Original NPC relevan dan dapat berpengaruh; tidak ada kebocoran informasi.
- Pertempuran besar memiliki taruhan, pilihan taktis, risiko, konsekuensi dan payoff; ending tergantung keadaan dunia.
- Semua bug P0 selesai, P1 besar diselesaikan; inspeksi Android dan desktop offline lulus; ekspor/impor dan kompatibilitas save lama diverifikasi.
- Laporan rilis bersifat **spoiler-free** dan membedakan yang diuji secara sintetik dari yang sudah diuji secara organik.

## H. Aturan pengembangan dan change control

1. **Jangan mulai dari nol**: lanjutkan HTML aktif, pertahankan scene, pilihan, save, sprite/portrait, fitur lama yang valid.
2. **Prioritas cerita & gameplay** mengungguli tambahan menu/demo dekoratif. UI Showcase semua menu tetap dibatalkan.
3. Perubahan desain baru harus menyebut dampaknya pada jadwal penulisan, audit, integrasi dan QA.
4. Kerjakan per *batch* kecil dengan QA tertarget; jangan selalu mengulang seluruh game pada revisi kosmetik.
5. Gunakan sumber asli ROTK/history sebagai acuan untuk materi historis; tandai dengan jelas bagian alternate history dan jabatan gameplay adaptasi.
6. Biaya tambahan, plugin, hosting atau produk berbayar **tidak diasumsikan**; perlu persetujuan pengguna terlebih dahulu.
7. Penamaan Imperial Staff/Council **masih hold**; tetap tampil sebagai Special Staff pada Emperor sampai keputusan baru.

## I. Urutan kerja langsung berikutnya

1. **M0**: bekukan dan inventaris baseline v0.4.99.3e; buat matrix `scene → choice → event → state → UI → NPC → later callback` untuk Prologue–Chapter III dulu.
2. **M1**: mulai dari **Prologue/Chapter I**; perbaiki kualitas narasi dan sambungkan pilihan nyata ke state/UI serta People/Chronicle. Jangan langsung lompat menulis bab kekaisaran.
3. Uji **Chapter I→II→III** dengan minimal jalur terima dan tolak tanggung jawab; verifikasi relasi dan superior; simpan QA Receipt.
4. Teruskan M2–M7 berurutan, dengan audit dan test tiap bab, lalu M8–M11 sebagai audit lintas-kampanye dan release gate.

**Catatan akhir:** Ini roadmap target, bukan checklist yang sudah lulus. Dokumen roadmap 12 chapter v0.5 tetap berharga sebagai catatan audit awal, tetapi jadwal produksinya telah **digantikan** oleh roadmap 19 chapter ini.
