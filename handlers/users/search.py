from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command

from loader import dp
from states.search import Search
from binanceSearch.script import getCoinInfo, getMoreCoinInfo


@dp.message_handler(Command("search"), state=None)
async def enter_search(message: types.Message):
    await message.answer("\n".join(["Для поиска монеты отправьте её символ.", "Например: BTC"]))

    await Search.Find.set()


@dp.message_handler(state=Search.Find)
async def find_answer(message: types.Message, state: FSMContext):
    coin = message.text.upper()
    await state.update_data(coin_name=coin)
    await message.answer(getCoinInfo(coin))
    # await message.answer("Вам нужна более подробная информация?")

    await Search.next()
#
# @dp.message_handler(state=Search.MoreInfo)
# async def more_info_answer(message: types.Message, state: FSMContext):
#     need_more_info = False
#     data = await state.get_data()
#     coin = data.get("coin_name")
#     if message.text.upper() == "ДА" or message.text.upper() == "YES":
#         need_more_info = True
#
#     await state.update_data(need_info=need_more_info)
#
#     if need_more_info:
#         await message.answer(getMoreCoinInfo(coin))
#
#     await Search.next()
