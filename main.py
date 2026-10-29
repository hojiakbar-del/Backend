import asyncio
from aiogram.utils import formatting
from aiogram import Bot, Dispatcher
from aiogram.exceptions import (
    TelegramNetworkError,
    TelegramUnauthorizedError,
)
from config.settings import BOT_TOKEN
from handlers.users.time import rt as time
from handlers.users.start import rt as start
from handlers.users.prezident import rt as prezident
from handlers.users.car import rt as car
from handlers.users.formatting import rt as formatting
from handlers.users.info import rt as info
from handlers.users.message import rt as message
from handlers.users.admin import rt as admin
from handlers.users.me import rt as me
from handlers.users.kuchuk import rt as kuchuk
from handlers.users.random_kuchuk import rt as random_kuchuk
from handlers.users.random_mushuk import rt as random_mushuk
from handlers.users.mushuk import rt as mushuk
# from handlers.users.contact import rt as contact
# from handlers.users.test import rt as test
from handlers.users.animation import rt as animation
dp = Dispatcher()
async def main():
    bot = Bot(BOT_TOKEN)
    dp.include_router(start)
    dp.include_router(info)
    dp.include_router(prezident)
    dp.include_router(car)
    # dp.include_router(formatting)
    dp.include_router(time)
    # dp.include_router(message)
    dp.include_router(admin)
    dp.include_router(me)
    dp.include_router(kuchuk)
    dp.include_router(random_kuchuk)
    dp.include_router(random_mushuk)
    dp.include_router(mushuk)
    # dp.include_router(contact)
    # dp.include_router(test)
    dp.include_router(animation)
    await dp.start_polling(bot)
if __name__ == "__main__":
    try:
        print("bot ishga tushdi")
        asyncio.run(main())
    except KeyboardInterrupt:
        print("bot to'xtatildi")
    except TelegramNetworkError:
        print("internetga ulanish yo'q")
    except TelegramUnauthorizedError:
        print("token xato!")
