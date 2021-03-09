##implemente as seguintes classes

from abc import ABC, abstractmethod
import random as r

class Bot(ABC):

    def __init__(self, nome, comandos):
        self.__nome = nome
        self.comandos = comandos

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

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
        pass
    
    @abstractmethod
    def despedida():
        pass