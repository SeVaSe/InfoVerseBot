"""ВИКИ"""
"""ВИКИ"""
import wikipedia
import types
from aiogram import *
from bs4 import BeautifulSoup
import requests


async def wiki_command(message: types.Message):
    mes = message.text.split(' ', 2)
    wikipedia.set_lang('ru')

    search_query = mes
    search_result = wikipedia.search(search_query)

    if search_result:
        page = wikipedia.page(search_result[0])

        text_wiki = f'''📖 По вашему запросу найдена статья - {page.title} 📖

💭 Описание: {page.content[:1000]}'''
        await message.reply(text_wiki)
    else:
        await message.reply('Я ничего не смог найти по вашему запросу')



