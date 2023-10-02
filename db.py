import sqlite3
import datetime


def first_join(id, name, username):
  with sqlite3.connect('identification.sqlite') as connect:
    cursor = connect.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users(
       user_id INT PRIMARY KEY UNIQUE,
       user_name TEXT,
       reg_time TEXT,
       activity INT);
    ''')
    connect.commit()

    cursor.execute(f"SELECT user_id FROM users WHERE user_id = {id}")
    data = cursor.fetchone()
    if data is None:
      time = datetime.datetime.now().strftime('%F')
      cursor.execute(
        "INSERT INTO users VALUES(?,?,?,?)",
      (id, f'<a href="https://t.me/{username}">{name}</a>', time, 0))
      connect.commit()


def is_registered(ID):
  with sqlite3.connect('identification.sqlite') as connect:
    cursor = connect.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users(
             user_id INT PRIMARY KEY UNIQUE,
             user_name TEXT,
             reg_time TEXT,
             activity INT);
         ''')
    connect.commit()

    cursor.execute(f"SELECT user_id FROM users WHERE user_id = {ID}")
    data = cursor.fetchone()
    if data:
      return True
    else:
     return False


def check_users(parameter: str):
  with sqlite3.connect('identification.sqlite') as connect:
    cursor = connect.cursor()
    if parameter == 'all':
      cursor.execute("SELECT * FROM users")
    elif parameter == 'time':
      cursor.execute("SELECT user_name, reg_time FROM users")
    elif parameter == 'activ':
      cursor.execute("SELECT user_name, activity FROM users")
    else:
      cursor.execute("SELECT user_id, user_name FROM users")
    data = cursor.fetchall()
    return data


def delete_user(id):
  with sqlite3.connect('identification.sqlite') as connect:
    cursor = connect.cursor()
    cursor.execute(f"SELECT user_id, user_name FROM users WHERE user_id = {id}")
    data = cursor.fetchone()
    cursor.execute(f"DELETE FROM users WHERE user_id={id}")
    connect.commit()
    return data


def activity(id):
  with sqlite3.connect('identification.sqlite') as connect:
    cursor = connect.cursor()
    cursor.execute(
    f"UPDATE users SET activity = activity + 1 WHERE user_id = {id}")
    connect.commit()