class Estoque:
    def __init__(self, name, code_bar, n):
        self.name = name
        self.code_bar = code_bar
        self.n = n

    def getName(self):
        return self.name
    def getCodeBar(self):
        return self.code_bar
    def getN(self):
        return self.n

    def setName(self, name):
        self.name = name
    def setCodeBar(self, code_bar):
        self.code_bar = code_bar
    def setN(self, stock):
        self.n = stock

    def addProducts(self, products):
        self.setN(self.n + products)

    def removeProducts(self, products):
        if self.n < products:
            print('Não há estoque suficiente')
            self.setN(self.n)
        else:
            self.setN(self.n - products)