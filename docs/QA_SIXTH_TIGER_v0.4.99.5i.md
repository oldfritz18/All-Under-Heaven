# M3-B — Hanzhong dan Sixth Tiger, v0.4.99.5i

Build: `GAME/ALL_UNDER_HEAVEN_v0.4.99.5i_THE_SIXTH_STANDARD.html`. SHA-256 `06183588f67d7f006f877ec5f94ce389c5cf8bff3f4a914bc83482556d390977`. Penerus byte-preserving 5h (`90e0d40`); enam commit pengarahan remote sampai `546d654`, termasuk Issue #2, diambil dengan fast-forward sebelum development. Tidak memulai game baru.

## Scope playable dan kontinuitas

Tiga belas scene opsional menambahkan permohonan/relief 218, perjalanan melalui Jiangzhou dan inland passes, receiving council dan operasi Hanzhong 219, checked/disputed return, tawaran General lebih awal, royal hearing, proposal Sixth Tiger, investiture, first duty, intimate aftermath dan perjalanan pulang ke Jing. Semua diberi display Chapter X karena window 219 berada sebelum kontak Jing; bukan memindahkan kalender XI atau memaksa kehadiran pada seluruh campaign.

Entry ditambahkan setelah pilihan lama pada `ch10_c58_06_frontier_218`. Menolak/menunda tetap di 218 lalu old continuation maju ke 219 satu kali; menerima memerlukan relief dan travel yang dimainkan. Return akhir menggunakan old forward choice/effect, tetap 219/45 pada starting age normal. Older-age comparator tetap relatif. River branch, optional personal scenes dan seluruh 676 ID lama dipertahankan; registry 689. Save yang sudah melewati kesempatan ini tidak mendapat perjalanan/merit/meeting/honour retroaktif.

Battle chain memberikan unit/perwira/soldier context, visible enemy, terrain, objective, limited knowledge, tiga tugas × tiga peran × tiga respons. Musuh mempertahankan reserve dan ground; counterstroke tidak selalu berhasil. Ada sembilan hasil lokal, delay/ground/convoy consequences dan personal forearm-cut pada risiko spesifik. Tidak menggantikan Dingjun atau aksi historis Zhao Yun dengan kemenangan protagonis. Wounded/receiving/recovery dicatat sebagai pengalaman personal, bukan sistem casualty/death simulation lengkap yang belum ada.

General lebih awal memerlukan Major/Baxi warrant dan tiga company sah, river service, checked Hanzhong result yang sesuai vacancy serta acceptance eksplisit. Refusal/defer/pending dan lower ranks tidak dipromosikan. Warrant mereform tiga detachment masing-masing 200 Infantry +40 Cavalry, total 600/120; company sebelumnya ditutup ke total baru. Warrant 222 dan recognition/first command 5h tetap jalur valid bagi yang belum mendapat/menerima General lebih awal. General/Grand General yang sudah diterima tidak diberi promosi General kedua pada 222.

Sixth Tiger merupakan rangkaian terpisah: rekomendasi kumulatif, royal hearing, competing perspectives, tawaran, pilihan final acceptance/vow atau refusal/defer, public recognition, real first duty dan quiet aftermath. Eligibility memerlukan accepted General, actual early encounters/service dan confidence Liu Bei yang cukup; angka tidak ditampilkan sebagai pengganti drama. Tiga vows menghasilkan callbacks berbeda. Setelah appointment diterima, penurunan hubungan kemudian tidak menghapus komisi historisnya.

Grand General/Sixth Tiger diangkat secara eksplisit oleh Liu Bei sebagai King of Hanzhong pada 219. Tidak menambah unit, staff, Dragon, equipment, coins, relationships, Governor, imperial offices atau succession right. Military units dan Special Staff yang ada tetap. Tidak menunjuk lima bawahan atau memberi semua tentara milik para Tiger kepada protagonis.

## Historical cast dan pengetahuan

ROTK 73 dan Sanguozhi 32/36 diperiksa untuk Hanzhong, acclamation dan separate commands. Novel/records berbeda dalam beberapa detail titles/dates; 219 digunakan sebagai shared-life window. Sixth Tiger protagonis, local combat/royal encounters dan dialog adalah fiksi alternatif game, bukan klaim kejadian historis. Grand General dan angka formasi adalah adaptasi gameplay.

Huang Zhong dan Zhao Yun ditemui di receiving council; Liu Bei, Zhang Fei, Ma Chao dan Huang Zhong berpartisipasi di royal receiving camp dengan perjalanan yang dinarasikan. Zhao Yun kemudian tetap pada field duty dengan dated return; Guan Yu berada di Jing melalui laporan/dispatch, bukan ceremonial teleport atau new personal meeting. Senior commanders dapat mempertanyakan kelayakan dan precedence; tidak mengarang unanimous consent. Proclamation menyebut Liu Shan sebagai heir; honour militer ini tidak diam-diam menggantikannya.

