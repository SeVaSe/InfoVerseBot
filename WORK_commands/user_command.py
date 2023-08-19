"""ПОЛЬЗОВАТЕЛЬСКТЕ КОМАНДЫ"""
from aiogram import types
from content.TEXT_content import text_help, text_wrong_input
import random


# кости игральные
async def play_dice(message: types.Message, bot):
    await bot.send_dice(message.chat.id)


# функция "ифи команды"
async def command_help(message: types.Message, bot):
    await message.reply(text_help)
