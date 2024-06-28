import os
import asyncio
import logging

from aiogram import Bot, Dispatcher
from config import settings
from infrastructure.application import create_bot, create_dp


async def main() -> None:
    logging.basicConfig(level=logging.INFO)

    bot: Bot = await create_bot(
        token=settings.token,
        parse_mode=settings.parse_mode
    )

    dp: Dispatcher = create_dp()

    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    except Exception as e:
        raise


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        raise
