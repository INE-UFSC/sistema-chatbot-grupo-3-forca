import PySimpleGUI as sg

class BotView:
    def __init__(self, ):
        self.__container []
        self.__window = sg.Window("SistemaChatBot", self.__container ,font=("Helvetica", 16))


    def tela_consulta(self):
        linha0 = [sg.Text('Escolha um Bot')]
        linha1 = [sg.Button('Importar')]
        self.__container = [linha0, linha1]
    
    def mostra_resultado(self, resultado):
        self.__Element('NAO SEI O QUE É AQUI').Update(restultado)
    
    def le_eventos(self):
        return self.__window.read()
    
    def fim(self):
        self.__window.close()
