from telebot import types

back = types.InlineKeyboardMarkup()
button = types.InlineKeyboardButton(text='Вернуться', callback_data='main_menu')
back.add(button)
