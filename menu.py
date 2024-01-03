from telebot import types

menu_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
menu_keyboard.row('/help', '/register', '/info')