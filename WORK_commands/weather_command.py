"""ПОГОДА"""
import json
import types
from aiogram import *
from content.API_content import API_weather
import requests
import datetime
import math


# создание погоды
class CreateWeather:
    code_to_smile = {
        "Clear": "Ясно ☀️",
        "Clouds": "Облачно ☁️",
        "Rain": "Дождь 🌧",
        "Drizzle": "Маленький дождь 🌦",
        "Thunderstorm": "Гроза ⛈",
        "Snow": "Снег ❄️",
        "Mist": "Туман 😶‍🌫️"
    }

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
        # РАСПАКОВКА ДАННЫХ ИЗ JSON
        data = self.response.json()  # json данные
        city = data['name']
        weather = data['weather'][0]['main']
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        temp_min = data['main']['temp_min']
        temp_max = data['main']['temp_max']
        pressure = data['main']['pressure']
        humidity = data['main']['humidity']
        wind = data['wind']['speed']
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day = sunset_timestamp - sunrise_timestamp

        if weather in self.code_to_smile:
            wd = self.code_to_smile[weather]
        else:
            wd = "Не пойму погоду, попробуй сам определить 😢"

        text_weather = f'''📅 Погода на {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')} 
        
        
    🏙 Погода в городе: {city} 
    
    Температура: {temp}°C {wd}
    
    🌡 Ощущается как: {feels_like}°C 
    
    💨 Ветер: {wind} м/с 
    
    📈 Максимально возможная температура: {temp_max}°C 
    
    📉 Минимально возможная температура: {temp_min}°C 
    
    🧼 Давление: {math.ceil(pressure/1.333)} мм.рт.ст
    
    💧 Влажность: {humidity} %
    
    🌅 Восход солнца: {sunrise_timestamp} 
    
    🌄 Закат солнца: {sunset_timestamp} 
    
    ⏱ Продолжительность дня: {length_of_the_day} 
    
    
❤️ Приятного времяпровождения! 
        '''


        return text_weather


# функция погоды
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




