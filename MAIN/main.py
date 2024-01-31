import asyncio
import logging
import time

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from datetime import datetime

dp = Dispatcher()
logging.basicConfig(level=logging.INFO)

HELP_COMMAND = """
/help - список комманд
/start - начать работу с ботом
/gimme - Отправаляет красивый стикер
/count - считает количесвто вызывов этой функцией
/dice - присылает эмодзи(кубик)
/info - время запуска бота
/reply_heart - 
"""
count = 0
dp["started_at"] = datetime.now().strftime("%Y-%m-%d %H:%M")


@dp.message(Command("info"))
async def cmd_info(message: types.Message, started_at: str):
    await message.answer(f"Бот запущен {started_at}")


@dp.message(Command("gimme"))
async def sticker_give(message: types.Message, bot=None):
    for i in range(1, 5, 1):
        await bot.send_sticker(message.from_user.id,
                               sticker="CAACAgIAAxkBAAELRjNlt5ArSlWlQu5GWsRqV2dx3m8PLAACwhcAAmsgUEjKrGkqZXjZETQE")


@dp.message(Command("dice"))
async def cmd_dice(message: types.Message):
    await message.answer_dice(emoji="🎲")


@dp.message(Command("count"))
async def check_count(message: types.Message):
    global count
    await message.answer(f'COUNT: {count}')
    count += 1


@dp.message(Command("help"))
async def help_command(message: types.Message):
    await message.reply(text=HELP_COMMAND)


@dp.message(Command("start"))
async def help_command(message: types.Message):
    await message.delete()
    await message.answer("<em>Добро пожаловать в нашего <b>ботяру!</b></em>", parse_mode="HTML")


@dp.message(Command("reply_heart"))
async def reply_heart(message: types.Message, string=None):
    a = input(string("Напиши что-то"))
    await message.reply(a + "❤️")


@dp.message()
async def echo_upper(message: types.Message):
    if message.text.count(' ') >= 1:
        await message.answer(text=message.text.upper())
    else:
        await message.answer(text=message.text.capitalize())


async def start_bot(bot: Bot):
    await bot.send_message(1026131979, text='Бот запущен!')


async def stop_bot(bot: Bot):
    await bot.send_message(1026131979, text='Бот остановлен!')


async def main():
    bot = Bot(token="6914705938:AAEv4_7-6VoXhJGVGYSqLxJcm50XJliSrww")

    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
