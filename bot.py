import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# 🔑 ВСТАВ СЮДИ СВІЙ ТОКЕН ВІД BOTFATHER
TOKEN = "8532748795:AAGBWiCoIVOUkLDmuFsxcX4gUr_Iu82zc6E"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# /start команда
@dp.message(F.text == "/start")
async def start(message: Message):

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🍋 Play Lime Empire",
                web_app=WebAppInfo(
                    url="https://github.com/alexkuzyshyn12-del/lime-empire/settings/pages"
                )
            )
        ]
    ])

    await message.answer(
        "🍋 Welcome to Lime Empire!",
        reply_markup=keyboard
    )

# запуск бота
async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())