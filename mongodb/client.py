from .database import MongoDB
from config import MONGO_DB, MONGO_PORT, MONGO_HOST

mongo = MongoDB(host=MONGO_HOST,
                port=MONGO_PORT, database=MONGO_DB)


def mongo_connection(func):
    def wrapper(*args, **kwargs):
        with mongo:
            return func(*args, **kwargs)
    return wrapper
