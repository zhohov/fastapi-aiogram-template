__all__ = ("register_user_interaction_handlers",)

from aiogram import F, Router
from aiogram.filters import Command

from .start import start_command
from .message_api import get_message_from_api


def register_user_interaction_handlers(router: Router) -> None:
    router.message.register(start_command, Command(commands=["start"]))
    router.message.register(get_message_from_api, F.text)
