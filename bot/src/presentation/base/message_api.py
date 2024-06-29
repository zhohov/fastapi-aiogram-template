from aiogram import types
from domain.message import Message as MessageDomain
from infrastructure.external_api import message_client


async def get_message_from_api(message: types.Message) -> types.Message:
    data = message_client.get_message()
    api_message: MessageDomain = MessageDomain(
        id=data.id,
        text=data.text,
    )
    
    return await message.answer(text=f"id: {api_message.id}, text: {api_message.text}")