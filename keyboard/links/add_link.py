import os
from admins_id import current_sem, uch_mat_data, commands

def create_paths():
  paths = list()
  for i in range(int(current_sem)-1):
    for chapter in uch_mat_data[i]:
      sem_ID = str(i+2)
      if i < 8:
        sem_ID = '0'+sem_ID
      paths.append(f'{chapter}_{sem_ID}')
  return paths


def add_link(tmp_new_item: str) -> bool:
  paths = create_paths()
  flag = True
  text = '<b>Изменения сохранены успешно</b>'
  
  rcount = tmp_new_item.count(']')
  lcount = tmp_new_item.count('[')
  if not(rcount==lcount and rcount == 6):
    flag = False
    text = 'В параметрах запрещено использовать символы "[" и "]"\nЗапрещено удалять скобки, определяющие параметры\n\n<code>/ChangeLinkList [cmd] [path] [id1] [id2] [title] [url]</code>'

  
  if flag:
    new_item = list()
    
    lpos, rpos = 0, 0
    for i in range(6):
        lpos = tmp_new_item.find("[", lpos)+1
        rpos = tmp_new_item.find("]", rpos)
        new_item.append(tmp_new_item[lpos:rpos])
        rpos += 1

    cmd = new_item[0]
    if not(cmd in commands):
      flag = False
      text = f'Указана неверная команда изменения списка ссылок [command] ({cmd})\n'
      text += 'Допустимые команды:'
      for prm in commands:
        text +=f' {prm}'

  
  if flag:
    path = new_item[1]
    
    if not(path in paths):
      flag = False
      text = f'Указан неверный раздел списка ссылок [section] ({path})\n'
      text += 'Допустимые разделы:'
      for prm in paths:
        text +=f' {prm}'

  
  if flag:
    id1 = new_item[2]

    try:
      id1 = int(id1)
    except:
      flag = False
      text = f'Параметр [id1] должен быть числом ({id1})'

  
  if flag and cmd == 'swap':
    id2 = new_item[3]

    try:
      id2 = int(id2)
    except:
      flag = False
      text = f'Параметр [id2] должен быть числом ({id2})'

  if flag:
    if not (os.path.exists(f'links_files/{path}')):
      file = open(f'links_files/{path}', 'w')
      file.write('0\n')
      file.close()
  
    file = open(f'links_files/{path}', 'r', encoding='utf-8')
    lst = list()
    lines = file.readlines()

    title = new_item[4]
    url = new_item[5]
    count = int(lines.pop(0))
    
    if len(lines):
      for line in lines:
        tmp = line[1:-2].split("] [")
        tmp[0] = int(tmp[0])
        lst.append(tmp)

      if cmd == 'add':
        if id1 > count:
          id1 = lst[-1][0]+1
          lst.append([id1, title, url])
          count+=1
        else:
          if id1 < 1:
            id1 = 1;
          lst.insert(id1-1, [id1, title, url])
          for i in range(id1, len(lst)):
            lst[i][0] = lst[i][0]+1
          count+=1
      elif cmd in commands[1:]:
        if id1 < 1 or id1 > count:
          flag = False
          text = f'Параметр [id1] должен быть числом от 1 до {count}'
        elif cmd == 'rplcurl':
          lst[id1-1][2] = url
        elif cmd == 'rplcttl':
          lst[id1-1][1] = title
        elif cmd == 'rplcbttn':
          lst[id1-1][2] = url
          lst[id1-1][1] = title
        elif cmd == 'swap':
          if id2 < 1 or id2 > count:
            flag = False
            text = f'Параметр [id2] должен быть числом от 1 до {count}'
          else:
            lst[id1-1][1], lst[id2-1][1] = lst[id2-1][1], lst[id1-1][1]
            lst[id1-1][2], lst[id2-1][2] = lst[id2-1][2], lst[id1-1][2]
        elif cmd == 'del':
          lst.pop(id1-1)
          for i in range(id1-1, len(lst)):
            lst[i][0] = lst[i][0]-1
          count-=1
    elif cmd == 'add':
      count = 1
      lst.append([1, title, url])
    else:
      flag = False 
      text = 'Список ссылок пусть. Возможна только команда "add"'
      
    file.close()

  if flag:
    file = open(f'links_files/{path}', 'w', encoding='utf-8')
    file.write(str(count)+"\n")
    for line in lst:
      file.write(f"[{line[0]}] [{line[1]}] [{line[2]}]\n")
    file.close()

  if not(flag):
    text = f'<b>Допущена ошибка ввода</b>\n\nError:\n{text}'

  return text
    

def read_links(path: str, parametr: str) -> str:
  text = str()
  if not (os.path.exists(f'links_files/{path}')):
    file = open(f'links_files/{path}', 'w')
    file.write('0\n')
    file.close()
    text = 'Список ссылок пусть'
  else:
    file = open(f'links_files/{path}', 'r', encoding='utf-8')
    lines = file.readlines()
    lines.pop(0)
    if len(lines):
      for line in lines:
        tmp = line[1:-2].split("] [")
        if parametr == 'admin':
          text+=f'[{tmp[0]}] [<code>{tmp[1]}</code>] [<code>{tmp[2]}</code>] [<a href="{tmp[2]}">CLICK</a>]\n'
        elif parametr == 'user':
          text += f'<a href="{tmp[2]}">{tmp[1]}</a>\n'

      if parametr != 'admin' and parametr != 'user':
        text = '<b>Упс! Что-то пошло не так!</b>'
    else:
      text = 'Список ссылок пусть'
      
    file.close()
  return text