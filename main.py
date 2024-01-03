import telebot
from menu import menu_keyboard

bot = telebot.TeleBot('6711309319:AAEgBRjAlC8HkAuf0z_XQIQ1SOoT2UZFjqc')


bot_data = {}

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    bot.send_message(user_id, 'Hello! Welcome to register bot', reply_markup=menu_keyboard)

@bot.message_handler(commands=['help'])
def help_command(message):
    user_id = message.from_user.id
    bot.send_message(user_id, 'Commands\n'
                     '/start for start bot\n'
                     '/help to show all commands\n'
                     '/help_me to contact us\n'
                     '/register to registration', reply_markup=menu_keyboard)


@bot.message_handler(commands=['help_me'])
def help_me(message):
    user_id = message.from_user.id
    bot.send_message(user_id, 'Admin: @AADEMAN\n'
                     'Phon number: +9989100XXXXX\n'
                     'E-mail: dxxxxxxxxx@gmail.com', reply_markup=menu_keyboard)


@bot.message_handler(commands=['register'])
def register(message):
    user_id = message.from_user.id
    bot.send_message(user_id, 'Please enter your name: ', reply_markup=menu_keyboard)
    bot.register_next_step_handler(message, regist)


def regist(message):
    user_id = message.from_user.id
    bot_data[user_id] = {'name': message.text, 'location': None}
    bot.send_message(user_id, 'Name added! Now, please share your location:', reply_markup=menu_keyboard)
    bot.register_next_step_handler(message, regist_location)


def regist_location(message):
    user_id = message.from_user.id
    location = message.location
    bot_data[user_id]['location'] = location
    bot.send_message(user_id, 'Location added! Registration complete.\n'
                              'If you want to see info, please use the /info command', reply_markup=menu_keyboard)


@bot.message_handler(commands=['info'])
def info_user(message):
    user_id = message.from_user.id
    if user_id in bot_data:
        bot.send_message(user_id, f'Name: {bot_data[user_id]['name']}\n'
                         f'Location: {bot_data[user_id]['location'].latitude},'
                                  f' {bot_data[user_id]['location'].longitude}', reply_markup=menu_keyboard)
    else:
        bot.send_message(user_id, 'You not registered yet!', reply_markup=menu_keyboard)


bot.polling(non_stop=True)









