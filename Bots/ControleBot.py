from Botview import BotView
from BotGrellertView import BotGrellertView
from BotTyskaView import BotTyskaView
from DAO_bots import BotDAO
import PySimpleGUI as sg
from bot import Bot

class ControleBot:
    def __init__(self):
        self.__telaBot = BotView()
        self.__telaGrellert = BotGrellertView()
        self.__telaTyska = BotTyskaView()
        self.__BotDAO = BotDAO()
        self.__bot = "0"

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
        container = self.__telaBot.tela_consulta()
        rodando = True
        resultado = ''
        grellert_activate = False
        tyska_activate = False
        while rodando:
            if grellert_activate == True:
                grellert_activate = self.handle_grellert()

            elif tyska_activate == True:
                tyska_activate = self.handle_tyska()
            
            else:
                event, values = self.__telaBot.le_eventos() 
                if event == sg.WIN_CLOSED:
                    rodando = False
                elif event == 'Bot Grellert':
                    grellert_activate = True
                elif event == 'Bot Tyska':
                    tyska_activate = True
                elif event == 'Bot aluno exausto':
                    pass
                elif event == 'importar':
                    pass
                else:
                    pass

        self.__telaBot.fim()

    def handle_grellert(self):
        self.__telaGrellert.tela_consulta()
        event_grellert, values = self.__telaGrellert.le_eventos()
        #print(values)
        rodando = True
        
        while rodando:
            if event_grellert == sg.WIN_CLOSED:
                self.__telaGrellert.fim()
                    
            elif event_grellert == '1':
                self.__telaGrellert.mostra_resultado('Hahaha, jamais, o objetivo eh justamente aprender a trabalhar em grupo ;)')
                grellert_activate = False
                return grellert_activate

            elif event_grellert == '2': 
                self.__telaGrellert.mostra_resultado('I <3 Python')
                grellert_activate = False
                return grellert_activate
                    
            elif event_grellert == '3':
                self.__telaGrellert.mostra_resultado('"hardware sempre, tenho bom gosto"')
                grellert_activate = False
                return grellert_activate

    def handle_tyska(self):
        self.__telaTyska.tela_consulta()
        event_tyska, values = self.__telaTyska.le_eventos()
        #print(values)
        rodando = True
        
        while rodando:
            if event_tyska == sg.WIN_CLOSED:
                self.__telatyska.fim()
                    
            elif event_tyska == '1':
                self.__telaTyska.mostra_resultado('Para mim o importante he ter uma metodologia ativa sempre')
                tyska_activate = False
                return tyska_activate

            elif event_tyska == '2': 
                self.__telaTyska.mostra_resultado('Um bom codigo eh um codigo bem abstrato com pouca rigidez.')
                tyska_activate = False
                return tyska_activate
                    
            elif event_tyska == '3':
                self.__telaTyska.mostra_resultado('Fazer mais execicios para os alunos')
                tyska_activate = False
                return tyska_activate
