class Turma():
    def __init__(self, nome, nusp):
        self.nome = nome
        self.nusp = nusp
        
    def getNome(self):
        return self.nome
    def getNusp(self):
        return self.nusp
        
    def setNome(self, nome):
        self.nome = nome
    def setNusp(self, nusp):
        self.nusp = nusp