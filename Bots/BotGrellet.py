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
        print("Ola alunes, so um segundo, deixa eu pegar meu cafezinho\n")
        print("Opa, voltei, como estamos?.")

    def mostra_comandos(self):
        comandos = []
        for comando in self.comandos:
            comandos.append(comando)
        return comandos


def executa_comando(self, cmd):
    print(self.mostra_comandos[cmd])


def boas_vindas(self):
    stringa = "essa sema discutiremos algumas das minhas funcionalidades"
    stringb = "Olá todos e todas, sejam bem vindos ao chat bot do tyska,"
    normal = stringb + stringa
    print(normal)


def despedida(self):
    pass