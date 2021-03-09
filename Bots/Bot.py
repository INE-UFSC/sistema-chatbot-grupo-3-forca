##implemente as seguintes classes

from abc import ABC, abstractmethod
import random as r

class Bot(ABC):

    def __init__(self, nome, comandos):
        self.nome = nome
        self.comandos = comandos
        self.boas_vindas = "string de boas vindas"
        self.despedida = "string de despedida"

    @property
    def nome(self):
        return self.nome

    @nome.setter
    def nome(self, nome):
        self.nome = nome

    @property
    def mostra_comandos(self):
        comandos = []
        for comando in self.comandos:
            comandos.append(comando)
        return comandos

    @abstractmethod
    def executa_comando(self,cmd):
        print(self.mostra_comandos[cmd])

    @abstractmethod
    def boas_vindas():
        print(self.boas_vindas)
    
    @abstractmethod
    def despedida():
        print(self.despedida)