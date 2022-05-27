from Pessoa import *
from PessoaFisica import *
from PessoaJuridica import *
from sys import *

SIZE = 1000

class AgendaContatos():
    def __init__(self):
        self.pessoas = list()
        self.nPessoas = 0
    
    def registerPF(self):
        if self.nPessoas == (SIZE - 1):
            print("** AVISO **\nAgenda de contatos cheia!")
            return
        
        try:
            print('Cadastrar Pessoa Física\n')
            name = input('Insira o nome:')

            index = self.findRegister(name)

            if index != -1:
                return ('\nJá existe um registro com este nome!')
                
            address = input('Insira o endereco: ')
            email = input('Insira o e-mail: ')
            bdate = input('Insira o aniversario: ')
            cstate = input('Insira o estado civil: ')
            cpf = input('Insira o CPF: ')

            self.pessoas[self.nPessoas] = PessoaFisica(name, cpf, address, bdate, email, cstate)
            print(self.pessoas)
            num_pessoas += 1

        except:
            print("Não foi possível realizar o cadastro")

    def registerPJ(self):
        if self.nPessoas == (SIZE - 1):
            print("** AVISO **\nAgenda de contatos cheia!")
            return
        
        try:
            print('Cadastrar Pessoa Jurídica\n')
            name = input('Insira o nome:')

            index = self.findRegister(name)

            if index != -1:
                return ('\nJá existe um registro com este nome!')
                
            address = input('Insira o endereco: ')
            email = input('Insira o e-mail: ')
            substate = input('Insira a inscrição estadual: ')
            socialr = input('Insira a razão social: ')
            cnpj = input('Insira o CNPJ: ')

            self.pessoas[self.nPessoas] = PessoaJuridica(name, cnpj, address, substate, email, socialr)
            num_pessoas += 1

        except:
            print("Não foi possível realizar o cadastro")

    def printContact(self):
        if isinstance(self.pessoa, PessoaFisica):
            print(PessoaFisica(self.pessoa))
        else:
            print(PessoaJuridica(self.pessoa))

    def printContacts(self):
        for i in range(self.nPessoas):
            if self.pessoas:
                self.printContact(self.pessoas[i])
            else:
                pass

    def findRegister(self, name):
        for i in range(self.nPessoas):
            if self.pessoas:
                self.pessoas[i].getName().equalTo(name)
            else:
                pass
    
    def findRegister(self, code):
        for i in range(self.nPessoas):
            if self.pessoas:
                if isinstance(self.pessoa, PessoaFisica):
                    self.pessoas[i] = self.PessoaFisica() 
                    if(self.pessoas[i].getCPF() == code):
                        return i
                else:
                    self.pessoas[i] = self.PessoaJuridica()
                    if(self.pessoas[i].getCNPJ() == code):
                        return i
        return -1

    def findPerson(self):
        print("Insira a chave de busca: ")
        
        index = -1

        try:
            key = input()
        except:
            print("** AVISO **\nNão foi possível ler a chave!")

        try:
            index = self.findRegister(int(key))
        except:
            index = self.findRegister(key)

        if index == -1:
            return ("** AVISO **\n Pessoa não encontrada")

        pessoa = self.pessoas[index]
        self.printContact(pessoa)

    def removePerson(self):
        print("Insira a chave de busca: ")

        index = -1

        try:
            key = input()
        except:
            print("** AVISO **\nNão foi possível ler a chave!")
        
        try:
            index = self.findRegister(int(key))
        except:
            index = self.findRegister(key)

        if index == -1:
            return ("** AVISO **\n Pessoa não encontrada")

        for index in range(self.nPessoas):
            self.pessoas[index] = self.pessoas[index + 1]
            
        self.nPessoas -= 1

    def getKey(self):
        if isinstance(self.pessoa, PessoaFisica):
            self.pessoa = PessoaFisica()
            return self.pessoa.getCPF()
        else:
            self.pessoa = PessoaJuridica()
            return self.pessoa.getCNPJ()
            
    def sortContacts(self):
        pf = list(SIZE)
        nf = 0
        pj = list(SIZE)
        nj = 0

        for i in range(self.nPessoas):
            if isinstance(self.pessoa[i], PessoaFisica):
                pf[nf] = self.pessoas[i]
                nf += 1
            else:
                pj[nj] = self.pessoas[i]
                nj += 1
        
        sorted(pf)
        sorted(pj)

        self.printContacts();