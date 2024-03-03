import requests
import aiohttp
import logging
import datetime
from tg_token import api_key


logging.basicConfig(level=logging.INFO)

last_request_time = None
cached_data = None


async def cryptorank_requests():
    global last_request_time, cached_data
    current_time = datetime.datetime.now()

    if last_request_time is None or (current_time - last_request_time) > datetime.timedelta(days=1):
        logging.info("Making request to CryptoRank API")
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
            link = f"https://api.cryptorank.io/v1/currencies?{api_key}"
            async with session.get(link) as response:
                data = await response.json()
                logging.info("Response from CryptoRank API received")
                cached_data = data
                last_request_time = current_time
    else:
        logging.info("Using cached data")
    return cached_data


async def id_pars(coinname):
    data = await cryptorank_requests()
    for token in data['data']:
        if token['name'].lower() == coinname or token['symbol'].lower() == coinname:
            result = await price_pars(token['id'])
            return float(result)


async def price_pars(id):
    link = f"https://api.cryptorank.io/v1/currencies/{id}?{api_key}"
    response =  requests.get(link)
    data = response.json()
    price_info = data['data']['values']['USD']
    price = price_info['price']
    return float(price)
