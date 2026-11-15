# ALL UNDER HEAVEN — Combat Role Lock v1.0

**Keputusan pemain:** 14 November 2026  
**Status:** APPROVED DESIGN DECISION — belum dinyatakan terimplementasi dalam HTML.  
**Scope:** Prologue–Chapter XIX dan Epilogue; berlaku untuk kedua part roadmap 190–250 M.

## Aturan wajib

1. **Unit tempur protagonis hanya INFANTRY atau CAVALRY.** Pemain boleh memulai sebagai infanteri, lalu bergabung/beralih ke kavaleri hanya jika ada penugasan/kejadian yang sah dan memenuhi syarat di cerita.
2. **Tidak ada penempatan protagonis pada pasukan SUPPORT.** Hindari assignment sebagai juru logistik, pembawa suplai, petugas medis, kurir non-tempur, administrasi, pekerja kamp, atau unit pembantu perang sebagai role utamanya.
3. **Tugas tempur tetap boleh beririsan dengan kebutuhan pasukan** (mis. infanteri/kavaleri menjaga jalur konvoi, melindungi warga, atau mengawal kereta di tengah operasi). Narasi harus memperjelas bahwa protagonis adalah **anggota pasukan tempur** yang menjaga perimeter atau menghadapi musuh, bukan anggota unit logistik yang mengurus pengiriman barang.
4. **Posisi dan pengalaman di medan perang wajib terasa langsung:** barisan, sayap, garis depan, formasi, serangan, pertahanan, mundur, korban, perintah atasan, dan konsekuensi tindakan. Bukan laporan perang dari luar barisan.
5. **Pangkat dan komando tidak boleh otomatis.** Saat pangkat berkembang, protagonis dapat mengendalikan infanteri/kavaleri sesuai kewenangan yang benar-benar diberikan. Kebutuhan logistik tetap berdampak pada kampanye, tetapi dikelola NPC/sistem, bukan dengan memindahkan protagonis ke unit support.
6. **Pilihan pemain:** jika adegan menawarkan role tempur, opsi utama hanya infanteri/kavaleri yang sah secara naratif; pilihan lain seperti menarik mundur atau membantu orang terluka ketika bertempur boleh ada sebagai tindakan situasional **bukan perubahan unit menjadi support**.
7. **Kompatibilitas:** scene/choice/save lama tidak dihapus. Audit semua scene dan choice yang saat ini menempatkan protagonis pada peran support; lakukan penyesuaian pada konteks narasi, assignment dan UI tanpa mengarang bahwa revisi sudah selesai.

## Audit yang wajib saat development

- Story: sebutkan unit, posisi, komandan, dan misi tempur protagonis pada setiap battle scene.
- Character / Military: tampilkan role dan status unit tempur aktual; jangan beri label Support pada protagonis.
- People / Chronicle: catat prestasi, luka, pertemanan, korban, dan akibat hanya jika terjadi.
- Save/load: assignment infanteri/kavaleri konsisten lintas save dan tidak berubah hanya karena chapter/tahun.
- Regression: cek jalur Chapter I (termasuk konvoi dan Hulao Gate), Chapter II Pan River, lalu seluruh perang ROTK dan Emperor Saga pada milestone masing-masing.

**Catatan batas implementasi:** dokumen ini mengunci keputusan desain, **tidak mengubah HTML** sampai patch narasi/state/UI dan QA benar-benar dilakukan.
