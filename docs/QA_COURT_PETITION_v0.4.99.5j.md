# M4-A — perjalanan dan jawaban istana, v0.4.99.5j

Build `GAME/ALL_UNDER_HEAVEN_v0.4.99.5j_THE_COURT_THAT_CAN_REFUSE.html`; SHA-256 `1490bf4b6860097725c7c096c5b8f727952fcd34467efa24db89ed127209c3a8`, 13.019.476 byte. Penerus 5i / `5841cf8108188694fee0d9d4de24699a176ec24a`. Engine, 689 ID lama dan 35 embedded image URIs identik dipertahankan; registry menjadi 695. Tidak ada ZIP atau perubahan portrait.

## Implementasi playable

Enam scene XII menghubungkan settlement 223/entry 224 ke hearing lama 225: tujuan petisi, izin perjalanan/relay, receiving route, chancery, jawaban istana, return. Menjaga actual General/Grand General/Captain/Private, unit custody yang diterima/dikembalikan, local mandate dan keputusan personal lama. Travel memerlukan duty coverage dan sumber muster sah; tidak membawa private army ke Chengdu atau membuat ulang unit yang sudah diserahkan. Li Yan tetap pada receiving command Yong'an; pertemuan Zhuge Liang/Liu Shan hanya melalui perjalanan dan hearing yang benar-benar dimainkan.

Pemain dapat meminta service reporting, hearing legitimasi atau local terms; menggunakan bounded journey atau relay; memeriksa copy, mengirim urgent copy, atau menarik petisi; menerima batas jawaban, menyimpan keberatan atau menariknya. Jawaban acknowledgement/reservation/withdrawal dibaca kembali secara berbeda pada return, public hearing 225, Civic, Chronicle dan actual Liu Shan memory; reservation tetap terbuka untuk dibacakan, withdrawal menutup current request. Lima hasil dibedakan: withdrawn, unverified, case registered, local terms, further service report. Checked personal chancery memberi actual encounter; royal audience membutuhkan General/Grand General atau civil office yang sah, bukan sekadar tiba di Chengdu. Relay/urgent/private local acknowledgement tidak menjadi royal meeting.

`militaryCareer.leave224` dan `civicCareer.shuPetition224` opsional menyimpan actual source/year/path/authority, departure rank/custody dan response. History/visited mendukung proof; flags saja tidak. Audience historis memakai departure snapshot, tidak hilang ketika jabatan atau pangkat kemudian berubah. Tahun/usia 224→225 maju sekali; terlambat/later posting/legacy tidak dipundurkan atau mendapat meeting backfill.

People Liu Shan dan entri Zhuge Liang hanya mengikuti actual knowledge; bukan fake early encounter. Chronicle, Character, Military dan Civic mencatat petisi pada scope yang sama. Initial hearing 225 memakai record/jabatan yang nyata serta proposal yang perlu persetujuan delegates; legacy prose/effects dan seluruh side choices tetap tersedia tanpa record baru.

**Batas keras:** ini pembuka M4-A, bukan penobatan Shu, keputusan imperial pertama, lawful succession final, appointment Dragon atau penyatuan. Tidak mengarang testament/adoption/abdication, menghapus Liu Shan, memberi imperial office/troops/treasury/staff/relationship reward atau menutup Issue #1/#2.

## Bukti QA dan batas

Receipt terstruktur: `docs/qa/BATCH_5j.json`. Seluruh suite harus melaporkan hash yang sama di atas. `scripts/qa_court224.py`: 1.080 canonical local routes per viewport 390/1280, delapan prior career/custody/charter profiles yang dibentuk dengan original handlers (termasuk real Sixth Tiger dan actual 223 handover). Seluruh lima hasil, audience vs relay, no crown/office/grants, date once, pure views, provenance, replay, legacy/later-post/unknown-force/older-age guards dan JSON resolve diperiksa. Governor admission memakai synthetic pre-existing office comparator, dibandingkan Captain tanpa civil office; actual scene chain, historical audience sesudah kehilangan office, serta forged departure rank ikut diperiksa.

Tujuh pilihan DOM full-history per viewport membawa Grand General dengan **nol** pasukan melalui actual audience→225; reload HTTP, Civic/People Liu Shan, overflow, actual JSON download dan file-input import lulus. Tidak membuat kembali pasukan. Matrix memakai compact historical bodies dan menonaktifkan paint/storage untuk evaluasi handler; ini bukan playthrough DOM semua 1.080 jalur atau semua kombinasi previous world/relationship.

Regresi bertarget: `qa_hanzhong219` (810 combat +486 conditional commission/ceremony routes per viewport), `qa_settlement223` (702), `qa_general222` (162). Penambahan scene pada strict registry checks diizinkan hanya sebagai exact six-ID group; tidak menerima ID sembarang. Smoke 8/8, Node parse melalui browser fixture dan Python compile.

Review kontinuitas: petisi berbeda dari mandate; court dan Liu Shan dapat membatasi/mengembalikan pertanyaan; earned military distinction tidak mengangkat ahli waris; actual unit ledger dan record delegasi tetap; private/household choices tidak dihapus. Hearing memberikan fondasi konflik XII, belum menggantikan kebutuhan multi-scene accession/first decision.

Chromium mobile/desktop diuji melalui localhost HTTP. Physical Android/iOS dan persistence pada perangkat nyata `file://` belum diuji. Environment ini memblokir navigasi browser `file://`; bukan bukti file HTML rusak atau sertifikasi offline-device. Seluruh M4, M8–M11, editorial keseluruhan dan ending/unification acceptance tetap terbuka. Formal rollback tetap 5h dari checkpoint 5i; 5i lengkap tersedia di Git.
