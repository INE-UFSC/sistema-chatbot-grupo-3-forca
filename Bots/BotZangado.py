from Bots.Bot import Bot

class BotZangado(Bot):
    def __init__(self,nome):
        super().__init__(nome, comandos)
        comandos = {1 : ""}
    #nao esquecer o decorator
    @property
    def nome(self):
        return self.__nome

    #nao esquecer o decorator
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def apresentacao(self):
        stringa = "essa sema discutiremos algumas das minhas funcionalidades"
        stringb = "Olá todos e todas, sejam bem vindos ao chat bot do tyska,"
        normal = stringb + stringa
        print(normal)
 
    def mostra_comandos(self):
        
    
    def executa_comando(self,cmd):
        pass

    def boas_vindas(self):
        pass

    def despedida(self):
        pass