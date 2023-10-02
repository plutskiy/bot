from telebot import types

homework = types.InlineKeyboardMarkup(row_width=2)
tekuchki = types.InlineKeyboardButton(text='Текучки', callback_data='tek')
tipovik = types.InlineKeyboardButton(text='Типовое ДЗ', callback_data='tip')
back = types.InlineKeyboardButton(text="Вернуться", callback_data='main_menu')
homework.add(tipovik, tekuchki)
homework.row(back)