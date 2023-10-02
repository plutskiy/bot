from telebot import types

attend_cancel_menu = types.InlineKeyboardMarkup(row_width=1)
attend_button_cancel_enter = types.InlineKeyboardButton(text='Отмена', callback_data='attend_cnl_enter')
attend_cancel_menu.add(attend_button_cancel_enter)
