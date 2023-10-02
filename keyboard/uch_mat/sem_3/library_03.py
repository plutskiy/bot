from telebot import types

lst = types.InlineKeyboardMarkup(row_width=1)

proga_YA = types.InlineKeyboardButton(
    text="Основы Прогроммирования (Я)",
    url='https://disk.yandex.ru/d/MpL_crPwHbEkYg'
)

proga_GD = types.InlineKeyboardButton(
    text="Основы Прогроммирования (G)",
    url='https://drive.google.com/drive/folders/10RxD-f4e1cGWRyPluJUUSs-Me6nLbk_E?usp=share_link'
)

phys_labi_YA = types.InlineKeyboardButton(
    text='Решенные лабораторные работы по физике (Я)',
    url='https://disk.yandex.ru/d/HIJg_Gj34qeC9w'
)

phys_labi_GD = types.InlineKeyboardButton(
    text='Решенные лабораторные работы по физике (G)',
    url='https://drive.google.com/drive/folders/1sSAUy60RMyuKLtF3OX8-L3qUZpNJlNif?usp=sharing'
)

# ryad = types.InlineKeyboardButton(
#     text='Кратные интегралы',
#     url=''
# )

# FA = types.InlineKeyboardButton(
#     text='Функ. Анализ',
#     url=''
# )

physics = types.InlineKeyboardButton(
    text='Физика',
    url='https://disk.yandex.ru/d/Gyu8qoPNwgGMvQ'
)

eltech = types.InlineKeyboardButton(
    text='Разобранные задачи по электротехнике',
    url='https://drive.google.com/file/d/1zg_rItby4Utz-Ft6DQ4tzR5GOZ2lZPKk/view?usp=sharing'
)

back = types.InlineKeyboardButton(text="Вернуться", callback_data='uch_mat_03')

lst.add(proga_YA, proga_GD, physics, phys_labi_YA, phys_labi_GD, eltech)
lst.row(back)
