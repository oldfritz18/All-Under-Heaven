# Assigned River Patrol — v0.4.99.4y

Build `GAME/ALL_UNDER_HEAVEN_v0.4.99.4y_THE_ASSIGNED_RIVER_PATROL.html`.
SHA-256 `c0829fa65a9d3584162a094f394c4ce722b79cea371386e8d0fb1fa30ddc037a`.

Sembilan node lama dari flotilla sampai twilight/`ch08_03` diperluas sebagai rangkaian embarkation, council, crew drill, briefing, patroli, kontak, shore coordination, konflik perintah serta malam setelah kontak. Konteks ROTK lama dipertahankan; patroli company, dialog dan tugas spesifik adalah fiksi orisinal, bukan klaim adanya unit/komisi pemain dalam sumber sejarah.

Boatmaster mengatur crew/navigation; deck officer dan company memimpin tugas tempur. Private tetap di dalam section. Commander hanya memerintah active muster. Cavalry naik perahu sebagai dismounted combatants; branch tidak berubah menjadi Support/naval class. Tidak ada kapal pribadi atau resource baru. Satu perintah escort dinyatakan eksplisit dan dicatat sebagai posisi 208; posting lebih akhir tidak ditimpa. Callback laporan pagi menerima proof 4x maupun 4y yang benar-benar dimainkan untuk menutup posisi.

Pilihan lama, next IDs, enum, scores, relations dan wrapper flags dipertahankan oleh handler yang sama. Label/Chronicle baru mengikuti scope sebenarnya. Tiga tujuan patroli menghasilkan laporan berbeda (shoal, partial enemy watch, civilian receiving route), biaya lokal, batas informasi serta recall. Bukti opsional `campaignEvidence.riverRecon208` baru direkam pada exit kontak setelah embarkation yang terbukti; Military/People memerlukan sumber/aksi/branch/tahun dan visit/history. Tidak ada credit ketika render/load, flag-only, enum invalid atau branch tak diketahui.

## Hasil eksekusi

- `python3 scripts/smoke.py`: 8/8 PASS.
- `python3 scripts/qa_river_patrol.py --report /workspace/work/4y_patrol.json`: **216 rute per viewport 390/1280**; empat seed karier organik (Captain, Sergeant lama, Sergeant baru, Private), dua branch (Cavalry fixture sintetis), 27 kombinasi pairwise dari lima keputusan tiga-arah.
- Seluruh efek pilihan pada sembilan node dibandingkan dengan 4x untuk seed Captain dan Private, identik selain field position, bukti, flag embarkation serta Chronicle yang disengaja. Body/label/effect fixture Major identik penuh.
- Rank/unit/staff/goods/recruit tetap; Cavalry dismounted tetap Cavalry; laporan, recall, provenance, history-only, idempotence, read-only dan later-post guard PASS.
- Reload localStorage HTTP, Military DOM dan **9 klik nyata** memakai Private/history penuh PASS. Tidak ada page error/overflow horizontal.
- Registry tetap 658; 35 embedded images byte-identical via fixture; JS syntax check dan Python compile PASS. Tidak mengubah engine/save key.

Matriks tidak melukis/menulis storage setiap variasi dan mengosongkan body history lama sebagai string; jalur DOM terpisah memakai history penuh. Belum membuktikan seluruh novel, semua cabang fire battle/settlement, chapter mapping baru, Android atau perangkat `file://`. M3–M11 belum tuntas. Tidak ada biaya, push, portrait baru atau perubahan locked decisions.

Regresi `scripts/qa_river_councils.py` pada hash yang sama juga PASS: 216 rute dan 17 klik DOM per viewport, termasuk penutupan posisi escort pada laporan pagi 209. Bukti gabungan: `docs/qa/BATCH_4y.json`.
