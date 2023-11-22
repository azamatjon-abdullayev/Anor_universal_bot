from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.Bolalar_menyusi import bolalar_buttons
from keyboards.default.Nonushta_uchun import nonushta_buttons
from keyboards.default.supermarket import supermarket_buttons
# from keyboards.default.Nonushta uchun import nonushta_buttons
from keyboards.default.Pitsa_uchun import pitsa_buttons
from keyboards.default.Taomlar import taomlar_buttons
from keyboards.default.Ichimliklar import ichimliklar_buttons
from keyboards.default.Fast_food import fast_food_buttons


from loader import dp, base, bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    ism = message.from_user.first_name
    familya = message.from_user.last_name
    user_name = message.from_user.username
    user_id = message.from_user.id
    try:
        base.user_qoshish(ism=ism, tg_id=user_id, fam=familya, username=user_name)
    except Exception as x:
        print(x)
    await message.answer(f"Salom", reply_markup=supermarket_buttons)


@dp.message_handler(text='Taomlar')
async def bot_start(message: types.Message):
    await message.answer(f"tanlovni amalga oshiring", reply_markup=taomlar_buttons)


@dp.message_handler(text='Ichimliklar')
async def bot_start(message: types.Message):
    await message.answer(f"tanlovni amalga oshiring", reply_markup=ichimliklar_buttons)


@dp.message_handler(text='Pitsa')
async def bot_start(message: types.Message):
    await message.answer(f"tanlovni amalga oshiring", reply_markup=pitsa_buttons)


@dp.message_handler(text='Nonushta uchun')
async def bot_start(message: types.Message):
    await message.answer(f"tanlovni amalga oshiring", reply_markup=nonushta_buttons)


@dp.message_handler(text='Fast food')
async def bot_start(message: types.Message):
    await message.answer(f"tanlovni amalga oshiring", reply_markup=fast_food_buttons)

@dp.message_handler(text='Bolalar menyusi')
async def bot_start(message: types.Message):
    await message.answer(f"tanlovni amalga oshiring", reply_markup=bolalar_buttons)


@dp.message_handler(text='Ortga')
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!", reply_markup=supermarket_buttons)


@dp.message_handler(commands='users',)
async def bot_start(message: types.Message):
    soni = base.user_sanash()
    await message.answer(text=f"Botdan {soni} ta odam foydalanmoqda ")


@dp.message_handler(commands='reklama', )
async def bot_start():

    userlar = base.barcha_foydalanuvchilarni_tanlash()

    for user in userlar:
        user_id = user[4]
        await bot.send_message(chat_id=user_id, text=f"Bu reklama")
