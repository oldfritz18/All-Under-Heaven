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
