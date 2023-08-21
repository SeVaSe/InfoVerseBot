import asyncio
import unittest
from unittest.mock import MagicMock
import main
from main import start_main_func

class TestMainFuncBot(unittest.TestCase):
    def setUp(self):
        self.bot = MagicMock()

    async def test_weather_ord(self):
        message = MagicMock()
        message.text.lower.return_value = 'ифи погода москва'

        loop = asyncio.get_event_loop()
        asyncio.run_coroutine_threadsafe(start_main_func(message), loop)

        self.bot.send_message.assert_called_once()

    async def test_convert(self):
        message = MagicMock()
        message.text.lower.return_value = 'ифи конвертер 200 RUB USD'

        loop = asyncio.get_event_loop()
        asyncio.run_coroutine_threadsafe(start_main_func(message), loop)

        self.bot.send_message.assert_called_once()

    async def test_wiki(self):
        message = MagicMock()
        message.text.lower.return_value = 'ифи вики книга'

        loop = asyncio.get_event_loop()
        asyncio.run_coroutine_threadsafe(start_main_func(message), loop)

        self.bot.send_message.assert_called_once()

    async def test_trans(self):
        message = MagicMock()
        message.text.lower.return_value = 'ифи перевод англ: привет как дела ифи'

        loop = asyncio.get_event_loop()
        asyncio.run_coroutine_threadsafe(start_main_func(message), loop)

        self.bot.send_message.assert_called_once()

    async def test_feedback(self):
        message = MagicMock()
        message.text.lower.return_value = 'ифи ошибка: плохо работает переводчик'

        loop = asyncio.get_event_loop()
        asyncio.run_coroutine_threadsafe(start_main_func(message), loop)

        self.bot.send_message.assert_called_once()

    async def test_help(self):
        message = MagicMock()
        message.text.lower.return_value = 'ифи команды'

        loop = asyncio.get_event_loop()
        asyncio.run_coroutine_threadsafe(start_main_func(message), loop)

        self.bot.send_message.assert_called_once()

    async def test_play_dice(self):
        message = MagicMock()
        message.text.lower.return_value = 'ифи ролл'

        loop = asyncio.get_event_loop()
        asyncio.run_coroutine_threadsafe(start_main_func(message), loop)

        self.bot.send_message.assert_called_once()

if __name__ == '__main__':
    unittest.main()
