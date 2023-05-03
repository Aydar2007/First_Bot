"""1) Напишите телеграмм бот который загадывает случайное число с помощью
библиотеки random и вы должны угадать его.
Бот: Я загадал число от 1 до 3 угадайте
Пользователь: Вводит число 2, если число правильное то выводит “Правильно вы
отгадали”"""
from aiogram import Bot, Dispatcher,types,executor
bot=Bot("5873054581:AAE5z8uUDqc_sk5FzmkE2tB7bs1PDTEyVts")
dp=Dispatcher(bot)

import random
while True:
    a=random.randint(1,3)
    break
@dp.message_handler(commands=["start","go"])
async def start(message:types.message):
    await message.answer("Привет!,для списка команд:\n /command")

@dp.message_handler(commands=["Привет","привет","ПРИВЕТ"])
async def start2(message:types.message):
    await message.answer("Привет!,для списка команд:\n /command")


@dp.message_handler(commands=["start","go"])
async def start3(message:types.message):
    await message.answer("Привет!,для списка команд:\n /command")

@dp.message_handler(commands=["command"])
async def commands(message:types.message):
    await message.answer("/start-запускает, /go-запускает , /game-начинает игру с отгадыванием цифры")

@dp.message_handler(commands=["game"])
async def game(message:types.message):
    await message.answer("Отгадай загаданное число от /1 ,/2 или /3")



    @dp.message_handler(commands="1")
    async def game1(message:types.message):
        if a == 1:
            await message.answer(f"ВЫ были правы ☻ я загадал число 1")
        else:
            await message.answer(f"ВЫ ошиблись я загадал число {a}")

    @dp.message_handler(commands="2")
    async def game2 (message:types.message):
        if a == 2:
            await message.answer(f"ВЫ были правы ☻ я загадал число 2")
        else:
            await message.answer(f"ВЫ ошиблись я загадал число {a}")

    @dp.message_handler(commands="3")
    async def game3 (message:types.message):
        if a == 3:
            await message.answer(f"ВЫ были  правы ☻ я загадал число 3")
        else:
            await message.answer(f"ВЫ ошиблись я загадал число {a}")
                                 
    @dp.message_handler()
    async def end (message:types.message):
        await message.answer("Я вас не понял, для списка команд:\n /command")


# @dp.message_handler()
# async def end (message:types.message):
#     await message.answer("Я вас не понял, для списка команд:\n /command")
executor.start_polling(dp)
