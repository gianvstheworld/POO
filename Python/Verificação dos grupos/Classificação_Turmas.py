# -*- coding: utf-8 -*-

from Turmas import *
import csv, sys, os

path = os.getcwd() + "\\Data Assets\\"

class Classificação_Turmas():
    def __init__(self):
        self.turma1 = list()
        self.nTurma1 = 0
        self.turma2 = list()
        self.npessoas2 = 0
        
    def readCSV(self, directory):
        try:
            print("Lendo o arquivo CSV das turmas")
            relative_path = path + directory
            for file in os.listdir(relative_path):
                if os.path.isfile(os.path.join(directory, file)):
                    yield file
                    
        except Exception as e:
            return "Erro ao ler o arquivo!"