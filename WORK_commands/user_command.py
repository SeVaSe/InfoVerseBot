"""ПОЛЬЗОВАТЕЛЬСКТЕ КОМАНДЫ"""
from aiogram import types
import random


# кости игральные
async def play_dice(message: types.Message, bot):
    await bot.send_dice(message.chat.id)