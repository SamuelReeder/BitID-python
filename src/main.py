from server import Server
from chain import Chain
from block import Block 
from http.server import BaseHTTPRequestHandler, HTTPServer

def main():
    print('Hello World!')

    
    # create server to broadcast to clients
    hostName = "localhost"
    serverPort = 8080

    webServer = HTTPServer((hostName, serverPort), Server)
    print("Server started http://%s:%s" % (hostName, serverPort))

    
    # create blockchain
    blockchain = Chain("testnet chain", "http://localhost:8080/")
    second_block = Block(blockchain.blocks[-1].hash)
    # second_block.catch_transactions()
    second_block.add_transaction("test")
    second_block.compute_hash()
    blockchain.broadcast_block(second_block)
    blockchain.add_block(second_block)
    
    s = ""
    for i in blockchain.blocks: 
        s += str(i.hash) + " "
    
    print("<p>Chain: %s</p>" % s, "utf-8")
    # TODO: catch for amount of time before signing and starting new block 
    
    
    

    # run server
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
    


if __name__ == '__main__':
    main()