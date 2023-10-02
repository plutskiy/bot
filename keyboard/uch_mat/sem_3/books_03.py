from telebot import types

lst = types.InlineKeyboardMarkup(row_width=1)

sbornik = types.InlineKeyboardButton(
    text='Задачник для ВТУЗОВ',
    url='https://drive.google.com/file/d/1c2XV3DOx-Wt670uYpLRExMeBWru6kcWI/view?usp=drive_link'
)

en = types.InlineKeyboardButton(
    text='Учебник по английскому',
    url='https://drive.google.com/file/d/1TnHaxHz3zTHGmtU4e4dTvoRcGYZut2L2/view?usp=drive_link'
)

physics_metodichki = types.InlineKeyboardButton(
    text='Методички по физике',
    url='http://fn.bmstu.ru/learning-work-fs-4/46-sem3/155-phys-labs-sem3?'
)

physics_ucheb = types.InlineKeyboardButton(
    text='Задачник по физике',
    url='https://drive.google.com/file/d/1uidee4t0CjxxZ60VianesrLPCw00T4cn/view?usp=drive_link'
)

FA = types.InlineKeyboardButton(
    text='Справочник по ФА',
    url='https://drive.google.com/file/d/1QM_0pHL6ZjzMBRJOdw9C7XkZtZ8KbUQb/view?usp=drive_link'
)

eltech_labi = types.InlineKeyboardButton(
    text='Лабы по электротехнике',
    url='http://fn.bmstu.ru/learning-work-fs-7/laboratory-works-fs-7'
)

eltech_metodichki = types.InlineKeyboardButton(
    text='Методички по электротехнике',
    url='http://fn.bmstu.ru/learning-work-fs-7/methodical-materials-fs-ru'
)


eltech_ucheb = types.InlineKeyboardButton(
    text='Учебники по электротехнике',
    url='https://drive.google.com/drive/folders/13Sx79ceD_L8-n_HyB2k2-dFLgg-yH-rI?usp=drive_link'
)

back = types.InlineKeyboardButton(text='Вернуться', callback_data='uch_mat_03')

lst.add(sbornik, en, physics_metodichki, physics_ucheb, FA, eltech_labi, eltech_metodichki, eltech_ucheb)
lst.row(back)