from random import randrange
class Comando:
    # recebe o id (inteiro), a mensagem e as respostas (opcional)
    def __init__(self, id, msg):
        self.__id = id
        self.__msg = msg
        self.__respostas = []

    @id.setter
    def id(self):
        return self.__id

    @msg.setter
    def msg(self):
        return self.__msg

    # retorna uma resposta aleatória
    def getRandomResposta(self):
        return self.__respostas[randrange(len(self.__respostas))]

    # adiciona resposta
    def addResposta(self, resposta):
        self.__respostas.append(resposta)

    # remove resposta (opcional)
    def delResposta(self, resposta):
        self.__respostas.remove(resposta)