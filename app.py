from handers import bot, dp
from aiogram import executor

if __name__ == '__main__':
    executor.Executor(dp, skip_updates=True).start_polling()
