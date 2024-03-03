from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram import Router, types, F
from aiogram.types import Message
from aiogram.filters import Command
from de_parser import coinpars

coin = ''

router = Router()


@router.message(Command('start'))
async def hell(message: Message):
    await message.answer("Hello")


@router.message(F.text.lower)
async def coin_request(message: Message):
    global coin
    coin = message.text
    result = await coinpars(coin)
    await message.answer(str(result))