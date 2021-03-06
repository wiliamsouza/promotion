"""Settings from enviroment variable"""
import datetime
import decimal

from prettyconf import config

DATABASE_URL = config("DATABASE_URL")
TEST_DATABASE_URL = config("TEST_DATABASE_URL")
BLACK_FRIDAY_DATE = datetime.datetime.strptime(
    config("BLACK_FRIDAY_DATE"), "%Y-%m-%d"
).date()
USER_BIRTHDAY_PERCENTAGE = config("USER_BIRTHDAY_PERCENTAGE", cast=decimal.Decimal)
MAX_DISCOUNT_PERCENTAGE = config("MAX_DISCOUNT_PERCENTAGE", cast=decimal.Decimal)
BLACK_FRIDAY_PERCENTAGE = config("BLACK_FRIDAY_PERCENTAGE", cast=decimal.Decimal)
TRACER_ENDPOINT_HOST = config("TRACER_ENDPOINT_HOST", cast=str, default="")
TRACER_ENDPOINT_PORT = config("TRACER_ENDPOINT_PORT", cast=int, default=0)
APPROVED_ORDER_IDENTITIES = config("APPROVED_ORDER_IDENTITIES", cast=config.list)
BALANCE_TOKEN = config("BALANCE_TOKEN")
RSA_PRIVATE_KEY = config("RSA_PRIVATE_KEY")
ID_TOKEN_EXPIRE_SECONDS = config("ID_TOKEN_EXPIRE_SECONDS", cast=int)
ISS_ENDPOINT = config("ISS_ENDPOINT")
