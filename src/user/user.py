import hashlib 

class User:

    def __init__(self, pending_user):
        self.user = pending_user
        
    def update(self, updates):
        self.user = updates
    
    
def compute_unique_id(user):
    # take each unique piece of info in the user object and add it to the hash
    data = "EXAMPLE"

    encoded_data = data.encode()
    hash_object = hashlib.sha256()
    hash_object.update(encoded_data)
    unique_id = hash_object.hexdigest()

    print("Unique ID:", unique_id)