import asyncio
import logging
import sys
import os

from aiogram import Bot, Dispatcher, Router, types, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold

from app.handlers import router
from app.database.models import async_main

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv('.env'))
# Bot token can be obtained via https://t.me/BotFather
TOKEN = os.getenv('TOKEN')



async def main() -> None:
    await async_main()
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot, skip_updates=True)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Bye!")