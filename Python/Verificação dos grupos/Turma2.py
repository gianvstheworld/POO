from Turmas import *

class Turma2(Turmas):
    def __init__(self, nome, nusp):
        super().__init__(nome, nusp)
        
    def __str__(self):
        return('TURMA 2\nNome: {}\nNúmero USP: {}'.format(self.nome, self.nusp))

