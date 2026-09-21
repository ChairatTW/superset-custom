import os
from urllib.parse import quote_plus


SECRET_KEY = os.getenv("SECRET_KEY")


# =========================================================
# PostgreSQL Metadata Database
# =========================================================

POSTGRES_HOST = os.getenv("POSTGRES_HOST", "superset610-postgres")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB = os.getenv("POSTGRES_DB", "superset-db")


SQLALCHEMY_DATABASE_URI = (
    f"postgresql+psycopg2://"
    f"{quote_plus(POSTGRES_USER)}:"
    f"{quote_plus(POSTGRES_PASSWORD)}@"
    f"{POSTGRES_HOST}:"
    f"{POSTGRES_PORT}/"
    f"{POSTGRES_DB}"
)

SQLALCHEMY_TRACK_MODIFICATIONS = False


# =========================================================
# Redis
# =========================================================

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = os.getenv("REDIS_PORT", "6379")
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD")


CACHE_CONFIG = {
    "CACHE_TYPE": "RedisCache",
    "CACHE_DEFAULT_TIMEOUT": 300,
    "CACHE_KEY_PREFIX": "superset_",

    "CACHE_REDIS_HOST": REDIS_HOST,
    "CACHE_REDIS_PORT": int(REDIS_PORT),
    "CACHE_REDIS_DB": 1,
    "CACHE_REDIS_PASSWORD": REDIS_PASSWORD,
}
