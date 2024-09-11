import http.server
import socketserver

PORT = 23  # Privileged port

Handler = http.server.SimpleHTTPRequestHandler

try:
    # Try to bind to the port without serving
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Successfully bound to port {PORT}")
except PermissionError as e:
    print(f"Failed to bind to port {PORT}: {e}")
