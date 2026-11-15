# Pembuka Chapter VIII — QA bertarget v0.4.99.4v

Build: `GAME/ALL_UNDER_HEAVEN_v0.4.99.4v_CHAPTER_VIII_THE_ISSUED_ROLL.html`.
SHA-256: `5260f7cb408217b4d4d60c3a8d3b924442e221269b18f8f09c17ac128080b904`.

## Perubahan dan kontrak

Delapan scene baru menyambungkan pembacaan packet 208 ke penugasan Bowang, kontak/return dan laporan, penugasan Xinye, kontak/return dan laporan, review dinas serta aftermath personal. Sumber naratif sejarah: ROTK bab 39–40, https://kongming.net/threekingdoms/39 dan https://kongming.net/threekingdoms/40 (diakses 15 November 2026). Penempatan perusahaan/regu, dialog, saksi, korban material dan komisi pemain adalah fiksi orisinal. Tahun 208 mengikuti urutan **Romance** pada roadmap; bukan klaim bahwa pertempuran Bowang historis terjadi pada 208 atau Zhuge Liang memimpin peristiwa historis tersebut.

| Peristiwa | State | Bukti / batas |
|---|---|---|
| Pilih persiapan Bowang | `m3_208_bowang_preparation`; posisi aktif | Infantry/Cavalry saja; perintah company dan reserve corridor |
| Pilih tindakan Bowang | `m3_208_bowang_action`; posisi retired | interval/signal/pair dengan biaya lokal berbeda |
| Kirim laporan | `campaignEvidence.bowang208` | sumber scene, aksi, branch, tahun dan visit/history cocok |
| Pilih sektor/tindakan Xinye | `m3_208_xinye_station/action`; posisi aktif lalu retired | tugas tempur di luar kota; bukan petugas Support atau saksi seluruh jebakan |
| Kirim laporan Xinye | `campaignEvidence.xinye208` | tidak diberikan retroaktif oleh tahun atau flag-only |
| Terima komisi | satu appointment + satu muster | Private → Sergeant/20; Sergeant dengan warrant road watch valid → Captain/60 Infantry atau 30 Cavalry; angka adalah penugasan fiktif eksplisit |
| Terima Captain | road watch lama inactive | muster lama dikembalikan; tidak dijumlah dua kali |
| Tolak / tunda | rank, muster dan appointment lama tetap | eligibility tidak sama dengan penerimaan; tidak ada staff, item atau circle gratis |
| Dewan/compact awal | ID serta tiga arah keputusan lama tetap; scope company | bagi Private/Sergeant/Captain, preference bukan kedaulatan/pasukan independen; UI Recent Command menyebut permintaan penugasan |

Registry 658 = seluruh 650 ID 4u + delapan ID baru. Semua 35 embedded image data URI identik secara byte. Save key/schema utama tetap; field baru opsional. Save setelah batas tidak dipundurkan. Cerita/rank/unit lebih tinggi pada dua node dewan legacy tetap melalui fallback lama; ini kompatibilitas, bukan sertifikasi semua otoritas lama.

## Eksekusi

`python3 scripts/smoke.py`: 8/8 PASS.

`python3 scripts/qa_chapter8.py --report /workspace/work/4v_chapter8.json`: PASS pada 390 dan 1280 px. Per viewport:

- 324 rute pairwise: dua seed Private/Sergeant yang dimainkan organik dari Prologue baseline 4u; dua combat branch; tiga aksi Bowang, tiga sektor Xinye, tiga aksi Xinye, seluruh tiga keputusan komisi. Persiapan, surat, council dan compact diseimbangkan untuk pasangan pilihannya. Bukan seluruh produk Kartesius.
- Komisi/muster benar, refusal/defer tanpa grant, pengembalian watch, tidak ada goods/staff/recruit tambahan, posisi retired, read-only view, replay idempotent.
- Tahun lebih akhir, branch tak diketahui, arc sudah direview dan flag-only tidak membuka komisi baru; history-only mempertahankan bukti; enum invalid ditolak.
- Dua scene dewan/compact: body, opsi dan hasil efek fixture Major identik dengan 4u. Fixture Major dan Cavalry bersifat sintetis, tidak membuktikan perjalanan organik kedua karier tersebut.
- 11 klik tombol nyata menyelesaikan pembuka sampai `ch08_pb55_succession`, mendapat Captain hanya setelah acceptance; reload localStorage HTTP dan Military DOM lulus. Tidak ada overflow horizontal atau page error.

Matriks memakai handler `choose` asli dengan render/save/scroll sementara dinonaktifkan, dan body history lama dikosongkan sambil mempertahankan field string, ID serta metadata. Ini membatasi pemakaian memori saat ratusan variasi; pengujian DOM terpisah memakai seed penuh dan rendering/penyimpanan asli. Percobaan pertama dengan full history/repaint setiap variasi membuat target Chromium crash; harness diperbaiki, bukan dicatat sebagai PASS. Kesalahan selector single-choice dan mutasi fixture QA juga diperbaiki sebelum hasil final.

Regresi M2 `python3 scripts/qa_m2_continuity.py --report /workspace/work/4v_m2.json` juga PASS: 108 rute W08 + 144 W10 per viewport pada hash 4v identik. Katalog QA menerima penambahan scene di luar cakupannya; assert tujuan packet mengikuti routing saat ini sambil tetap memverifikasi acquaintance legacy. Bukti gabungan: `docs/qa/BATCH_4v.json`.

## Batas

Ini gate pembuka VIII, bukan kelulusan M3. Bagian retreat/Changban/Red Cliffs legacy, pengelompokan bab VIII–X, tawaran komisi 209, biografi/NPC lintas tahun dan full-novel editorial masih perlu audit. Perangkat nyata/Android/file:// belum disertifikasi. Tidak ada biaya, portrait baru, perubahan locked decisions, atau push GitHub dalam batch ini.
