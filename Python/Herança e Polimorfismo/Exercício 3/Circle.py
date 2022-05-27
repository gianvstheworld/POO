from GeoFormat import *
import math

class Circle(GeoFormat):
    def __init__(self, radius: float, full: bool, color: str) -> None:
        super().__init__(0, 0, full, color)
        self.radius = radius

    def __str__(self) -> str:
        self.full = self.getFull()
        s = '\nForma Geométrica: CIRCULO\n'
        s += "Lados: " + str(self.radius) + "\n"
        s += "Area: " + str(self.area()) + "\n"
        s += "Perímetro: " + str(self.perimeter()) + "\n"
        s += "Colorido: " + str(self.full) + "\n"

        if(self.full):
            s += "Cor: " + self.getColor() + "\n"
        
        return 

    def area(self):
        return float(math.pi) * self.radius * self.radius

    def perimeter(self):
        return 2 * math.pi * self.radius