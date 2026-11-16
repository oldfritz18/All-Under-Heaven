# Pengakuan dan pengangkatan legendaris — persetujuan Issue #1

**Addendum pemilik, 16 November 2026 — DISETUJUI:** penunjukan luar biasa tanpa adopsi **dan** mandat baru pasca-223 dengan actual Liu Shan/court consent; `DESIGN/APPROVED_SHU_SUCCESSION_2026-11-16.md` menggantikan status pertanyaan mekanisme dinasti yang belum dipilih dalam bagian historis di bawah. Persetujuan bukan implementasi; jangan meminta konfirmasi ulang atau mengarang testament/backfill.

**Disetujui pemilik:** 16 November 2026. Sumber dibaca langsung: [GitHub Issue #1](https://github.com/oldfritz18/All-Under-Heaven/issues/1), **OPEN**. Ini persyaratan desain yang berlaku, bukan bukti implementasi atau QA. Referensi 5f di issue adalah baseline historis; lanjutkan penerus dalam `GAME/ACTIVE_BUILD.txt` (5g saat integrasi persetujuan).

Addendum ini memperinci mutu `01_NARRATIVE_NPC_CONCEPT_v1.0.md`, `05_CORE_STORY_DECISIONS_LEGACY.md` dan locked decisions 15 November. Tidak mengganti aturan awal Private, otonomi NPC, waktu, consent, lima Special Staff, lima posisi Dragon, portraits atau saves. Tidak memilih mekanisme dinasti yang masih terbuka pada core decisions.

## A. General dan Sixth Tiger — M3

- Pertahankan ID, acceptance/refusal/defer, eligibility dan actual muster pada `m3_222_field_review` / `m3_222_after_review`. Tingkatkan pengakuan, reaksi comrades yang benar-benar hadir/dikenal, emosi dan pengalaman pertama menjalankan komando. Upacara tidak memberi pasukan, staf atau honours tambahan.
- **Sixth Tiger General / Grand General** adalah klimaks militer/relasi tersendiri, luar biasa dan earned, bukan nama baru bagi General 222. Build-up prestasi, kesetiaan, competing perspectives, pengakuan dan aftermath menanggapi perjalanan pemain.
- Liu Bei dan jenderal Shu relevan berpartisipasi hanya dalam shared-life window, lokasi, afiliasi, pengetahuan dan perjalanan yang masuk akal, atau divergence yang sungguh dimainkan. Jangan menghadirkan Five Tigers yang wafat/tidak dikenal/tidak tersedia. Surat bukan pertemuan; tidak perlu memaksa seluruh tokoh hadir fisik bersamaan.
- Five/Six Tigers adalah konvensi tradisi novel, bukan klaim satu jabatan formal yang tak diperdebatkan dalam sejarah. Pangkat Grand General, honour dan tanggung jawab komando harus memiliki authority/acceptance yang dapat dibuktikan.

## B. Emperor of Shu — M4, XII–XIII

Penobatan adalah salah satu **klimaks utama novel**, berupa rangkaian scene substansial dan reading-first dalam prosa Inggris orisinal. Progresi wajib:

1. Sengketa legitimasi/suksesi, kepentingan istana, pandangan Liu Shan/pejabat/tentara, keberatan nyata dan alternatif bila prasyarat atau komitmen tidak terpenuhi.
2. Mandat sah yang dapat dibuktikan, jawaban pribadi protagonis dan kesempatan menolak/menunda. Tahun/bab bukan legitimasi.
3. Investiture/proclamation megah: solemn court, panji, insignia/seal, protocol, hierarki pejabat/militer, penantian dan sudut pandang rakyat. Pengakuan publik bukan konsensus universal rekaan.
4. Akibat intim: awal sederhana, warisan Liu Bei, pengorbanan, duka, comrades/rumah tangga yang memang ada, dan **keputusan imperial pertama yang bermakna** beserta konsekuensinya.

Menggantikan Liu Shan adalah **sejarah alternatif**. Persetujuan mutu ini tidak diam-diam mengesahkan adoption ke keluarga Liu, hukum suksesi baru, penyingkiran Liu Shan, atau kesepakatan seluruh court. Buat rancangan mekanisme yang konkret sebelum menyelesaikan pertanyaan dinasti yang masih terbuka; minta persetujuan hanya bila keputusan desain baru memang diperlukan, sambil melanjutkan bagian lain yang sudah disetujui.

Reaksi Zhuge Liang, Liu Shan, court, companions, household, troops dan populace mengikuti presence/survival/allegiance/knowledge/relations aktual. NPC boleh menolak. **Emperor of Shu berbeda dari Emperor/unifier seluruh Tiongkok**: accession tidak menaklukkan Wei/Wu atau memberi treasury/territory/army/ministers. Audit pembaca predicate legacy agar title/authority/UI/ending dan save lama yang sah tetap benar.

## C. Five Dragon Generals — M4 dan kelanjutannya

- Sesudah protagonis **sah menjadi Emperor**, buka arc **opsional** untuk 0–5 posisi. Posisi bukan lima nama terpilih atau class permanen Infantry/Cavalry. Bedakan dari Sixth Tiger protagonis dan lima Special Staff yang tetap.
- Pemain menominasikan calon. Tiap calon memerlukan hubungan yang berkembang, actual service/merit, kualifikasi, availability, political/command authority, consent dan acceptance eksplisit. Calon dapat menolak, tidak tersedia, pergi, berbeda pendapat atau membiarkan kursi kosong.
- Tiap appointment sah mendapat **rangkaian personal tersendiri**: council deliberation/nomination, public recognition, dialog/vow atau refusal yang berbeda emosinya, reaksi perwira/jenderal lain dan handover tanggung jawab/komando yang **benar-benar ada**. Nama pada roster saja tidak cukup.
- Appointment Dragon yang diterima memberi pangkat Grand General sesuai konsep, tanpa unit/civil office rekaan. Preserve pengangkatan legacy sah; audit gate royal legacy sebelum gate imperial baru, tanpa retroaktif mengangkat calon atau menghapus save.
- Hanya setelah **lima** appointment sah yang masih membentuk kelompok terpenuhi, sediakan adegan kolektif khusus: camaraderie, rivalitas, humor dan loyalitas yang telah dibangun. Empat, zero, refusal, dead/departed atau slot tak tersedia tidak memicu lima tokoh berkumpul.

## D. Bukti dan kelulusan

Event menerima/menolak/menunda idempotent, tersimpan dengan source scene, pilihan, waktu, authority dan history. Story → persistent state → Character/Military/Civic/People/Chronicle; menu/migrasi tidak menciptakan appointment. Preserve scene IDs, pilihan valid, portraits, engine, save/export/import dan legacy endings.

QA wajib: acceptance/refusal/defer, state negatif, chronology/rank, NPC absen/tidak dikenal/wafat/berpindah, reload dan legacy tanpa backfill; Emperor tanpa Dragons, 0–5 vacancy, calon menolak, alternative succession dan first imperial decision. Bedakan handler matrix, klik DOM, narrative review dan perangkat nyata.

**Issue #1 tetap OPEN** sampai General, Sixth Tiger, enthronement lengkap, appointment personal 0–5/collective scene, UI/save dan gate relevan diimplementasikan serta diverifikasi. Jangan memakai `Fixes #1` atau menandai selesai dari rencana/tag chapter/satu batch General. Pelaksanaan: `docs/ISSUE_1_IMPLEMENTATION_PLAN.md`, `docs/PROGRESS.md`.
