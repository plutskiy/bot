from telebot import types

tip_cancel = types.InlineKeyboardMarkup(row_width=1)
tip_button = types.InlineKeyboardButton(text='Отмена', callback_data='tip_cnl')
tip_cancel.add(tip_button)

tek_cancel = types.InlineKeyboardMarkup(row_width=1)
tek_button = types.InlineKeyboardButton(text='Отмена', callback_data='tek_cnl')
tek_cancel.add(tek_button)

rk_cancel = types.InlineKeyboardMarkup(row_width=1)
rk_button = types.InlineKeyboardButton(text='Отмена', callback_data='rk_cnl')
rk_cancel.add(rk_button)
