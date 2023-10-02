from telebot import types
import os

def create_link_list(path: str):
  sem_ID = path[-2:]
  
  lst = types.InlineKeyboardMarkup(row_width=1)

  if not (os.path.exists(f'links_files/{path}')):
      file = open(f'links_files/{path}', 'w')
      file.write('0\n')
      file.close()
  else:
    file = open(f'links_files/{path}', 'r', encoding='utf-8')
    lines = file.readlines()
    lines.pop(0)
    for line in lines:
      tmp = line[1:-2].split("] [")
      lst.add(types.InlineKeyboardButton(text=tmp[1], url=tmp[2]))
  back = types.InlineKeyboardButton(text='Вернуться', callback_data=f'uch_mat_{sem_ID}')
  lst.row(back)
  
  return lst