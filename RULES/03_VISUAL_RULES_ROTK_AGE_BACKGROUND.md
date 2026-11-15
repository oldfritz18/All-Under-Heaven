# All Under Heaven — M1 NPC Portrait Visual Rules v1.1

**Tanggal:** 14 November 2026  
**Status:** keputusan visual user + proof penilaian; belum ada penggantian aset dalam HTML v0.4.99.3i.
**Mengacu pada:** Visual Roadmap M1 v1.0; World Bible legacy v1.99.2m; narasi sekitar 190 M; reference portrait protagonis `soldier.webp` / `general.webp`.

## Keputusan terbaru

1. **Gaya dan framing:** original art yang terinspirasi desain karakter ROTK, tidak menyalin art resmi secara persis. Format setipe protagonist: gambar dekat persegi-vertikal, semi-realistis sinematik, detail tinggi, torso-up, dan dapat dibesarkan saat membuka People. Satu karakter / satu aset portrait, tanpa tulisan atau bingkai dalam gambar final.
2. **Wajah, umur, pakaian, helm/tutup kepala:** mengikuti identitas ROTK yang relevan pada tahun kejadian. Jangan memakai wajah tua di Chapter I apabila usia karakter masih muda; jangan memberikan simbol kekaisaran atau titel yang belum diperoleh.
3. **Warna:** arah desain ROTK — kelompok Liu Bei/Shu hijau; Cao Cao/Wei biru; Sun/Wu merah; faksi lain memakai warna tokoh/warlord yang sesuai. **Tahun 190 belum ada negara Shu, Wei, atau Wu.** Warna hanya bahasa visual; jangan memakai bendera kerajaan yang belum berdiri, dan jangan mengalihkan kesetiaan secara otomatis. Warna harus tetap mengikuti faksi aktual jika sejarah alternatif mengubahnya.
4. **Latar sesuai peran saat portrait dipakai:** Military → kamp, latihan, medan perang, kavaleri, tenda komando; Civic → kantor pemerintahan, ruang pengadilan, buku besar, aula dewan, arsip; Civilian merchant → pasar, rumah dagang, kereta logistik, pembukuan. Hindari camp militer universal untuk semua.
5. **Sinkronisasi UI/state:** NPC only after witnessed encounter; portrait perubahan rank/role/affiliation hanya dari state/peristiwa sah. Jangan auto-promote atau auto-transfer karena chapter/tahun. Thumbnail dan klik-untuk-perbesar menggunakan aset sama. Save key lama tidak berubah.

## Batch 1: Visual age & backdrop register (Chapter I, sekitar 190 M)

| NPC | ID | Karakter/peran awal | Acuan visual usia di 190 M | Latar | Palet dominan |
|---|---|---|---|---|---|
| Liu Bei | `liubei` | Pemimpin / perwira lapangan | ~29 (lahir 161) | Kamp/pos komando, tidak imperial court | Hijau dengan aksen hangat/emas |
| Guan Yu | `guanyu` | Military | Tanggal lahir historis tidak pasti; dewasa dan lebih senior dari Zhang Fei | Kamp/latihan/pertempuran | Hijau dan metal gelap |
| Zhang Fei | `zhangfei` | Military | Tanggal lahir historis tidak pasti; lebih muda dari Guan Yu, pria dewasa | Latihan/kamp lapangan | Hijau dengan ikat kepala merah |
| Gongsun Zan | `gongsunzan` | Komandan kavaleri/warlord independen | Lebih tua dari Liu Bei; perkiraan visual usia 30–40-an, bukan tanggal lahir pasti | Kavaleri kuda putih dan benteng wilayah utara | Putih-perak, netral |
| Cao Cao | `caocao` | Pemimpin komando & politik | ~35 (lahir 155) | Tenda komando/perencanaan militer | Biru gelap, emas |
| Zhang Miao | `zhangmiao` | Administrator / Civic | Tahun lahir tak terverifikasi; tampilan dewasa matang | Kantor administrator Chenliu / arsip sipil | Biru gelap atau netral era koalisi |
| Qiao Mao | `qiaomao` | Administrator / Civic | Tahun lahir tak terverifikasi; tampilan matang | Kantor pemerintah / buku besar | Coklat/ungu netral |
| Bao Xin | `baoxin` | Pemimpin pasukan / Military | ~39 (wafat 192 usia 41 menurut Sanguozhi) | Kamp komando atau inspeksi pasukan | Oker/perunggu |
| Liu Dai | `liudai` | Pejabat provinsi / Civic | Sumber bervariasi; tampil matang, **bukan klaim usia pasti** | Aula pemerintah provinsi | Ungu/plum netral |
| Shen Lian | `shen` | **Perempuan**, original NPC, pedagang/supply | **29**, anchor internal yang sudah disetujui (BUKAN tokoh historis ROTK) | Pasar, karavan, pembukuan dagang | Warna sipil natural sesuai kostum dan situasi |

