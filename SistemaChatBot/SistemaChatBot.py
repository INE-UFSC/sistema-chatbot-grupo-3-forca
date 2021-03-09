from Bots.Bot import Bot


print('teste')
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
        print('Seja bem vindo!')
        ##mostra mensagem de boas vindas do sistema

    def mostra_menu(self):
        print('Qual bot você deseja? '))
        print('1. Bot Matheus')
        print('2. Bot Jonata')
        ##mostra o menu de escolha de bots
    
    def escolhe_bot(self, dados):
        self.__bot = dados
        ##faz a entrada de dados do usuário e atribui o objeto ao atributo __bot
    def mostra_comandos_bot(self):
        for i in self.__bot.comandos:
            print('Os comandos diposníveis são: ')
            print(f' {i}')

        ##mostra os comandos disponíveis no bot escolhido

    def le_envia_comando(self):
        pass
        ##faz a entrada de dados do usuário e executa o comando no bot ativo

    def inicio(self):
        pass
        ##mostra mensagem de boas-vindas do sistema
        ##mostra o menu ao usuário
        ##escolha do bot      
        ##mostra mensagens de boas-vindas do bot escolhido
        ##entra no loop de mostrar comandos do bot e escolher comando do bot até o usuário definir a saída
        ##ao sair mostrar a mensagem de despedida do bot
