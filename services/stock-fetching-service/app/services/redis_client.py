import redis 
from app.core.config import config
from app.core.logger import logger

class RedisClient:
    def __init__(self):
        self.client = redis.Redis(host=config.REDIS_HOST, port=config.REDIS_PORT, decode_responses=True)

    def get(self, key):
        value = self.client.get(key)
        if value:
            logger.info(f"Cache hit for {key}")
            return value
        logger.info(f"Cache miss for {key}")
        return None

    def set(self, key, value):
        self.client.set(key, value)
        logger.info(f"Cache set for {key}")

    def delete(self, key):
        self.client.delete(key)
        logger.info(f"Cache deleted for {key}")