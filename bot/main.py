import asyncio
from os import getenv

from aiogram import Bot, Dispatcher
from handlers import router


async def main():
    bot = Bot(getenv('BOT_TOKEN'))
    dp = Dispatcher()

    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try: 
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot disabled")
        