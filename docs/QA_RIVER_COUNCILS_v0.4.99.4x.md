# Dewan sungai — v0.4.99.4x

Build `GAME/ALL_UNDER_HEAVEN_v0.4.99.4x_RIVER_COUNCILS_AND_ORDERS.html`.
SHA-256 `55b966bf9fbf2ab1118ab2d4d8b1aa81649ffd91391eace42154c34398a3bddd`.

Lima belas node lama dari dewan Hanjin sampai pemberian tugas company direvisi secara kondisional untuk Private/Sergeant/Captain. Perbaikan meliputi daftar penumpang, peran boatmaster, otonomi Guan Yu/Liu Qi/Lu Su/Zhuge Liang, permintaan yang masih perlu diterima, signal, laporan, ketidakpastian, humor dan aftermath. Tidak ada armada pribadi, Quartermaster atau lieutenant pribadi yang muncul tanpa penunjukan.

Helper pilihan mempertahankan handler lama, enum, skor, relasi, wrapper flags dan routing. Hanya label serta teks Chronicle baru yang mengklaim otoritas melampaui muster diperjelas. Custody ledger adalah tugas membawa dokumen; proposal sekutu bukan treaty yang diterima. Pilihan pada `ch08_player_council` memberi tugas tempur lokal dengan muster yang sudah ada: reserve, shared signals atau forward screen. Private tetap di bawah section leader. Tidak ada promotion/unit/staff/ship/resource grant. Character social position dan Military recent service mencerminkan otoritas ini; state formal lebih tinggi tetap melalui fallback lama.

`fieldPosition` mendapat perintah/sektor/formasi/objective/superior pada tugas yang benar-benar diterima. Exit laporan pagi lama menutup **hanya** proof tugas 4x yang sudah melewati node pertempuran, tanpa menimpa posting lain atau tahun lebih akhir. Ini perbaikan lifecycle posisi, bukan sertifikasi seluruh prosa pertempuran lama.

## Bukti

- `python3 scripts/smoke.py`: 8/8 PASS; Node inline JS check dan byte comparison 35 embedded images melalui fixture PASS.
- `python3 scripts/qa_river_councils.py --report /workspace/work/4x_river.json`: **216 rute per viewport 390/1280**, empat seed karier organik × dua branch × 27 baris orthogonal. Sebelas kelompok pilihan diuji seluruh pasangan lokal; harness juga mengassert coverage pasangan, bukan hanya mengasumsikannya. Cavalry merupakan fixture legacy sintetis.
- Tidak ada rank/unit/staff/ship/goods/recruit tambahan. Company task, Private authority, Chronicle/Character/Military, stable repeated task dan posting tahun lebih akhir PASS. Lima belas node fixture Major mempertahankan body/label/effect lama.
- Reload localStorage HTTP dan Military DOM PASS. **17 klik browser nyata** memakai seed Private/history penuh mencapai flotilla berikutnya tanpa promotion. Pemeriksaan handler terpisah melanjutkan battle default sampai 209 untuk memverifikasi posisi tugas retired; tidak mengklaim mutu prosa/outcome battle sudah lulus. Page error 0; overflow horizontal 0.
- `python3 scripts/qa_changban.py --report /workspace/work/4x_changban.json` kembali PASS pada hash yang sama: 216 rute serta 9 klik DOM per viewport.
- Matriks menonaktifkan paint/storage/scroll sementara dan mengosongkan body history lama sebagai string; jalur DOM/reload terpisah memakai rendering serta penyimpanan asli. Registry tetap 658; save key/engine dan portrait tidak diganti.

Data: `docs/qa/BATCH_4x.json`. Belum selesai: prosa/otoritas/outcome Red Cliffs setelah flotilla, settlement dan komisi 209, pemetaan bab VIII–X serta M3–M11. Physical-device/Android/file:// belum diuji. Tidak ada biaya, push, atau perubahan locked decisions.
