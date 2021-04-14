import json
from Bots.DAO import DAO
from Bots.Bot import Bot

class BotDAO(DAO):
    def __init__(self):
        super().__init__('bots.json')

    def add(self, bot: Bot):
        if (bot is not None) and (isinstance(bot, Bot)):
            if isinstance(bot, Bot):
                super().add(bot.tipo, bot)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)

