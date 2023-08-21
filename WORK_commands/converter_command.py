from aiogram import types
from forex_python.converter import CurrencyRates


# функция конвертера
async def command_converter(message: types.Message):
    msg = message.text  # сообщение пользователя
    words = msg.split(' ')  # список слов сообщения

    if words[3].upper() == 'RUB':
        total = float(words[2])    # сумма для конвертации
        convert_currency = words[4].upper()    # валюта, в которую конвертируем

        c = CurrencyRates()
        converted_total = c.convert('RUB', convert_currency, total)
        await message.reply(f"{total} RUB = {converted_total:.2f} {convert_currency}")

    elif words[3].upper() == 'USD':
        total = float(words[2])    # сумма для конвертации
        convert_currency = words[4].upper()    # валюта, в которую конвертируем

        c = CurrencyRates()
        converted_total = c.convert('USD', convert_currency, total)
        await message.reply(f"{total} USD = {converted_total:.2f} {convert_currency}")

    elif words[3].upper() == 'EUR':
        total = float(words[2])    # сумма для конвертации
        convert_currency = words[4].upper()   # валюта, в которую конвертируем

        c = CurrencyRates()
        converted_total = c.convert('EUR', convert_currency, total)
        await message.reply(f"{total} EUR = {converted_total:.2f} {convert_currency}")
