from telebot import types
from admins_id import current_sem, uch_mat_data, callback_text


def create_uch_mat_sem_list(num: str):
    sem_ID = int(num)
    buttons = []

    for callback in callback_text:
        if callback in uch_mat_data[sem_ID - 2]:
            buttons.append(
                types.InlineKeyboardButton(text=callback_text[callback][0], callback_data=f'{callback}_sem_{num}'))

    if num == current_sem:
        callback_data = 'main_menu'
        text = 'Вернуться'
    else:
        callback_data = 'semestr_menu'
        text = 'Выбор семестра'
    back = types.InlineKeyboardButton(text=text, callback_data=callback_data)

    buttons_list = [buttons[i:i + 2] for i in range(0, len(buttons), 2)]
    sem_list = types.InlineKeyboardMarkup(buttons_list)
    sem_list.row(back)
    return sem_list
