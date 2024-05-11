import logging
import asyncio
from aiogram import Bot, Dispatcher
from config_reader import config
from handlers import questions, different_types

# Запуск бота
async def main():
    bot = Bot(token=config.bot_token.get_secret_value(),  parse_mode="HTML")
    dp = Dispatcher()

    dp.include_routers(questions.router, different_types.router)
    # Запускаем бота и пропускаем все накопленные входящие
    # Да, этот метод можно вызвать даже если у вас поллинг
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())