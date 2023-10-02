from telebot import types

names = {
    'ANA': 'Акиньшин Н.А.',
    'AMR': 'Андросов М.Р.',
    # 'BDL': 'Бондарев Д.Л.',
    'BTM': 'Бородин Т.М.',
    # 'VSA': 'Вандышев С.А.',
    # 'GAM': 'Гололобова А.М.',
    'DVD': 'Данилов В.Д.',
    'DMA': 'Девятайкина М.А.',
    'IVV': 'Игревский В.В.',
    # 'KAA': 'Королев А.А.',
    'KAP': 'Крутов А.П.',
    # 'MDM': 'Макеенков Д.М.',
    # 'MDS': 'Марьенко Д.С.',
    'MNA': 'Мельников Н.А.',
    'OAA': 'Овсяников А.А.',
    'OAM': 'Осминин А.М.',
    'PAD': 'Панов А.Д.',
    'PSS': 'Песецкий С.С.',
    'PPD': 'Петров П.Д.',
    # 'SAA': 'Сухов А.А.',
    'TVI': 'Ткачук М.И.',
    'FAV': 'Федотов А.В.',
    'HAA': 'Хасанов А.А.',
    'HSD': 'Храмкова С.Д.',
    # 'SMU': 'Шамочкин М.Ю.',
    # 'HDM': 'Шепелев М.Д.',
    # 'YSV': 'Якунин С.В.'
}

attend_menu = types.InlineKeyboardMarkup(row_width=2)
for name_id in names:
    button = types.InlineKeyboardButton(text=f'{names[name_id]}', callback_data=f'{name_id}')
    attend_menu.add(button)
attend_button_cancel = types.InlineKeyboardButton(text='Отмена', callback_data='attend_cnl')
attend_button_enter = types.InlineKeyboardButton(text='Завершить', callback_data='attend_enter')
attend_menu.add(attend_button_cancel, attend_button_enter)
