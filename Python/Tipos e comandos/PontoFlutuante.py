'''
-- Nome: Gianluca Capezzuto Sardinha
-- NUSP: 11876933

-- Exercício 7
'''

def main():

    listanum = []

    min = 0
    max = 0

    while True:
        x = leu()

        if x == 0:
            print("Fim da lista!")
            break

        listanum.append(x)
        
    for i in range(0, len(listanum)):
        if i == 0: 
            min = max = listanum[i]
        else:
            if listanum[i] < min:
                max = listanum[i]
            if listanum[i] > max:
                max = listanum[i]

    print("Você digitou os valores {}".format(listanum))
    print('O menor número digitado foi {} e o maior {}'.format(min, max))


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




