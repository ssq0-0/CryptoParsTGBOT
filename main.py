# import apikey
# import requests
#
#
# api = 'api_key=8ee1428c3dbdf56cf18e716b5b47152872f86d68223149b9403edc418d2a'
#
# params = {
#     'key1': 1,
#     'key2': api
# }
#
# link = f'https://api.cryptorank.io/v1/currencies/{params["key1"]}?{api}'
# response = requests.get(link, params=params)
# print(link)
# none = 'https://api.cryptorank.io/v1/currencies/?api_key=8ee1428c3dbdf56cf18e716b5b47152872f86d68223149b9403edc418d2a'
# print(response.text)
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