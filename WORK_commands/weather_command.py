"""ПОГОДА"""
import json
import types
from aiogram import *
from content.API_content import API_weather
import requests


class CreateWeather:
    def __init__(self, trigger, command, city, response):
        self.trigger = trigger
        self.command = command
        self.city = city
        self.response = response

    # ошибка
    def call_error(self):
        pass

    # получение данных json
    def create_data(self):
        print(json.dumps(self.response.json(), indent=4, ensure_ascii=False))
        data = self.response.json()
        dt = data['main']
        return dt



async def weather_info(message: types.Message):
    # обработка строки
    com_word_mes = message.text.split(' ', 2)
    trigger = com_word_mes[0].lower()  # тригер слово
    command = com_word_mes[1].lower()  # команда
    city = com_word_mes[2]  # город

    # GET-запрос
    response = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&lang=ru&units=metric&appid={API_weather}"
    )

    if trigger == 'ифи' and command == 'погода':

        create_weather = CreateWeather(trigger, command, city, response)
        weather_data = create_weather.create_data()
        await message.answer(weather_data)




