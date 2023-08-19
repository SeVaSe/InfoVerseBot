"""ГЛАВНЫЙ ФАЙЛ"""
from aiogram import Bot, Dispatcher, executor, types
from content.API_content import *
from content.TEXT_content import *
from WORK_commands.weather_command import weather_info
from WORK_commands.feedBack_command import feedback
from WORK_commands.user_command import *

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


# старт главных функций
@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def start_main_func(message: types.Message):
    if 'ифи ошибка' in message.text.lower():
        await feedback(message, bot)
    elif 'ифи погода' in message.text.lower():
        await weather_info(message)
    elif 'ифи ролл' in message.text.lower():
        await play_dice(message)






if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_start)
