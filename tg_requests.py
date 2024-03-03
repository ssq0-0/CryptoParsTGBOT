from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from de_parser import id_pars
import re

coin = ''

router = Router()


@router.message(Command('start'))
async def hell(message: Message):
    await message.answer("Hello")


@router.message(F.text.lower())
async def coin_request(message: Message):
    global coin
    match = re.match(r'^(\d+(\.\d+)?)(\s+)?(.+)?$', message.text.lower())
    if match:
        number = float(match.group(1)) if match.group(1) else None
        coin = match.group(4).strip() if match.group(4) else None
        coin_price = await id_pars(coin)
        result = number * coin_price
    else:
        number = None
        coin = message.text.lower().strip()
        result = await id_pars(coin)
    await message.answer(f"{result:.2f}$")
