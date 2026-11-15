# Chapter I — batch perkenalan dan gate bertarget v0.4.99.4n

## Kriteria selesai dan hasil

- Empat scene awal calon sahabat/penasihat memiliki percakapan substantif, kepribadian, kesalahan yang dikoreksi, hak menolak, dan posisi protagonis yang sesuai kewenangannya: selesai melalui review naskah batch.
- Pilihan bekerja sebagai keputusan personal, bukan pengangkatan: lulus pemeriksaan state dan perbandingan dengan starter asli.
- Callback tidak mengarang ingatan pada save yang hanya memuat flag tanpa kejadian: lulus pengujian visit/history, termasuk history-only yang sah.
- Prosa game tetap Inggris; narasi Chapter I mempertahankan usia 16 pada 190, tanpa otoritas baru, pasangan, atau rekrutmen otomatis.

## Bukti yang dieksekusi

Build: `GAME/ALL_UNDER_HEAVEN_v0.4.99.4n_CHAPTER_I_COMPANIONS.html`.

SHA-256: `427c044f500690d2006337394e610a8f4abadc656dd3c0a34d09eac62871a834`.

Perintah:

```sh
python3 scripts/smoke.py
python3 scripts/qa_chapter1.py --report /workspace/work/chapter1_qa.json
```

Harness browser memerlukan Playwright dan Chromium; pengujian dilakukan di Chromium headless melalui server HTTP lokal, tanpa layanan berbayar.

| Pemeriksaan | Hasil |
|---|---|
| Smoke statis | PASS, 8/8 |
| JavaScript `node --check` | PASS |
| Registry dan lima Special Staff | PASS, 630 scene dan daftar/threshold identik |
| Data URI portrait | PASS, 35 identik dengan ZIP baseline |
| BFS Chapter I dalam satu state representatif per scene | PASS, 93 scene, 262 choice edge pada setiap viewport 390/1280 |
| Label, tujuan dan efek state pilihan lama | PASS, dibandingkan dengan HTML v0.4.99.4m dari ZIP; hanya enum jawaban baru serta dua catatan Chronicle baru dikecualikan dari parity |
| Tiga jawaban Wei Zhen dan People recall | PASS pada kedua viewport |
| Callback read-only, visit/history dan flag-only negatif | PASS |
| Save/reload HTTP, tiga jawaban | PASS |
| Save baseline dibaca melalui handler game lalu reload HTTP | PASS; tidak mengisi enum baru secara retroaktif |
| Tombol pagination, lanjut/skip perkenalan, buka/tutup menu | PASS melalui DOM pada kedua viewport, tanpa horizontal overflow |
| Page error | 0 |

## Review kontinuitas dan batas

- Wei Zhen tetap copyist yang mempunyai pekerjaan dan ambisi sendiri; salah salin dapat ia akui, tetapi keputusan resmi tetap milik clerk pemegang seal. Menolak atau berdebat tidak mengangkat atau merekrutnya.
- Han Sheng tetap komandan patroli. Pemeriksaan singkat fastening menjelaskan risiko jalan bagi infanteri; bukan penempatan protagonis ke logistik atau tugas support.
- Xu Wen tetap rekan satu file. Pilihan kedekatan, bantuan terbatas, dan menjaga jarak memiliki tanggapan berbeda tanpa menghilangkan kewajibannya sebagai prajurit.
- Perkenalan dan callback direview terhadap scene masuk/keluar, Chapter I tahun 190 dan posisi awal patroli; review batch tidak berarti semua prosa lama atau kombinasi rute sudah dibaca dan disertifikasi.
- BFS memakai satu state representatif per scene. Kombinasi seluruh keputusan, full campaign, physical-device `file://`, dan Android belum disertifikasi. Hasil ini cukup untuk melanjutkan batch Chapter II, bukan sign-off rilis.
