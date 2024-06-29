from aiogram.fsm.storage.base import BaseStorage
from aiogram.fsm.storage.redis import RedisStorage

from infrastructure.redis import client

redis_storage: BaseStorage = RedisStorage(
    redis=client,
)
