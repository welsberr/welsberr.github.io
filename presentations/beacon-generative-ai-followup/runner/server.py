#!/usr/bin/env python3
"""Local presentation server; exposes one fixed, read-only test action."""
import datetime, hashlib, hmac, json, os, secrets, subprocess, threading
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEST = ROOT / 'preview/population-genetics.test.js'
PREVIEW_API = ROOT / 'preview/population-genetics.js'
SOURCE_API = Path(os.environ.get('BEACON_SOURCE_API', Path.home() / 'dev/evo-edu.org/apps/api/population-genetics/population-genetics.js'))
TOKEN = secrets.token_urlsafe(32)
LOCK = threading.Lock()

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)
    def do_GET(self):
        if self.path == '/__demo/session':
            if self.headers.get('Host') != f'127.0.0.1:{self.server.server_port}':
                return self.json_response(403, {'message':'Forbidden'})
            return self.json_response(200, {'token': TOKEN})
        return super().do_GET()
    def json_response(self, code, obj):
        data = json.dumps(obj).encode()
        self.send_response(code); self.send_header('Content-Type','application/json'); self.send_header('Cache-Control','no-store'); self.send_header('X-Content-Type-Options','nosniff'); self.end_headers(); self.wfile.write(data)
    def do_POST(self):
        expected = f'http://127.0.0.1:{self.server.server_port}'
        if self.path != '/__demo/check' or self.headers.get('Origin') != expected or self.headers.get('Host') != f'127.0.0.1:{self.server.server_port}' or not hmac.compare_digest(self.headers.get('X-Demo-Token',''), TOKEN):
            return self.json_response(403, {'message':'Forbidden'})
        if not LOCK.acquire(blocking=False):
            return self.json_response(409, {'message':'A check is already running.'})
        try:
            timestamp = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds')
            try:
                proc = subprocess.run(['node','--test',str(TEST)],capture_output=True,text=True,timeout=20)
                if proc.returncode:
                    message = 'Bundled API tests failed. Inspect the server console.'
                    print(proc.stdout, proc.stderr, flush=True)
                elif not SOURCE_API.is_file():
                    message = 'Bundled API tests passed; independent source comparison unavailable on this machine.'
                elif hashlib.sha256(SOURCE_API.read_bytes()).digest() == hashlib.sha256(PREVIEW_API.read_bytes()).digest():
                    message = 'Bundled API tests passed; source and preview API hashes match.'
                else:
                    message = 'Bundled API tests passed, but source and preview API copies differ; review the mismatch.'
            except (OSError,subprocess.TimeoutExpired) as exc:
                message = 'The check could not complete. Use the recorded result.'
                print(type(exc).__name__, flush=True)
            record = {'action':'population-genetics-api-tests','mode':'live','time':timestamp,'message':message}
            state = Path.home() / '.local/state/beacon-followup'
            state.mkdir(parents=True, exist_ok=True, mode=0o700)
            with (state / 'check-runs.jsonl').open('a') as log:
                log.write(json.dumps(record) + '\n')
            return self.json_response(200, record)
        finally: LOCK.release()

if __name__ == '__main__':
    port = int(os.environ.get('BEACON_PORT', '8769'))
    server=ThreadingHTTPServer(('127.0.0.1',port), Handler)
    print(f'Presentation: http://127.0.0.1:{port}/',flush=True)
    server.serve_forever()
