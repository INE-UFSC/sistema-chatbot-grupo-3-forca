<<<<<<< HEAD
#from Bots.Botview import BotView
from Bots.DAO_bots import BotDAO
from Bots.Bot import Bot
=======
from Botview import BotView
from DAO_bots import BotDAO
from Bot import Bot
import PySimpleGUI as sg
from BotGrelletView import BotGrellertView 
>>>>>>> f63d18f7510674330b6c79740fc526fc13871572

class ControleBot:
    def __init__(self):
        #self.__telaBot = BotView()
        self.__BotDAO = BotDAO()
        self.__bot = ''
        self.__telaGrellert = BotGrellertView()

    def addBot(self,bot):
        self.__BotDAO.add(bot)

    def inicia(self):
<<<<<<< HEAD
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
=======
        self.__telaBot.tela_consulta()
        
        # Loop de eventos
        rodando = True
        resultado = ''
        telaGrellert = False
        while rodando:
            event, values = self.__telaBot.le_eventos()

            if event == sg.WIN_CLOSED:
                rodando = False

            elif event == 'Bot Grellert':
                #aqui ele espera do view qual o bot sera usado
                self.__bot = self.__BotDAO.get('Grellert')
                telaGrellert = True
                print('sim')

            elif event == 'Bot Tyska':
                self.__bot = self.__BotDAO.get('Tyska')

            elif event == 'Bot aluno exausto':
                self.__bot = self.__BotDAO.get('aluno')
        while telaGrellert:
            self.__telaGrellert.tela_consulta()
            event, values = self.__telaGrellert.le_eventos()

a = ControleBot()
a.inicia()
>>>>>>> f63d18f7510674330b6c79740fc526fc13871572
