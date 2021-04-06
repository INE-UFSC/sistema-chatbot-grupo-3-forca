##implemente as seguintes classes

from abc import ABC, abstractmethod
import random as r
from Bots.Comando import Comando

class Bot(ABC):

    def __init__(self, nome:str, comandos:list):
        self.__nome = nome
        self.__comandos = comandos

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome:str):
        try:
            if not isinstance(str,nome):
                raise TypeError
            self.__nome = nome
        except TypeError:
            print("O nome do bot deve ser uma string.")

    def mostra_comandos(self):
        # printa a mensagem que corresponde a cada comando
        listacom = []
        for comando in self.__comandos:
            listacom.append(comando)
        return listacom

    def cria_comandos(self,comando):
        # adiciona comando a lista
        self.__comandos.append(comando)

    def executa_comando(self,cmd):
        # printa uma resposta possivel do comando
        print(self.__comandos[cmd].getRandomResposta())

    @abstractmethod
    def apresentacao(self):
        pass

    @abstractmethod
    def boas_vindas(self):
        pass
    
    @abstractmethod
    def despedida(self):
        pass

