from hashlib import sha256
import random

class Block:
    
    def __init__(self, prev_hash):
        self.prev_hash = prev_hash
        self.transactions = []
        self.nonce = 0
        self.hash = None
        
    def add_transaction(self, transaction):
        self.transactions.append(transaction)
        
    def get_transactions(self):
        return self.transactions
    
    def get_prev_hash(self):
        return self.prev_hash

    def compute_hash(self):
        # self.hash = sha256(str(self.prev_hash + str(self.transactions) + str(self.nonce)).encode()).hexdigest()
        self.hash = random.randint(0, 100)
    
    def catch_transactions(self):
        pass 