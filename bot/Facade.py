import telebot

class _Bot(object):
    def __init__(self):
        self.bot = telebot.TeleBot(
            "701028435:AAHhV1pODQEf6eaMZvcGk_uuAOYMz6fGtGQ")

    def startPolling(self):
        self.bot.polling()

    def getBot(self):
        return self.bot

class BotFacade(object):
    def __init__(self):
        self.bot = _Bot()

    def startBot(self):
        self.bot.startPolling()

    def getBot(self):
        return self.bot.getBot()
