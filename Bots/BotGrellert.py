from bot import Bot
from comando import Comando


class BotGrellert(Bot):
    def __init__(self, nome):
        comandos = [
            Comando(1,"Professor, posso fazer individual? :(", ["Hahaha, jamais, o objetivo eh justamente aprender a trabalhar em grupo ;)"]),
            Comando(2,"Do que voce mais gosta? ",["I <3 Python", "Eu gosto muito de cafe", "Pronome neutro"]),
            Comando(3,"Voce gosta mais de software ou hardware?",["hardware sempre, tenho bom gosto"])
        ]
        apresentacao = "Ola queridos, sou o prof. Mateus, leciono POO2 com meu caro, Jonata, e dou lab de SD\n"
        boas_vindas = "Ola alunes, so um segundo, deixa eu pegar meu cafezinho\nOpa, voltei, como estamos?"
        despedida = "Ate a proxima"
        super().__init__(nome, comandos,apresentacao,boas_vindas,despedida)
