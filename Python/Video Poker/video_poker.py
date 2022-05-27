from deck import *
from placar import *

def main():

    # criação do objeto jogador
    jogador = Jogador()

    # quandtidade de créditos inicial de cada jogador e a entrada da aposta
    creditos = 200
    aposta = int(input("Aposte um número de cŕeditos para a rodada:\n"))

    # enquanto o valor da aposta não for de acordo com o desejado, pede para inserir novamente
    while aposta < 0 or aposta >= 200:
        print("O valor apostado deve ser maior que zero e menor ou igual ao número de créditos na sua carteira!")
        aposta = int(input("Aposte um número de cŕeditos para a rodada:\n"))

    # enquanto os créditos dos jogadoor forem maior que zero, o jogo continua acontecendo
    while creditos > 0:
        print("Você tem {0} créditos\n".format(creditos - aposta))

        # criação do objeto baralho
        baralho = BaralhoPadrao()
        baralho.embaralhar()

        # adiciona cartas a mão do jogador
        for _ in range(5):
            jogador.adicionaCartas(baralho.deal())

        # torna as cartas visíveis para o jogador que a possui
        for carta in jogador.cartas:
            carta.virada = True

        # mostra as cartas
        print(jogador.cartas)

        print("Quais cartas você deseja descartar? Separe por espaços!")
        print("Caso queira continuar com elas, aperte ENTER! E caso queira sair, escreva SAIR.")
        input_string = input()

        # caso o jogador não queira mais jogar, apenas digita "SAIR"
        if input_string == "SAIR": 
            creditos = 0
            break

        # tenta verificar quais cartas o jogador deseja trocar, caso contrário pede para o mesmo utilizar espaços para fazer a separação
        try:
            input_lista = [int(input_cartas.strip()) for input_cartas in input_string.split(" ") if input_cartas]

            for input_cartas in input_lista:
                if input_cartas > 6:
                    continue
                if input_cartas < 1: 
                    continue

            for input_cartas in input_lista:
                jogador.cartas[input_cartas - 1] = baralho.deal()
                jogador.cartas[input_cartas - 1].virada = True

        except:
            print("Use espaços para separar as cartas que você deseja descartar")

        # printa novamente a mão do jogador
        print(jogador.cartas)

        # criação do objeto placcar
        score = Placar(jogador.cartas)

        # atribuição de possíveis tipos de multiplicadores 
        par = score.checaPares()
        trinca = score.checaTrinca()
        straight = score.checaStraight()
        flush = score.checaFlush()
        quadra = score.checaQuadra()

        # verificação de dois pares 
        if len(par) == 2:
            print("Dois pares!")
            aposta = aposta

        # verificação de trinca
        elif trinca:
            print("Trinca!")
            aposta *= 2

        # verificação de straight
        elif straight:
            print("Straight!")
            aposta *= 5

        # verificação de flush
        elif flush:
            print("Flush!")
            aposta *= 10
        
        # verificação de full hand
        elif trinca and par:
            print("Full hand!")
            aposta *= 20

        # verificação de quadra
        elif quadra: 
            print("Quadra!")
            aposta *= 50

        # verificação de straight flush
        elif straight and flush:
            print("Straight Flush!")
            aposta *= 100

        # verificação de royal straight flush
        elif straight and flush and straight == 14:
            print("Royal Straight Flush!")
            aposta *= 200

        jogador.cartas = []

if __name__ == "__main__":
    main()