#encoding: utf-8

from SistemaChatBot import SistemaChatBot
from Bots.BotZangado import BotTyska
from Bots.BotGrellet import BotGrellet
from Bots.BotAlunoExausto import BotAlunoExausto

###construa a lista de bots disponíveis aqui
lista_bots = [BotAlunoExausto("Bernardo")]

sistema = SistemaChatBot("CrazyBots",lista_bots)
sistema.inicio()