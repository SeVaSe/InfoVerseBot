"""ГЛАВНЫЙ ФАЙЛ"""
from aiogram import Bot, Dispatcher, executor, types
from content.API_content import *
from content.TEXT_content import *
from WORK_commands import weather_command



# конфиг бота
bot = Bot(API_bot)
dp = Dispatcher(bot)


# функция обозначения запуска
async def on_start(_):
    print('Бот запущен')


# отправка стартового соо
@dp.message_handler(commands=['start'])
async def start_bot(message: types.Message):
    await message.answer(text_start)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_start)












