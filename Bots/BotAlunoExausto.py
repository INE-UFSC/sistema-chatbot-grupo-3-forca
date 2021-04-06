from Bots.Bot import Bot
from Bots.Comando import Comando


class BotAlunoExausto(Bot):
    def __init__(self, nome):

        comandos = [
            Comando(1,"Qual o problema?",["Eu sinto que toda materia que curso no EaD eh desperdicada",
                                          "Meu semestre entrou em colpaso, eu perdi o controle",
                                          "Voce, voce eh o problema"]),
            Comando(2,"Por que voce ta tao cansado?",["Eu nao tenho mais relogio biologico, eu nao dormi direito",
                                                      "Eu mordi mais do que conseguia engolir, eu nunca paro de botar materia em dia"]),
            Comando(3,"Por que tu nao desiste?", ["Eu nao consigo, eu nao tenho coragem"]),
            Comando(4,"Por que tu nao pede ajuda?", ["Nao tenho tempo pra pedir ajuda", "Ego.", "Preguica, eu minto pra mim que vou desistir e nao faco, mas eu nao desisto"]),
            Comando(5,"Sempre foi assim?", ["Nao, antigamente eu tinha vontade de estudar trabalhar, eu nao sei o que aconteceu...",
                                            "Acho que depois da puberdade foi uma linha reta pro fundo do poco"])
        ]
        super().__init__(nome, comandos)

    def apresentacao(self):
        print("Ahn? oi, eh, so me diz que nao tem atividade pra fazer... Ah cara\n")

    def boas_vindas(self):
        print("Olha, aqui diz que eu tenho que falar boas vindas, mas por favor, me deixa ir embora")

    def despedida(self):
        print("Tchau, vou dormir")