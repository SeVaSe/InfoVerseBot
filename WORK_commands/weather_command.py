"""ПОГОДА"""
import json
import types
import aiogram
from aiogram import *
from content.API_content import API_weather
import requests
import datetime
import math
from content.TEXT_content import *


class CreateDataWeather:
    """КЛАСС ПО РАСПАКОВКЕ ДАНЫХ"""
    code_to_smile = {
        "Clear": "☀️ Ясно",
        "Clouds": "☁️ Облачно",
        "Rain": "🌧 Дождь",
        "Drizzle": "🌦 Маленький дождь",
        "Thunderstorm": "⛈ Гроза",
        "Snow": "❄️ Снег",
        "Mist": "😶‍🌫️ Туман"
    }

    def __init__(self, response):
        self.response = response

    # анпакинг данных на сегодня и завтра
    def data_unpacking_weather(self):
        """АНПАКИНГ ДАННЫХ НА СЕГОДНЯ И ЗАВТРА"""
        # РАСПАКОВКА ДАННЫХ ИЗ JSON
        self.data = self.response.json()
        self.city = self.data['city']['name']

        # на сегодня
        self.temp_m = self.data['list'][2]['main']['temp']  # утро
        self.temp_d = self.data['list'][4]['main']['temp']  # день
        self.temp_n = self.data['list'][6]['main']['temp']  # вечер
        # осадки
        self.wea_m = self.code_to_smile[self.data['list'][2]['weather'][0]['main']]  # утро
        self.wea_d = self.code_to_smile[self.data['list'][4]['weather'][0]['main']]  # день
        self.wea_n = self.code_to_smile[self.data['list'][6]['weather'][0]['main']]  # вечер

        # на завтра
        self.temp_m_f = self.data['list'][10]['main']['temp']  # утро
        self.temp_d_f = self.data['list'][12]['main']['temp']  # день
        self.temp_n_f = self.data['list'][14]['main']['temp']  # вечер
        # осадки
        self.wea_m_f = self.code_to_smile[self.data['list'][10]['weather'][0]['main']]  # утро
        self.wea_d_f = self.code_to_smile[self.data['list'][12]['weather'][0]['main']]  # день
        self.wea_n_f = self.code_to_smile[self.data['list'][14]['weather'][0]['main']]  # вечер

    # анпакинг фулл данных на сегодня
    def data_unpacking_full(self):
        """АНПАКИНГ ФУЛЛ ДАННЫХ НА СЕГОДНЯ"""
        # РАСПАКОВКА ДАННЫХ ИЗ JSON
        self.data_full = self.response.json()  # json данные
        self.city_full = self.data_full['name']
        self.weather_full = self.data_full['weather'][0]['main']
        self.temp_full = self.data_full['main']['temp']
        self.feels_like_full = self.data_full['main']['feels_like']
        self.temp_min_full = self.data_full['main']['temp_min']
        self.temp_max_full = self.data_full['main']['temp_max']
        self.pressure_full = self.data_full['main']['pressure']
        self.humidity_full = self.data_full['main']['humidity']
        self.wind_full = self.data_full['wind']['speed']
        self.sunrise_timestamp_full = datetime.datetime.fromtimestamp(self.data_full["sys"]["sunrise"])
        self.sunset_timestamp_full = datetime.datetime.fromtimestamp(self.data_full["sys"]["sunset"])
        self.length_of_the_day_full = self.sunset_timestamp_full - self.sunrise_timestamp_full

        if self.weather_full in self.code_to_smile:
            self.wd = self.code_to_smile[self.weather_full]
        else:
            self.wd = "Не пойму погоду, попробуй сам определить 😢"

    # анпакинг данных на завтра
    def data_unpacking_tommorow(self):
        """АНПАКИНГ ДАННЫХ НА ЗАВТРА"""
        self.data_tom = self.response.json()  # json данные
        time_12 = []

        count = 0
        for time_zone in self.data_tom['list']:
            dt = time_zone['dt_txt']
            dt_date, dt_time = dt.split(' ')
            dt_time_parts = dt_time.split(':')
            twelv = dt_time_parts[0]

            if twelv == '12':
                time_12.append(count)

            count += 1

        index_tom = time_12[0]

        print(time_12)
        print(index_tom)
        # РАСПАКОВКА ДАННЫХ ИЗ JSON
        self.city_tom = self.data_tom['city']['name']
        self.weather_tom = self.data_tom['list'][index_tom]['weather'][0]['main']
        self.temp_tom = self.data_tom['list'][index_tom]['main']['temp']
        self.feels_like_tom = self.data_tom['list'][index_tom]['main']['feels_like']
        self.temp_min_tom = self.data_tom['list'][index_tom]['main']['temp_min']
        self.temp_max_tom = self.data_tom['list'][index_tom]['main']['temp_max']
        self.pressure_tom = self.data_tom['list'][index_tom]['main']['pressure']
        self.humidity_tom = self.data_tom['list'][index_tom]['main']['humidity']
        self.wind_tom = self.data_tom['list'][index_tom]['wind']['speed']
        self.dt_tom = self.data_tom['list'][index_tom]['dt_txt']

        if self.weather_tom in self.code_to_smile:
            self.wd_tom = self.code_to_smile[self.weather_tom]
        else:
            self.wd_tom = "Не пойму погоду, попробуй сам определить 😢"


