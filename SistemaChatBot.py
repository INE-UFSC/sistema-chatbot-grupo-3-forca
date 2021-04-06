from Bots.Bot import Bot
from time import sleep

class SistemaChatBot:
    def __init__(self,nomeEmpresa,lista_bots):
        self.__empresa = nomeEmpresa
        self.__lista_bots = []
        self.comando = 100
        ##verificar se a lista de bots contém apenas
        for bot in lista_bots:
            if isinstance(bot, Bot):
                self.__lista_bots.append(bot)
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
        i=0
        for bot in self.__lista_bots:
            i+=1
            print(str(i)+". "+bot.nome)
    
    def escolhe_bot(self):
        dados = int(input('Resposta: '))
        self.__bot = self.__lista_bots[dados-1]

    def mostra_comandos_bot(self):
        print('-'*20)
        print('Os comandos diposníveis são: ')
        listacom = self.__bot.mostra_comandos()
        for comando in listacom:
            print(comando.id, comando.msg)
        ##mostra os comandos disponíveis no bot escolhido

    def le_envia_comando(self):
        self.comando = input('Resposta: ')
        naoEhValido = False

        #Checagem se inteiro
        try: self.comando = int(self.comando)
        except:
            naoEhValido = True

        if self.comando > len(self.__bot.mostra_comandos()):
            naoEhValido = True

        #Tratamento de erro
        while naoEhValido:
            self.comando = input('Por favor, so numeros inteiros citados: ')
            try:
                self.comando = int(self.comando)
                if self.comando > len(self.__bot.mostra_comandos()):
                    pass
                else:
                    naoEhValido = False
            except:
                pass

        self.__bot.executa_comando(self.comando)
        sleep(2)
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
        self.mostra_comandos_bot()
        self.le_envia_comando()

        while self.comando != -1:
            self.mostra_comandos_bot()
            self.le_envia_comando()

        ##ao sair mostrar a mensagem de despedida do bot
        self.__bot.despedida()
