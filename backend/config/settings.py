import os
import configparser

class BaseConfig():
   API_PREFIX = '/api'
   TESTING = False
   DEBUG = False

   config = configparser.ConfigParser()

   @staticmethod
   def get_or_else(section, option, default_value):
      if BaseConfig.config.has_option(section, option):
         return BaseConfig.config.get(section, option,
                                  fallback=default_value)
      else:
         return os.environ.get(section, option, )


class DevConfig(BaseConfig):
   FLASK_ENV = 'development'
   DEBUG = True
   SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/kale_server_development'
   CELERY_BROKER = 'pyamqp://rabbit_user:rabbit_password@broker-rabbitmq//'
   CELERY_RESULT_BACKEND = 'rpc://rabbit_user:rabbit_password@broker-rabbitmq//'


class ProductionConfig(BaseConfig):
   FLASK_ENV = 'production'
   SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/kale_server_production'
   CELERY_BROKER = 'pyamqp://rabbit_user:rabbit_password@broker-rabbitmq//'
   CELERY_RESULT_BACKEND = 'rpc://rabbit_user:rabbit_password@broker-rabbitmq//'


class TestConfig(BaseConfig):
   FLASK_ENV = 'development'
   TESTING = True
   DEBUG = True
   # make celery execute tasks synchronously in the same process
   CELERY_ALWAYS_EAGER = True
