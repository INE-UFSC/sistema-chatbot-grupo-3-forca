from Bots.Bot import Bot


class BotGrellet(Bot):
    def __init__(self, nome):
        comandos = {"": "",
                    "Professor, posso fazer individual? :(": "Hahaha, jamais, o objetivo eh justamente aprender a trabalhar em grupo ;)"}
        super().__init__(nome, comandos)

    def apresentacao(self):
        print("Ola queridos, sou o prof. Mateus, leciono POO2 com meu caro, Jonata, e dou lab de SD\n")

    def mostra_comandos(self):
        i = 0
        for comando in self.comandos:
            i += 1
            print(str(i)+". "+comando+"\n")


    def executa_comando(self, cmd):
        i = 1
        for comandos in self.comandos:
            if comando.id == i:
                print(comando.getRandomResposta())
            i += 1


    def boas_vindas(self):
        print("Ola alunes, so um segundo, deixa eu pegar meu cafezinho\nOpa, voltei, como estamos?")

    def despedida(self):
        print("Ate a proxima")