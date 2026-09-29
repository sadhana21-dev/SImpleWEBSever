from http.server import HTTPServer, SimpleHTTPRequestHandler

HOST = "127.0.0.1"
PORT = 8000


class CustomRequestHandler(SimpleHTTPRequestHandler):
    pass


server = HTTPServer((HOST, PORT), CustomRequestHandler)

print("Simple Web Server Started")
print(f"Server running at http://{HOST}:{PORT}")
print("Press Ctrl+C to stop the server.")

server.serve_forever()