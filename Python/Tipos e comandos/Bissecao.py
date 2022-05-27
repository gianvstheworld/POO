'''
-- Nome: Gianluca Capezzuto Sardinha
-- NUSP: 11876933

-- Exercício 8
'''

def f(x):
    fx = x**3 - x**2 - (13 * x) + 8
    return fx

def leu():

    while(True):

        try:
            k = int(input('Digite um inteiro: '))
            break

        except ValueError:
            print('O valor digitado deve ser um número inteiro!')
    
    return k

def bissecao(f, a, b, erro):

    if f(a) * f(b) >= 0:
        print("Não há como aplicar o método da bisseção.")
        return None
    
    a1 = a
    b1 = b

    i = 0
    cond = True

    while cond:

        ponto_medio = (a + b) / 2

        if f(a) * f(ponto_medio) < 0:
            b = ponto_medio
        else:
            a = ponto_medio

        i += 1
        cond = abs(f(ponto_medio)) > erro
    

    print('\nIntervalo: [{}, {}], tendo como solução: {} em {} iterações'.format(a1, b1, ponto_medio, i))


def main():

    a0 = leu()
    b0 = leu()
    erro = 0.0000001

    bissecao(f, a0, b0, erro)

if __name__ == '__main__':
    main()