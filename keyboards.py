from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Toshkent'),
            KeyboardButton('Samarqand'),
        ],
        [
            KeyboardButton('Termez'),
            KeyboardButton('Sirdaryo'),
        ],
        [
            KeyboardButton('Qashqadaryo'),
            KeyboardButton('Buxoro'),
        ],
        [
            KeyboardButton('Jizzax'),
            KeyboardButton('Urgench'),
        ],
        [
            KeyboardButton('Navoiy'),
            KeyboardButton('Namangan'),
        ],
        [
            KeyboardButton('Andijon'),
            KeyboardButton('Fargona'),
        ]
    ],
    resize_keyboard=True
)

