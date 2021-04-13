import PySimpleGUI as sg

class BotView:
<<<<<<< HEAD
    def __init__(self, ):
=======
    def __init__(self):
>>>>>>> f63d18f7510674330b6c79740fc526fc13871572
        self.__container = []
        self.__window = sg.Window("SistemaChatBot", self.__container ,font=("Helvetica", 16))


    def tela_consulta(self):
        linha0 = [sg.Text('Escolha um Bot')]
        linha1 = [sg.Button('Bot Grellert'), sg.Button('Bot Tyska'),sg.Button('Bot aluno exausto')]
        linha2 = [sg.Button('Importar'), sg.Button('Exportar')]
        self.__container = [linha0, linha1, linha2]
        self.__window = sg.Window("SistemaChatBot", self.__container ,font=("Helvetica", 16))
    
    def mostra_resultado(self, resultado):
        self.__Element('NAO SEI O QUE É AQUI').Update(restultado)
    
    def le_eventos(self):
        return self.__window.read()
    
    def fim(self):
        self.__window.close()

