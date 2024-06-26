import logging
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.methods import SendMessage
from config_reader import config
from handlers import questions, different_types
from keyboards.for_questions import get_yes_no_kb

# Запуск бота
async def main(text):
    bot = Bot(token=config.bot_token.get_secret_value(),  parse_mode="HTML")
    dp = Dispatcher()

    dp.include_routers(questions.router, different_types.router)
    await bot.send_message(chat_id="615228120", text="sdfasfd", reply_markup=get_yes_no_kb())
    # Запускаем бота и пропускаем все накопленные входящие
    # Да, этот метод можно вызвать даже если у вас поллинг
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    text = "asdfasdf"
    asyncio.run(main(text))
