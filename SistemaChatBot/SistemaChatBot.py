from Bots.Bot import Bot

class SistemaChatBot:
    def __init__(self,nomeEmpresa,lista_bots):
        self.__empresa = nomeEmpresa
        ##verificar se a lista de bots contém apenas
        if isinstance(lista_bots, Bot):
            self.__lista_bots=lista_bots
        self.__bot = None
    
    @property
    def empresa(self):
        return self.__empresa
    @property
    def lista_bots(self):
        return self.__lista_bots
    @property
    def bot(self):
        return self.__bot

    def boas_vindas(self):
        print('Seja bem vindo os sistema Chatbots do Tyska e do Mateus!')
        ##mostra mensagem de boas vindas do sistema

    def mostra_menu(self):
        print('Qual bot você deseja? ')
        print('1. Bot Matheus')
        print('2. Bot Jonata')
        ##mostra o menu de escolha de bots
    
    def escolhe_bot(self):
        dados = input('Resposta: ')
        if dados == '1':
            self.__bot = BotTyska()
        elif dados == '2':
            self.__bot = BotGrellert()

        ##faz a entrada de dados do usuário e atribui o objeto ao atributo __bot

    def mostra_comandos_bot(self):
        print('Os comandos diposníveis são: ')
        self.__bot.mostra_comandos()
        ##mostra os comandos disponíveis no bot escolhido

    def le_envia_comando(self):
        self.comando = input('Resposta: ').lower()
        self.__bot.executa_comados(self.comando)
        ##faz a entrada de dados do usuário e executa o comando no bot ativo

    def inicio(self):
        ##mostra mensagem de boas-vindas do sistema
        self.boas_vindas()
        ##mostra o menu ao usuário
        self.mostra_menu()
        ##escolha do bot
        self.escolhe_bot()
        ##mostra mensagens de boas-vindas do bot escolhido
        self.__bot.boas_vindas()
        ##entra no loop de mostrar comandos do bot e escolher comando do bot até o usuário definir a saída
        while True:
            if self.comando != '':
                print('Por favor, escolha um comando!')
                print('-'*20)
                self.mostra_comandos_bot()
                self.le_envia_comando()

        ##ao sair mostrar a mensagem de despedida do bot
        self.__bot.despedida()
