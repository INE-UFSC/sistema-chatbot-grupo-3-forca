from bot import Bot
from comando import Comando

class BotTyska(Bot):
    def __init__(self,nome):
        comandos = [
            Comando(1, "O que você acha mais importante na faculdade?", ["Para mim o importante é ter uma metodologia ativa sempre"]),
            Comando(2, "Qual o aspecto de um código orientado a objetos mais importante?", ["Um bom código é um código bem abstrato com pouca rigidez."]),
            Comando(3, "O que vc gosta de fazer no seu tempo livre?", ["Fazer mais execícios para os alunos", "Treinar meu cachorro", "Ouvir um pagode"])
        ]
        apresentacao = "Ola me escolham para participar de um método de aprendizado ativo e utilizarem diversas ferrramens da internet."
        boas_vindas = "Olá todos e todas, sejam bem vindos ao chat bot do tyska, essa semana discutiremos algumas das minhas funcionalidades"
        despedida = "Boa semana de estudos!!"
        super().__init__(nome, comandos,apresentacao,boas_vindas,despedida)
