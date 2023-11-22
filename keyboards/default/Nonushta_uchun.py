from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

from loader import base

menu = base.select_nonushta(turi='Nonushta uchun')

index = 0
keys = []
j=0
for maxs in menu:
    if j % 2 == 0 and j !=0:
        index += 1
    if j % 2 == 0:
        keys.append([KeyboardButton(text=f"{maxs[1]}")])
    else:
        keys[index].append(KeyboardButton(text=f"{maxs[1]}"))
    j += 1

nonushta_buttons = ReplyKeyboardMarkup(resize_keyboard=True,keyboard=keys)
