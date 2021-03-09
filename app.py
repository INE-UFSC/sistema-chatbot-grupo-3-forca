#encoding: utf-8
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotZangado import BotZangado
from Bots.BotGrellet import BotGrellet

###construa a lista de bots disponíveis aqui
lista_bots = [BotTyska("Tyska"),BotGrellet("Grellet")]

sistema = scb.SistemaChatBot("CrazyBots",lista_bots)
sistema.inicio()