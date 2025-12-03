from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import json

from . import keva_mem as store


class KevaHandler(BaseHTTPRequestHandler):
    """Very small HTTP API over the in-memory keva store.

    Endpoints (all return JSON):
      - GET /get?key=foo          -> {"key": "foo", "value": "..."}
      - POST /set?key=foo&value=bar
      - POST /delete?key=foo
      - POST /reset
    """

    def _send_json(self, status: int, payload: dict) -> None:
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:
        parsed = urlparse(self.path)
        if parsed.path != "/get":
            self._send_json(404, {"error": "not_found"})
            return

        params = parse_qs(parsed.query)
        key = params.get("key", [""])[0]
        if not key:
            self._send_json(400, {"error": "missing_key"})
            return

        value = store.get(key)
        self._send_json(200, {"key": key, "value": value})

    def do_POST(self) -> None:
        parsed = urlparse(self.path)
        params = parse_qs(parsed.query)

        if parsed.path == "/set":
            key = params.get("key", [""])[0]
            value = params.get("value", [""])[0]
            if not key:
                self._send_json(400, {"error": "missing_key"})
                return
            store.set(key, value)
            self._send_json(200, {"status": "ok", "key": key, "value": value})
        elif parsed.path == "/delete":
            key = params.get("key", [""])[0]
            if not key:
                self._send_json(400, {"error": "missing_key"})
                return
            store.delete(key)
            self._send_json(200, {"status": "ok", "key": key})
        elif parsed.path == "/reset":
            store.reset()
            self._send_json(200, {"status": "ok"})
        else:
            self._send_json(404, {"error": "not_found"})


def run_server(host: str = "", port: int = 8000) -> None:
    """Run HTTP server exposing keva_mem backend."""
    server_address = (host, port)
    httpd = HTTPServer(server_address, KevaHandler)
    print(f"Starting keva HTTP server on {host or '0.0.0.0'}:{port}")
    httpd.serve_forever()


if __name__ == "__main__":
    run_server()
