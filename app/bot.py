from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from .config import BOT_TOKEN, DEFAULT_PARSE_MODE


bot = Bot(token=BOT_TOKEN, parse_mode=DEFAULT_PARSE_MODE)

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)






