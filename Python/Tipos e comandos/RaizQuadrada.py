'''
-- Nome: Gianluca Capezzuto Sardinha
-- NUSP: 11876933

-- Exercício 1
'''

def main():

    x = leu() 
    erro = 1

    if(x > 10):
        x0 = x/5
    else:
        x0 = x/2

    xi = x0 
    yi = xi - 1

    while(erro > 0.00000001):
        xi = (yi+(x/yi))/2
        erro = abs(xi - yi)
        yi = xi

    print("A raiz de {0} é {1}".format(x, xi))

def leu():

    while(True):

        try:
            k = int(input('Digite um inteiro: '))
            if(k < 0):
                print('O número deve ser positivo!')
                continue

            break

        except ValueError:
            print('O valor digitado deve ser um número inteiro!')
    
    return k

if __name__ == '__main__':
    main()




