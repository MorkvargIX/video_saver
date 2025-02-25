from aiogram import Bot, Dispatcher, types
from aiogram import F

from app.settings import TOKEN, URL_PATTERN, ALLOWED_USERS
from app.logger import logger
from app.utils import is_video_url


bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(F.text)
async def handle_message(message: types.Message):
    user_id = message.from_user.id
    if user_id not in ALLOWED_USERS:
        logger.info("User is not in allowed users for saving video")
        return

    urls = URL_PATTERN.findall(message.text)
    if not urls:
        logger.info("Urls did not found in the user message")
        return

    video_url = urls[0]
    if is_video_url(video_url):
        logger.info(f"Video URL found: {video_url}")
        await message.reply(f"📽️ Url has been found")
    else:
        await message.reply(f"Current url is not video or not in allowed hosts {{youtube, vimeo}}")
