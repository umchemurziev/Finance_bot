from aiogram import types
from aiogram.dispatcher.filters.builtin import Command

from data.config import ADMINS, ME, my_binance_api_key, my_binance_api_secret, STANISLAV, STANISLAV_binance_api_key, \
    STANISLAV_binance_api_secret, ANDREW, Andrew_binance_api_key, Andrew_binance_api_secret
from loader import dp

from binanceBalance.script import getBalanceSheet


@dp.message_handler(Command("binance"))
async def bot_binance(message: types.Message):
    if message.from_user.id == ME:
        await message.answer(f"Вот ваша статистика баланса, {message.from_user.full_name}!")
        csv_rows = getBalanceSheet(my_binance_api_key, my_binance_api_secret)
        with open('positions.csv', 'w') as f:
            f.write("\n".join(csv_rows))
        f = open('positions.csv', 'r')
        await message.answer_document(f)
    elif message.from_user.id == ANDREW:
        await message.answer(f"Вот ваша статистика баланса, {message.from_user.full_name}!")
        csv_rows = getBalanceSheet(Andrew_binance_api_key, Andrew_binance_api_secret)
        with open('positions.csv', 'w') as f:
            f.write("\n".join(csv_rows))
        f = open('positions.csv', 'r')
        await message.answer_document(f)
    elif message.from_user.id == STANISLAV:
        await message.answer(f"Вот ваша статистика баланса, {message.from_user.full_name}!")
        csv_rows = getBalanceSheet(STANISLAV_binance_api_key, STANISLAV_binance_api_secret)
        with open('positions.csv', 'w') as f:
            f.write("\n".join(csv_rows))
        f = open('positions.csv', 'r')
        await message.answer_document(f)
    else:
        return await message.answer(f"У вас нет доступа, {message.from_user.full_name}!")
