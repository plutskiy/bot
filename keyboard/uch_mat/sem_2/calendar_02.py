from telebot import types

lst = types.InlineKeyboardMarkup(row_width=1)

dif = types.InlineKeyboardButton(
    text='Диффуры',
    url='https://disk.yandex.ru/d/M56ISnxt8gtr5/1%20курс/2%20семестр/СМ%2C%20РК4%2C%20ИУ10/Интегралы%20и%20диф.%20уравнения'
)

linal = types.InlineKeyboardButton(
    text='Линал',
    url='https://disk.yandex.ru/d/M56ISnxt8gtr5/1%20курс/2%20семестр/СМ%2C%20РК4%2C%20ИУ10/Линейная%20алгебра%20и%20ФНП')

physic = types.InlineKeyboardButton(
    text='Физика',
    url='http://fn.bmstu.ru/learning-work-fs-4/semester-2-fs-4'
)

back = types.InlineKeyboardButton(text='Вернуться', callback_data='uch_mat_02')
lst.add(dif, linal, physic)
lst.row(back)
