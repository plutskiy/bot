from telebot import types

tip_back = types.InlineKeyboardMarkup()
button = types.InlineKeyboardButton(text='Вернуться', callback_data='tip')
tip_back.add(button)