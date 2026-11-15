# Retreat–Changban–Hanjin: QA bertarget 4w

Build: `GAME/ALL_UNDER_HEAVEN_v0.4.99.4w_CHANGBAN_THE_RECEIVING_LINE.html`.
SHA-256: `c16ff751d643d0239a7f628b2cbf025c3895af11bf42ec8a069768d301d696b0`.

Sembilan node legacy dipertahankan dan direvisi sesuai cakupan: succession, refugees, march, Zhao Yun road, cavalry contact, Changban, Zhang Fei crossing, Xu Shu report, Hanjin. Pada Private/Sergeant/Captain narasi dan keputusan kini mengikuti perintah company, active muster, formasi Infantry/Cavalry, sektor, recall, NPC otonom serta batas informasi. Komandan dengan muster dapat memerintah personelnya; Private/tanpa muster beraksi di dalam section yang dipimpin section leader. Tokoh historis tidak menjadi bawahan karena pilihan dialog.

Semua enum penting dipertahankan: evacuation `families|stores|pilots`, Zhao `search|guard|intelligence`, Changban `hold|screen|river`, Zhang `joint|feint|withdraw`, Xu `inquiry|escort|search`. Relasi Zhao trust/respect dan Zhang respect tetap mengikuti pilihan yang sesuai. Catatan Chronicle diubah dari klaim pasukan mandiri menjadi tindakan yang benar-benar dimainkan. Callback retreat dan Military/People memakai bukti `campaignEvidence.changban208` yang memerlukan sumber, aksi, tahun, branch dan visit/history; record baru hanya pada exit Hanjin setelah kontak/crossing nyata. Tidak ada hadiah pangkat/pasukan/item/staff baru.

Xu Shu tidak lagi ditemui sedang menerima berita keluarganya di Changban. Pada **semua rank**, node lama menjadi pembacaan dispatch terdahulu dan laporan misi Fancheng; tidak menambahkan acquaintance, rescue, perjalanan scout yang tidak diotorisasi, atau keanggotaan. Acquaintance lama tetap dipertahankan. Riset kontinuitas: ROTK bab 41–42, https://kongming.net/threekingdoms/41 dan https://kongming.net/threekingdoms/42 (15 November 2026): pengungsian, kewajiban terpisah Zhao/Zhang, penyeberangan, serta Xu Shu sebagai utusan yang kembali ke utara. Dialog dan situasi company baru adalah fiksi orisinal, bukan kutipan terjemahan; laporan bukan pengetahuan mahatahu.

## Pemeriksaan yang dijalankan

- Smoke: `python3 scripts/smoke.py`, 8/8 PASS.
- `python3 scripts/qa_changban.py --report /workspace/work/4w_changban.json`, PASS pada 390/1280 px. Per viewport: **216 rute pairwise**, empat seed karier organik 4v (Captain diterima, Sergeant lama menolak komisi baru, Sergeant baru dari Private, Private tetap menolak), dua branch (Cavalry sintetis), 27 kombinasi yang mencakup seluruh pasangan lima keputusan tiga-arah.
- Tahun/usia tetap 208/34; posisi aktif saat kontak dan retired setelah recall; rank, muster, appointment, staff, branch, circle, coins/items tidak berubah. Tidak ada acquaintance dari laporan; enum dan callback lokal tepat; read-only dan idempotence PASS.
- History-only diterima; flag-only, enum invalid dan branch tidak diketahui tidak memberi credit. Posisi sah 214 tidak ditimpa. Tujuh node di luar koreksi Xu Shu: body/choice/effect fixture Major identik dengan baseline 4v.
- Reload localStorage HTTP dan Military DOM PASS; **9 klik DOM nyata** dari seed Private dengan history penuh mencapai dewan Hanjin berikutnya tanpa promosi. Page error 0, overflow horizontal 0.

Matriks memakai handler `choose`/validasi asli, history body lama dikosongkan sebagai string dan render/save/scroll dimatikan sementara; uji DOM terpisah memakai history penuh dan penyimpanan/render asli. Ini bukan pembuktian semua kombinasi novel atau perangkat nyata/file://. Registry tetap 658 dan semua 35 embedded image identik. Save key dan engine lama dipertahankan.

Gerbang M3 belum selesai: dewan sungai/Red Cliffs, otoritas komisi 209, pemetaan chapter VIII–X dan kampanye lanjut masih perlu kerja. Tidak ada biaya, push atau perubahan locked decisions.

Regresi pembuka VIII `scripts/qa_chapter8.py` juga PASS pada hash 4w yang sama: 324 rute dan 11 klik DOM per viewport. Bukti gabungan: `docs/qa/BATCH_4w.json`.
