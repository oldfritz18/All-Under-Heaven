# Chapter V — The Road Between Orders, v0.4.99.4r

SHA-256: `750dd63e9d8ece906546295e785b32b99ea0e6458a4a91a414c8eaa042172aac`.

## Kriteria dan review

- Tujuh pertemuan yang sebelumnya sangat pendek kini memperlihatkan pekerjaan NPC, fallibility, humor, batas loyalitas serta kewajiban di luar circle. Efek pilihan lama dipertahankan.
- Kampanye W05 mendapat tiga scene pada 197, setelah pilihan akhir V dan sebelum VI/198. Protagonis mengalami sebagian konflik di jalan tempat ia ditugaskan; tidak menggantikan duel, kampanye atau keputusan komandan ROTK.
- Field/district/both menentukan lokasi tugas. District adalah keamanan bersenjata dan both adalah fighting screen yang melapor ketika relief; clerks dan couriers tetap NPC. Kalimat recall lama yang menjadikan penugasan district/both pekerjaan utama logistik dikoreksi.
- Pilihan posisi, sinyal dan penarikan menghasilkan catatan yang berbeda, field position aktif/terakhir, People memory, Chronicle serta recall VI yang membutuhkan bukti kejadian. Kerugian driver tidak diubah menjadi reward atau kemenangan strategis.
- Waktu bergerak dari 196/22 ke 197/23 lalu 198/24. Tidak ada rewind bagi save yang melewati insert, dan tidak ada retro-credit.

Basis adaptasi: W05 pada roadmap 196–197 dan [ROTK Bab 17, Kongming’s Archives](https://kongming.net/threekingdoms/17), yang diperiksa untuk konteks klaim imperial Yuan Shu dan konflik Xu Province. Pertempuran jalan, dialog prajurit/driver dan akibat lokal adalah prosa fiksi orisinal; bukan kutipan novel atau klaim kejadian historis spesifik. Tidak ada perkenalan personal dengan Yuan Shu yang diberikan.

## Bukti dieksekusi

```sh
python3 scripts/smoke.py
python3 scripts/qa_chapter5.py --report /workspace/work/chapter5_qa.json
```

Perbandingan dengan commit `a4d7458`/4q. Chromium headless, HTTP lokal, viewport 390 dan 1280 px.

| Pemeriksaan | Hasil per viewport |
|---|---|
| Smoke / JavaScript parsing / portrait | PASS, 35 data URI identik |
| Registry | Seluruh 632 ID sebelumnya + tiga baru = 635 |
| Chapter V state representatif | 16 scene, 33 edge lama, delapan edge scene baru |
| Parity efek, label dan state lama | PASS; exit V sengaja masuk ke 197 sebelum kembali ke target lama 198 |
| Semua kombinasi lokal 197 | 108: 3 preferensi × 2 branch × 3 posisi × 3 aksi × 2 laporan |
| Branch/unit/rank/staff/circle/coins/items | PASS, tidak ada grant atau rewrite dari arc baru |
| Posisi aktif lalu terakhir, 197/23 dan 198/24 | PASS |
| Recall pilihan di People dan VI | PASS, read-only dan evidence-gated |
| Idempotence efek baru | PASS |
| Save lama 198 / flag-only negatif | PASS, tidak rewind atau memberi ingatan |
| HTTP reload 197 dan save lama 198 | PASS |
| Menu Military dan overflow | PASS |
| Page error | 0 |

Fixture Cavalry merupakan penugasan lama sintetis. Seluruh kombinasi lokal arc 197 diuji, tetapi itu bukan seluruh kombinasi Chapter V atau full campaign. Audit novel lintas bab, biografi lengkap dan physical-device `file://` tetap terbuka. Lanjutkan VI–VII sebelum menyatakan M2 tuntas.
