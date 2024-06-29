from redis import Redis # type: ignore

from config import settings


def get_redis_client() -> Redis:
    client = Redis(
        host=settings.redis.redis_host,
        port=settings.redis.redis_port,
        password=settings.redis.redis_password, 
    )

    return client

client = get_redis_client()
