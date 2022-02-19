from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Список команд: ",
            "/start - Начать диалог",
            "/help - Получить справку",
            "/binance - Получить таблицу с вашими позициями в Binance",
            "/search - Найти информацию по монете")
    
    await message.answer("\n".join(text))
