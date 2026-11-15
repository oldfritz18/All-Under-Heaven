# Eastern service dan field warrant — v0.4.99.5f

Build aktif: `GAME/ALL_UNDER_HEAVEN_v0.4.99.5f_THE_EASTERN_FIELD_WARRANT.html`. SHA-256 lihat `docs/qa/BATCH_5f.json`; semua tiga suite memakai hash HTML identik.

## Perubahan terintegrasi

Audit XI/5e membuktikan bahwa Private/0 diperlakukan sebagai pemilik army dan bahwa body 222 berjalan pada clock 221. Batch ini memperluas enam node hearing/courier/bridge 220–221, persiapan eastern front, tiga node frontline dan campaign return 222, lalu menambahkan `m3_222_field_review` serta `m3_222_after_review`. Seluruh ID lama, enum/skor/relasi, wound outcomes dan valid routes dipertahankan. Perubahan route hanya berupa review setelah return baru yang benar-benar dimainkan; legacy mid-arc tanpa issued event tetap melanjutkan jalur lama.

Proposal court/household kini dibedakan dari military commission dan formal civic office. Private memiliki agency bertempur di file, Captain/Major memberi perintah pada muster yang nyata, accepted charter mempertahankan batas sipilnya, delegated chair tetap milik delegates. Character 220–222 membaca rank aktual dan charter yang terbukti; proposal tidak otomatis menjadi independent army. Higher-command legacy/crowned/office yang sah tidak direduksi.

Entry council memajukan clock ke 222 sebelum eastern front, sekali saja. Jalur baru 190/16 tiba 222/48 lalu personal exit 223/49. Older starting age tetap relatif. Save mid-arc 221/47 tidak dipaksa maju saat load; displayed header menyesuaikan tanpa menulis ulang history/journal lama atau menambahkan service record.

Assignment dan pilihan role mengeluarkan/memperbarui posisi aktif hanya dari event aktual. Clash/return mengakhirinya. Receipt opsional `campaignEvidence.eastern222` mengharuskan known branch, issued proof, source/history, mission dan role/action yang cocok; parley/shelter tidak memperoleh raid credit. Military/People/Character/Chronicle memakai account sama. Lu Xun acquaintance tetap diberikan hanya setelah guarded parley yang benar-benar dipilih; percakapan tidak menjadikannya bawahan atau sekutu otomatis.

Field review mengisi **vacancy khusus** berdasarkan checked ford return, komisi sebelumnya dan active muster yang sah. Private dapat menerima Sergeant/watch 20; Sergeant menerima Captain/company 60 Infantry atau 30 Cavalry; Captain dengan company menerima Major/tiga company 180/90. Captain 209 tanpa issued company menerima assignment Captain, bukan naik ke Major. Major dari Baxi dengan bukti dinas Jing dan checked eastern return dapat menerima General. General menerima tiga detachment pimpinan Major, total 600 Infantry +120 Cavalry, dengan perusahaan lama ditutup ke roll baru. Formasi mixed arms tidak menjadi class Infantry/Cavalry General permanen.

Semua warrant berasal dari authority western Han field appointment yang dinyatakan dalam prose dan memerlukan acceptance. Refuse/defer atau bukti/vacancy yang tidak cocok mempertahankan grade/muster. Parley/shelter tetap menjadi service yang diakui, dengan pilihan pribadi dan politik selanjutnya, tanpa otomatis mengisi vacancy ford-command ini. Tidak ada staff appointment, Grand General/legendary cohort/Dragon General, personal goods/coins/circle/civic office/crown dari batch ini. Lima staff role/threshold lama tetap.

## Review kontinuitas dan sejarah

Novel prose baru orisinal: perusahaan tempur dan field office menghadapi enemy captain dengan reserve dan perintahnya sendiri; route/wounded/collecting signal mempunyai akibat. Private Infantry menghadapi lawan berkuda dengan foot file, tanpa diberi kuda pribadi. Cavalry tetap mempunyai mounted screen dan dismounted work sesuai ground. Familiar humor, pendapat veteran dan hak menolak tetap. Meeting/family tail dipertahankan; tidak mengganti pernikahan atau consent yang sudah sah.

