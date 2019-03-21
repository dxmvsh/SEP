from telebot import types

class Keyboard(object):
    def __init__(self):
        self.rowWidth = 2
        self.resizeKeyboard = True
        self.isOneTimeKeyboard = True

    def addButtons(self, texts):
        self.texts = texts

    def setRowWidth(self, width):
        self.rowWidth = width

    def setOneTimeKeyboard(self, isOneTimeKeyboard):
        self.isOneTimeKeyboard = isOneTimeKeyboard

    def shouldKeyboardBeResized(self, shouldKeyboardBeResized):
        self.resizeKeyboard = shouldKeyboardBeResized

    def getResult(self):
        markup = types.ReplyKeyboardMarkup(row_width=self.rowWidth,
                                           resize_keyboard=self.resizeKeyboard,
                                           one_time_keyboard=self.isOneTimeKeyboard)
        for text in self.texts:
            markup.add(types.KeyboardButton(text))

        return markup
