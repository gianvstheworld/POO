from Pessoa import *
from PessoaFisica import *
from PessoaJuridica import *
from sys import *

class AgendaContatos():
    def __init__(self):
        self.pessoas = list() 
        self.nPessoas = 0

    def registerPF(self):
        try:
            print('\nCadastrar Pessoa Física')
            name = input('Insira o nome: ')

            index = self.findRegisterName(name)

            if index != -1:
                print('\nJá existe um registro com este nome!')
            else:  
                address = input('Insira o endereco: ')
                email = input('Insira o e-mail: ')
                bdate = input('Insira o aniversario: ')
                cstate = input('Insira o estado civil: ')
                cpf = int(input('Insira o CPF: '))

                self.pessoas.append(PessoaFisica(name, cpf, address, bdate, email, cstate)) 
                self.nPessoas += 1
                print("Cadastro realizado com sucesso!")
                
        except Exception as e:
            print("\nNão foi possível realizar o cadastro")
            print(e)

    def registerPJ(self):
        try:
            print('\nCadastrar Pessoa Jurídica')
            name = input('Insira o nome: ')

            index = self.findRegisterName(name)

            if index != -1:
                print('\nJá existe um registro com este nome!')
            else:
                address = input('Insira o endereco: ')
                email = input('Insira o e-mail: ')
                substate = input('Insira a inscrição estadual: ')
                socialr = input('Insira a razão social: ')
                cnpj = int(input('Insira o CNPJ: '))

                self.pessoas.append(PessoaJuridica(name, cnpj, address, substate, email, socialr))
                self.nPessoas += 1
                print("Cadastro realizado com sucesso!")

        except Exception as e:
            print("\nNão foi possível realizar o cadastro")
            print(e)

    def printContact(self, pessoa):
        if isinstance(self.pessoas, PessoaFisica):
            print(pessoa)
        else:
            print(pessoa)

    def printContacts(self):
        for pessoas in self.pessoas:
            if len(self.pessoas) == 0:
                continue
            self.printContact(pessoas)

    def findRegisterName(self, name):
        for i in range(self.nPessoas):
            if len(self.pessoas) == 0:
                continue
            if self.pessoas[i].getName() == name:
                return i
        return -1
    
    def findRegisterCode(self, code):
        for i in range(len(self.pessoas)):
            if len(self.pessoas) == 0:
                continue
            if isinstance(self.pessoas[i], PessoaFisica):
                if self.pessoas[i].getCPF() == code: 
                    return i
            else: 
                if self.pessoas[i].getCNPJ() == code:
                    return i
        return -1

    def findPerson(self):
        print("\nInsira a chave de busca (Nome, CPF ou CNPJ): ")
        
        index = -1

        try:
            key = input()
        except:
            print("** AVISO **\nNão foi possível ler a chave!")

        try:
            index = self.findRegisterCode(int(key))
        except:
            index = self.findRegisterName(key)

        if index == -1:
            print("** AVISO **\n Pessoa não encontrada")
        else:
            self.printContact(self.pessoas[index])

    def removePerson(self):
        print("\nInsira a chave de busca (Nome, CPF ou CNPJ): ")

        index = -1

        try:
            key = input()
        except:
            print("** AVISO **\nNão foi possível ler a chave!")
        
        try:
            index = self.findRegisterCode(int(key))
        except:
            index = self.findRegisterName(key)

        if index == -1:
            print ("** AVISO **\n Pessoa não encontrada")
        else:
            del self.pessoas[index]
            print("Pessoa removida da agenda de contatos!\n")
            self.nPessoas -= 1 
    
    def bubbleSort(self, lista):
        for passnum in range(len(lista) - 1, 0, -1):
            for i in range(passnum):
                if isinstance(self.pessoas, PessoaFisica):
                    if lista[i].getCPF() > lista[i + 1].getCPF():
                        temp = lista[i]
                        lista[i] = lista[i + 1]
                        lista[i + 1] = temp
                elif isinstance(self.pessoas, PessoaJuridica): 
                    if lista[i].getCNPJ() > lista[i + 1].getCNPJ():
                        temp = lista[i]
                        lista[i] = lista[i + 1]
                        lista[i + 1] = temp
    
    def sortContacts(self):
        self.fisica = list()
        self.juridica = list()
        nFisica = 0
        nJuridica = 0

        for i in range(len(self.pessoas)):
            if len(self.pessoas) == 0:
                continue
            if isinstance(self.pessoas[i], PessoaFisica):
                self.fisica.append(self.pessoas[i])
                nFisica += 1
            else:
                self.juridica.append(self.pessoas[i])
                nJuridica += 1

        self.bubbleSort(self.fisica)
        self.bubbleSort(self.juridica)

        for i in range(len(self.fisica)):
            self.pessoas[i] = self.fisica[i]
        
        for i in range(len(self.juridica)):
            self.pessoas[i + nFisica] = self.juridica[i]

        print("Lista ordenada!")
        self.printContacts()


