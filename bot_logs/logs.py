import datetime
from admins_id import admin_id

def write_log_to_file(message, action):
    time = datetime.datetime.now()
    user_id = message.from_user.id
    user = message.from_user.username
    is_admin = user_id in admin_id

    if action == 'command':
      text= message.text.replace('\n', ' ')
    elif action == 'callback':
      text = message.data

    log = f'[{time}] ID: {user_id}; ADMIN: {is_admin}; USER_NAME: {user}; {action}: {text}\n'
    file = open('bot_logs/logs.txt', 'a', encoding='utf-8')
    file.write(log)
    file.close()
