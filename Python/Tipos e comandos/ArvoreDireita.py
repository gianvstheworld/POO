'''
-- Nome: Gianluca Capezzuto Sardinha
-- NUSP: 11876933

-- Exercício 4
'''

def main():

    x = leu()
    spaceL = 0

    while x > 0:

        i = 0

        for _ in range(0, spaceL):
            print(" ", end = "")

        while i < x:
            print("*", end = "")
            i += 1

        print("\n")
        x -= 1
        spaceL += 1

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




