#!/usr/bin/python3
import http.server


class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Set the required headers to enable SharedArrayBuffer
        self.send_header("Cross-Origin-Opener-Policy", "same-origin")
        self.send_header("Cross-Origin-Embedder-Policy", "require-corp")
        super().end_headers()


if __name__ == "__main__":
    PORT = 2828  # Set your port number
    server_address = ("", PORT)
    httpd = http.server.HTTPServer(server_address, CustomHTTPRequestHandler)

    print(f"Serving on port {PORT}")
    httpd.serve_forever()
