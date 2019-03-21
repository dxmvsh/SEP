import telebot
import time
from Facade import BotFacade
from Keyboard import Keyboard
from ATMBot import ATMBot

facade = BotFacade()
bot = facade.getBot()
atmIn = ATMBot()
atmOut = ATMBot()
atmIn.setLocation("ATM in SDU")
atmOut.setLocation("ATM outside SDU")
updatingATM = ""

@bot.message_handler(commands = ['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Welcome!\nType /help for more information.')
    show_start(message.chat.id)

@bot.message_handler(func = lambda message : message.text == 'ATM')
def send_atm(message):
    show_atm(message.chat.id)

@bot.message_handler(func = lambda message : message.text == 'Check')
def send_check(message):
    bot.send_message(message.chat.id, atmIn.analyze()+"\n"+atmOut.analyze())

@bot.message_handler(func = lambda message : message.text == 'Update')
def send_update(message):
    show_update(message.chat.id)

@bot.message_handler(func = lambda message : message.text == 'ATM in SDU' or 
                                             message.text == 'ATM outside SDU')
def send_workingUpdate(message):    
    updatingATM = message.text
    show_workingUpdate(message.chat.id)

@bot.message_handler(func = lambda message : message.text == 'Yes' or
                                             message.text == 'No')
def send_workingUpdate(message):    
    if message.text == 'Yes':
        if updatingATM == 'ATM in SDU':
            atmIn.countYes()
        else:
            atmOut.countYes()
    else:
        if updatingATM == 'ATM in SDU':
            atmIn.countNo()
        else:
            atmOut.countNo()

    show_workingUpdate(message.chat.id)

def show_start(chat_id):
    keyboard = Keyboard()
    keyboard.addButtons(["ATM"])
    keyboard.setRowWidth(1)
    bot.send_message(chat_id, "Press ATM", reply_markup=keyboard.getResult())

def show_atm(chat_id):
    keyboard = Keyboard()
    keyboard.addButtons(["Check", "Update"])
    bot.send_message(chat_id, "What you want to do with ATM status?"
                            , reply_markup=keyboard.getResult())

def show_check(chat_id):
    keyboard = Keyboard()
    keyboard.addButtons(["Update", "Exit"])
    bot.send_message(chat_id, "What you want to do next?"
                            , reply_markup=keyboard.getResult())

def show_update(chat_id):
    keyboard = Keyboard()
    keyboard.addButtons([atmIn.getLocation(), atmOut.getLocation()])
    bot.send_message(chat_id, "Which ATM's status you want to update?"
                            , reply_markup=keyboard.getResult())

def show_workingUpdate(chat_id):
    keyboard = Keyboard()
    keyboard.addButtons(["Yes", "No"])
    bot.send_message(chat_id, "Does it work?"
                            , reply_markup=keyboard.getResult())
    
if __name__ == '__main__':
    facade.startBot()
