from AgendaDeContatos import *

agenda = AgendaContatos()

while True:

    print("\n******** AGENDA ********")
    print("Selecione a função que deseja executar:")
    print("1 - Cadastrar Pessoa Física")
    print("2 - Cadastrar Pessoa Jurídica")
    print("3 - Buscar por contato existente")
    print("4 - Remover contato")
    print("5 - Sair")

    func = int(input())

    if func == 1:
        agenda.registerPF()
    elif func == 2:
        agenda.registerPJ()
    elif func == 3:
        agenda.findPerson()
    elif func == 4:
        agenda.removePerson()
    else:
        break
