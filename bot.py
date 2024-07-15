import asyncio
from os import getenv

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command


bot = Bot(getenv('BOT_TOKEN'))

dp = Dispatcher()


@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    await message.answer('Hi!')

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
