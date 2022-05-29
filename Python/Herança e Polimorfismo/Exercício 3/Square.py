from GeoFormat import *

class Square(GeoFormat):
    def __init__(self, side: float, full: bool, color: str):
        super().__init__(side, side, full, color)

    def __str__(self) -> str:
        self.full = self.getCheio()
        s = '\nForma Geométrica: Quadrado\n'
        s += "Lados: " + str(self.getSides()[0]) + " e " + str(self.getSides()[1]) + "\n"
        s += "Área: " + str(self.area()) + "\n"
        s += "Perímetro: " + str(self.perimeter()) + "\n"
        s += "Colorido: " + str(self.full) + "\n"

        if(self.full):
            s += "Cor: " + self.getColor() + "\n"
        
        return s