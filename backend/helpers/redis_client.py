import redis
from settings import get_config

r = redis.Redis(host=get_config('REDIS_HOST'), port=get_config('REDIS_PORT'), db=get_config('REDIS_DB'))



