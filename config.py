import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6984371912:AAFcZe2u4X8n7ofEBsRQ9JeJww5Gfqu6JSs")

    APP_ID = int(os.environ.get("APP_ID", 26335449))

    API_HASH = os.environ.get("API_HASH", "84c8ff5308268c2bc94c1d2c54e865ec")

    