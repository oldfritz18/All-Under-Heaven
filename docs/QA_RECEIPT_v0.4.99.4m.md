# All Under Heaven — QA Receipt v0.4.99.4m

**Input:** v0.4.99.4l · **Output:** v0.4.99.4m  
**Scope:** the five edited historical-coalition scenes, their existing decisions, and a new optional Chapter II recall.

| Test | Result |
|---|---|
| JavaScript syntax (`node --check`) | PASS |
| Registered scene IDs vs baseline | PASS — all **630** identical |
| Old choice labels, destinations, and effect functions | PASS — identical in a representative enrolled state |
| Embedded image byte hashes | PASS — **35** unchanged |
| Existing Special Staff role list | PASS — unchanged |
| Direct `choose()` branch walks in Chromium | PASS — **12 per viewport**, 24 runs at widths 390 and 1280 px |
| Eligible Chapter II memory callback | PASS — **9 per viewport**, 18 confirmations |
| Incorrect retrospective memories on legacy/flag-only states | PASS — suppressed |
| Historical direct encounter flags vs indirect/declined routes | PASS for Zhang Miao, Qiao Mao, Bao Xin, Liu Dai, Cao Cao |
| Private rank / chronological age / 190 calendar in modified Chapter I branches | PASS |
| Four chained playthroughs from council through Chapter II | PASS — **59, 59, 59, 57 choices**, all enter 191 CE at age 17 as Private |
| JSON state validation and serialization roundtrip | PASS within targeted tests |
| JS page errors / horizontal overflow at 390 and 1280 px | PASS |
| Full 630-scene gameplay regression | NOT RUN — outside targeted scope |
| Real-device `file://` local save persistence | NOT TESTED |

**Environment caution:** Chromium `page.set_content()` uses an opaque document origin in this QA; localStorage failures visible in a screenshot do not establish how the HTML behaves when opened on a real device. Actual on-device save/reload remains unverified.

**Source SHA-256:** `b99d515bd2c701e9c4fdf9592aa458f7d25242a6ee249fcd1894a3e8a044f441`  
**Build SHA-256:** `fa304c41f644a6ce5d75e567957c24d5c7731ec8d619fad7e10d63db7bd260fe`

No ZIP created per Fast Development agreement.
