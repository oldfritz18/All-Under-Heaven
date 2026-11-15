# Checkpoint fungsional M1 — Roads of Trust, v0.4.99.4p

SHA-256 HTML aktif: `6694f0b6c3f8ea38f69c98df94f09f7851cab1a0d7591fb29e238763d0fd8400`.

## Perubahan dan review kontinuitas

Chapter III memperoleh dua scene opsional sepanjang jalur sebelum drill. Continue lama tetap menuju scene latihan yang sama. Proposal hanya dikaji dan dikirim melalui pejabat yang bertanggung jawab; protagonis tetap Private dan tidak memerintah driver, perusahaan, atau rute pasukan.

Perkenalan yang dilewatkan pada 190 tidak lagi mengunci satu-satunya tawaran awal kandidat strategist jika pemain benar-benar bekerja bersamanya pada 191 dan 192, mencapai trust yang diperlukan, serta menyetujui pertukaran berikutnya. Tawaran 193 masih memerlukan penerimaan eksplisit. Pertemuan pertama pada 192 saja tidak menyediakan riwayat bertahun-tahun. Penolakan hubungan personal pada 192 menutup tawaran itu tanpa menghapus kehidupan mandiri NPC atau melarang pemain melanjutkan cerita.

Relasi personal tersebut bukan posisi Strategist pada lima Special Staff. Tidak ada jabatan militer, pangkat, unit, romance, biaya, atau portrait yang diberi oleh cabang baru. Pengetahuan People menggunakan scene yang benar-benar dimainkan, termasuk history-only yang tersimpan; enum tanpa bukti kejadian tidak menghasilkan ingatan.

## Kriteria dan bukti selesai

```sh
python3 scripts/smoke.py
python3 scripts/qa_chapter1.py --report /workspace/work/chapter1_checkpoint_4p.json
python3 scripts/qa_chapter2.py --report /workspace/work/chapter2_checkpoint_4p.json
python3 scripts/qa_m1.py --report /workspace/work/m1_qa.json
```

Semua dijalankan pada source 4p yang hash-nya dicatat di atas. Browser: Chromium headless melalui HTTP lokal, viewport 390 dan 1280 px.

| Bukti | Hasil |
|---|---|
| Smoke dan parsing JavaScript | PASS |
| Semua ID lama / scene tambahan | 630 dipertahankan + 2 opsional = 632 |
| Portrait dan Special Staff | 35 data URI identik; lima role/threshold identik |
| Chapter I | 93 scene, 262 edge per viewport; parity dan save/UI tests PASS |
| Chapter II | 43 scene, 70 edge serta 27 rute pairwise per viewport; PASS |
| Chapter III | 14 scene representatif; 28 edge lama identik, tujuh edge opsional baru; PASS |
| Tujuh rute penuh Prologue–193 per viewport | PASS, 146–148 pilihan per rute |
| Skip 190, kerja 191/192, accept 193 | PASS; hanya menjadi anggota setelah pilihan menerima |
| Skip 190, kerja 191/192, decline 193 | PASS; tidak direkrut |
| Pertama bertemu 192 / courtesy / meninggalkan meja | PASS; tidak memperoleh tawaran palsu |
| Menolak hubungan personal 192 | PASS; dihormati pada 193 |
| Tawaran lama 190 + 191 tanpa cabang baru | PASS |
| Efek baru dipanggil ulang | PASS, tidak menumpuk trust/catatan atau menimpa keputusan |
| Bukti history-only dan flag-only negatif | PASS |
| Bypass Pan: Cavalry dan tahun lebih akhir | PASS, kontrak lama dipertahankan |
| Save/reload HTTP serta UI cabang opsional/People | PASS |
| Page error | 0 |

## Rollback dan batas

Checkpoint menyimpan v0.4.99.4o sebagai satu-satunya HTML pada `ROLLBACK/`. Baseline 4m dan checkpoint yang lebih tua tetap ada di ZIP starter dan histori Git. `INITIAL_MANIFEST_SHA256.txt` adalah manifest paket awal, bukan manifest source yang sudah berkembang.

Ini checkpoint fungsional dan review naratif batch I–III yang mengizinkan pekerjaan berurutan IV. Ini **bukan** sertifikat semua kombinasi pilihan, pembacaan editorial seluruh novel, audit biografi lengkap, actual-device `file://`, Android, atau rilis M11. Objective Prologue–XIX/Epilogue belum selesai.
