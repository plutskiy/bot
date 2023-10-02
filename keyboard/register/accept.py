from telebot import types


def accept_for(id, name, username):
    text = f'<a href="https://t.me/{username}">{name}</a> запрашивает доступ к боту\n'
    text += f'ID пользователя: <span class="tg-spoiler">{id}</span>'
    return text

def tmp_accept_for(id, name, username):
    text = f'Временная регистрация: <a href="https://t.me/{username}">{name}</a>\n'
    text += f'ID пользователя: <code>{id}</code>'
    return text

def accepted(id, name, username, callback):
    callback_text = {'accept': 'РАЗРЕШИЛИ', 'reject': 'ЗАПРЕТИЛИ', 'add': 'ВЫДАЛИ'}

    text = f'Вы <b>{callback_text[callback]}</b> <a href="https://t.me/{username}">{name}</a> доступ к боту\n'
    text += f'ID пользователя: <span class="tg-spoiler">{id}</span>'
    return text


def accept_menu(id, name, username):
    data = f'ID:{id}_NM:{name}_UN:{username}'
    accept_menu = types.InlineKeyboardMarkup(row_width=1)
    accept_button = types.InlineKeyboardButton(text='Дать доступ', callback_data=f'rg_accept_{data}')
    reject_button = types.InlineKeyboardButton(text='Отклонить', callback_data=f'rg_reject_{data}')
    accept_menu.add(accept_button, reject_button)
    return accept_menu
