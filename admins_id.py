from keyboard.uch_mat.sem_2 import library_02, calendar_02, books_02
from keyboard.uch_mat.sem_3 import library_03, calendar_03, books_03, proga_03

admin_id = frozenset([1094304777, 1493854180, 1909812069, 331346891])
tmp_users_id = frozenset([1023832280,424619231,1064902898, 561008276, 1352115836, 519275089, 918110338, 314082845, 1597987421])
ad_cnl = frozenset(['tip_cnl', 'tek_cnl', 'rk_cnl'])
admin_request = {}
name_list = []

# =======================================
# ================ MENUS ================

attend_menu_message = None
attend_message = None
keyboard_id = None

# ================ MENUS ================
# =======================================

current_sem = 3


current_sem = str(current_sem)
if len(current_sem) < 2:
    current_sem = '0' + current_sem


# =======================================
# ================= CFG =================

commands = ['add', 'rplcurl', 'rplcttl', 'rplcbttn', 'swap', 'del']

commands_button_text = {
    'add': 'Добавить ссылку',
    'rplcurl': 'Заменить ссылку',
    'rplcttl': 'Заменить надпись',
    'rplcbttn': 'Заменить кнопку',
    'swap': 'Поменять ссылки местами',
    'del': 'Удалить ссылку'
}

ad_tip_dz = {
    'alg': ['АиСД', 'АиСД'],
    'ryad': ['Кроты','КРОТАМ'],
    'fanal': ['Функан', 'ФУНКАНУ'],
    'syst': ['СПО', 'СПО'],
    'etech': ['Элтех', 'ЭЛТЕХУ'],
    'phys': ['Физика', 'ФИЗИКЕ'],
}

ad_tek_dz = {
    'alg': ['АиСД', 'АиСД'],
    'ryad': ['Кроты','КРОТАМ'],
    'fanal': ['Функан', 'ФУНКАНУ'],
    'syst': ['СПО', 'СПО'],
    'etech': ['Элтех', 'ЭЛТЕХУ'],
    'phys': ['Физика', 'ФИЗИКЕ'],
}

uch_mat_data = [
    {'lib': library_02, 'cal': calendar_02, 'book': books_02},
    {'lib': library_03, 'cal': calendar_03, 'book': books_03, 'proga': proga_03},
]

callback_text = {
    'lib': ['Учебные материалы', 'Выберите предмет'],
    'cal': ['Календарные планы', 'Выберите предмет'],
    'book': ['Учебники', 'Выберите книгу'],
    'proga': ['Ответы по проге', 'Выберите хранилище'],
}

# ================= CFG =================
# =======================================