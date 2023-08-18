from aiogram import types

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
