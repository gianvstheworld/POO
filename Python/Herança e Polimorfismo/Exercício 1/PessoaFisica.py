from Pessoa import *

class PessoaFisica(Pessoa):
    def __init__(self, name: str, cpf: int, address: str, bdate: str, email: str, cstate: str):
        super().__init__(name, address, email)
        self.cpf = cpf
        self.bdate = bdate
        self.cstate = cstate

    def __str__(self):
        return("\nNome: {}\nEndereço: {}\nE-mail: {}\nData de nascimento: {}\nEstado Civil: {}\nCPF: {}".format(self.name, self.address, self.email, self.bdate, self.cstate, self.cpf))

    def getCPF(self):
        return self.cpf
    def getBDate(self):
        return self.bdate
    def getCState(self):
        return self.cstate

    def setCPF(self, cpf):
        self.cpf = cpf
    def setBDate(self, bdate):
        self.bdate = bdate
    def setCState(self, cstate):
        self.cstate = cstate



