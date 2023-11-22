# from aiogram import types
# from . import tarjima_bot_uchun
# from loader import dp, bot, base
#
# taom_maxsulotlar = base.select_all_pitsa()
#
# @dp.message_handler(text=[nomi[1] for nomi in taom_maxsulotlar])
# async def bot_echo(message: types.Message):
#     taom_nomi = message.text
#     taom = base.select_Taom(nomi=taom_nomi)
#     user_id = message.from_user.id
#     taom_narxi = taom[3]
#     rasm_manzili = taom[4]
#     await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption=f"Taom narxi : {taom_narxi} so'm")
