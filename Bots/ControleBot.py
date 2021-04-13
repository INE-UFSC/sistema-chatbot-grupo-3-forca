from Botview import BotView
from DAO_bots import BotDAO
from Bot import Bot
import PySimpleGUI as sg

class ControleBot:
    def __init__(self):
        self.__telaBot = BotView()
        self.__BotDAO = BotDAO()
        self.__bot = ''

    def inicia(self):
        self.__telaBot.tela_consulta()
        
        # Loop de eventos
        rodando = True
        resultado = ''
        while rodando:
            event, values = self.__telaBot.le_eventos()

            if event == sg.WIN_CLOSED:
                rodando = False

            elif event == 'Bot Grellert':
                #aqui ele espera do view qual o bot sera usado
                self.__bot = 'Grellert'
                print(self.__bot)

a = ControleBot()
a.inicia()
