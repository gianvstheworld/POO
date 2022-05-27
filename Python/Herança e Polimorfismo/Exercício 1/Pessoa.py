class Pessoa():
    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email
        
    def getName(self):
        return self.name
    def getAddress(self):
        return self.address
    def getEmail(self):
        return self.email
    
    def setName(self, name):
        self.name = name
    def setAddress(self, address):
        self.address = address
    def setEmail(self, email):
        self.email = email

