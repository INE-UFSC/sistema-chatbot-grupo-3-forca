import PySimpleGUI as sg

class BotView:
    def __init__(self, ):
        self.__container = []
        self.__window = sg.Window("SistemaChatBot", self.__container ,font=("Helvetica", 16))


    def tela_consulta(self):
        linha0 = [sg.Text('Escolha um Bot')]
        linha1 = [sg.Button('Bot Grellert'), sg.Button('Bot Tyska'),sg.Button('Bot aluno exausto')]
        linha2 = [sg.Button('Importar'), sg.Button('Exportar')]
        self.__container = [linha0, linha1, linha2]
        self.__window = sg.Window("SistemaChatBot", self.__container ,font=("Helvetica", 16))
    
    def mostra_resultado(self, resultado):
        self.__Element('resultado').Update(restultado)
    
    def le_eventos(self):
        return self.__window.read()
    
    def fim(self):
        self.__window.close()

