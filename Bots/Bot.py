##implemente as seguintes classes

import random as r
from Bots.Comando import Comando

class Bot:

    def __init__(self, nome:str, comandos:list,apresentacao:str,boas_vindas:str,despedida:str):
        self.__nome = nome
        self.__comandos = comandos
        self.__apresentacao = apresentacao
        self.__boas_vindas = boas_vindas
        self.__despedida = despedida

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

    @property
    def comandos(self):
        return self.__comandos

    @comandos.setter
    def comandos(self, comandos: str):
        try:
            if not isinstance(str, comandos):
                raise TypeError
            self.__comandos = comandos
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
        if not isinstance(Comando,comando): print("Comando deve ser da classe Comando.")
        else:
            for i in self.mostra_comandos():
                if comando.id == i.id:
                    print("Um comando com essa mesma id já existe.")
                    break
            else:
                self.__comandos.append(comando)

    def executa_comando(self,cmd):
        # printa uma resposta possivel do comando
        for comando in self.__comandos:
            if comando.id == cmd:
                print(comando.getRandomResposta())
                break
        else:
            print("Esse comando não existe.")

    def apresentacao(self):
        print(self.__apresentacao)

    def boas_vindas(self):
        print(self.__boas_vindas)
    
    def despedida(self):
        print(self.__despedida)

