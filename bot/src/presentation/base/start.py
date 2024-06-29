from aiogram import types
from domain.message import Message as MessageDomain
from infrastructure.external_api import message_client


async def start_command(message: types.Message) -> types.Message:
    return await message.answer(text="Hello, World!")
