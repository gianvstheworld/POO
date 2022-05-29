from numpy import intp
from Geometry import *

geofigure = Geometry()

while True:

    print("\n******** FIGURAS GEOMÉTRICAS ********")
    print("Selecione a função que deseja executar:")
    print("1 - Inserir quadrado")
    print("2 - Inserir retângulo")
    print("3 - Inserir circulo")
    print("4 - Imprimir todas as formas")
    print("5 - Sair")

    func = int(input())

    if func == 1:
        geofigure.insertSquare()
    elif func == 2:
        geofigure.insertRectangle()
    elif func == 3:
        geofigure.insertSquare()
    elif func == 4:
        geofigure.printFormats()
    else:
        break