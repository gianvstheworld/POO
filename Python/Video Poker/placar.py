from deck import *

class Placar(object): # definindo a classe placar
    def __init__(self, cartas):
        if not len(cartas) == 5: # caso o jogador não tenha o número de cartas correto, retorna um erro
            return "Número de cartas distribuído errado!"

        # atribui as cartas 
        self.cartas = cartas

    def checaPares(self): # verifica a existência de pares
        pares = [] # cria uma lista de pares, pois há a possibilidade de existir mais de um
        valores = [carta.valor for carta in self.cartas]

        # verifica os valores das cartas
        for valor in valores:
            if valores.count(valor) == 2 and valor not in pares: # conta se há dois valores iguais e o par já não está inserido
                pares.append(valor) # então, adiciona o par na lista 

        return pares # retorna o número de pares 

    def checaTrinca(self): # verifica a existência de trincas
        # cria uma lista valores com o valor de cada carta
        valores = [carta.valor for carta in self.cartas]
        for valor in valores: # passa por todas as cartas e verifica se há uma trinca
            if valores.count(valor) == 3: 
                return True

    def checaStraight(self): # verifica a existência de um straight
        # cria uma lista valores com o valor de cada carta e ordena para facilitar ao checar o straight
        valores = [carta.valor for carta in self.cartas]
        valores.sort()

        # se o vetor valores não for igual a 5 retorna, já sabemos que não é um straight
        if len(set(valores)) != 5:
            return False

        # verififcação do straight, corroborando com a verificação do straight royal flush 
        if valores[0] == 2 and valores[1] == 3 and valores[2] == 4 and valores[3] == 5 and valores[4] == 14:
            return 5

        else:
            if valores[0] + 1 != valores[1]:
                return False
            if valores[1] + 1 != valores[2]:
                return False
            if valores[2] + 1 != valores[3]:
                return False
            if valores[3] + 1 != valores[4]:
                return False

        return valores[4]

    def checaFlush(self): # verifica a existência de um flush
        # como o flush depende apenas dos naipes, cria um vetor naipes com o naipe de cada carta
        naipes = [carta.naipe for carta in self.cartas]

        # caso o naipe encontrado seja apenas 1, é um flush
        if len(set(naipes)) == 1:
            return True

        return False
        
    def checaQuadra(self): # verifica a existência de uma quadra
        # cria uma lista valores com o valor de cada carta
        valores = [carta.valor for carta in self.cartas]

        # varre os valores e se houver quatro deles iguais, sabe que é uma quadrad
        for valor in valores:
            if valores.count(valor) == 4:
                return True

