from telebot import types
from admins_id import current_sem

sem_menu = types.InlineKeyboardMarkup(row_width=1)
for i in range(2, int(current_sem)):
    num = str(i)
    if i < 10:
        num = '0' + str(i)
    sem_menu.add(types.InlineKeyboardButton(f'{i} СЕМЕСТР', callback_data=f'uch_mat_{num}'))
sem_menu.add(types.InlineKeyboardButton(f'{int(current_sem)} СЕМЕСТР\n(текущий)', callback_data=f'main_menu'))
