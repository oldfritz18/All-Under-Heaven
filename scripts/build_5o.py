#!/usr/bin/env python3
"""Integrate the Xu Wen 230-231 service batch into the existing 5n offline HTML.

No engine rebuild, character reset, portrait import, rank award or migration.
This script deliberately refuses to replace a different active baseline.
"""
from __future__ import annotations
from hashlib import sha256
from pathlib import Path
import json
import re
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parent.parent
GAME = ROOT / "GAME"
OLD = "ALL_UNDER_HEAVEN_v0.4.99.5n_THE_STANDARD_HE_CHOSE.html"
NEW = "ALL_UNDER_HEAVEN_v0.4.99.5o_THE_MEASURED_ROAD.html"
EXT = GAME / "EXTENSIONS" / "M4_XU_WEN_SERVICE_v0.4.99.5o.js"
EXPECTED_SHA = "15e85e566f259e9e253536f83710c00be4729ae7e69474c54451cb9e1eb9050d"
ANCHOR = "\nconst storageAvailableAtBoot=storageProbe();"
TITLE_OLD = "<title>All Under Heaven — v0.4.99.5n The Standard He Chose</title>"
TITLE_NEW = "<title>All Under Heaven — v0.4.99.5o The Measured Road</title>"
META_OLD = '<meta name="auh-build" content="v0.4.99.5n">'
META_NEW = '<meta name="auh-build" content="v0.4.99.5o">'
NEW_IDS = [
    "m4_230_xu_hearing", "m4_230_xu_terms", "m4_230_xu_order",
    "m4_230_xu_muster", "m4_231_xu_road", "m4_231_xu_contact",
    "m4_231_xu_return", "m4_231_xu_review", "m4_231_xu_close",
]

active_path = GAME / "ACTIVE_BUILD.txt"
active = active_path.read_text("utf-8").strip()
if active not in (OLD, NEW):
    raise SystemExit("Active build changed; rebase and audit rather than overwriting " + active)
source_bytes = (GAME / OLD).read_bytes()
if sha256(source_bytes).hexdigest() != EXPECTED_SHA:
    raise SystemExit("5n baseline bytes differ from verified checkpoint")
source = source_bytes.decode("utf-8")
addition = EXT.read_text("utf-8")
assert source.count(ANCHOR) == 1, "pre-boot injection anchor not unique"
assert source.count(TITLE_OLD) == source.count(META_OLD) == 1
assert "/* v0.4.99.5o" not in source
assert addition.count("/* v0.4.99.5o") == 1
for marker in ("auh5oParent", "auh5oMuster", "auh5oClose", "auh5oReviewProof"):
    assert marker in addition, marker

updated = source.replace(ANCHOR, "\n" + addition + "\n" + ANCHOR)
updated = updated.replace(TITLE_OLD, TITLE_NEW).replace(META_OLD, META_NEW)
before = set(re.findall(r"\bscene\('([^']+)'", source))
after = set(re.findall(r"\bscene\('([^']+)'", updated))
assert before <= after and after - before == set(NEW_IDS), "scene IDs changed unexpectedly"
assert updated.count("data:image/") == source.count("data:image/") == 35
assert updated.replace("\n" + addition + "\n" + ANCHOR, ANCHOR).replace(TITLE_NEW, TITLE_OLD).replace(META_NEW, META_OLD) == source
assert "dragonGenerals.active.push" not in addition, "reconnaissance must not appoint Dragon"
assert "Grand General" not in addition or "NOT a General" in addition
assert updated.count('const storageAvailableAtBoot=storageProbe();') == 1
target = GAME / NEW
target.write_text(updated, encoding="utf-8")
active_path.write_text(NEW + "\n", encoding="utf-8")

with tempfile.TemporaryDirectory() as td:
    js_path = Path(td) / "game.js"
    scripts = re.findall(r"<script[^>]*>(.*?)</script>", updated, flags=re.S)
    assert len(scripts) >= 2
    js_path.write_text("\n".join(scripts), encoding="utf-8")
    subprocess.run(["node", "--check", str(js_path)], check=True)

receipt = {
    "status": "STATIC_AND_JS_PARSE_PASS__BROWSER_GAMEPLAY_NOT_YET_CERTIFIED",
    "baseline": OLD,
    "baseline_sha256": EXPECTED_SHA,
    "active": NEW,
    "active_sha256": sha256(target.read_bytes()).hexdigest(),
    "registered_scene_ids_added": NEW_IDS,
    "previous_literal_scene_ids_preserved": len(before),
    "portrait_data_uris_unchanged": 35,
    "save_engine_and_baseline_source": "byte-identical outside addition + title + version metadata",
    "new_rank_or_dragon_award": False,
    "known_limits": [
        "No Chromium playthrough or full interactive branch matrix executed by this build script",
        "No physical Android file:// persistence test",
        "New service is not yet an accepted General or Dragon appointment",
    ],
}
output = ROOT / "docs" / "qa" / "BATCH_5o_SOURCE.json"
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(json.dumps(receipt, indent=2, ensure_ascii=False))
