##implemente as seguintes classes

from abc import ABC, abstractmethod
import random as r

class Bot(ABC):

    def __init__(nome,):
        self.nome = nome
        self.comandos = {"boas-vindas":"string de boas vindas","despedida":"string de despedida"}

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
        pass

    @abstractmethod
    def boas_vindas():
        print(self.comandos["boas-vindas"])
    
    @abstractmethod
    def despedida():
        print(self.comandos["despedida"])