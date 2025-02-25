import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram import F

from settings import TOKEN, URL_PATTERN, ALLOWED_USERS


bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(F.text)
async def handle_message(message: types.Message):
    user_id = message.from_user.id

    if user_id not in ALLOWED_USERS:
        return

    urls = URL_PATTERN.findall(message.text)

    if not urls:
        return

    await message.reply(f"📽️ Обнаружена ссылка: {urls[0]}")
