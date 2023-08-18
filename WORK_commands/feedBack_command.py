from aiogram import types
from content.TEXT_content import text_wrong_input

# ID группы админов
admin_group_id = -1001657428568


# функция обратной связи
async def feedback(message: types.Message, bot):

    msg = message.text   # сообщение пользователя
    words = msg.split(' ')   # список слов сообщения

    # тригер "ифи ошибка:"
    if words[0].lower() == 'ифи' and words[1].lower() == 'ошибка:':

        error_message = ' '.join(words[2:])   # соединяем слова сообщения без тригера

        # тег пользователя
        user_tag = message.from_user.username

        await bot.send_message(chat_id=admin_group_id, text=f"@{user_tag}: {error_message}", parse_mode='HTML')
    # если команда введена не правильно
    else:
        await message.answer(text=text_wrong_input)
        
