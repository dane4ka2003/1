import os
from aiogram import Bot, Dispatcher, executor, types
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from dotenv.main import load_dotenv
from tg_bot.apsched import send_message_interval
from volume_analyze.Standard_deviation_and_Z_score.stream_analize import StandartDeviationAnalize
from aiogram.types import ParseMode
from io import BytesIO

load_dotenv()
API_TOKEN = os.environ['BOT_TOKEN']

# Configure logging
# logging.basicConfig(level=logging.INFO)

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


# Функция для отправки сообщения через бота
async def send_message_to_user(chat_id, text, photo_path=None):
    if photo_path:
        with open(photo_path, 'rb') as photo:
            await bot.send_photo(chat_id, photo, caption=text, parse_mode=ParseMode.MARKDOWN)
    else:
        await bot.send_message(chat_id, text, parse_mode=ParseMode.MARKDOWN)




async def send_message_to_all(text, photo_path=None):
    user_list=[691902762]
    for chat_id in user_list:
        if photo_path:
            with open(photo_path, 'rb') as photo:
                await bot.send_photo(chat_id, photo, caption=text, parse_mode=ParseMode.MARKDOWN)
        else:
            await bot.send_message(chat_id, text, parse_mode=ParseMode.MARKDOWN)


def run_bot():
    scheduler = AsyncIOScheduler(timezone='Europe/Moscow')
    scheduler.add_job(send_message_interval, trigger='interval', seconds=60, kwargs={'bot': bot})
    scheduler.start()
    print('sheduler started!')

    executor.start_polling(dp, skip_updates=True)
    print('бот запущен!')


if __name__ == "__main__":
    run_bot()
