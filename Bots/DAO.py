#coding: utf-8
from abc import ABC
import json

class DAO(ABC):
    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.objectCache = {}
        #AO INICIAR TENTA CARREGAR OS CONTEUDOS DO JSON, SE NAO ONSEGUE ELE CRIA UM ARQUIVO SEM CONTEUDO
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __dump(self):
        #SOBREESCREVE O ARQUIVO COM OS CONTEUDOS DE OBJECT CACHE
        json.dump(self.objectCache, open(self.arquivo, 'w'))

    def __load(self):
        try:
            #CARREGA OS CONTEUDOS DO ARQUIVO EM OBJECT CACHE
            self.objectCache = json.load(open(self.arquivo, 'r'))
        except:
            pass

    def add(self, key, obj):
        #ACRESCENTA O NOVO ELEMENTO AO DICIONARIO OU SUBSTITUI UM ANTIGO SE A CHAVE FOR REPETIDA
        self.objectCache[key] = obj.encoded
        #ATUALIZA O ARQUIVO
        self.__dump()

    def get(self, key):
        try:
            #RETORNA UM ELEMENTO DO DICIONARIO
            return self.objectCache[key]
        except KeyError:
            pass

    def remove(self, key):
        try:
            #REMOVE UM ELEMENTO DO DICIONAIO E ATUALIZA O ARQUIVO
            self.objectCache.pop(key)
            self.__dump()
        except KeyError:
            pass

    def get_all(self):
        #RETORNA O DICIONARIO
        return self.objectCache