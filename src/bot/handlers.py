from aiogram import Dispatcher
from aiogram.dispatcher.filters import Text
from gpt import get_answer_gpt
from log import write_log


async def answer(msg):
    start_text = 'Нужно написать 5 комментариев о товаре, разделитель новая строка.  Короткие от 20 до 50 символов. Комментарии о опыте использования\n\nПост:'
    text = start_text + '\n' + msg.text[5:].strip()
    await msg.answer('Подождите, я подбираю ответ...')
    result = get_answer_gpt(text)
    await msg.answer(result)
    write_log(text, result)


async def other_answer(msg):
    text = msg.text[17:].strip()
    await msg.answer('Подождите, я подбираю ответ...')
    result = get_answer_gpt(f'{text}')
    await msg.answer(result)
    write_log(text, result)




def register_all_handlers(dp: Dispatcher):
    dp.register_message_handler(answer, Text(startswith='пост', ignore_case=True))
    dp.register_message_handler(other_answer, Text(startswith='мои настройки:', ignore_case=True))
