from Bots.Bot import Bot

class BotTyska(Bot):
    def __init__(self,nome):
        comandos = {"O que você acha mais importante na faculdade?" : "Para mim o importante é ter uma metodologia ativa sempre", "Qual o aspecto de um código orientado a objetos mais importante?" : "Um bom código é um código bem abstrato com pouca rigidez."}
        super().__init__(nome, comandos)

    def apresentacao(self):
        print("Ola me escolham para participar de um método de aprendizado"
              "ativo e utilizarem diversas ferrramens da internet.")
 
    def mostra_comandos(self):
        i = 0
        for comando in self.comandos:
            i += 1
            print(str(i)+". "+comando+"\n")
    
    def executa_comando(self,cmd):
        i = 1
        for chave in self.comandos:
            if cmd == i:
                print(self.comandos[chave])
            i += 1

    def boas_vindas(self):
        stringa = "essa semana discutiremos algumas das minhas funcionalidades"
        stringb = "Olá todos e todas, sejam bem vindos ao chat bot do tyska,"
        normal = stringb + stringa
        print(normal)

    def despedida(self):
        print("Boa semana de estudos!!")