### Catatan penting khusus Shen Lian

Desain sebelumnya yang menggambarkan Shen Lian sebagai pria mengenakan armor tidak sesuai World Bible dan adegan `shen_talk` yang menyebutnya perempuan dan pedagang. **Jangan gunakan artwork Shen Lian versi prajurit laki-laki.** Scene/portrait berikutnya menggunakan identitas perempuan dan peran pedagang; usia 29 merupakan anchor karakter original menurut World Bible, bukan umur sejarah ROTK.

## Status aset proof

- 10 file `_PROOF.webp` yang diberikan hanya **proof resolusi menengah yang diolah dari contact-sheet**; bukan 10 portrait final hasil render independent resolusi penuh. Jangan masukkan ke HTML tanpa persetujuan pengguna dan QA final.
- Source contact-sheet / proof sifatnya non-final; satu portrait final per NPC harus dirender dengan detail tersendiri, proporsi seperti protagonist, tanpa nama/bingkai, lalu dioptimalkan WebP untuk HTML offline.
- Belum ada penggantian source `PORTRAITS`, perubahan scene, save, atau UI.

## Gate QA visual sebelum integrasi

1. Tidak ada usia/jenis kelamin/peran yang bertentangan dengan dokumen NPC.
2. Militer dan Civic memakai lokasi yang tepat pada saat cerita berjalan.
3. Tidak ada simbol kerajaan atau jabatan anachronistic (misalnya kerajaan Wei berdiri pada 220, bukan 190).
4. Palette didasarkan pada faction-state, bukan label statis untuk perubahan alur alternatif.
5. `People` discovery, thumbnail dan zoom, save/load lama, serta file:// Android diuji secara bertarget setelah embedding.

## Rujukan usia dan jabatan

- Project: `04_WORLD_BIBLE_LEGACY_v1.99.2m.md`, `ALL_UNDER_HEAVEN_VISUAL_ROADMAP_AND_NPC_REGISTER_M1_v1.0.md` dan narasi `shen_talk` dalam HTML v0.4.99.3i.
- [Liu Bei 161–223; Cao Cao 155–220](https://www.societyforasianart.org/sites/default/files/2020-10-09%20Besio%20Study%20Guide.pdf).
- [Sanguozhi Bao Xin wafat usia 41](https://sanguozhi.app/en/chapter/12).
- [Sanguozhi Guan Yu lebih tua dari Zhang Fei](https://sanguozhi.app/en/chapter/36).
- [Gongsun Zan tahun lahir tidak pasti; lebih tua Liu Bei](https://en.wikipedia.org/wiki/Gongsun_Zan).
- [Zhang Miao lahir tidak diketahui](https://en.wikipedia.org/wiki/Zhang_Miao_(politician)); [Qiao Mao lahir tidak diketahui](https://en.wikipedia.org/wiki/Qiao_Mao); [Liu Dai lahir tidak diketahui](https://en.wikipedia.org/wiki/Liu_Dai).
