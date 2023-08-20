from aiogram import types
from translate import Translator
from langid import classify
from content.TEXT_content import text_wrong_lang, text_translate

languages = ['de', 'en', 'ru'] # список доступных языков


async def translate_command(message: types.Message):

    msg = message.text  # сообщение пользователя
    words = msg.split(' ')  # список слов сообщения
    text_to_translate = ' '.join(words[4:])   # текст для перевода

    detected_lang, _ = classify(text_to_translate)  # распознавание языка

    # если язык есть в списке доступных языков
    if detected_lang in languages:

        if words[3] == 'немецкий:':

            translator = Translator(from_lang=detected_lang, to_lang='de')
            translation = translator.translate(text_to_translate)
            await message.reply(f' Перевод: {translation} \n [{text_translate}]')

        elif words[3] == 'английский:':

            translator = Translator(from_lang=detected_lang, to_lang='en')
            translation = translator.translate(text_to_translate)
            await message.reply(f' Перевод: {translation} \n [{text_translate}]')

        elif words[3] == 'русский:':

            translator = Translator(from_lang=detected_lang, to_lang='ru')
            translation = translator.translate(text_to_translate)
            await message.reply(f' Перевод: {translation} \n [{text_translate}]')

    else:
        await message.reply(text_wrong_lang)
