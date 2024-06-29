from typing import Any, Optional

from aiogram import Dispatcher, Bot, BaseMiddleware
from aiogram.types import BotCommand
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import BaseStorage, MemoryStorage


def create_dp(
    *_: tuple[Any],
    storage: Optional[BaseStorage] = None,
    middlewares: list[BaseMiddleware] = None,
    handlers: list = None,
    **kwargs: dict[str, Any],
) -> Dispatcher:
    
    if storage is None:
        storage = MemoryStorage()
    
    dp = Dispatcher(storage=storage)

    if handlers:
        for handler in handlers:
            handler(dp)

    if middlewares:
        for middleware in middlewares:
            dp.message.register(middleware)

    return dp


async def create_bot(
    *_: tuple[Any],
    token: str,
    bot_commands: Optional[list[BotCommand]] = None,
    parse_mode: str = ParseMode.MARKDOWN,
    **kwargs: dict[str, Any],
) -> Bot:
    
    if not token:
        raise ValueError("Token must be provided")
    
    bot = Bot(
        token=token,
        default=DefaultBotProperties(
            parse_mode=parse_mode
        ),
    )

    if bot_commands:
        await bot.set_my_commands(commands=bot_commands)

    return bot
