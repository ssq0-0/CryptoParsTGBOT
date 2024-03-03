import requests
import apikey
import aiohttp
import logging
logging.basicConfig(level=logging.INFO)
from tg_token import api_key


async def cryptorank_requests():
    logging.info("Making request to CryptoRank API")
    link = f"https://api.cryptorank.io/v1/currencies?{api_key}"
    data = requests.get(link)  # Этот вызов должен быть асинхронным, если функция асинхронная
    logging.info(f"Response from CryptoRank API: {data.text}")
    return data.json()  # Предполагается, что вы хотите работать с данными в формате JSON


async def coinpars(coinname):
    data = await cryptorank_requests()
    for token in data['data']:
        if token['name'].lower() == coinname or token['symbol'].lower() == coinname:
            print(token)
            return token['id']