# создание погоды
class CreateWeather(CreateDataWeather):
    """КЛАСС ПО СОЗДАНИЮ ПОГОДЫ"""
    def __init__(self, response):
        super().__init__(response)  # Вызываем конструктор родительского класса

    # получение данных json и создание погоды
    def create_weather(self):
        """СОЗДАНИЕ ПОГОДЫ НА СЕГОДНЯ И ЗАВТРА (класс)"""
        try:
            text_weather = f'''Прогноз погоды для  🌿{self.city}🌿  на сегодня:
            - Утро: {self.temp_m}°C, {self.wea_m}
            - День: {self.temp_d}°C, {self.wea_d}
            - Вечер: {self.temp_n}°C, {self.wea_n}
            
Прогноз погоды для  🌿{self.city}🌿  на завтра:
            - Утро: {self.temp_m_f}°C, {self.wea_m_f}
            - День: {self.temp_d_f}°C, {self.wea_d_f}
            - Вечер: {self.temp_n_f}°C, {self.wea_n_f}
            '''

            return text_weather
        except KeyError:
            return

    # получение данных json и создание погоды
    def create_weather_full(self):
        """СОЗДАНИЕ ПОГОДЫ ФУЛЛ (класс)"""
        try:
            text_weather = f'''📅 Погода на {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n
        - Погода в городе: {self.city_full} 🏙
        - Температура: {self.temp_full}°C {self.wd}
        - Ощущается как: {self.feels_like_full}°C 🌡
        - Ветер: {self.wind_full} м/с 💨
        - Максимально возможная температура: {self.temp_max_full}°C 📈
        - Минимально возможная температура: {self.temp_min_full}°C 📉
        - Давление: {math.ceil(self.pressure_full / 1.333)} мм.рт.ст ⬇️
        - Влажность: {self.humidity_full} % 💧
        - Восход солнца: {self.sunrise_timestamp_full} 🌅
        - Закат солнца: {self.sunset_timestamp_full} 🌄
        - Продолжительность дня: {self.length_of_the_day_full} ⏱\n\n
❤️ Приятного времяпровождения!
            '''

            print(json.dumps(self.data_full, indent=4, ensure_ascii=False))
            return text_weather
        except KeyError:
            return

    # получение данных json и создание погоды
    def create_weather_tommorow(self):
        """СОЗДАНИЕ ПОГОДЫ НА ЗАВТРА (класс)"""
        try:
            text_weather = f'''📅 Погода на завтра\n\n
        - Погода в городе: {self.city_tom} 🏙
        - Температура: {self.temp_tom}°C {self.wd_tom}
        - Ощущается как: {self.feels_like_tom}°C 🌡
        - Ветер: {self.wind_tom} м/с 💨
        - Максимально возможная температура: {self.temp_max_tom}°C 📈
        - Минимально возможная температура: {self.temp_min_tom}°C 📉
        - Давление: {math.ceil(self.pressure_tom / 1.333)} мм.рт.ст ⬇️
        - Влажность: {self.humidity_tom} % 💧\n\n
❤️ Приятного времяпровождения!
            '''

            print(json.dumps(self.data_tom, indent=4, ensure_ascii=False))
            return text_weather
        except KeyError:
            return


# функция погоды сегодня и завтра
async def weather_ordinary(message: types.Message):
    """ФУНКЦИЯ ПОГОДЫ СЕГОДНЯ И ЗАВТРА"""
    mes = message.text.split(' ', 2)
    city = mes[2]

    print(city)

    # GET-запросы
    response = requests.get(
        f"http://api.openweathermap.org/data/2.5/forecast?q={city}&cnt=16&lang=ru&units=metric&appid={API_weather}"
    )

    print(json.dumps(response.json(), indent=4))

    cr = CreateWeather(response)
    cr.data_unpacking_weather()
    weather_data = cr.create_weather()
    await message.answer(weather_data)


# функция погоды фулл
async def weather_full(message: types.Message):
    """ФУНКЦИЯ ПОГОДЫ ФУЛЛ"""
    mes = message.text.split(' ', 3)
    city = mes[3]

    print(city)

    # GET-запросы
    response = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&lang=ru&units=metric&appid={API_weather}"
    )

    print(json.dumps(response.json(), indent=4))

    cr = CreateWeather(response)
    cr.data_unpacking_full()
    weather_data = cr.create_weather_full()
    await message.answer(weather_data)


# функция погоды на завтра
async def weather_tommorow(message: types.Message):
    """ФУНКЦИЯ ПОГОДЫ НА ЗАВТРА"""
    mes = message.text.split(' ', 3)
    city = mes[3]

    print(city)

    # GET-запросы
    response = requests.get(
        f"http://api.openweathermap.org/data/2.5/forecast?q={city}&cnt=16&lang=ru&units=metric&appid={API_weather}"
    )

    print(json.dumps(response.json(), indent=4))

    cr = CreateWeather(response)
    cr.data_unpacking_tommorow()
    weather_data = cr.create_weather_tommorow()
    await message.answer(weather_data)


# функция погоды на 5 дней
# async def weather_forecast(message: types.Message):
#     """ФУНКЦИЯ ПОГОДЫ НА 5 ДНЕЙ"""
#     mes = message.text.split(' ', 2)
#     city = mes[2]
#
#     print(city)
#
#     # GET-запросы
#     response = requests.get(
#         f"http://api.openweathermap.org/data/2.5/weather?q={city}&lang=ru&units=metric&appid={API_weather}"
#     )
#
#     print(json.dumps(response.json(), indent=4))
#
#     cr = CreateWeather(response)
#     cr.data_unpacking_tommorow()
#     weather_data = cr.create_weather_full()
#     await message.answer(weather_data)