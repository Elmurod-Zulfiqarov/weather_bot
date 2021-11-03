import requests
from config import dp, bot
from aiogram import types
from keyboards import main_keyboard


@dp.message_handler(commands=['start', 'help'])
async def start_and_help(message: types.Message):
    await message.reply('Botga hush kelibsiz, iltimos shaharingizni tanlang!', reply_markup=main_keyboard)

@dp.message_handler()
async def weather_sender(message: types.Message):
    city = message.text
    res = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=415a7d47092e3f4e796b8f123cefc0b6")
    if res.ok:
        d = res.json()
    await message.reply(str(d['main']['temp']-273.15))
                                               