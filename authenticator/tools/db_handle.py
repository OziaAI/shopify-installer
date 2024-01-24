import os
import psycopg2


def fetch_env(env_name):
    value = os.getenv(env_name)
    if not value:
        print(env_name + " environment variable is not set.")
        exit(1)
    return value


def get_db():
    db_host = fetch_env("DB_HOST") 
    db_name = fetch_env("DB_NAME") 
    db_user = fetch_env("DB_USER") 
    db_password = fetch_env("DB_PASSWORD") 

    db = psycopg2.connect(host=db_host,
                          database=db_name,
                          user=db_user,
                          password=db_password)

    return db
