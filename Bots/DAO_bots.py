import json
from DAO import DAO
from Bot import Bot

class BotDAO(DAO):
    def __init__(self):
        super().__init__('clientes.json')

    def add(self, bot: Bot):
        if (bot is not None) and (isinstance(bot, Bot)):
            if isinstance(bot.nome, str):
                super().add(bot.nome, bot)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)
