from aiogram import Router
from aiogram.types.message import Message
from aiogram.filters.command import CommandStart, Command 

import keyboards as kb


router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Please choose your language / Пожалуйста, выберите ваш язык", reply_markup=kb.select_lang)
