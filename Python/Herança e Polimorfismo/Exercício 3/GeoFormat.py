class GeoFormat:
    def __init__(self, side1: float, side2: float, full: bool, color: str):
        self.full = full
        self.sides = [0,0]
        self.sides[0] = side1
        self.sides[1] = side2

        if(self.full):
            self.color = color
            
    def getSides(self):
        return self.sides
    def getFull(self):
        return self.full
    def getColor(self):
        return self.color
    
    def perimeter(self):
        return 2 * (self.sides[0] + self.sides[1])

    def area(self):
        return self.sides[0] * self.sides[1]
