import logging

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware

storage = MemoryStorage()

admin_id = 478768504

# Токен бота
bot = Bot(token='5631096596:AAG4OZxb9vcz4AAE7EojkX3zs3h2Xg3SOM0', parse_mode=types.ParseMode.HTML)
# Диспетчер
dp = Dispatcher(bot, storage=storage)
# Устанавливаем логгирование
dp.middleware.setup(LoggingMiddleware())
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
