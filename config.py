import os

BOT_TOKEN = os.environ.get('BOT_TOKEN')

MONGO_HOST = os.environ.get('MONGO_HOST', 'localhost')
MONGO_PORT = os.environ.get('MONGO_PORT', 27017)
MONGO_DB = os.environ.get('MONGO_DATABASE', 'test')
DEFAULT_PARSE_MODE = "MarkdownV2"