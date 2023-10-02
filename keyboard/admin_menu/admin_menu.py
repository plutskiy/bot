from telebot import types

admin_menu = types.InlineKeyboardMarkup(row_width=1)
rk = types.InlineKeyboardButton(text='КР и РК', callback_data='ad_date')
tip = types.InlineKeyboardButton(text='Типовое ДЗ', callback_data='ad_tip')
tek = types.InlineKeyboardButton(text='Текущее ДЗ', callback_data='ad_tek')
admin_menu.add(tek, tip, rk)
