from block import Block

class Chain:
    
    def __init__(self, name, host, permissioned = False, public = True):
        self.name = name
        self.host = host
        self.permisioned = permissioned
        self.public = public
        self.blocks = []
        self.unconfirmed_transactions = []
        self.key = 0
        self.genesis_block()
        
    
    def genesis_block(self):
        genesis_block = Block("0")
        genesis_block.compute_hash()
        self.blocks.append(genesis_block)
        
    def add_block(self, block):
        prev_hash = self.blocks[-1].hash
        if prev_hash != block.prev_hash:
            return False
        
        if not block.is_valid():
            return False
        
        block.compute_hash()
        self.blocks.append(block)
        return True
    
    def broadcast_block(self, block):
        pass
    
    def get_key(self):
        return self.key
    