from Loja import *

loja = Loja()

while(True):

    print("\n*************  PRODUTOS *************n\n")

    print("1 - Cadastrar produto")
    print("2 - Adicionar estoque em produto existente")
    print("3 - Buscar produto")
    print("4 - Vender produto")
    print("5 - Exibir estoque completo")
    print("6 - Excluir item")
    print("7 - Encerrar programa")
    print("\n")

    func = int(input())

    if func == 1:
        loja.registerProduct()
    elif func == 2:
        loja.addProduct()
    elif func == 3:
        loja.getProduct()
    elif func == 4:
        loja.removeProduct()
    elif func == 5:
        loja.printStock()
    elif func == 6:
        loja.deleteProduct()
    elif func == 7:
        exit()
    else:
        print('Erro: Modo inválido')
        
