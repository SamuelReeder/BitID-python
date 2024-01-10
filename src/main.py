from http.server import HTTPServer
import threading
import time as t 
import json
import requests
from node import Node
from server import Server
from chain import Chain
from block import Block
from registry import Registry


def main():

    # create server to broadcast to clients
    port = 8080

    web_server = HTTPServer(("localhost", port), Server)
    try:
        web_server.serve_forever()
    except KeyboardInterrupt:
        web_server.server_close()
    # create blockchain
    

    blockchain = Chain("testnet chain", "http://localhost:8080/")

    # add nodes to the registry as the join the network, registry sent to each server
    # take unique id as key and weight as value for now
    # registry kept separate, node can fetch and get random upon requesting validation
    nodes, registry = dummy_nodes([8081, 8082, 8083])
    threads = start_threads(nodes)
    
    
    

    # need to always catch new transactions 
    # every x seconds, queue up transactions and create a new block
    # existing transactions are cleared from the queue and put in block
    # remaining is queued up again
    
    # begin creation of a new block
    
    cache = []
    transaction_thread = threading.Thread(target= lambda: dummy_transactions(cache, 10))
    try:
        transaction_thread.start()
    except KeyboardInterrupt:
        pass
    
    def create_new_block(c):
        print("Creating a new block...")
        block = Block(blockchain.blocks[-1].hash)

        cache_len = block.add_transactions(c)
        block.compute_hash()
        
        block_data = json.dumps(block.__dict__, sort_keys=True)
        print("Block data:", block_data)
        
        registry_dict = registry.get_registry()
        peers = registry_dict.keys()
        approval = 0
        for peer in peers:
            response = requests.post("http://localhost:" + str(peer) + '/new_block', json={'block': block_data})
            if response.status_code == 200:
                approval += 1
        if approval > len(peers) / 2:
            blockchain.add_block(block)
            
        print(blockchain.blocks[-1].hash + "\n")
            
        c = c[cache_len:]
        
        
    def timer_loop(c):
        while True:
            create_new_block(c)
            t.sleep(5)

    # Create and start the timer thread
    timer_thread = threading.Thread(target=lambda : timer_loop(cache))
    try:
        timer_thread.start()
    except KeyboardInterrupt:
        pass


def dummy_nodes(ports):

    # each has equal weight for now
    nodes = []
    registry = Registry()
    for port, i  in enumerate(ports):
        nodes.append(Node(port))
        registry.register(port, 1)
    return nodes, registry


def start_node(node):
    try:
        node.serve_forever()
    except KeyboardInterrupt:
        node.server_close()


def start_threads(nodes):

    # Creating and starting a thread for each node

    threads = []

    for node in nodes:
        thread = threading.Thread(target=start_node, args=(node,))
        thread.start()
        threads.append(thread)

    return threads

def dummy_transactions(cache, amt):
    while True:
        cache.append("test")
        t.sleep(1)


if __name__ == '__main__':

    main()


# basically:

#  - create server

#    - hosted locally

#    - different port for each node

#    - registry of ports and nodes

#  - create blockchain

#  - nodes join


#  - node creates block

#  - node broadcasts block

#  - other nodes validate block

#  - other nodes add block

#  - repeat
