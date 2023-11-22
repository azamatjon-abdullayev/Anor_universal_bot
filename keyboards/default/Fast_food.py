from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

from loader import base

menu = base.select_maxsulotlar(turi='Fast food')

index = 0
keys = []
j=0
for maxsulot in menu:
    if j % 2 == 0 and j !=0:
        index += 1
    if j % 2 == 0:
        keys.append([KeyboardButton(text=f"{maxsulot[1]}")])
    else:
        keys[index].append(KeyboardButton(text=f"{maxsulot[1]}"))
    j += 1

fast_food_buttons = ReplyKeyboardMarkup(resize_keyboard=True,keyboard=keys)
