from Estoque import *
from Livro import *
from CD import *
from DVD import *

TAM = 1000

class Loja:
    def __init__(self):
        self.items = list()
        self.mode = -1 
        self.qte = 0 
        self.num_items = 0
        self.name = ""     

    def registerProduct(self):
        
        print('\nAdicionar Item')

        print("1 - Inserir Livro")
        print("2 - Inserir CD")
        print("3 - Inserir DVD\n")

        self.mode = int(input('> ')) 

        try:
            code_bar = int(input('Código de barras para este produto: '))
            name = input('Insira nome do produto: ')

            try:
                self.qte = int(input("Insira uma quantidade inicial para o estoque:"))
                
                if self.qte < 0: 
                    print("\nErro: A quantidade inicial minima é 0")
                    self.qte = 0
            
            except Exception as e: 
                print(f'Erro: {e}')
                self.qte = 0 

            if self.mode == 1:
                self.items.append(Livro(name, code_bar, self.qte)) 
            elif self.mode == 2: 
                self.items.append(CD(name, code_bar, self.qte))
            elif self.mode == 3: 
                self.items.append(DVD(name, code_bar, self.qte)) 
            else:
                return

            if (self.ctCode_Product(code_bar) == -1) or (self.ctCode_Product(name) == -1): 
                print("Erro: produto já cadastrado\n") 
            self.num_itens += 1

        except Exception as e: 
            print(f"\nErro: {e}") 
            return 
    
    def addProduct(self):
        self.qte = 0

        print('\nAdicionar Estoque')

        pos = self.ctIndex()
        if pos == -1: 
            print("Erro \nItem não encontrado") 
            return 

        try:
            print("Item "+ str((self.items[pos]).getName()) + "encontrado")
            print("Insira a quantidade que deseja acrescentar: ")
            self.qte = input()

            if self.qte <= 0: 
                print("\nErro: Quantia inválida") 
                return 

        except Exception as e: 
            print(f"\nErro: {e}") 
            return 

        self.items[pos].addProducts(self.qte)
        print("\n Quantia adicionada com sucesso ")
        print("Quantidade atual: "+ str(self.items[pos].getself.Qte()))

    def ctCode_Product(self, key):
        if isinstance(key, int):
            for item in self.items:
                if int(key) == item.getCodeBar(): 
                    return self.items.index(item)
        else:
            for item in self.items:
                if key ==  item.getName(): 
                    return self.items.index(item)
        return -1

    def ctIndex(self):
        key = ""
        self.qte = 0
        pos = -1

        try:
            key = input('Insira o nome ou código de barras do item que deseja modificar: ')
            try:
                code = int(key)                
                pos = self.ctCode_Product(code)
                if pos == -1: 
                    pos = self.ctCode_Product(key)  
            except Exception as e:
                pos = self.ctCode_Product(key)
            
        except Exception as e: 
            print(f"\nErro:{e}") 
            return -2 

        return pos

    def getProduct(self):
        print('Buscar Item')
        pos = self.ctIndex()
        print('pos: ', pos)
        if pos == -1: 
            print("\nErro: Item não encontrado") 
            return 
        print("\n Produto encontrado:\n" + str(self.items[pos]))

    def printStock(self):
        print('Imprimindo estoque')
        for item in self.items:
            print(item)
            

    def deleteProduct(self):
        print('Excluir Item')
        self.pos = self.ctIndex() 
        
        if self.pos == -1: 
            print("\nErro: Item não encontrado") 
            return 
        else:
            del self.items[self.pos]
        
        self.num_items -= 1
        print("\n Item excluido")

    def removeProduct(self):
        print('Vender Item')
        self.qte = 0
        self.pos = self.ctIndex()

        if self.pos == -1: 
            print("\nErro: Item não encontrado") 
            return 

        print("Item "+ str((self.items[self.pos]).getName()) + "encontrado")
        print("Insira a quantidade que deseja retirar: ")
        self.qte = int(input())

        if self.qte <= 0: 
            print("\nErro: Quantia inválida") 
            return 

        (self.items[self.pos]).removeProducts(self.qte)
        print("\n Remoção realizada com sucesso \nNovo estoque: "+ (self.items[self.pos]).getself.Qte())
