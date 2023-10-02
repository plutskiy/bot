from telebot import types

lst = types.InlineKeyboardMarkup(row_width=1)

ryad = types.InlineKeyboardButton(
    text='Кратные интегралы',
    url='https://disk.yandex.ru/d/M56ISnxt8gtr5/2%20%D0%BA%D1%83%D1%80%D1%81/3%20%D1%81%D0%B5%D0%BC%D0%B5%D1%81%D1%82%D1%80/%D0%A1%D0%9C%2C%20%D0%98%D0%A310/%D0%9A%D1%80%D0%B0%D1%82%D0%BD%D1%8B%D0%B5%20%D0%B8%D0%BD%D1%82%D0%B5%D0%B3%D1%80%D0%B0%D0%BB%D1%8B%2C%20%D1%82%D0%B5%D0%BE%D1%80%D0%B8%D1%8F%20%D0%BF%D0%BE%D0%BB%D1%8F%2C%20%D1%80%D1%8F%D0%B4%D1%8B%20(%D1%81%D0%BF%D0%B5%D1%86%D0%B8%D0%B0%D0%BB%D0%B8%D1%81%D1%82%D1%8B)'
)

FA = types.InlineKeyboardButton(
    text='Функ. Анализ',
    url='https://drive.google.com/drive/folders/13mzrVi5xLZ4-3ZJUilFyq8Gvis35Tine?usp=drive_link'
)

physic = types.InlineKeyboardButton(
    text='Физика',
    url='http://fn.bmstu.ru/learning-work-fs-4/learning-semestr-3-fs-4'
)

back = types.InlineKeyboardButton(text='Вернуться', callback_data='uch_mat_03')
lst.add(ryad, FA, physic)
lst.row(back)
