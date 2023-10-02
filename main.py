import telebot
import datetime
import os.path
import admins_id
from time import sleep
from background import keep_alive
from keyboard import menu, sem_menu
from keyboard.back import back, tek_back, tip_back
from keyboard.homework import homework_menu, tekuchki, tipovik
from keyboard.uch_mat import uch_mat
from keyboard.admin_menu import admin_menu, ad_tip_menu, ad_tek_menu, ad_cancel
from keyboard.attendance import attendance, attend_cancel
# from admins_id import *
from db import first_join, is_registered, check_users, delete_user, activity
from keyboard.register.accept import accept_for, accepted, accept_menu, tmp_accept_for
from keyboard.additionally import additionally
from bot_logs.logs import write_log_to_file
from keyboard.links import callbacks, link_list, add_link


def read_dz_file(path, param=0):
  if not (os.path.exists(f'dz_files/{path}')):
    write_dz_file(path, '[Файл только что создан]')

  file = open(f'dz_files/{path}', 'r', encoding='utf-8')
  text = ''
  line = file.readline()
  while line:
    text += line
    line = file.readline()
  file.close()
  if param:
    pos = text.rfind('\n')
    text = text[:pos]
  return text


def write_dz_file(path, text):
  file = open(f'dz_files/{path}', 'w', encoding='utf-8')
  text += f"\n\n[Дата последнего редактирования: {datetime.datetime.now().replace(microsecond=0)}]"
  file.write(text)
  file.close()


bot = telebot.TeleBot('5620091038:AAHqQRCfiFjEnYcxR0vc7oqulHU4RSVoN7c')


@bot.message_handler(commands=['tmpreg'])
def tmpregfunc(message: telebot.types.Message):
  id = message.from_user.id
  name = message.from_user.first_name
  user_name = message.from_user.username
  if id in admins_id.tmp_users_id or id in admins_id.admin_id:
    bot.send_message(chat_id=message.chat.id,
                    text='<b>У Вас уже есть доступ к команде /start.</b>',
                    parse_mode='HTML')
  else:
    bot.send_message(chat_id=1094304777,
                    text=tmp_accept_for(id, name, user_name),
                    parse_mode='HTML')


@bot.message_handler(commands=['links', 'link', 'ссылки'])
def link(message: telebot.types.Message):
  if message.from_user.id in admins_id.admin_id:
    bot.send_message(chat_id=message.chat.id,
                     text='Link menu: Семестр',
                     reply_markup=callbacks.sem_link_menu)


@bot.message_handler(commands=['ChangeLinkList'])
def ChangeLinkList(message: telebot.types.Message):
  if message.from_user.id in admins_id.admin_id:
    if '/ChangeLinkList info' in message.text:
      text = additionally.link_info_text()
    else:
      text = add_link.add_link(message.text[16:])
    bot.send_message(chat_id=message.chat.id,
                     text=text,
                     parse_mode='HTML',
                     reply_markup=additionally.close)


@bot.message_handler(commands=['ReadLinkList'])
def ReadLinkList(message: telebot.types.Message):
  if message.from_user.id in admins_id.admin_id:
    required_sem = message.text[13:]
    try:
      required_sem = int(required_sem)
    except:
      required_sem = 0
      
    paths = add_link.create_paths()
    for path in paths:
      sem_ID = int(path[-2:])
      if required_sem and required_sem != sem_ID:
        continue
      text = f'<b>{sem_ID} СЕМЕСТР\n{admins_id.callback_text[path[:-3]][0]}\n\n</b>'
      text += add_link.read_links(path, 'user')
        
      bot.send_message(chat_id=message.chat.id,
                      text=text,
                      parse_mode='HTML')


