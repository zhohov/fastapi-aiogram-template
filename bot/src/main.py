import asyncio
import logging

from aiogram import Bot, Dispatcher

from config import settings
from infrastructure.application import create_bot, create_dp, redis_storage
from presentation.base import register_user_interaction_handlers


async def main() -> None:
    logging.basicConfig(level=logging.INFO)

    bot: Bot = await create_bot(token=settings.token, parse_mode=settings.parse_mode)

    dp: Dispatcher = create_dp(
        storage=redis_storage,
        handlers=[
            register_user_interaction_handlers,
        ],
    )

    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    except Exception as e:
        raise e


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        raise e
