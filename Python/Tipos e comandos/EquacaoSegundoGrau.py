from cmath import sqrt


'''
-- Nome: Gianluca Capezzuto Sardinha
-- NUSP: 11876933

-- Exercício 2
'''

def main():

    a = leu() 
    b = leu()
    c = leu()

    delta = b**2 - 4 * a * c

    x1 = (-b + sqrt(delta)) / (2 * a)
    x2 = (-b - sqrt(delta)) / (2 * a) 

    print("A equação tem como raiz {0} e {1}".format(x1, x2))

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




