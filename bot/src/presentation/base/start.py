from aiogram import types


async def start_command(message: types.Message) -> types.Message:
    return await message.answer(text="Hello, World!")
