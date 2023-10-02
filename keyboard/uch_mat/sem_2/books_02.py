from telebot import types

lst = types.InlineKeyboardMarkup(row_width=1)
sbornik = types.InlineKeyboardButton(
    text='Задачник для ВТУЗОВ',
    url='https://drive.google.com/file/d/1oarasDzMnua8JpjjdJUd-19Aw2kqpmTV/view?usp=share_link'
)

popov = types.InlineKeyboardButton(
    text='Учебник Поповича',
    url='https://drive.google.com/file/d/1UUWcmR_XN0VkRyT5p1Ftf3TR40eZVcvd/view?usp=share_link'
)

en = types.InlineKeyboardButton(
    text='Учебник по английскому',
    url='https://drive.google.com/file/d/1jp_Cyizvvbsxlm7PJ2L1UlDjnZFmCqjB/view?usp=share_link'
)

his_book = types.InlineKeyboardButton(
    text='Учебник по истории',
    url='https://docs.google.com/viewer?a=v&pid=sites&srcid=ZGVmYXVsdGRvbWFpbnxoaXN0b3J5OTkwMDk5MDA5OTAwfGd4OjFlZmQxY2RlODJkY2JhOTk'
)

physics_metodichki = types.InlineKeyboardButton(
    text='Методички по физике',
    url='http://fn.bmstu.ru/learning-work-fs-4/45-sem2/154-phys-labs-sem2?'
)

back = types.InlineKeyboardButton(text='Вернуться', callback_data='uch_mat_02')

lst.add(sbornik, en, his_book, popov, physics_metodichki)
lst.row(back)
