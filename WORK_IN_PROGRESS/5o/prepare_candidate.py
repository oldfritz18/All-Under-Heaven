#!/usr/bin/env python3
"""Reconstruct the preserved draft without promoting or replacing the active game."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
metadata = json.loads((HERE / 'DRAFT_MANIFEST.json').read_text())
baseline = (ROOT / metadata['base_html']).read_bytes()
assert hashlib.sha256(baseline).hexdigest() == metadata['base_sha256'], 'Use the exact verified 5n source'
source = baseline.decode().replace('v0.4.99.5n', 'v0.4.99.5o').replace('The Standard He Chose', 'The Unfinished Map')
anchor = 'const storageAvailableAtBoot=storageProbe();'
assert source.count(anchor) == 1
source = source.replace(anchor, (HERE / 'xu_review_5o.js').read_text() + '\n' + anchor, 1)
candidate = source.encode()
assert hashlib.sha256(candidate).hexdigest() == metadata['candidate_sha256'], 'Draft reconstruction differs'
assert len(candidate) == metadata['candidate_bytes']
destination = HERE / metadata['candidate']
if destination.exists():
    assert destination.read_bytes() == candidate, 'Existing candidate differs; keep it for review'
else:
    destination.write_bytes(candidate)
print(destination)
print('UNVERIFIED DRAFT. GAME/ACTIVE_BUILD.txt was not changed.')
