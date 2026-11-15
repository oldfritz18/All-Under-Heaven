# Chapter II — The Left Crossing, v0.4.99.4o

Build SHA-256: `9cda6b8a24ceb35748ea2fd367ecc5a15315ad146c8be5856036b24c906ca997`.

## Selesai

- Review dan perluasan delapan scene: tujuh scene Pan River dan satu surat antarpasukan. Fokus: posisi infanteri, Han Sheng sebagai atasan, pengalaman terbatas pemain, tindakan mandiri komandan ROTK, tradeoff posisi, humor dan akibat manusiawi.
- Tidak menambahkan duel pemain, perkenalan personal dengan Zhao Yun, kematian rekaan, promosi, pengalihan loyalitas, portrait atau jabatan staf.
- Laporan sore kini memakai status posisi **last witnessed**. Sebelumnya, posisi tetap aktif sampai pemain memilih cara menyusun laporan, walaupun narasi sudah keluar dari medan perang.
- Migrasi untuk save yang sudah mencapai laporan hanya menyelesaikan pencatatan gerakan yang memiliki proof yang cocok; tidak mengulang efek pilihan, menambah Chronicle retroaktif, atau mengubah penugasan lain.

## Bukti yang dijalankan

```sh
python3 scripts/smoke.py
python3 scripts/qa_chapter2.py --report /workspace/work/chapter2_qa.json
```

| Pemeriksaan | Hasil |
|---|---|
| Smoke statis dan parsing JavaScript | PASS |
| Registry, Special Staff, 35 data URI portrait | PASS, identik baseline |
| Chapter II BFS, state representatif | 43 scene, 70 edge pada masing-masing 390/1280 px |
| Kontrak pilihan vs ZIP v0.4.99.4m | PASS kecuali status posisi yang diperbaiki dan catatan penarikan baru |
| Rute taktis lengkap | 27 per viewport; semua pasangan dari enam keputusan tiga-arah tercakup |
| Posisi aktif sebelum penarikan / nonaktif setelahnya | PASS pada setiap rute taktis |
| Protagonis 17 tahun, 191 CE, Private, Infantry | PASS; tidak mendapat pertemuan Zhao Yun atau jabatan otomatis |
| Ingatan Military dan People / Chronicle satu kali | PASS, read-only saat panel dirender |
| Migrasi save visited dan history-only | PASS; hanya status posisi berubah |
| Negatif: flag-only, cavalry, proof lain, scene lain | PASS, posisi tidak diubah |
| HTTP save/reload setelah mundur | PASS |
| Navigasi Military lewat menu dan pagination Story | PASS pada kedua viewport, tanpa horizontal overflow |
| Page error | 0 |

## Batas dan langkah berikutnya

Review historis batch mempertahankan adaptasi ROTK Bab 7 dan penanggalan 191 dari roadmap; deskripsi baru dibatasi pada tindakan lokal dan informasi yang dapat didengar pemain. Nama/deed dari pertarungan berkuda tetap laporan bersumber, terutama untuk pilihan rear yang tidak melihat duel.

Hasil bukan full-combination regression, audit semua sumber biografi, pembacaan semua jalur novel, atau sertifikasi Android/physical-device `file://`. Langkah berikutnya: Chapter III, pertemanan yang dapat ditolak, review layanan, serta checkpoint M1 lintas tiga chapter.
