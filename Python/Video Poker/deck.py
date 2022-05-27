import random

class Carta(object): # definindo a classe das cartas
    def __init__(self, carta, valor, naipe, icone):
        # atribuindo os valores, naipes e dizendo se ela está sendo mostrada ou não
        self.valor = valor
        self.naipe = naipe
        self.carta = carta
        self.icone = icone
        self.virada = False

    def __repr__(self):
        if self.virada: # caso a carta esteja virada, diz qual carta é
            return self.icone
        else: # caso não, diz somente que é uma carta
            return "Carta"

class Baralho(object): # definindo a classe baralho
    # embaralha o baralho aleatoriamente
    def embaralhar(self, n = 1):
        random.shuffle(self.cartas)
        print("Baralho embaralhado")

    # distribui as cartas, retirando sempre o ultimo elemento da lista, ou seja, a primeira do monte do baralho
    def deal(self):
        return self.cartas.pop(0)

class BaralhoPadrao(Baralho): # definindo a classe baralho padrão
    def __init__(self):
        self.cartas = [] # atribui as cartas a uma lista
        naipes = {"Ouros": "♦", "Espadas": "♠", "Copas": "♥", "Paus": "♣"} # define os naipes
        # define o valor de cada carta, sendo dois o mais fraco e ás o mais forte
        valores = {"Dois": 2, 
                   "Três": 3, 
                   "Quatro": 4,
                   "Cinco": 5,
                   "Seis": 6,
                   "Sete": 7,
                   "Oito": 8,
                   "Nove": 9,
                   "Dez": 10,
                   "J": 11,
                   "Q": 12,
                   "K": 13,
                   "A": 14}

        # faz a combinação de todas as 52 cartas do baralho
        for carta in valores:
            for naipe in naipes:
                iconeCarta = naipes[naipe]

                if valores[carta] < 11:
                    icone = str(valores[carta]) + iconeCarta
                else:
                    icone = carta[0] + iconeCarta

                self.cartas.append(Carta(carta, valores[carta], naipe, icone))

    # retorna quantas cartas ainda estão presentes no baralho
    def __repr__(self):
        return "O baralho ainda possui: {0} cartas restantes".format(len(self.cartas))

class Jogador(object): # definindo a classe jogador
    def __init__(self):
        self.cartas = [] # criam uma lista com as cartas do jogador

    def contaCartas(self): 
        return len(self.cartas) # retorna o número de cartas do jogador

    def adicionaCartas(self, carta):
        self.cartas.append(carta) # adiciona carta ao jogador


