import logging
import asyncio
import os
from volume_analyze.Standard_deviation_and_Z_score.stream_analize import StandartDeviationAnalize
from dotenv.main import load_dotenv
from aiogram import Bot, Dispatcher, executor, types
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from tg_bot.apsched import send_message_interval



load_dotenv()
API_TOKEN = os.environ['BOT_TOKEN']

# Configure logging
#logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def echo(message: types.Message):
    await bot.send_message(message.chat.id, str(message.chat.id))

@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    deviation = StandartDeviationAnalize()
    result = deviation.analize()
    await bot.send_message(691902762, result)


if __name__ == '__main__':
    scheduler = AsyncIOScheduler(timezone='Europe/Moscow')
    scheduler.add_job(send_message_interval, trigger='interval', seconds=60, kwargs={'bot': bot})
    scheduler.start()
    print('sheduler started!')



    executor.start_polling(dp, skip_updates=True)


