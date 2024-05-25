import asyncio
from aiogram import Bot, Dispatcher
from tg_token import token
import tg_requests



async def main():
    bot = Bot(token=token)
    dp = Dispatcher()
    dp.include_routers(tg_requests.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
