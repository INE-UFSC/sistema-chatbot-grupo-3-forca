#from Bots.Botview import BotView
from Bots.DAO_bots import BotDAO
from Bots.Bot import Bot

class ControleBot:
    def __init__(self):
        #self.__telaBot = BotView()
        self.__BotDAO = BotDAO()

    def addBot(self,bot):
        self.__BotDAO.add(bot)

    def inicia(self):
        #self.__telaCliente.tela_consulta()
        #CRIA TODOS OS BOTS SALVOS NO JSON
        lista_de_bots = []
        tipos_de_bots = self.__BotDAO.get_all()
        for tipo in tipos_de_bots:
            bot = Bot("tipo","nome",[])
            bot.decode(tipo,tipos_de_bots)
            lista_de_bots.append(bot)

        # PRINT DAS INFORMACOES DE TODOS OS BOTS P/ DEBUG
        # for bot in lista_de_bots:
        #     print(bot.tipo,bot.nome)
        #     for comando in bot.comandos:
        #         print(comando.msg,comando.respostas)


        # Loop de eventos
        # rodando = True
        # resultado = ''
        # while rodando:
        #     event, values = self.__telaBot.le_eventos()
