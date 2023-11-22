from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

from loader import base

menu = base.select_all_menu()

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
keys.append([KeyboardButton(text=f"Lokatsiya", request_location=True)])
keys[index].append(KeyboardButton(text=f"Kontakt",request_contact=True))
supermarket_buttons = ReplyKeyboardMarkup(resize_keyboard=True,keyboard=keys)
