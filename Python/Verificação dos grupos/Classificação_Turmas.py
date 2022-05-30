from Turmas import *
import csv

class Classificação_Turmas():
    def __init__(self):
        self.turma1 = list()
        self.nTurma1 = 62
        self.turma2 = list()
        self.npessoas2 = 42
        
    def readCSV(self):
        try:
            print('Lendo o arquivo CSV das turmas')

        