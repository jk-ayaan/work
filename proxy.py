#!/usr/bin/env python3
"""
CORS Proxy Server - CEO+ Help
간단한 CORS 프록시 서버입니다. 별도 패키지 설치 없이 Python 3 기본 라이브러리만 사용합니다.

실행:
    python proxy.py
    python proxy.py --port 9999

기본 포트: 8888
"""

import http.server
import urllib.request
import urllib.parse
import urllib.error
import json
import sys
import ssl

PORT = 8888


class CORSProxyHandler(http.server.BaseHTTPRequestHandler):
    """Forward requests to target URLs with CORS headers added."""

    def _send_cors_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, PATCH, DELETE, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
        self.send_header('Access-Control-Expose-Headers', '*')
        self.send_header('Access-Control-Max-Age', '86400')

    def do_OPTIONS(self):
        self.send_response(200)
        self._send_cors_headers()
        self.end_headers()

    def do_GET(self):
        self._proxy_request('GET')

    def do_POST(self):
        self._proxy_request('POST')

    def do_PUT(self):
        self._proxy_request('PUT')

    def do_PATCH(self):
        self._proxy_request('PATCH')

    def do_DELETE(self):
        self._proxy_request('DELETE')

    def _proxy_request(self, method):
        # /health endpoint
        if self.path == '/health':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self._send_cors_headers()
            self.end_headers()
            response = json.dumps({'status': 'ok', 'port': PORT})
            self.wfile.write(response.encode('utf-8'))
            return

        # Parse the target URL from the path
        target_url = self.path.lstrip('/')
        if not target_url:
            self.send_response(400)
            self.send_header('Content-Type', 'application/json')
            self._send_cors_headers()
            self.end_headers()
            self.wfile.write(json.dumps({'error': 'No target URL provided. Usage: http://localhost:{}/https%3A%2F%2Fexample.com%2Fapi'.format(PORT)}).encode('utf-8'))
            return

        # URL decode the target
        target_url = urllib.parse.unquote(target_url)

        # Ensure the URL has a scheme
        if not target_url.startswith('http://') and not target_url.startswith('https://'):
            target_url = 'https://' + target_url

        # Read request body if present
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length) if content_length > 0 else None

        # Build the proxied request
        try:
            req = urllib.request.Request(target_url, data=body, method=method)

            # Forward relevant headers
            skip_headers = {'host', 'connection', 'accept-encoding', 'content-length', 'transfer-encoding'}
            for header, value in self.headers.items():
                if header.lower() not in skip_headers:
                    req.add_header(header, value)

            # Disable SSL verification for internal APIs
            ctx = ssl.create_default_context()
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE

            with urllib.request.urlopen(req, context=ctx, timeout=30) as response:
                response_body = response.read()
                self.send_response(response.status)
                # Forward response headers
                for header, value in response.getheaders():
                    if header.lower() not in ('transfer-encoding', 'content-encoding', 'content-length',
                                               'access-control-allow-origin', 'access-control-allow-methods',
                                               'access-control-allow-headers'):
                        self.send_header(header, value)
                self.send_header('Content-Length', str(len(response_body)))
                self._send_cors_headers()
                self.end_headers()
                self.wfile.write(response_body)

        except urllib.error.HTTPError as e:
            error_body = e.read()
            self.send_response(e.code)
            self.send_header('Content-Type', 'application/json')
            self._send_cors_headers()
            self.end_headers()
            try:
                self.wfile.write(error_body)
            except Exception:
                self.wfile.write(json.dumps({'error': str(e), 'status': e.code}).encode('utf-8'))

        except Exception as e:
            self.send_response(502)
            self.send_header('Content-Type', 'application/json')
            self._send_cors_headers()
            self.end_headers()
            self.wfile.write(json.dumps({'error': str(e), 'target': target_url}).encode('utf-8'))

    def log_message(self, format, *args):
        """Custom log format with color."""
        method = args[0].split(' ')[0] if args else ''
        status = args[1] if len(args) > 1 else ''
        path = args[0].split(' ')[1] if args and len(args[0].split(' ')) > 1 else ''

        # Decode URL for readability
        decoded_path = urllib.parse.unquote(path) if path else ''
        if len(decoded_path) > 80:
            decoded_path = decoded_path[:77] + '...'

        print(f"  [{self.log_date_time_string()}] {method} {status} → {decoded_path}")


def main():
    global PORT
    # Parse --port argument
    if '--port' in sys.argv:
        idx = sys.argv.index('--port')
        if idx + 1 < len(sys.argv):
            PORT = int(sys.argv[idx + 1])

    server = http.server.HTTPServer(('0.0.0.0', PORT), CORSProxyHandler)

    print()
    print("  ┌─────────────────────────────────────────┐")
    print(f"  │  CORS Proxy Server (CEO+ Help)          │")
    print(f"  │  http://localhost:{PORT}/                  │")
    print("  │                                         │")
    print("  │  Usage:                                 │")
    print(f"  │  http://localhost:{PORT}/<encoded_url>      │")
    print("  │                                         │")
    print("  │  Health: /health                        │")
    print("  │  Press Ctrl+C to stop                   │")
    print("  └─────────────────────────────────────────┘")
    print()

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n  Server stopped.")
        server.server_close()


if __name__ == '__main__':
    main()
