import asyncio

from app.core import dp, bot


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
