from telebot import types
from admins_id import ad_tip_dz

buttons = list()

for subject in ad_tip_dz:
    buttons.append(
        types.InlineKeyboardButton(text=ad_tip_dz[subject][0], callback_data=f'mm_tip_{subject}'))

back = types.InlineKeyboardButton(text='Вернуться', callback_data='hw')

buttons_list = [buttons[i:i + 2] for i in range(0, len(buttons), 2)]
homework = types.InlineKeyboardMarkup(buttons_list)
homework.row(back)
