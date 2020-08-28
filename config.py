from environs import Env
import redis


class Config(object):
    env = Env()
    env.read_env()

    SQLALCHEMY_DATABASE_URI = env("DATABASE_URL")
    SECRET_KEY = env("SECRET_KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True


def init_redis():
    return redis.Redis(host="localhost", port=6379, db=0)
