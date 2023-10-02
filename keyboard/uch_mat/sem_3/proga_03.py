from telebot import types

lst = types.InlineKeyboardMarkup(row_width=1)

AnsP = types.InlineKeyboardButton(
    text="Plutskiy",
    url="https://github.com/plutskiy/Proga"
)

AnsV = types.InlineKeyboardButton(
    text="Valzan",
    url="https://github.com/Valentin-Igrevsky/Basic_String"
)

AnsB = types.InlineKeyboardButton(
    text="Bebra",
    url="https://github.com/orgs/BebraHunters/repositories"
)

AnsNB = types.InlineKeyboardButton(
    text="NeBebra",
    url="https://github.com/orgs/NeBebraHunters/repositories"
)

back = types.InlineKeyboardButton(text='Вернуться', callback_data='uch_mat_03')
lst.add(AnsP, AnsV, AnsB, AnsNB)
lst.row(back)