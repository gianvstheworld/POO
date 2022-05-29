from Estoque import *

class CD(Estoque):
    def __init__(self, name, code_bar, n):
        super().__init__(name, code_bar, n)

    def __str__(self):
        s = '\nTipo: CD\n'
        s += "name: " + str(self.getName()) + "\n"
        s += "Código de Barras: " + str(self.getCodeBar()) + "\n"
        s += "Quantia em Estoque: " + str(self.getN()) + "\n"
        return s