import os


def fetch_env(env_name):
    """
    Fetch the environment variable.
    @param env_name: The name of the environment variable.
    @return: The value of the environment variable.
    """
    value = os.getenv(env_name)
    if not value:
        print(env_name + " environment variable is not set.")
        exit(1)
    return value
