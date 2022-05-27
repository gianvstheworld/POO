'''
-- Nome: Gianluca Capezzuto Sardinha
-- NUSP: 11876933

-- Exercício 5
'''

def main():

    x = leu()
    multiplo = 0

    for i in range(2, x):
        if(x % i == 0):
            multiplo += 1
            break;

    if multiplo == 0:
        print("O número é primo!")
    else:
        print("O número não é primo e seu menor divisor é {}".format(i))

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




