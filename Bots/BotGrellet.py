from Bots.Bot import Bot
from Bots.Comando import Comando


class BotGrellet(Bot):
    def __init__(self, nome):
        comandos = [
            Comando(1, "Professor, posso fazer individual? :(", ["Hahaha, jamais, o objetivo eh justamente aprender a trabalhar em grupo ;)"])

        ]
        super().__init__(nome, comandos)

    def apresentacao(self):
        print("Ola queridos, sou o prof. Mateus, leciono POO2 com meu caro, Jonata, e dou lab de SD\n")
        
    def boas_vindas(self):
        print("Ola alunes, so um segundo, deixa eu pegar meu cafezinho\nOpa, voltei, como estamos?")

    def despedida(self):
        print("Ate a proxima")