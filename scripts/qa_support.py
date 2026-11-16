"""Shared local Chromium fixture for targeted narrative QA; no external hosting."""
from contextlib import contextmanager
import hashlib
import http.server
import json
import re
import shutil
import subprocess
import tempfile
import threading
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def normalize_chapter_headers(value):
    """Ignore only display chapter H2s in legacy prose parity comparisons.

    Heading placement and numbering have their own qa_chapter_map assertions.
    Scene IDs, labels, destinations and all state/effects still compare exactly.
    """
    if isinstance(value, list):
        return [normalize_chapter_headers(item) for item in value]
    if isinstance(value, dict):
        return {key: (re.sub(r'<h2 class="chapter-title-inline">Chapter [IVX]+</h2>\s*', '', item).strip()
                      if key == 'body' and isinstance(item, str) else normalize_chapter_headers(item))
                for key, item in value.items()}
    return value


@contextmanager
def fixture(baseline_ref):
    from playwright.sync_api import sync_playwright
    active = ROOT / 'GAME' / (ROOT / 'GAME/ACTIVE_BUILD.txt').read_text().strip()
    current = active.read_bytes()
    baseline = subprocess.run(['git', 'show', baseline_ref], cwd=ROOT, check=True, capture_output=True).stdout
    images = lambda content: re.findall(rb'data:image/[^;"\s]+;base64,[A-Za-z0-9+/=]+', content)
    assert images(current) == images(baseline), 'Embedded image changed'
    with tempfile.TemporaryDirectory() as temporary:
        script = Path(temporary) / 'game.js'
        script.write_bytes(b'\n'.join(re.findall(rb'<script[^>]*>(.*?)</script>', current, re.S)))
        subprocess.run(['node', '--check', str(script)], check=True, capture_output=True)
    documents = {'/baseline.html': baseline, '/active.html': current}

    class Handler(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            content = documents.get(self.path)
            self.send_response(200 if content else 404)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers()
            if content:
                self.wfile.write(content)

        def log_message(self, *_):
            pass

    server = http.server.ThreadingHTTPServer(('127.0.0.1', 0), Handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    try:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(executable_path=shutil.which('chromium'), headless=True, args=['--no-sandbox'])
            try:
                yield browser, f'http://127.0.0.1:{server.server_port}', {
                    'build': active.name,
                    'sha256': hashlib.sha256(current).hexdigest(),
                    'portrait_data_uris': len(images(current)),
                    'checks': [],
                }
            finally:
                browser.close()
    finally:
        server.shutdown()
        server.server_close()


def write_report(result, destination=None):
    if destination:
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))

# Exact registered IDs added by the optional 218–219 M3-B arc.
HANZHONG_219_SCENES = frozenset({
    'm3_218_hanzhong_request', 'm3_218_hanzhong_road',
    'm3_219_hanzhong_council', 'm3_219_hanzhong_orders',
    'm3_219_hanzhong_clash', 'm3_219_hanzhong_return',
    'm3_219_hanzhong_warrant', 'm3_219_hanzhong_hearing',
    'm3_219_tiger_council', 'm3_219_tiger_standard',
    'm3_219_tiger_first_orders', 'm3_219_tiger_aftermath',
    'm3_219_west_homeward',
})

# Exact registered IDs of the optional M4-A 224–225 court petition.
COURT_224_SCENES = frozenset({
    'm4_224_petition', 'm4_224_dispatch', 'm4_224_road',
    'm4_224_chancery', 'm4_224_audience', 'm4_225_return',
})

# Exact IDs for the witnessed conditional royal review of 221.
DESIGNATION_221_SCENES = frozenset({
    'm4_221_summons', 'm4_221_road', 'm4_221_private',
    'm4_221_household', 'm4_221_designation', 'm4_221_return',
})
