from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from de_parser import id_pars

coin = ''

router = Router()


@router.message(Command('start'))
async def hell(message: Message):
    await message.answer("Hello")


@router.message(F.text.lower())
async def coin_request(message: Message):
    global coin
    coin = message.text.lower()
    result = await id_pars(coin)
    await message.answer(str(result))
