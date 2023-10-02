from telebot import types
from admins_id import *

button = types.InlineKeyboardButton(text='Убрать', callback_data='ad_close_info')
close = types.InlineKeyboardMarkup(row_width=1)
close.add(button)


def reg_text(parametr, name):
    if parametr == 'reg':
        text = f'Привет <b>{name}</b>!\n'
        text += 'Ты уже имеешь доступ к функционалу бота!\n'
        text += 'Пиши <b>/start</b> и получи необходимую информацию!'
    elif parametr == 'admin':
        text = f'Добро пожаловать в систему, <b>ADMIN {name}</b>\n\n'
        text += '<b>Вам доступны следующие команды:</b>\n'
        text += '<b>/DZ</b> - Панель редактирования домашнего задания\n'
        text += '<b>/CFG</b> - Параметры меню бота\n'
        text += '<b>/attend</b> - Список присутствующих\n'
        text += '<b>/DB [параметр]</b> - Информация о всех пользователях бота (более подробно - /DB info)\n'
        text += '<b>/del [id]</b> - Удалить пользователя бота по его id\n'
        text += '<b>/sch</b> - Поиск данных пользователя в сообщении <b>(ограниченный доступ)</b>\n'
        text += '<b>/arg</b> - Ручное добавление пользователя в систему <b>(ограниченный доступ)</b> (/arg info)\n'
        text += '<b>/ChangeLinkList</b> - Редактирование списков учебных материалов (/ChangeLinkList info)\n'
        text += '<b>/link</b> - Вспомогательная панель для редактирования списков учебных материалов\n'
    elif parametr == 'not_reg':
        text = '<b>Запрос на получение доступа к боту был отправлен администратору.</b>\n\n'
        text += 'Администратор откроет Вам доспут или свяжется с Вами <b>в ближайшее время!</b>\n\n'
        text += 'Если на Вашу заявку не был дан ответ или с Вами не связались в течение 12ти часов, свяжитесь с <a href="https://t.me/FDX_VI">заместителем старосты</a>.'
    else:
        text = '<b>Допущена ошибка в функции.\nРазраб - еблан.</b>'
    return text


def db_info_text():
    text = '<b>Параметры:</b>\n\n'
    text += '<b>Без параметра</b> - (id, user_name)\n'
    text += '<b>all</b> - (id, user_name, reg_time, activity)\n'
    text += '<b>time</b> - (user_name, reg_time)\n'
    text += '<b>activ</b> - (user_name, activity)\n'
    text += '\n<b>Обозначения:</b>\n\n'
    text += '<b>id</b> - ID пользователя\n'
    text += '<b>user_name</b> - Ник пользователя с ссылкой на его профиль\n'
    text += '<b>reg_time</b> - Дата регистрации пользователя\n'
    text += '<b>activity</b> - Счетчик взаимодействий пользователя с ботом\n'
    return text

def arg_info_text():
    text = '<b>/arg [ID] [NAME] [USER_NAME]</b>\n\n'
    text += 'ID - id пользователя\n'
    text += 'NAME - ник пользователя в телеграме\n'
    text += 'USER_NAME - имя пользователя (@ABC - нужно записать ABC)\n'
    text += '\n<b>Пример оформления</b>\n\n'
    text += '/arg 1094304777 Valentin FDX_VI'
    return text

def link_info_text():
    text = '<b>/ChangeLinkList [cmd] [path] [id1] [id2] [title] [url]</b>\n\n'
    text += 'Параметры:\n'
    text += '<b>cmd</b> - команда изменения списка ссылок\n'
    text += '<b>path</b> - раздел, в котором будут проводиться изменения\n'
    text += '<b>id1</b> - номер позиции, на которой будут проводиться изменения\n'
    text += '<b>id2</b> - номер позиции; использутся только при смене позиций\n'
    text += '<b>title</b> - заголовок на кнопке\n'
    text += '<b>ulr</b> - ссылка кнопки\n'
    text += '\nКоманды изменения списка ссылок:\n'
    text += '<b>add</b> - добавить кнопку на позицию [id1] с заголовком [title] и ссылкой [url]\n'
    text += '<b>rplcttl</b> - заменить заголовок кнопки на позиции [id1] на заголовок [title]\n'
    text += '<b>rplcurl</b> - заменить ссылку кнопки на позиции [id1] на ссылку [url]\n'
    text += '<b>rplcbttn</b> - заменить заголовок и ссылку на позиции [id1] на [title] и [url]\n'
    text += '<b>swap</b> - поменять местами кнопки на позициях [id1] и [id2]\n'
    text += '<b>del</b> - удалить кнопку на позиции [id1]\n'
    text += '\nВспомогательная функция:\n'
    text += '<b>/link</b> - Вспомогательная панель для редактирования списков учебных материалов\n\n'
    text += 'При использовании панели параметры [cmd] и [path] заполняются автоматически\n\n'
    text += 'Автоматеческое заполнение полей в зависимости от [cmd]:\n'
    text += '/ChangeLinkList [add] [path] [] [None] [] []\n'
    text += '/ChangeLinkList [rplcttl] [path] [] [None] [] [None]\n'
    text += '/ChangeLinkList [rplcurl] [path] [] [None] [None] []\n'
    text += '/ChangeLinkList [rplcbttn] [path] [] [None] [] []\n'
    text += '/ChangeLinkList [swap] [path] [] [] [None] [None]\n'
    text += '/ChangeLinkList [del] [path] [] [None] [None] [None]\n'
    text += '\nNone - параметр не указывается\n'
    return text
  
def cfg_text():

    text = f'current_sem = <b>{current_sem}</b>'
    text += '\n\n<b>ad_tip_dz = {</b>\n'
    for subject in ad_tip_dz:
        text += f'\t\t\t{subject}: {ad_tip_dz[subject]}\n'
    text += '<b>}</b>\n\n<b>ad_tek_dz = {</b>\n'
    for subject in ad_tek_dz:
        text += f'\t\t\t{subject}: {ad_tek_dz[subject]}\n'
    text += '<b>}</b>\n\n<b>uch_mat_data = [</b>\n'
    for sem in uch_mat_data:
        text += '\t\t\t<b>{</b>\n'
        for data in sem:
            text += f'\t\t\t\t\t\t{data}: {sem[data].__name__.split(".")[-1]}\n'
        text += '\t\t\t<b>}</b>\n'
    text += '<b>]</b>\n\n<b>callback_text = {</b>\n'
    for callback in callback_text:
        text += f'\t\t\t{callback}: {callback_text[callback]}\n'
    text += '<b>}</b>'
    return text
