"""Local preview server that applies the redirects and rewrites from vercel.json.

Usage:  python scripts/dev_server.py [port]      (default port 3000)
"""
import json
import sys
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "vercel.json"


def load_rules():
    config = json.loads(CONFIG.read_text(encoding="utf-8"))
    redirects = {r["source"]: r["destination"] for r in config.get("redirects", [])}
    rewrites = {r["source"]: r["destination"] for r in config.get("rewrites", [])}
    return redirects, rewrites


class Handler(SimpleHTTPRequestHandler):
    def _route(self):
        redirects, rewrites = load_rules()
        parts = urlsplit(self.path)
        path = parts.path

        if path in redirects:
            location = redirects[path] + (f"?{parts.query}" if parts.query else "")
            self.send_response(308)
            self.send_header("Location", location)
            self.end_headers()
            return False

        target = ROOT / path.lstrip("/")
        if path != "/" and not target.exists() and path in rewrites:
            self.path = rewrites[path] + (f"?{parts.query}" if parts.query else "")
        return True

    def do_GET(self):
        if self._route():
            super().do_GET()

    def do_HEAD(self):
        if self._route():
            super().do_HEAD()

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
    server = ThreadingHTTPServer(("127.0.0.1", port), partial(Handler, directory=str(ROOT)))
    print(f"Serving {ROOT} at http://localhost:{port}/")
    server.serve_forever()
