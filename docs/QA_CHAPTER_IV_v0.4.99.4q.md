# Chapter IV — Roads of Xu Province, v0.4.99.4q

SHA-256: `d8175df350554d8f3173450a34e25914e387b95f268d8faa52c69dde3b9c9637`.

## Kriteria dan perubahan

- Perluasan substantif tujuh scene menambah dialog, independensi NPC, risiko pertahanan, perintah yang diteruskan lewat chain of command, serta pilihan kedekatan/menolak yang tetap sah.
- FieldPosition yang masih menunjuk Pan River 191 pada operasi Beihai/Xuzhou 194 diganti melalui lima event pilihan yang benar-benar terjadi. Setiap posisi mencantumkan branch yang sudah tercatat, sektor, formasi, atasan yang diketahui sebagai section leader, tujuan, tahun dan proof pilihan.
- Posisi ditutup pada akhir kontak Beihai dan pertahanan Xuzhou sebelum aftermath. Tidak ada promosi, branch baru, unit baru, staff atau kemenangan besar yang diberikan.
- Migrasi hanya merekonstruksi pencatatan posisi dari kombinasi scene tujuan + pilihan valid + visit/history + branch yang telah sah. Posisi lain tahun 194 atau lebih baru dipertahankan. Tidak ada reward, Chronicle atau marker event baru yang diciptakan migrasi.
- Lin Yue: rujukan dua tahun di 193 dikoreksi setelah perkenalan III dipindah ke 192 oleh kalender baseline. Bahasa komando pada bridge party dikoreksi agar Private memberi laporan di bawah section leader.

## Bukti dieksekusi

```sh
python3 scripts/smoke.py
python3 scripts/qa_chapter4.py --report /workspace/work/chapter4_qa.json
```

Baseline perbandingan: commit `5ca2665`, build 4p. Browser Chromium headless melalui HTTP lokal.

| Pemeriksaan | Hasil di 390 dan 1280 px |
|---|---|
| Smoke / JavaScript syntax | PASS |
| Registry dan embedded portrait | 632 ID dan 35 data URI dipertahankan |
| BFS Chapter IV | 20 scene, 53 edge per viewport |
| Parity pilihan/state | PASS, kecuali FieldPosition dan marker event yang disengaja |
| Rute kampanye | 54 per viewport: 27 Infantry + 27 fixture Cavalry |
| Semua pasangan delapan keputusan tiga-arah | PASS untuk kedua branch |
| Lifecycle posisi dan tahun/usia | PASS; 194/20, transisi asli ke 196/22 dipertahankan |
| Migrasi visited/history-only | 10 kasus positif per viewport |
| Flag-only, enum invalid, branch tak diketahui, posisi masa depan, posisi 194 lain, scene lain | Enam kasus negatif per viewport PASS |
| Efek berulang / tidak menimpa posisi setelahnya | PASS |
| Kronologi Lin Yue, bahasa Private, adult entry gate | PASS |
| HTTP save/reload posisi aktif dan terakhir | PASS |
| Menu Military, sektor aktual, overflow | PASS |
| Page error | 0 |

Fixture Cavalry adalah state penugasan lama sintetis untuk menguji preservasi branch, bukan klaim telah memainkan semua jalur memperoleh cavalry. Rute pairwise bukan semua kombinasi delapan pilihan. Physical-device `file://`, full novel editorial, dan release gates tetap belum selesai. Langkah berikutnya adalah Chapter V secara berurutan.
