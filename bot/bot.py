import telebot
import time
from Facade import BotFacade

facade = BotFacade()
bot = facade.getBot()

@bot.message_handler(commands = ['start'])
def send_welcome(message):
    bot.reply_to(message, 'Welcome!')

if __name__ == '__main__':
    facade.startBot()
