import redis
from .env_fetcher import fetch_env

redis_host = fetch_env("REDIS_HOST")
redis_port = int(fetch_env("REDIS_PORT"))

redis_connection = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)