Research just-in-time: [ROTK 81](https://kongming.net/threekingdoms/81) tentang keberatan terhadap eastern campaign, [82](https://kongming.net/threekingdoms/82) untuk persiapan/pergerakan 221, [84](https://kongming.net/threekingdoms/84) untuk api dan mundur 222, dibandingkan [Sanguozhi 32 teks Tionghoa](https://zh.wikisource.org/wiki/三國志/卷32) dan [terjemahan pembanding](https://sanguozhi.app/en/chapter/32) yang menandai dirinya pending human review. Policy/movement/death tokoh jauh tampil sebagai laporan bertanggal; tidak memasang pertemuan atau kematian baru lewat pembacaan. Local ford action/parley, dialog dan warrant pemain merupakan fiksi game. Grade/count warrant meneruskan career UI dan kandidat institusional World Bible/GDD; angka 20/30/60/180/720 bukan standar universal Han atau ladder XP wajib.

## Bukti pengujian

- `python3 scripts/smoke.py`: 8/8 PASS.
- `python3 scripts/qa_eastern222.py --report /workspace/work/5f_eastern.json`: **3.078 rute per viewport 390/1280**, sembilan seed terpilih yang dicapai organik: lima keadaan karier, dua variasi world, satu Major earned Baxi/Jing dan satu delegated charter. Cavalry serta legacy Major parity merupakan fixture sintetis; bukan seluruh world×career×relationship.
- Seluruh tiga proposal 220 × tiga request 221; delapan jalur mission/role/action (enam raid + parley/shelter), serta available acceptance/refusal/defer tercakup. Exact rank/active unit totals dan transfer tanpa duplikasi, Captain tanpa company, General mixed arms, no-legendary/no-staff/no-other-grant, source/history/branch, read-only/replay/later-post PASS.
- Efek lama sebelas node dibandingkan pada input sama, memproyeksikan hanya issued position/optional event fields dan teks note yang disengaja. Sembilan node higher legacy Major body/label/effect parity PASS. New arrival 222, older initial age, old mid-arc 221 tanpa backfill, Character rank dan meeting/family tail PASS.
- **23 klik DOM pilihan** dari Major organik menuju accepted General, lalu reload localStorage HTTP dan Military DOM. Negative warrant checks memakai salinan qualifying state organik dengan source/prior merit/branch yang dihapus; positive acceptance tidak berasal dari fixture promosi. Page error/overflow 0. Halaman terakhir dituju via pagination/render asli sebelum klik pilihan.
- `qa_jing219.py`: regresi 540 rute, delapan klik DOM per viewport PASS. Assertion registry hanya diperluas dengan dua ID field-review yang disengaja; tidak mengizinkan ID lain secara bebas.
- `qa_chapter_map.py`: dua route organik Captain/Private 207–214 per viewport PASS; internal clock tables tetap. Dua scene baru memiliki display chapter XI; metadata 503 scene lainnya tetap seperti checkpoint sebelumnya.
- Fixture memeriksa JavaScript syntax dan semua 35 image URI byte-identical terhadap 5e. Registry 669, seluruh 667 ID lama tetap. Python compile dan staged diff whitespace PASS.

Matriks memakai handler/validasi asli, dengan paint/storage/scroll sementara dimatikan serta body history lama dikosongkan. Jalur DOM memakai full history dan storage/render asli. Sertifikasi Android/perangkat nyata `file://`, semua cabang personal, settlement 223 dan gate XI/M3/M11 tetap terbuka. Tidak mengklaim XIX/Epilogue selesai; milestone formal terakhir 5a VIII–IX, rollback 4z.

Struktur root dan seluruh riwayat sampai review 5e sudah berhasil dipush ke `d97b951` dan remote head diverifikasi. Hambatan 403 terdahulu resolved; record historisnya dipertahankan. Batch 5f di-commit/push setelah QA dengan pemeriksaan remote tersendiri. Tidak ada biaya, ZIP baru, portrait baru, force-push atau perubahan locked decisions.
