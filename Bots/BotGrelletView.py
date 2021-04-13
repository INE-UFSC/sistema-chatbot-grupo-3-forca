from BotGrellet import BotGrellet as bg
import PySimpleGUI as sg

class BotGrellertView():
    def __init__(self):
        self.__obj = bg('Grellert')
        self.__container = []
        self.__window = sg.Window("Bot Grellert", self.__container ,font=("Helvetica", 16))


    def tela_consulta(self):
        linha0 = [sg.Text(bg.apresentacao())]
        self.__container = [linha0]
        self.__window = sg.Window("Bot Grellert", self.__container ,font=("Helvetica", 16))
    
    def mostra_resultado(self, resultado):
        self.__Element('NAO SEI O QUE É AQUI').Update(restultado)
    
    def le_eventos(self):
        return self.__window.read()
    
    def fim(self):
        self.__window.close()