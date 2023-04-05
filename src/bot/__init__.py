from aiogram.utils import executor
from aiogram import Dispatcher
from aiogram import Bot

from config import TELEGRAM_BOT_TOKEN
from .handlers import register_all_handlers


async def __on_start_up(dp: Dispatcher) -> None:
    register_all_handlers(dp)


def run_bot():
    bot = Bot(token=TELEGRAM_BOT_TOKEN, parse_mode='HTML')
    dp = Dispatcher(bot)
    executor.start_polling(dp, skip_updates=True, on_startup=__on_start_up)