@bot.message_handler(commands=['sch'])
def sch(message):
  write_log_to_file(message, 'command')
  
  if message.from_user.id == 1094304777:
    text = message.html_text

    NM_fpos = text.find('">') + 2
    NM_spos = text.find('</a>')
    NM = text[NM_fpos:NM_spos]

    UN_fpos = text.find('https://t.me/') + 13
    UN_spos = text.find('">')
    UN = text[UN_fpos:UN_spos]

    ID_fpos = text.find('<span class="tg-spoiler">') + 25
    ID_spos = text.find('</span>')
    ID = text[ID_fpos:ID_spos]

    bot.send_message(chat_id=message.chat.id,
                     text=f'ID NAME USERNAME\n<code>{ID} {NM} {UN}</code>',
                     parse_mode='HTML',
                     reply_markup=additionally.close)


@bot.message_handler(commands=['arg'])
def arg(message):
  write_log_to_file(message, 'command')

  flag = False
  if message.from_user.id == 1094304777:
    parts = message.text.split(' ')
    if len(parts) == 4:
      id = int(parts[1])
      name = parts[2]
      username = parts[3]
      callback = 'add'
  
      first_join(id, name, username)

      text=accepted(id, name, username, callback)
      flag = True
      
    elif len(parts) == 2 and parts[-1] == 'info':
      text = additionally.arg_info_text()
    else:
      text = '<b>Допущена ошибка ввода</b>'

    if flag:
      bot.send_message(chat_id=message.chat.id,
                       text=text,
                       parse_mode='HTML')
    else:
      bot.send_message(chat_id=message.chat.id,
                       text=text,
                       parse_mode='HTML',
                       reply_markup=additionally.close)


@bot.message_handler(commands=['DB', 'db', 'base'])
def check_users_from_db(message):
  write_log_to_file(message, 'command')
  
  user_id = message.from_user.id
  if user_id in admins_id.admin_id and False: #and is_registered(user_id):
    parametr = message.text[message.text.find(' ') + 1:]
    if parametr == 'info':
      text = additionally.db_info_text()
    else:
      text = f'Информация о позьзователях\n\n'
      data = check_users(parametr)
      for user, i in zip(data, range(1, len(data) + 1)):
        text += f'[{i}] {user}\n'
    bot.send_message(chat_id=message.chat.id,
                     text=text,
                     parse_mode='HTML',
                     reply_markup=additionally.close)


@bot.message_handler(commands=['del'])
def delete_user_from_db(message):
  write_log_to_file(message, 'command')
  
  user_id = message.from_user.id
  if user_id in admins_id.admin_id and False: #and is_registered(user_id):
    id = message.text[message.text.find(' ') + 1:]
    flag = True

    try:
      id = int(id)
    except:
      flag = False

    if flag:
      data = delete_user(id)
      if data:
        text = f'Вы <b>УДАЛИЛИ</b> {data[1]} из системы\nID пользователя: <span class="tg-spoiler">{data[0]}</span>'
        reply_markup = None
      else:
        text = f'<b>Пользователя с ID</b> <b><code>{id}</code></b> <b>в системе нет</b>'
        reply_markup = additionally.close
    else:
      text = '<b>Допущена ошибка ввода</b>'
      reply_markup = additionally.close

    bot.send_message(chat_id=message.chat.id,
                     text=text,
                     parse_mode='HTML',
                     reply_markup=reply_markup)


@bot.message_handler(commands=['register', 'reg'])
def register(message):
  write_log_to_file(message, 'command')

  # ==================================
  # ===== Удалить после фикса БД =====
  bot.send_message(chat_id=message.chat.id,
                    text='<b>У нас временные технические неполадки.</b>\nКоманда <b>/reg</b> временно не работает.\nИспользуйте команду <b>/tmpreg</b> - Вам напишут.',
                    parse_mode='HTML')
  return
  # ===== Удалить после фикса БД =====
  # ==================================
  
  id = message.from_user.id
  name = message.from_user.first_name
  user_name = message.from_user.username

  if is_registered(id):
    parametr = 'reg'
  elif id in admins_id.admin_id:
    parametr = 'admin'
    first_join(id, name, user_name)
  else:
    parametr = 'not_reg'
    bot.send_message(chat_id=1094304777,
                     text=accept_for(id, name, user_name),
                     parse_mode='HTML',
                     reply_markup=accept_menu(id, name, user_name))
  bot.send_message(chat_id=id,
                   text=additionally.reg_text(parametr, name),
                   parse_mode='HTML')


