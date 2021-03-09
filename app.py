#encoding: utf-8
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotZangado import BotZangado

###construa a lista de bots disponíveis aqui
lista_bots = [BotTyska("Tyska")]

sistema = scb.SistemaChatBot("CrazyBots",lista_bots)
sistema.inicio()