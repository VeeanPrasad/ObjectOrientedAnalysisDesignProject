import os

default_settings = {
    'REDIS_HOST': '127.0.0.1',
    'REDIS_DB': 0,
    'REDIS_PORT': 6379
}

def get_config(key):
    try:
        value = os.environ.get(key)
        if value:
            return value
        else:
            return default_settings.get(key, None)
    except KeyError:
        pass
