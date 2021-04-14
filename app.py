from Bots.Comando import Comando
from Bots.ControleBot import ControleBot
from Bots.Bot import Bot

comandosG = [
            Comando(1,"Professor, posso fazer individual? :(", ["Hahaha, jamais, o objetivo eh justamente aprender a trabalhar em grupo ;)"]),
            Comando(2,"Do que voce mais gosta? ",["I <3 Python", "Eu gosto muito de cafe", "Pronome neutro"]),
            Comando(3,"Voce gosta mais de software ou hardware?",["hardware sempre, tenho bom gosto"])

        ]
comandosA = [
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
comandosJ = [
            Comando(1, "O que voce acha mais importante na faculdade?", ["Para mim o importante he ter uma metodologia ativa sempre"]),
            Comando(2, "Qual o aspecto de um codigo orientado a objetos mais importante?", ["Um bom codigo eh um codigo bem abstrato com pouca rigidez."]),
            Comando(3, "O que vc gosta de fazer no seu tempo livre?", ["Fazer mais execicios para os alunos", "Treinar meu cachorro", "Ouvir um pagode"])

        ]


# bj = Bot("jonata","jonata",comandosJ)
# bg = Bot("grellet","grellet",comandosG)
# ba = Bot("aluno exausto","bernardo",comandosA)
# json.dump({"jojo":b1.encoded},open("bots.json","w"))

cb = ControleBot()
cb.inicia()
# cb.addBot(ba)
# cb.addBot(bg)
# cb.addBot(bj)
