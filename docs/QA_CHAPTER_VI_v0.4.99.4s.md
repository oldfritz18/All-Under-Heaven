# Chapter VI — The File Outside Xiaopei, v0.4.99.4s

SHA-256: `53caa6c05cffa6f4fd938e229b5504ba9d2068a32b4c8d1b0abd0003b60cd37b`.

## Kriteria dan review

- W06 menjadi arc playable empat scene pada 198 bagi pilihan forward-service: perintah dan lokasi → serangan → penarikan → roll/aftermath. Jalur lain tetap sah dan laporan Xiapi/W07 pada scene lama tetap ada.
- Perbedaan aksi memberi konsekuensi lokal yang dapat diingat. Tidak ada kemenangan strategis, rekrutmen, rank, unit, barang pribadi, angka casualty atau perkenalan komandan yang diberikan otomatis.
- Pasukan lawan dan perubahan komando memiliki pergerakan sendiri. Player melihat hanya sektor file; Gao Shun, Zhang Liao, Liu Bei dan pertarungan Xiahou Dun tidak dijadikan pengalaman omniscient atau kemenangan pemain.
- Cabang baru kembali ke `ch06_07` dengan recall pilihan. Entry lama dan save setelahnya tidak dipaksa mengulang. Pangkat dan branch yang telah dicatat tetap dipertahankan.
- Kalimat yang membuat Private mengeluarkan perintah administratif atau mendirikan council diperjelas sebagai rekomendasi kepada pejabat berwenang.

Sumber adaptasi: roadmap W06 dan [ROTK Bab 18, Kongming’s Archives](https://kongming.net/threekingdoms/18), terutama penyerangan terhadap Liu Bei di Pei/Xiaopei dan gerak relief. Dialog dan tindakan prajurit lokal adalah prosa orisinal; bukan rekonstruksi faktual seorang prajurit nyata. W07 tetap laporan dunia pada cakupan batch ini; M2 keseluruhan belum disertifikasi selesai.

## Bukti dieksekusi

```sh
python3 scripts/smoke.py
python3 scripts/qa_chapter6.py --report /workspace/work/chapter6_qa.json
```

Perbandingan dengan commit `66e51f0`/4r, pada input save yang sama untuk setiap pilihan lama. Cara ini menghindari membandingkan state dari jalur berbeda setelah insert opsional. Chromium headless, HTTP lokal.

| Pemeriksaan | Hasil pada 390 dan 1280 px |
|---|---|
| Smoke, parsing JS, portrait | PASS, 35 data URI identik |
| Scene lama dipertahankan | 635 + empat baru = 639 |
| Cakupan scene VI | 12 lama + empat baru |
| Kontrak lama pada input identik | 25 edge PASS; hanya target forward-service masuk arc baru |
| Edge scene baru | 11 |
| Semua kombinasi lokal | 108 per viewport: 2 branch × 3 posisi × 3 aksi × 3 exit × 2 laporan |
| Usia/tahun, rank, branch, unit, staff, circle, coins/items | PASS, tidak ada grant |
| Posisi aktif saat tekanan / terakhir di aftermath | PASS |
| Jalur non-forward dan save lebih akhir | PASS, tidak dipaksa masuk |
| Recall People dan scene lama / flag-only negatif | PASS |
| Efek exit diulang | PASS, idempotent |
| HTTP reload save lama dan sesudah pertempuran | PASS |
| Military UI dan overflow | PASS |
| Page error | 0 |

Fixture Cavalry adalah penugasan lama sintetis. Semua kombinasi lokal arc baru diuji, tetapi bukan semua kombinasi chapter atau full novel. Full editorial, historical-source audit dan physical-device `file://` tetap terbuka. Berikutnya VII dan checkpoint M2.
