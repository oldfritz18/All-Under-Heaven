# Audit pemisahan authority — sumber aktif 5j

Audit kode pada SHA `1490bf4b6860097725c7c096c5b8f727952fcd34467efa24db89ed127209c3a8`, 16 November 2026. **Audit bukan implementasi accession, acceptance Issue #1/#2 atau signoff seluruh legacy ending.** Baris di bawah mengacu pada HTML aktif 5j; dapat bergeser pada successor. Tidak ada global replacement royal predicates dalam batch 5j.

## Fakta kode yang harus dipertahankan saat M4 berikutnya

- `auh65Eligible`/`auh65Crowned` (7046–7056) merupakan regional charter/territory/council/frontier/crown predicates lama. Bukan proof sah succession Shu. Regional route dan valid saves tetap kompatibel, tetapi maknanya harus diadaptasi per scene/reader pada jalur Shu baru; jangan menghapus seluruh underlying management.
- `auh79Emperor` (9153) menuntut crowned + north/west/east settled + ratified congress + imperial oath. Ini **legacy unification predicate**, bukan Shu accession. `auh79RegionsEarned` (9187) berbeda lagi karena belum mensyaratkan congress/oath. Shu crown tidak boleh otomatis membuat salah satu true.
- Pencarian literal `\bNAME\s*\(` menemukan 37 baris untuk `auh79Emperor`, 44 untuk `auh65Crowned`, masing-masing termasuk definisi. Ini inventaris statis, bukan jumlah effective runtime readers atau bukti semua closure telah diuji.

## Kelompok pembaca dan perubahan yang diperlukan

| Pembaca/source locator | Kontrak M4/M5 yang diperlukan |
|---|---|
| Character `auhMcPortraitStage`/overview sekitar 3590/3660 dan `auh63SocialPosition` wrappers 7177/9307/9750/10133 | Imperial Shu title dari actual accession; united China title dari actual conquest/settlement; rank/honour dan abdication dibaca terpisah. Pertahankan delapan portraits. |
| Civic unlock dan panel head `auhMcCivicUnlocked`, `auhMcPanelHead`, `civicPanel` 4417/4472/4547 | Shu office dapat membuka imperial government sebelum reunification; existing Governor/career/territory tidak disalin menjadi Emperor. Appointed imperial offices berbeda dari vacant potential seats. |
| People/office registry `auhStoryUIOfficialRegistry`, `auhStoryUILiveNpcFacts` 3980/3990 | Registry `imperialOfficials` berbeda dari `governorOfficials`; known NPC dan actual appointment perlu proof. Existing military staff tetap lima role, tidak otomatis diisi/diubah saat accession. |
| Military branch 4514, service/Dragon cards 4531/4540 | Emperor tetap mempunyai actual musters/field position, risks dan staff sah. Jangan memakai crown untuk mengarang Grand General military grade atau menyembunyikan seluruh unit ledger ketika new Emperor field routes dipasang. |
| Dragon `d82Royal`, `d82Eligible`, `d82Appoint`, `d82Release` 9573–9599 | Legacy royal awards tetap diarsipkan. New route memerlukan lawful Shu imperial authority + personal consent/merit/history/availability/command; kandidat lama adalah contoh legacy, bukan lima nama locked. `d82Ensure` memutasi state: jangan memanggilnya sebagai pure eligibility reader baru. |
| Legacy naming `auh83*` 9706/9746/9750 dan household/wartime `w83*` 9933/9953/9958 | Region/imperial names dan family succession harus mengikuti exact scope; tidak memaksa pasangan/anak, rename dynasty atau consent. |
| `auh79NorthEarned`/West/East/Regions 9160–9189; congress/imperial oath 9268–9290 | Biarkan proof dunia terpisah. Wu belum selesai hanya karena Wei/Western accord atau Shu accession. Jangan remap seluruh function menjadi broad imperial flag. |
| Endings E01/sovereign/retirement/i84 9134–9150/9318/9983–10138 | Pertahankan delapan families dan valid legacy state. New Shu Emperor tanpa unity dapat mendapat distinct ending prose, tidak menerima historical union text/first national council otomatis. |
| M3 scope wrappers 16466/16480/16787/17160/17192/17318/17348/17356/17623 dan M4 petition 17640/17642/17748 | New accession nanti harus menghentikan scoped pre-imperial career claims tanpa menghapus historical commissions. Pure historical M3 proof tetap valid setelah court/authority berubah. |

## Urutan aman setelah keputusan dinasti

1. Implementasikan legal producer dalam actual scenes dan source/history; final mandate acceptance, oath/public accession serta scope Shu disimpan sekali. Refusal/defer/retained incumbent dan unavailable proof tidak membuat crown. Jangan membuat unused predicate/schema lalu mengklaim playable accession.
2. Tambahkan distinct pure reader untuk witnessed lawful **Shu imperial office**, dan distinct current/retired status. Legacy `auh79Emperor` tetap legacy union proof. New settlement proof harus membedakan Wei/Wu/Shu dan tidak didapat dari legacy flags saja.
3. Adaptasi authority-facing Character/Civic/Military/People/known appointments bersamaan dengan scenes. Tangani wrappers/closures per source; global string substitution tidak cukup dan dapat memberi fake unified ending.
4. Baru integrasikan personal Dragon ceremonies dan future campaigns/ending. 0–5 seats, Commander still goes to field, independent NPC decisions, actual command handover dan court absence tetap kontrak.
5. Targeted QA: Shu Emperor tanpa union/Dragons, lower military grade, zero-force/handover, Governor legacy, old legitimate royal/unified saves, late/flags-only/unmet and consent-refusal, first policy callback, duty/custody integrity serta exact eight ending families. Browser/export/import/read-only proof, bukan documentation-only.

Penundaan pemilihan hukum terbatas pada keputusan dinasti yang masih terbuka di core decisions dan AGENTS. Roadmap frontline/legendary recognition/ceremony quality sudah disetujui dan tidak ditanya ulang. Usulan konkret: `docs/M4_DYNASTIC_MECHANISM_PROPOSAL.md` (belum menjadi canon).
