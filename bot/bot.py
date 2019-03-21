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

@bot.message_handler(commands = ['start'])
def send_welcome(message):
    botMessage = 'Welcome!\nType /help for more information.'
    bot.send_message(message.chat.id, botMessage)
    show_start(message.chat.id)

@bot.message_handler(func = lambda message : message.text == 'ATM')
def send_atm(message):
    show_atm(message.chat.id)

@bot.message_handler(func = lambda message : message.text == 'Check')
def send_check(message):
    botMessage = atmIn.analyze()+"\n"+atmOut.analyze()
    bot.send_message(message.chat.id, botMessage)
    show_check(message.chat.id)

@bot.message_handler(func = lambda message : message.text == 'Update')
def send_update(message):
    show_update(message.chat.id)

@bot.message_handler(func = lambda message : message.text == 'ATM in SDU' or 
                                             message.text == 'ATM outside SDU')
def send_workingUpdate(message):    
    if message.text == 'ATM in SDU':
        atmIn.setGonnaUpdate(True)
    else:
        atmOut.setGonnaUpdate(True)
    show_workingUpdate(message.chat.id)

@bot.message_handler(func = lambda message : message.text == 'Yes' or
                                             message.text == 'No')
def send_workingUpdate(message):    
    if message.text == 'Yes':
        if atmIn.isGonnaUpdate():
            atmIn.countYes()
        else:
            atmOut.countYes()
        show_billsUpdate(message.chat.id)
    else:
        if atmIn.isGonnaUpdate():
            atmIn.countNo()
        else:
            atmOut.countNo()
        send_back(message)

@bot.message_handler(func = lambda message : message.text == '1000' or
                                             message.text == '2000' or
                                             message.text == '5000')
def send_billsUpdate(message):
    if atmIn.isGonnaUpdate():
        atmIn.setMinBill(message.text)
        atmIn.setGonnaUpdate(False)
    else:
        atmOut.setMinBill(message.text)
        atmOut.setGonnaUpdate(False)
    send_back(message)
@bot.message_handler(func = lambda message: message.text == 'Back' or 
                                            message.text == 'Exit')
def send_back(message):
    botMessage = "Thank you for using our service!\n"
    botMessage = botMessage + "Press Check or Update next time you use our bot!"
    bot.send_message(message.chat.id, botMessage)
    show_atm(message.chat.id)

def show_start(chat_id):
    keyboard = Keyboard()
    keyboard.addButtons(["ATM"])
    keyboard.setRowWidth(1)
    botMessage = "Press ATM"
    bot.send_message(chat_id, botMessage, reply_markup=keyboard.getResult())

def show_atm(chat_id):
    keyboard = Keyboard()
    keyboard.addButtons(["Check", "Update"])
    botMessage = "What you want to do with ATM status?"
    bot.send_message(chat_id, botMessage, reply_markup=keyboard.getResult())

def show_check(chat_id):
    keyboard = Keyboard()
    keyboard.addButtons(["Update", "Exit"])
    botMessage = "What you want to do next?"
    bot.send_message(chat_id, botMessage, reply_markup=keyboard.getResult())

def show_update(chat_id):
    keyboard = Keyboard()
    keyboard.addButtons([atmIn.getLocation(), atmOut.getLocation()])
    botMessage = "Which ATM's status you want to update?"
    bot.send_message(chat_id, botMessage, reply_markup=keyboard.getResult())

def show_workingUpdate(chat_id):
    keyboard = Keyboard()
    keyboard.addButtons(["Yes", "No"])
    botMessage = "Does it work?"
    bot.send_message(chat_id, botMessage, reply_markup=keyboard.getResult())

def show_billsUpdate(chat_id):
    keyboard = Keyboard()
    keyboard.addButtons(["1000", "2000", "5000", "Back"])
    botMessage = "What is the minimum bill you got from ATM?\n"
    botMessage = botMessage + "If you didn't get any cash, press Back button"  
    bot.send_message(chat_id, botMessage, reply_markup=keyboard.getResult())

if __name__ == '__main__':
    facade.startBot()
