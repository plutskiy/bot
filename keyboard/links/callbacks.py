from telebot import types
from admins_id import current_sem, uch_mat_data, callback_text, commands_button_text

sem_link_menu = types.InlineKeyboardMarkup(row_width=1)
for i in range(2, int(current_sem)+1):
    num = str(i)
    if i < 10:
        num = '0' + str(i)
    sem_link_menu.add(types.InlineKeyboardButton(f'{i} СЕМЕСТР', callback_data=f'lr_{num}'))
sem_link_menu.add(types.InlineKeyboardButton('ЗАКРЫТЬ', callback_data=f'ad_close_info'))


def create_uchmat_link_menu(num: str):
  sem_ID = int(num)
  buttons = []
  
  for callback in callback_text:
        if callback in uch_mat_data[sem_ID - 2]:
            buttons.append(types.InlineKeyboardButton(text=callback_text[callback][0], callback_data=f'lr_{callback}_{num}'))
  back = types.InlineKeyboardButton(text='Вернуться', callback_data='lr_back')

  buttons_list = [buttons[i:i + 2] for i in range(0, len(buttons), 2)]
  uchmat_link_menu = types.InlineKeyboardMarkup(buttons_list)
  uchmat_link_menu.row(back)
  return uchmat_link_menu


def create_command_link_menu(callback_text: str):
  buttons = []
  
  for cmd in commands_button_text:
    callback = callback_text[:3]+cmd+'_'+callback_text[3:]
    buttons.append(types.InlineKeyboardButton(text=commands_button_text[cmd], callback_data=callback))
  back = types.InlineKeyboardButton(text='Вернуться', callback_data='lr_back')

  buttons_list = [buttons[i:i + 2] for i in range(0, len(buttons), 2)]
  uchmat_link_menu = types.InlineKeyboardMarkup(buttons_list)
  uchmat_link_menu.row(back)
  return uchmat_link_menu