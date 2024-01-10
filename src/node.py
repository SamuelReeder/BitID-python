from server import Server
from http.server import HTTPServer

class Node(Server):
    
    def __init__(self, port):
        self.port = port
        self.server = HTTPServer(("localhost", port), Server)
        # self.registry = Registry()
        # self.blockchain = Blockchain()
        self.cache = []
        self.threads = []
        # self.start()
        
    
    def serve_forever(self):
        try:
            self.server.serve_forever()
        except KeyboardInterrupt:
            self.server.server_close()
    
    