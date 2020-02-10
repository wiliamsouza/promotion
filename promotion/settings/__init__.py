from prettyconf import config

DATABASE_URL = config("DATABASE_URL")
TEST_DATABASE_URL = config("TEST_DATABASE_URL")
BLACK_FRIDAY_DATE = config("BLACK_FRIDAY_DATE")
USER_BIRTHDAY_PERCENTAGE = config("USER_BIRTHDAY_PERCENTAGE", cast=int)
MAX_DISCOUNT_PERCENTAGE = config("MAX_DISCOUNT_PERCENTAGE", cast=int)
BLACK_FRIDAY_PERCENTAGE = config("BLACK_FRIDAY_PERCENTAGE", cast=int)
