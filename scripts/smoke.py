#!/usr/bin/env python3
"""Static integrity smoke checks. This is not interactive gameplay/browser QA."""
from pathlib import Path
import re,sys
R=Path(__file__).resolve().parent.parent
active=(R/'GAME'/'ACTIVE_BUILD.txt').read_text('utf-8').strip()
if not active or '/' in active or '..' in active: raise SystemExit('Invalid active filename')
p=R/'GAME'/active
if not p.is_file(): raise SystemExit(f'Missing active HTML: {p}')
s=p.read_text('utf-8')
checks={
 'HTML root': '<html' in s and '</html>' in s,
 'scene registry': 'const SCENES={}' in s and 'function scene(' in s,
 'choice handler': 'function choose(index)' in s,
 'save/load hooks': 'localStorage' in s and 'JSON' in s,
 'five staff role IDs': all(f"['{k}'" in s for k in ['assistant','strategist','quartermaster','deputy','intelligence']),
 'Hulao and Pan River story': 'Hulao' in s and 'Pan River' in s,
 'large existing scene base': len(re.findall(r"\bscene\(['\"]",s)) >= 400,
 'English game UI': '<html lang="en">' in s,
}
for k,v in checks.items(): print(('PASS' if v else 'FAIL'), k)
print('ACTIVE:',p.name,'BYTES:',p.stat().st_size)
if not all(checks.values()): sys.exit(1)
