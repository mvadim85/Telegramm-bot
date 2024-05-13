import logging
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.methods import SendMessage
from config_reader import config
from handlers import questions, different_types
from keyboards.for_questions import get_yes_no_kb

# Запуск бота
async def main(text):
    vot = Bot(token=config.bot_token.get_secret_value(),  parse_mode="HTML")

    await vot.send_message(chat_id="615228120", text="sdfasfd", reply_markup=get_yes_no_kb())
    # Запускаем бота и пропускаем все накопленные входящие
    # Да, этот метод можно вызвать даже если у вас поллинг


asyncio.run(main(text))