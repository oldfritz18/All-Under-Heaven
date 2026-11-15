# Checkpoint batch I–VII — Twenty Names, v0.4.99.4t

Build: `GAME/ALL_UNDER_HEAVEN_v0.4.99.4t_CHAPTER_VII_TWENTY_NAMES.html`.

SHA-256: `dbe0f46f2f866a2d385dccd6b9ed0f7788c4353dbf43f2f9b0d0ba849af80f66`.

## Review batch VII

Warrant Sergeant dan road watch 20 personel sudah ada pada baseline. Arc baru tidak menerbitkan warrant pengganti: hanya jalur penerimaan yang sah dan Infantry yang masuk ke tiga scene Runan 201. Rank, unit dan proof diperiksa sebelum keterlibatan, dengan jalan lama tetap tersedia untuk penolakan, Cavalry, record yang tidak konsisten dan save lebih akhir.

Protagonis belajar memberi perintah yang dibatasi warrant, menerima koreksi veteran, meminta pengulangan signal dan menanggung biaya gerakan. Dua puluh nama benar-benar dibaca di akhir aksi lokal; tidak ada klaim tentang kembalinya seluruh pasukan Liu Bei. Ransum atau alat perusahaan yang hilang bukan reward atau pengurangan item pribadi rekaan. Keputusan komandan dan pasukan Liu Pi/Gong Du tetap di luar komando pemain. Tujuan Jing Province sesudah reverses berasal dari konteks W09 roadmap dan laporan legacy, bukan kemampuan player menentukan seluruh perang.

First-thaw 201 pada recall lama dibuat netral menjadi During 201 agar tidak memaksa urutan musim yang bertentangan dengan aksi yang baru dimainkan. Tidak ada skema save, NPC identity, role Special Staff atau portrait yang diubah.

## Bukti batch VII

```sh
python3 scripts/qa_chapter7.py --report /workspace/work/chapter7_qa.json
```

Pada setiap viewport 390/1280: 18 scene legacy dan tiga baru; 44 edge legacy diuji dengan input state identik, sembilan edge baru; seluruh 27 kombinasi posisi/aksi/review lulus. Penolakan dan permintaan kewenangan tidak memberi rank/unit. Empat kondisi entry negatif, replay commission tanpa unit duplikat, efek review berulang, memory flag-only, save/reload legacy dan aftermath, menu Military serta overflow lulus. Page error 0.

## Regression source checkpoint yang sama

Semua perintah berikut selesai dengan exit 0 pada HTML yang hash-nya tercantum di atas:

```sh
python3 scripts/smoke.py
python3 scripts/qa_chapter1.py --report /workspace/work/final_4t_chapter1.json
python3 scripts/qa_chapter2.py --report /workspace/work/final_4t_chapter2.json
python3 scripts/qa_m1.py --report /workspace/work/final_4t_m1.json
python3 scripts/qa_chapter4.py --report /workspace/work/final_4t_chapter4.json
python3 scripts/qa_chapter5.py --report /workspace/work/final_4t_chapter5.json
python3 scripts/qa_chapter6.py --report /workspace/work/final_4t_chapter6.json
python3 scripts/qa_chapter7.py --report /workspace/work/chapter7_qa.json
```

| Suite | Bukti per viewport 390/1280 |
|---|---|
| I | 93 scene, 262 edge, reply/legacy/save/UI tests PASS |
| II | 43 scene, 70 edge + 27 rute pairwise, migration/save/UI PASS |
| M1/III | 14 scene, 28 edge lama + tujuh baru; tujuh rute Prologue–193, 146–148 pilihan per rute PASS |
| IV | 20 scene, 53 edge + 54 rute kampanye, migration/branch/save/UI PASS |
| V | 16 scene, 33 edge lama + delapan baru; 108 rute lokal 197 PASS |
| VI | 12 scene legacy + empat baru, 25 edge lama + 11 baru; 108 rute lokal Xiaopei PASS |
| VII | 18 scene legacy + tiga baru, 44 edge lama + sembilan baru; 27 rute road watch PASS |

Seluruh 630 ID awal dipertahankan, total kini 642. Semua 35 data URI portrait identik dengan sumber. Lima Special Staff dan threshold dipertahankan; eligibility tidak dianggap appointment. Data hasil lengkap tersimpan di `docs/qa/CHECKPOINT_4t.json`.

## Batas, rollback dan pekerjaan berikutnya

- Browser yang diuji: Chromium headless melalui HTTP lokal. Interaksi DOM dipakai pada jalur UI terpilih; sebagian besar kontrak menggunakan handler `choose()` asli game. Ini bukan pembacaan semua kombinasi novel atau sertifikasi physical-device `file://`/Android.
- Cavalry pada suite IV–VI adalah fixture penugasan lama sintetis. VII tidak mengarang bahwa Infantry road watch adalah unit cavalry.
- W07/Xiapi, W08/Xuzhou dan W10/Fancheng masih memerlukan rekonsiliasi coverage partial/report terhadap gate M2; checkpoint ini tidak menyatakan semua kampanye M2 selesai.
- VIII–XIX/Epilogue dan M8–M11 belum selesai. Registry baseline hanya memiliki struktur chapter legacy sampai XII dan endings; tidak ada tag XIII–XIX. Tujuan penuh masih memerlukan pekerjaan besar.
- Rollback formal: `ROLLBACK/ALL_UNDER_HEAVEN_v0.4.99.4s_CHAPTER_VI_XIAOPEI.html`. Versi lebih lama tetap tersedia dalam Git dan ZIP awal. `INITIAL_MANIFEST_SHA256.txt` tetap manifest paket awal.
- Berhenti pada checkpoint ini karena batas sumber daya konteks sesi, dengan source, laporan dan antrian berikutnya tercatat. Tidak ada push atau layanan berbayar.