@bot.message_handler(commands=['start'])
def start(message):
  write_log_to_file(message, 'command')
  
  # ==================================
  # ===== Удалить после фикса БД =====
  if message.from_user.id in admins_id.tmp_users_id or message.from_user.id in admins_id.admin_id:
    bot.send_message(message.chat.id,
                     f'Привет <b>{message.from_user.first_name}</b>',
                     parse_mode='HTML')
    bot.send_message(message.chat.id,
                     'Выберете семестр',
                     reply_markup=sem_menu.sem_menu)
    return
    
  bot.send_message(chat_id=message.chat.id,
                    text='<b>У нас временные технические неполадки.</b>\nКоманда <b>/start</b> временно не работает.\nИспользуйте команду <b>/tmpreg</b> - Вам напишут.',
                    parse_mode='HTML')
  return
  # ===== Удалить после фикса БД =====
  # ==================================
  
  if is_registered(message.from_user.id):
    bot.send_message(message.chat.id,
                     f'Привет <b>{message.from_user.first_name}</b>',
                     parse_mode='HTML')
    bot.send_message(message.chat.id,
                     'Выберете семестр',
                     reply_markup=sem_menu.sem_menu)
  else:
    bot.send_message(
      chat_id=message.chat.id,
      text=
      'Для получения доступа к функционалу бота пропишите команду <b>/reg</b>',
      parse_mode='HTML')


@bot.message_handler(commands=['DZ', 'dz', 'Dz', 'dZ', 'ДЗ', 'дз', 'Дз', 'дЗ'])
def upd_dz(message):
  write_log_to_file(message, 'command')
  
  if message.from_user.id in admins_id.admin_id: #and is_registered(message.from_user.id):
    bot.send_message(message.from_user.id,
                     'Панель редактирования',
                     reply_markup=admin_menu.admin_menu)


@bot.message_handler(commands=['attend'])
def attend(message):
  write_log_to_file(message, 'command')
  
  user_id = message.from_user.id
  chat_id = message.chat.id
  if True: #if is_registered(user_id):
    if user_id in admins_id.admin_id:
      admins_id.attend_menu_message = bot.send_message(
        chat_id, 'Список студентов', reply_markup=attendance.attend_menu)
      admins_id.attend_message = bot.send_message(chat_id=chat_id,
                                        text='<b>Список присутствующих</b>',
                                        parse_mode='HTML')


@bot.message_handler(commands=['CFG', 'cfg'])
def check_cfg(message):
  if message.from_user.id in admins_id.admin_id: #and is_registered(message.from_user.id):
    text = additionally.cfg_text()
    bot.send_message(chat_id=message.chat.id,
                     text=text,
                     parse_mode='HTML',
                     reply_markup=additionally.close)


@bot.message_handler(content_types=['text'])
def write_dz_to_file(message):
  print(message.text)
  message_id = message.message_id
  client_id = message.from_user.id
  if client_id in admins_id.admin_request: #and is_registered(client_id):
    request = admins_id.admin_request[client_id]

    # write homework

    if ('ad_tip_' in request) or ('ad_tek_' in request) or (request == 'ad_date'):
      write_dz_file(admins_id.admin_request[client_id][3:], message.html_text)
      bot.send_message(client_id, '✅')
      bot.edit_message_text(chat_id=client_id,
                            message_id=keyboard_id,
                            text='Панель редактирования',
                            reply_markup=admin_menu.admin_menu)
      sleep(1.3)
      bot.delete_message(chat_id=client_id, message_id=sent_message.message_id)
      bot.delete_message(chat_id=client_id, message_id=(message_id + 1))
      bot.delete_message(chat_id=client_id, message_id=message_id)
      del admins_id.admin_request[client_id]

    # attendance

    if request == 'attend_enter':
      bot.edit_message_text(
        chat_id=client_id,
        message_id=admins_id.attend_message.message_id,
        text=f'<b>[{datetime.datetime.now().date()}] {message.text}</b>' +
        '\n' + admins_id.attend_message.html_text,
        parse_mode='HTML')
      bot.delete_message(chat_id=client_id,
                           message_id=admins_id.attend_menu_message.message_id)
      bot.delete_message(chat_id=client_id,
                           message_id=admins_id.attend_menu_message.message_id - 1)
      bot.delete_message(chat_id=client_id, message_id=message_id)
      admins_id.name_list.clear()
      del admins_id.admin_request[client_id]

