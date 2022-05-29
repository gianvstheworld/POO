from GeoFormat import *

class Rectangle(GeoFormat):
    def __init__(self, side1: float, side2: float, full: bool, color: str):
        super().__init__(side1, side2, full, color)

    def __str__(self) -> str:
        self.full = self.getFull()
        s = '\nForma Geométrica: Retângulo\n'
        s += "Lados: " + str(self.getSides()[0]) + " e " + str(self.getSides()[1]) + "\n"
        s += "Área: " + str(self.area()) + "\n"
        s += "Perímetro: " + str(self.perimeter()) + "\n"
        s += "Colorido: " + str(self.full) + "\n"

        if(self.full):
            s += "Cor: " + self.getColor() + "\n"
        
        return s