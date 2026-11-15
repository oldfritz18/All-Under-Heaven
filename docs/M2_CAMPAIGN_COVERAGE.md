# Coverage kampanye — gate M2 pada v0.4.99.4u

Klasifikasi berlaku pada rute yang benar-benar dimainkan. Tahun, rumor, portrait atau flag lama saja tidak menghasilkan pengalaman tempur. Ledger ini memperbarui status implementasi pada roadmap lama; tidak mengubah desain W01–W14.

| Anchor | Cakupan executable | Bukti dan batas kehadiran |
|---|---|---|
| W01, Sishui–Hulao 190 | Playable langsung, sektor infanteri | `hulao_*` dan interaksi Chapter I; duel tiga bersaudara tetap milik para tokoh novel. |
| W02, Pan River 191 | Playable langsung pada penugasan Infantry | `pan_*`; Cavalry/save lebih akhir melewati insert; Zhao Yun bukan acquaintance dari glimpse. |
| W03, Beihai 194 | Playable parsial, perlindungan jalan bantuan | `m2_194_beihai_*`; Kong Rong dan keadaan kota adalah laporan, bukan audiensi atau penaklukan oleh pemain. |
| W04, Xuzhou 194 | Playable langsung pada sektor defensive road | `m2_194_xuzhou_*`; menahan sektor tidak menetapkan kepemilikan provinsi. |
| W05, Yuan Shu/Xuzhou 197 | Playable parsial kampanye | `m2_197_*`; tiga preferensi layanan menentukan sektor, tetap combat; perang para lord lebih luas dari aksi lokal. |
| W06, Xiaopei 198 | Playable langsung bila memilih forward-service | `m2_198_xiaopei_*`; jalur non-forward tetap mendapat laporan tanpa credit tempur. |
| W07, Xiapi 198–199 | Laporan dunia bersumber | `ch06_08`/`ch06_09` dan dispatch opsional; perusahaan tidak menerima penugasan ke siege, jadi tidak diciptakan attendance atau credit penangkapan Lü Bu. |
| W08, Xuzhou 200 | Playable langsung pada penarikan sektor | `m2_200_xu_*`; masuk lewat exit VI dengan branch tercatat dan tahun sesuai. Save lebih akhir tidak dipundurkan. |
| W09, Runan/Rangshan 201 | Playable parsial bagi Sergeant road watch yang sah; laporan pada jalur lain | `m2_201_watch_*`; memerlukan penerimaan warrant dan unit 20 personel yang benar. Keputusan seluruh army tetap di luar kuasa watch. |
| W10, Xinye–Fancheng 207 | Playable langsung pada wing yang ditugaskan; pertemuan adviser opsional | `m2_207_fan_*` dan `m2_207_xushu_debrief`; central attack dan capture kota tetap operasi komandan lain. Tidak ada pertemuan hanya karena membaca salinan di 208. |

## Matriks insert dan kalender

| Jalur lama | Insert | Kembali |
|---|---|---|
| `ch06_10` → `ch07_01` | Empat `m2_200_xu_*`, bila branch sah/tahun ≤200 | `ch07_01`, 200 CE, usia default 26 |
| `ch07_13` → `ch08_pb55_foreword` | `m2_207_fan_orders/contact/report`; audience opsional | VIII pada 208, usia default 34; arc tetap 207/33 hingga selesai |
| `ch08_pb55_xushu` → `ch08_pb55_council` | Node tetap; narasi kini salinan tertanggal | ID dan tujuan dipertahankan, tanpa acquaintance baru |

Sumber adaptasi: roadmap kampanye yang disetujui; [ROTK Bab 24](https://kongming.net/threekingdoms/24) untuk reverses Xu Province, dan [Bab 36](https://kongming.net/threekingdoms/36) untuk pola serangan, recall dan operasi Fancheng oleh Xu Shu/Shan Fu. Tahun 207 mengikuti window roadmap adaptasi. Dialog/tindakan prajurit lokal adalah fiksi orisinal; bukan kutipan atau klaim biografi prajurit nyata.

Gate ini cukup untuk melanjutkan perbaikan M3 secara berurutan. Verifikasi semua jalur novel, kronologi seluruh NPC, actual-device offline storage, serta audit M8–M11 tetap belum selesai. Problem kewenangan dan urutan kampanye pada VIII dicatat di PROGRESS dan tidak dianggap selesai oleh ledger ini.
