"""Run the bio.tools metadata form on localhost."""

import argparse
import json
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit

from validate import SCHEMA_PATH, make_validators


FORM_DIR = Path(__file__).with_name("form")
ASSETS = {
    "/": ("index.html", "text/html; charset=utf-8"),
    "/form.js": ("form.js", "text/javascript; charset=utf-8"),
    "/style.css": ("style.css", "text/css; charset=utf-8"),
}
JSON_TYPE = "application/json; charset=utf-8"


class FormServer(ThreadingHTTPServer):
    def __init__(self, address):
        self.schema_bytes = SCHEMA_PATH.read_bytes()
        _, self.tool_validator = make_validators(json.loads(self.schema_bytes))
        super().__init__(address, FormHandler)


class FormHandler(BaseHTTPRequestHandler):
    def respond(self, content, content_type):
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)

    def do_GET(self):
        path = urlsplit(self.path).path
        if path == "/biotoolsj.json":
            self.respond(self.server.schema_bytes, JSON_TYPE)
        elif path in ASSETS:
            filename, content_type = ASSETS[path]
            self.respond((FORM_DIR / filename).read_bytes(), content_type)
        else:
            self.send_error(HTTPStatus.NOT_FOUND)

    def do_POST(self):
        if self.path != "/validate":
            self.send_error(HTTPStatus.NOT_FOUND)
            return
        if self.headers.get_content_type() != "application/json":
            self.send_error(HTTPStatus.UNSUPPORTED_MEDIA_TYPE)
            return
        try:
            length = int(self.headers.get("Content-Length", ""))
        except ValueError:
            self.send_error(HTTPStatus.LENGTH_REQUIRED)
            return
        if not 0 < length <= 8 * 1024 * 1024:
            self.send_error(HTTPStatus.REQUEST_ENTITY_TOO_LARGE)
            return
        try:
            data = json.loads(self.rfile.read(length))
        except (ValueError, RecursionError):
            self.send_error(HTTPStatus.BAD_REQUEST, "Expected JSON")
            return
        errors = [
            {"path": error.json_path, "message": error.message}
            for error in self.server.tool_validator.iter_errors(data)
        ]
        self.respond(json.dumps(errors).encode("utf-8"), JSON_TYPE)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, default=8000, help="local port (default: 8000)")
    args = parser.parse_args()
    with FormServer(("127.0.0.1", args.port)) as server:
        print(f"Open http://127.0.0.1:{server.server_port}/", flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass


if __name__ == "__main__":
    main()
