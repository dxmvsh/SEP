import telebot
import time
from Facade import BotFacade
from Keyboard import Keyboard

facade = BotFacade()
bot = facade.getBot()

@bot.message_handler(commands = ['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Welcome!\nType /help for more information.')
    show_start(message.chat.id)

@bot.message_handler(func = lambda message : "ATM")
def echo_all(message):
    show_atm(message.chat.id)

@bot.message_handler(func = lambda message : "Check")
def echo_all(message):
    show_atm(message.chat.id)


def show_start(chat_id):
    keyboard = Keyboard()
    keyboard.addButtons(["ATM"])
    keyboard.setOneTimeKeyboard(True)
    keyboard.setRowWidth(1)
    keyboard.shouldKeyboardBeResized(True)
    bot.send_message(chat_id, "Choose the button", reply_markup=keyboard.getResult())

def show_atm(chat_id):
    keyboard = Keyboard()
    keyboard.addButtons(["Check", "Update"])
    keyboard.setOneTimeKeyboard(True)
    keyboard.setRowWidth(2)
    keyboard.shouldKeyboardBeResized(True)
    bot.send_message(chat_id, "Choose the button", reply_markup=keyboard.getResult())

if __name__ == '__main__':
    facade.startBot()
