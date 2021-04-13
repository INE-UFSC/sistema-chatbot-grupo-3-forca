class ControleBot:
    def __init__(self):
        self.__telaBot = BotView()
        self.__BotDAO = BotDAO()

    def inicia(self):
        self.__telaCliente.tela_consulta()
        
        # Loop de eventos
        rodando = True
        resultado = ''
        while rodando:
            event, values = self.__telaBot.le_eventos()
