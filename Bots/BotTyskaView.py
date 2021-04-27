import PySimpleGUI as sg

class BotTyskaView():
    def __init__(self):
        self.__container = []
        self.__window = sg.Window("Bot Tyska", self.__container ,font=("Helvetica", 16))


    def tela_consulta(self):
        linha0 = [sg.Text('Pergunta para o professor:')]
        linha1 = [sg.Button('1'), sg.Text('O que voce acha mais importante na faculdade?')]
        linha2 = [sg.Button('2'), sg.Text('Qual o aspecto de um codigo orientado a objetos mais importante?')]
        linha3 = [sg.Button('3'), sg.Text('O que vc gosta de fazer no seu tempo livre?')]
        linha4 = [sg.Text('Resposta do professor Tyska: ')]
        linha5 = [sg.Text("", size=(80,1), key= "resultado")]
        self.__container = [linha0, linha1, linha2, linha3, linha4, linha5]
        self.__window = sg.Window("Bot Grellert", self.__container ,font=("Helvetica", 16))
    
    def mostra_resultado(self, resultado):
        self.__window.Element('resultado').Update(resultado)
    
    def le_eventos(self):
        return self.__window.read()
    
    def fim(self):
        self.__window.close()