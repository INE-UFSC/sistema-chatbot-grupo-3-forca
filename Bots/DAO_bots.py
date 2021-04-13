import json
from DAO import DAO
from Bot import Bot

class ClienteDAO(DAO):
    def __init__(self):
        super().__init__('clientes.json')

    def add(self, bot: Bot):
        if (bot is not None) and (isinstance(bot, Bot)):
            if isinstance(bot.codigo, int):
                super().add(bot.codigo, bot)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)
