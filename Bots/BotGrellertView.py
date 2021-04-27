#from BotGrellert import BotGrellert as bg
import PySimpleGUI as sg

class BotGrellertView():
    def __init__(self):
        #self.__obj = bg('Grellert')
        self.__container = []
        self.__window = sg.Window("Bot Grellert", self.__container ,font=("Helvetica", 16))


    def tela_consulta(self):
        linha0 = [sg.Text('Pergunta para o professor:')]
        linha1 = [sg.Button('1'), sg.Text('Professor, posso fazer individual? ')]
        linha2 = [sg.Button('2'), sg.Text('Do que voce mais gosta?')]
        linha3 = [sg.Button('3'), sg.Text('Voce gosta mais de software ou hardware?')]
        linha4 = [sg.Text('Resposta do professor Grellert: ')]
        linha5 = [sg.Text("", size=(80,1), key= "resultado")]
        self.__container = [linha0, linha1, linha2, linha3, linha4, linha5]
        self.__window = sg.Window("Bot Grellert", self.__container ,font=("Helvetica", 16))
    
    def mostra_resultado(self, resultado):
        self.__window.Element('resultado').Update(resultado)
    
    def le_eventos(self):
        return self.__window.read()
    
    def fim(self):
        self.__window.close()