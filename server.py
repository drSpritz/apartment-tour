import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("192.168.0.103", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()