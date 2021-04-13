from Botview import BotView
from DAO_bots import BotDAO
from Bot import Bot
import PySimpleGUI as sg
from BotGrelletView import BotGrellertView 

class ControleBot:
    def __init__(self):
        self.__telaBot = BotView()
        self.__BotDAO = BotDAO()
        self.__bot = ''
        self.__telaGrellert = BotGrellertView()

    def inicia(self):
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
