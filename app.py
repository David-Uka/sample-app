import http.server
import json
import os
import socketserver

PORT = 8080
ENVIRONMENT = os.environ.get("ENVIRONMENT", "unknown")


class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/healthz":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"ok")
            return
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        body = json.dumps({"message": "hello from sample-app", "environment": ENVIRONMENT})
        self.wfile.write(body.encode())

    def log_message(self, fmt, *args):
        pass


if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"serving on :{PORT} (env={ENVIRONMENT})")
        httpd.serve_forever()
