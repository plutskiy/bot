from telebot import types
from admins_id import current_sem

main_menu = types.InlineKeyboardMarkup(row_width=2)
timetable = types.InlineKeyboardButton('Расписание', url='https://docs.google.com/spreadsheets/d/1Srv-61c4ngRIs_ctDZuY1f1e0qM-v4VR8aFT_IEznbU/edit?usp=drivesdk')
library = types.InlineKeyboardButton('Учебные материалы', callback_data='uch_mat_' + current_sem)
homework = types.InlineKeyboardButton('Домашнее задание', callback_data='hw')
krki = types.InlineKeyboardButton('КР и РК', callback_data='mm_date')
back_to_sem_menu = types.InlineKeyboardButton('Выбор семестра', callback_data='semestr_menu')
main_menu.add(timetable, library, homework, krki, back_to_sem_menu)
