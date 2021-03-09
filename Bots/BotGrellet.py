from Bots.Bot import Bot


class BotGrellet(Bot):
    def __init__(self, nome):
        comandos = {"": ""}
        super().__init__(nome, comandos)

    # nao esquecer o decorator
    @property
    def nome(self):
        return self.__nome

    # nao esquecer o decorator
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def apresentacao(self):
        print("Ola sou o prof. Mateus, leciono POO2 com meu caro, Jonata, e dou lab de SD\n")

    def mostra_comandos(self):
        i = 0
        for comando in self.comandos:
            i += 1
            print(str(i)+". "+comando+"\n")


def executa_comando(self, cmd):
    print(self.mostra_comandos[cmd])


def boas_vindas(self):
    print("Ola alunes, so um segundo, deixa eu pegar meu cafezinho\nOpa, voltei, como estamos?")


def despedida(self):
    pass