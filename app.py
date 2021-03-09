#encoding: utf-8
<<<<<<< HEAD
from SistemaChatBot import SistemaChatBot
from Bots.BotZangado import BotTyska
=======
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotZangado import BotZangado
>>>>>>> 786d7463b53b6e0d96ffbea17a2b1989581b34a7
from Bots.BotGrellet import BotGrellet

###construa a lista de bots disponíveis aqui
lista_bots = [BotTyska("Tyska"),BotGrellet("Grellet")]

sistema = SistemaChatBot("CrazyBots",lista_bots)
sistema.inicio()