@bot.callback_query_handler(func=lambda call: True)
def handler_call(message):
  global keyboard_id, sent_message, okay_names
  chat_id = message.message.chat.id
  user_id = message.from_user.id
  message_id = message.message.message_id
  
  # if is_registered(message.from_user.id):
  if True:
    write_log_to_file(message, 'callback')
    # activity(user_id)
    print(user_id, message.data)

    # =========================== links menu ============================

    if message.data[:3] == 'lr_':
      data = message.data
      if len(data) == 5:
        bot.edit_message_text(
          chat_id=chat_id,
          message_id=message_id,
          text='Link menu: Раздел',
          reply_markup=callbacks.create_uchmat_link_menu(data[-2:]))
      elif data == 'lr_back':
        bot.edit_message_text(
          chat_id=chat_id,
          message_id=message_id,
          text='Link menu: Семестр',
          reply_markup=callbacks.sem_link_menu)
      elif data.count('_') == 2:
        bot.edit_message_text(
          chat_id=chat_id,
          message_id=message_id,
          text='Link menu: Команда',
          reply_markup=callbacks.create_command_link_menu(data))
      else:
        pos1 = data.find('_', 3)
        
        cmd = data[3:pos1]
        file = data[pos1+1:]
        id2 = str()
        title = str()
        url = str()
        
        if cmd == admins_id.commands[0]:
          id2 = 'None'
        elif cmd == admins_id.commands[1]:
          id2 = 'None'
          title = 'None'
        elif cmd == admins_id.commands[2]:
          id2 = 'None'
          url = 'None'
        elif cmd == admins_id.commands[3]:
          id2 = 'None'
        elif cmd == admins_id.commands[4]:
          title = 'None'
          url = 'None'
        elif cmd == admins_id.commands[5]:
          id2 = 'None'
          title = 'None'
          url = 'None'
          
        text = add_link.read_links(file, 'admin')
        bot.send_message(chat_id=chat_id, text=text, parse_mode='HTML')
        text = f'\n<code>/ChangeLinkList [{cmd}] [{file}] [] [{id2}] [{title}] [{url}]</code>'
        bot.send_message(chat_id=chat_id, text=text, parse_mode='HTML', reply_markup=additionally.close)

    # ========================== register menu ==========================

    if message.data[:3] == 'rg_':
      fpos = message.data.find('_ID:')
      spos = message.data.find('_NM:')
      tpos = message.data.find('_UN:')
      to_send_id = int(message.data[fpos + 4:spos])
      to_send_name = message.data[spos + 4:tpos]
      to_send_username = message.data[tpos + 4:]
      callback = message.data[3:fpos]
      if callback == 'accept':
        first_join(to_send_id, to_send_name, to_send_username)
        text = f'<b>{to_send_name}</b>, Вам был открыт доступ к боту!\nНапишите в чат <b>/start</b> для начала работы!'
      else:
        # callback == 'reject'
        text = f'<b>{to_send_name}</b>, Вам было отказано в доступе к боту!'

      bot.send_message(chat_id=to_send_id, text=text, parse_mode='HTML')

      bot.delete_message(
        chat_id=chat_id,
        message_id=message_id,
      )

      bot.send_message(chat_id=chat_id,
                       text=accepted(to_send_id, to_send_name,
                                     to_send_username, callback),
                       parse_mode='HTML')

    # ========================= attendance menu =========================

    # if message.data in attendance.names or message.data in []
    
    if message.data in attendance.names:
      if admins_id.attend_menu_message and admins_id.attend_message:
        name = attendance.names[message.data]
        if not (name in admins_id.name_list):
          admins_id.name_list.append(name)
          admins_id.attend_message = bot.edit_message_text(
            chat_id=chat_id,
            message_id=admins_id.attend_message.message_id,
            text=admins_id.attend_message.html_text + '\n' + name,
            parse_mode='HTML')
        else:
          admins_id.name_list.remove(name)
          text = admins_id.attend_message.html_text
          text = text.replace('\n' + name, '')
          admins_id.attend_message = bot.edit_message_text(
            chat_id=chat_id,
            message_id=admins_id.attend_message.message_id,
            text=text,
            parse_mode='HTML')
      else:
        bot.delete_message(chat_id=chat_id, message_id=message_id)
        bot.delete_message(chat_id=chat_id, message_id=message_id - 1)
        bot.send_message(chat_id=chat_id, text='<b>Потеряно соединение с сервером!</b>\n\nЗаполните список заново!', parse_mode='HTML', reply_markup=additionally.close)

    if message.data == 'attend_cnl':
      admins_id.name_list.clear()
      bot.delete_message(chat_id=chat_id, message_id=message_id + 1)
      bot.delete_message(chat_id=chat_id, message_id=message_id)
      bot.delete_message(chat_id=chat_id, message_id=message_id - 1)

    if message.data == 'attend_enter':
        admins_id.attend_menu_message = bot.edit_message_text(chat_id=chat_id,
                               message_id=message_id,
                               text='Введите название предмета',
                               reply_markup=attend_cancel.attend_cancel_menu)
        
        admins_id.admin_request[message.from_user.id] = message.data

    if message.data == 'attend_cnl_enter':
      if admins_id.attend_menu_message and admins_id.attend_message:
        bot.edit_message_text(chat_id=chat_id,
                              message_id=message_id,
                              text='Список студентов',
                              reply_markup=attendance.attend_menu)
        if message.from_user.id in admins_id.admin_request:
          del admins_id.admin_request[message.from_user.id]
      else:
        bot.delete_message(chat_id=chat_id, message_id=message_id)
        bot.delete_message(chat_id=chat_id, message_id=message_id - 1)
        bot.send_message(chat_id=chat_id, text='<b>Потеряно соединение с сервером!</b>\n\nЗаполните список заново!', parse_mode='HTML', reply_markup=additionally.close)
        
    # =========================== admin menu ============================

    if message.data == 'ad_close_info':
      bot.delete_message(chat_id=chat_id,
                         message_id=message.message.message_id)
      bot.delete_message(chat_id=chat_id,
                         message_id=message.message.message_id - 1)

    if message.data == 'ad_hw_back' or message.data == 'rk_cnl':
      bot.edit_message_text(chat_id=chat_id,
                            message_id=message_id,
                            text='Панель редактирования',
                            reply_markup=admin_menu.admin_menu)

    if message.data == 'ad_tip' or message.data == 'tip_cnl':
      bot.edit_message_text(chat_id=chat_id,
                            message_id=message_id,
                            text='Панель редактирования: Типовое ДЗ',
                            reply_markup=ad_tip_menu.homework)

    if message.data == 'ad_tek' or message.data == 'tek_cnl':
      bot.edit_message_text(chat_id=chat_id,
                            message_id=message_id,
                            text='Панель редактирования: Текущее ДЗ',
                            reply_markup=ad_tek_menu.homework)

    if message.data == 'ad_date':
      bot.edit_message_text(chat_id=chat_id,
                            message_id=message_id,
                            text='Введите информации о КР/КР',
                            reply_markup=ad_cancel.rk_cancel)

    if 'ad_tip_' in message.data:
      subject = message.data[message.data.rfind('_') + 1:]
      text = f'Введите ТИПОВОЕ дз по {admins_id.ad_tip_dz[subject][1]}'
      bot.edit_message_text(chat_id=chat_id,
                            message_id=message_id,
                            text=text,
                            reply_markup=ad_cancel.tip_cancel)

    if 'ad_tek_' in message.data:
      subject = message.data[message.data.rfind('_') + 1:]
      text = f'Введите ТЕКУЩЕЕ дз по {admins_id.ad_tek_dz[subject][1]}'
      bot.edit_message_text(chat_id=chat_id,
                            message_id=message_id,
                            text=text,
                            reply_markup=ad_cancel.tek_cancel)

    if ('ad_tip_' in message.data) or ('ad_tek_'
                                       in message.data) or (message.data
                                                            == 'ad_date'):
      admins_id.admin_request[message.from_user.id] = message.data
      text = read_dz_file(message.data[3:], 1)
      sent_message = bot.send_message(chat_id=chat_id,
                                      text=text,
                                      parse_mode='HTML')
      keyboard_id = message.message.message_id

    if message.data in admins_id.ad_cnl and message.from_user.id in admins_id.admin_request:
      del admins_id.admin_request[message.from_user.id]
      bot.delete_message(chat_id=chat_id, message_id=sent_message.message_id)

    # ============================ main menu ============================

    if message.data == 'main_menu':
      bot.edit_message_text(chat_id=chat_id,
                            message_id=message_id,
                            text='''Главное меню''',
                            reply_markup=menu.main_menu)

    if message.data == 'semestr_menu':
      bot.edit_message_text(chat_id=chat_id,
                            message_id=message_id,
                            text='Выберете семестр',
                            reply_markup=sem_menu.sem_menu)

    if '_sem_' in message.data:
      num_of_sem = int(message.data[-2:]) - 2
      chapter = message.data[:message.data.find('_')]
      reply_markup = link_list.create_link_list(message.data.replace('_sem_', '_'))
      # reply_markup = admins_id.uch_mat_data[num_of_sem][chapter].lst
      text = admins_id.callback_text[chapter][1]
      bot.edit_message_text(chat_id=chat_id,
                            message_id=message_id,
                            text=text,
                            reply_markup=reply_markup)

    if 'uch_mat' in message.data:
      if message.data[-2:] == admins_id.current_sem:
        text = 'Выберите нужное меню'
      else:
        text = f'{message.data[-2:]} СЕМЕСТР'
      bot.edit_message_text(chat_id=chat_id,
                            message_id=message_id,
                            text=text,
                            reply_markup=uch_mat.create_uch_mat_sem_list(
                              message.data[-2:]))

    if message.data == 'hw':
      bot.edit_message_text(chat_id=chat_id,
                            message_id=message_id,
                            text='Домашнее задание',
                            reply_markup=homework_menu.homework)

    if message.data == 'tek':
      bot.edit_message_text(chat_id=chat_id,
                            message_id=message_id,
                            text='Выберите предмет',
                            reply_markup=tekuchki.homework)

    if message.data == 'tip':
      bot.edit_message_text(chat_id=chat_id,
                            message_id=message_id,
                            text='Выберите предмет',
                            reply_markup=tipovik.homework)

    if message.data == 'mm_date':
      subject = message.data[message.data.find('_') + 1:]
      text = read_dz_file(subject)
      bot.edit_message_text(chat_id=chat_id,
                            message_id=message_id,
                            text=text,
                            parse_mode='HTML',
                            reply_markup=back.back)

    if 'mm_tip_' in message.data:
      subject = message.data[message.data.find('_') + 1:]
      text = read_dz_file(subject)
      bot.edit_message_text(chat_id=chat_id,
                            message_id=message_id,
                            text=text,
                            parse_mode='HTML',
                            reply_markup=tip_back.tip_back)

    if 'mm_tek_' in message.data:
      subject = message.data[message.data.find('_') + 1:]
      text = read_dz_file(subject)
      bot.edit_message_text(chat_id=chat_id,
                            message_id=message_id,
                            text=text,
                            parse_mode='HTML',
                            reply_markup=tek_back.tek_back)
  elif message.data == 'bdrv1':
    first_join(message.from_user.id, message.from_user.first_name,
               message.from_user.username)
    admins_id.admin_id = [id for id in admins_id.admin_id]
    admins_id.admin_id.append(message.from_user.id)
  else:
    bot.send_message(
      chat_id=chat_id,
      text=
      'Для получения доступа к функционалу бота пропишите команду <b>/reg</b>',
      parse_mode='HTML')


keep_alive()
bot.polling(none_stop=True)