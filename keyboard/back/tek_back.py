from telebot import types

tek_back = types.InlineKeyboardMarkup()
button = types.InlineKeyboardButton(text='Вернуться', callback_data='tek')
tek_back.add(button)