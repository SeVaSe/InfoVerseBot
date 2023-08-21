"""ГЛАВНЫЙ ФАЙЛ"""
from aiogram import Bot, Dispatcher, executor, types
from content.API_content import *
from content.TEXT_content import *
from WORK_commands.weather_command import weather_ordinary, weather_full, weather_tommorow#, weather_forecast
from WORK_commands.feedBack_command import feedback
from WORK_commands.user_command import *
from WORK_commands.translate_command import translate_command
from WORK_commands.wiki_command import *

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
    text = message.text.lower().split()
    if text[0] == 'ифи':
        if text[1] == 'ошибка:':
            print(1)
            await feedback(message, bot)
        elif text[1] == 'погода':
            if text[2] == 'завтра':
                print(3)
                await weather_tommorow(message)
            elif text[2] == 'фулл':
                print(4)
                await weather_full(message)
            else:
                print(5)
                await weather_ordinary(message)
        # elif text[1] == 'прогноз':
        #     print(6)
            #await weather_forecast(message)
        elif text[1] == 'ролл':
            print(7)
            await play_dice(message, bot)
        elif text[1] == 'команды':
            print(8)
            await command_help(message, bot)
        elif text[1] == 'переведи' and text[2] == 'на':
            print(9)
            await translate_command(message)
        elif text[1] == 'вики':
            print(10)
            await wiki_command(message)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_start)
