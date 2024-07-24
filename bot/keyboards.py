from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


select_lang = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Русский")],
                                            [KeyboardButton(text="English")]], resize_keyboard=True)
