# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import json


class Server(BaseHTTPRequestHandler):
    
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data.decode('utf-8'))

        # Handle block reception here
        if self.path == '/new_block':
            self.handle_new_block(data['block'])

        self.send_response(200)
        self.end_headers()
        
        
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))    
        
    
    def handle_new_block(self, block):
        print("Received new block:", block)
        return True