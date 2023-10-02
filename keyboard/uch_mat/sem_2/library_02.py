from telebot import types

lst = types.InlineKeyboardMarkup(row_width=1)

his = types.InlineKeyboardButton(
    text='История',
    url='https://drive.google.com/file/d/1sS8Rcu-EeyuV9sPp8DGxeoU1XZlk-w-d/view?usp=share_link'
)
proga = types.InlineKeyboardButton(
    text="Основы Прогроммирования",
    url='https://drive.google.com/drive/folders/10RxD-f4e1cGWRyPluJUUSs-Me6nLbk_E?usp=share_link'
)
labi = types.InlineKeyboardButton(
    text='Решенные лабораторные работы по физике',
    url='https://disk.yandex.ru/d/H4JIwCch3Diezg'
)

motis = types.InlineKeyboardButton(
    text='МОТИС',
    url='https://disk.yandex.ru/d/nDBaBK2wjJU7Fg'
)

dif = types.InlineKeyboardButton(
    text='Диффуры',
    url='https://drive.google.com/drive/folders/1MhaPK4VsoRYF_KQE5S690v5hh5PiB5rQ'
)

linal = types.InlineKeyboardButton(
    text='Линал',
    url='https://drive.google.com/drive/folders/181utKnDPo_g6i1mUZqRtprs4rb24AV4q'
)

answ = types.InlineKeyboardButton(
    text="Ответы по проге",
    url="https://github.com/plutskiy/Proga"
)

physics = types.InlineKeyboardButton(
    text='Физика',
    url='https://disk.yandex.ru/d/R37X2b-xewKnUw'
)

back = types.InlineKeyboardButton(text="Вернуться", callback_data='uch_mat_02')

lst.add(dif, his, labi, linal, motis, answ, proga, physics)
lst.row(back)
