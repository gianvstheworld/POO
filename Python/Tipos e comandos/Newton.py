'''
-- Nome: Gianluca Capezzuto Sardinha
-- NUSP: 11876933

-- Exercício 9
'''

from scipy import misc 

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

def newton(f, x, erro):
    
    x0 = x
    xn = x
    
    i = 0

    while True:

        x_n1 = xn - f(xn) / misc.derivative(f, xn)
        precisão = abs(x_n1 - xn)

        if precisão < erro:
            break
        
        xn = x_n1

        i += 1
    
    print('\nChute inicial: {}, tendo como solução: {} em {} iterações'.format(x0, x_n1, i))


def main():

    x0 = leu()
    erro = 0.0000001

    newton(f, x0, erro)

if __name__ == '__main__':
    main()