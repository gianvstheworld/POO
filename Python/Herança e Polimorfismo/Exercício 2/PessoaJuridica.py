from Pessoa import *

class PessoaJuridica(Pessoa):
    def __init__(self, name: str, cnpj: int, address: str, substate: str, email: str, socialr: str):
        super().__init__(name, address, email)
        self.cnpj = cnpj
        self.substate = substate
        self.socialr = socialr
        
    def getCNPJ(self):
        return self.cnpj
    def getSubState(self):
        return self.substate
    def getSocialr(self):
        return self.socialr
    
    def setCNPJ(self, cnpj):
        self.cnpj = cnpj
    def setSubState(self, substate):
        self.substate = substate
    def setSocialr(self, socialr):
        self.socialr = socialr

