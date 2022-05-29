from Square import *
from Rectangle import *
from Circle import *
from GeoFormat import *

TAM = 1000

class Geometry():
    def __init__(self):
        self.forms = [0 for i in range(0, TAM)]
        self.nForms = 0

    def getSide(self):
        try:
            return float(input('Lado: '))
        except:
            print('Um erro ocorreu')

    def printFormats(self):
        print('Formas:\n')
        
        for i in range(0, self.nForms):
            if isinstance(self.forms[i], Circle):
                print('\nCirculo: ' + str(self.forms[i]))
            if isinstance(self.forms[i], Square):
                print('\nSquare: ' + str(self.forms[i]))
            if isinstance(self.forms[i], Rectangle):
                print('\nRetangulo: ' + str(self.forms[i]))

    def insertSquare(self):
        self.insertFormats(0)

    def insertRectangle(self):
        self.insertFormats(1)

    def insertCircle(self):
        self.insertFormats(2)

    def insertFormats(self, flag):
        if flag == 0: 
            print("\nInserir quadrado") 
        elif flag == 1:
            print("\nInserir retângulo") 
        elif flag == 2:
            print("\nInserir círculo") 
        
        sides =  [-1.0, -1.0]

        if flag == 0:
            print("Insira o lado: ")
            sides[0] = self.getSide()
            sides[1] = sides[0]
        
        if flag == 1:
            print("Insira o lado 1: ")
            sides[0] = self.getSide()
            print("Insira o lado 2: ")
            sides[1] = self.getSide()
        
        if flag == 2:
            print("Insira o raio: ")
            sides[0] = self.getSide()
            sides[1] = sides[0]
        
        if sides[0] == -1 or sides[1] == -1: 
            print("ERRO: Não foi possível ler o valor para o lado")
            return
        
        try:
            self.full = False
            self.fullSTR = input('Mudar a cor?') 
            print(self.fullSTR.strip().lower())
            self.color = ""

            if self.fullSTR is 'Sim':
                self.full = True
                self.color = input('Insira a cor desejada: ')
            
            if flag == 0: 
                self.forms[self.nForms] = Square(sides[0], self.full, self.color)
                self.nForms += 1
                print("Forma criada com sucesso: ")
                print(str(self.forms[self.nForms]))
            
            if flag == 1:
                self.forms[self.nForms] = Rectangle(sides[0], sides[1], self.full, self.color)
                self.nForms += 1
                print("Forma criada com sucesso: ")
                print(str(self.forms[self.nForms]))
            
            if flag == 2: 
                self.forms[self.nForms] = Circle(sides[0], self.full, self.color)
                self.nForms += 1
                print("Forma criada com sucesso: ")
                print(str(self.forms[self.nForms]))
        
        except:
            return