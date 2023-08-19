"""ПОЛЬЗОВАТЕЛЬСКТЕ КОМАНДЫ"""
from aiogram import *
import random


# кости игральные
async def play_dice(message: types.Message):
    await bot.send_dice(chat_id=message.chat.id)