from aiogram import executor

from bot_dp import *
from handlers import client, other

client.register_handlers_client(dp)
other.register_handlers_other(dp)


async def on_startup(_):
    print("Бот запустился")


# Запуск бота
if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
