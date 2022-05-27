import http.server
import socketserver
import os


PORT = 33330
os.chdir('static')
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("servido iniciado", PORT)
    httpd.serve_forever()