`huangzhong` dan `machao` ditambahkan sebagai dua People yang hanya terbuka lewat encounter source/history. Huang Zhong berbeda dari original Han Sheng. Existing Zhao Yun acquaintance tetap; first contact baru 219 tidak menulis ulang northern meeting lama. Memories tentang return/private aftermath menunggu scene terkait dimainkan, tidak bocor dari future prose. Source King 219 diarsipkan; actual western notice 223 membuat current personal successor unconfirmed, tidak menampilkan Liu Bei sebagai atasan hidup yang baru memberi perintah sesudah notice.

## State/UI dan save

- Optional `militaryCareer.hanzhongRotation`, `campaignEvidence.hanzhong219`, `hanzhongWarrant219`, `sixthTiger219` dan event flags menyimpan authority/source/year, unit snapshots, pilihan, hasil dan confidence/vow saat accepted. Existing schemas/keys/IDs tetap.
- New Grand General verification memerlukan event/appointment/history yang cocok. Existing legitimate legacy Grand General tetap memakai reader lama; marker baru tidak menjadi migration grant.
- Field positions aktif hanya setelah issued order, retired sesudah actual receiving; wrong phase, later-year/same-year foreign posting dan replay tidak menimpa tugas. Travel tidak melompati posting yang lebih baru.
- Story, Chronicle, Character, Military, People dan Civic yang sudah terbuka mencerminkan jenis authority yang sama. Civic menegaskan retained local delegates dan tidak memperoleh office dari military honour. Views/readback/resolve tidak menciptakan evidence.
- 223 handover mengenali exact new warrant/roll yang sah. Uji melanjutkan Grand General/720 sampai actual handover→0 dan 224, mempertahankan grade/honour/history. Three existing lifetime endings mendapat historical callbacks; selector/choice/ending family tidak diganti.

## Bukti QA

`qa_hanzhong219.py` pada hash di atas PASS, masing-masing viewport 390/1280:

- **810 rute operasi**: lima prior career profiles melalui original handlers, dua current-branch variants, full 3×3×3×3 mission/role/action/report; sembilan hasil dan personal wound.
- **486 rute commission/ceremony**: conditional General acceptance/refusal/defer, tiga hearing answers, Tiger proposal, tiga final vows serta last-minute refusal/defer, first duty dan aftermath. Bukan full Cartesian product seluruh previous worlds/relationships.
- Exact muster/retired originals, no extra rank/staff/civic/Dragon/wealth, insufficient confidence, missing prior service, invalid receipt, history-only versus flags-only, later relation changes, replay/read-only, future/same-year posting, older age dan legacy without backfill PASS.
- **14 pilihan DOM**, full history, pada organic Major→General→Sixth Tiger dengan actual personal combat/wound, plus HTTP reload. Actual JSON browser download dan file input import dengan dialog pada isolated test context PASS. UI Military honour/archive, Character Health forearm/scar dan kartu People Ma Chao/Huang Zhong terlihat; page error/overflow 0. Existing later wounds tetap pada Health; luka baru tidak disembunyikan oleh default health text.
- **54 handler steps** lanjutan melalui Jing/220–223, handover 720→0, delegated local chair dan bridge XII/224 PASS. Ini handler continuation, bukan 54 DOM clicks. Current personal superior tidak diklaim sebagai Liu Bei sesudah source western notice.

Delapan suite pada hash identik PASS: `qa_hanzhong219`, `qa_general222` (162 rute/viewport), `qa_eastern222` (3.078), `qa_settlement223` (702), `qa_jing219` (540), `qa_baxi216` (864), `qa_chapter_map` dan `qa_m2_continuity`. Smoke 8/8, Node syntax, Python compile dan staged whitespace check PASS. Receipt gabungan: `docs/qa/CHECKPOINT_5i.json`. Rollback formal diperbarui ke 5h dari Git dengan SHA cocok receipt; 5f dan versi lain tetap di Git.

Matriks menonaktifkan sementara paint/storage/scroll dan mengosongkan historical body sambil mempertahankan IDs/evidence; DOM memakai full history/render/storage. Current Cavalry service/muster, Governor, later-post dan older-age comparators sintetis. Tidak ada physical Android/`file://` certification, seluruh world/relationship combinations, semua ending playthrough, full editorial/M3/M4 atau Issue #1/#2 completion claim.

## Kelanjutan

M3-B kini memiliki jalur recognition yang sungguh playable; seluruh gate M3/M8–M11 masih perlu audit lebih luas. Berikutnya M4: legitimacy/succession, Shu enthronement/first imperial decision dan personalized Dragon arcs, lalu M5–M7 termasuk playable Emperor frontline dari Issue #2. Kedua issue tetap OPEN. Tidak ada keputusan dinasti baru, biaya, portrait baru atau ZIP yang dibuat dalam batch ini.
