
class Transaction:
    
    def __init__(self, sender, modifications, fee):
        self.sender = sender
        self.modifications = modifications
        self.fee = fee
        self.validate()
        
        
    def validate(self):
        prev = self.get_prev(self.sender)
        if prev is None:
            self.validate_new()
        else:
            self.validate_update(prev)
            
    def validate_new(self):
        

    def __str__(self):
        return f"Sender: {self.sender}\nModification: {self.modifications}\nFee: {self.fee}\n"

    def __repr__(self):
        return f"Sender: {self.sender}\nModifications: {self.modifications}\nFee: {self.fee}\n"

    # def __eq__(self, other):
    #     return self.sender == other.sender and self.receiver == other.receiver and self.amount == other.amount and self.fee == other.fee

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.sender, self.modifications, self.fee))