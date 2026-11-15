# QA M2 — Roads and Witnesses, v0.4.99.4u

SHA-256 HTML: `b95b16f9ce6f2c422bfd9c5f481eea038315a3f0324ce9aefa8474adbc85c3b6`.

Delapan scene baru mengisi W08 dan W10. Tiga tahap W10 ditambah audience opsional mempertahankan kehadiran berdasarkan perintah dan persetujuan. Xu Shu tetap punya kewajiban sendiri; salinan 208 bukan pertemuan baru. Acquaintance valid pada save lama tidak dihapus. W07 tetap laporan dunia karena penugasan pemain berada di sektor lain.

```sh
python3 scripts/smoke.py
python3 scripts/qa_m2_continuity.py --report /workspace/work/m2_4u_qa.json
python3 scripts/qa_chapter1.py --report /workspace/work/4u_chapter1.json
python3 scripts/qa_chapter2.py --report /workspace/work/4u_chapter2.json
python3 scripts/qa_m1.py --report /workspace/work/4u_m1.json
python3 scripts/qa_chapter4.py --report /workspace/work/4u_chapter4.json
python3 scripts/qa_chapter5.py --report /workspace/work/4u_chapter5.json
python3 scripts/qa_chapter6.py --report /workspace/work/4u_chapter6.json
python3 scripts/qa_chapter7.py --report /workspace/work/4u_chapter7.json
```

Semua perintah selesai exit 0 pada source hash di atas. Browser: Chromium headless melalui HTTP lokal, viewport 390 dan 1280 px. Data terstruktur tersimpan di `docs/qa/CHECKPOINT_4u.json`.

| Kontrak baru | Hasil per viewport |
|---|---|
| Seluruh ID lama/portrait | 642 dipertahankan + delapan = 650; 35 data URI identik |
| W08 | 108 rute pairwise preferensi/posisi/aksi/exit, kedua branch dan dua jenis laporan |
| W10 | 144 kombinasi lokal: kedua branch, seed organik Sergeant/Private, posisi, aksi, laporan biasa/tiga balasan audience |
| Kalender default | W08 200/26; W10 tetap 207/33 sebelum kembali ke 208/34 |
| Rank/unit/staff/circle/items/coins | PASS, tidak ada grant dari arc |
| Field position | Aktif saat aksi, last witnessed di aftermath |
| Xu Shu | Meeting hanya setelah audience 207 yang dipilih; paket 208 tidak memberi acquaintance |
| Save lama dan attendance | Acquaintance lama dipertahankan; late save tidak rewind; flag-only tidak memberi memory/evidence |
| Evidence | Idempotent, read-only pada UI, history-only sah, enum tidak valid ditolak |
| HTTP reload dan Military DOM | PASS, tanpa overflow |
| Page error | 0 |

Regression suite I–VII juga lulus. Projector parity hanya mengecualikan target/act insert 200 dan target/kalender insert 207 yang disengaja; efek choice lama selain kontrak tersebut tetap dibandingkan. Pemeriksaan catalog mempertahankan seluruh ID baseline, sementara ID tambahan diuji pada suite arc terkait agar penambahan chapter lain tidak merusak tes yang tidak terkait.

Laporan suite lama masih mencatat batas scope historisnya. Klasifikasi implementasi terbaru untuk W07/W08/W10 adalah `M2_CAMPAIGN_COVERAGE.md` dan suite M2 ini. Ini bukan sertifikasi full-combination novel, semua biografi, atau physical-device `file://`. VIII masih membutuhkan koreksi kewenangan serta urutan Bowangpo/Xinye → Changban/Red Cliffs.
