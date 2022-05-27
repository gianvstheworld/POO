'''
-- Nome: Gianluca Capezzuto Sardinha
-- NUSP: 11876933

-- Exercício 6
'''

def main():

    x = leu()
    y = x

    while x > 0:
        multiplo = 0

        for i in range(2, x):
            if(x % i == 0):
                multiplo = 1
                break;

        if multiplo == 0:
            break

        x -= 1    

    print("O primeiro número primo menor depois de {} é {}".format(y, x))

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




