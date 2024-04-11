import os
from dotenv import load_dotenv


class Configs:

    def __init__(self):

        load_dotenv()

        self._S3_ACCESS_KEY = os.getenv('S3_ACCESS_KEY')
        self._S3_SECRET_ACCESS_KEY = os.getenv('S3_SECRET_ACCESS_KEY')
        self._DB_USER = os.getenv('DB_USER')
        self._DB_PASS = os.getenv('DB_PASS')
        self._DB_NAME = os.getenv('DB_NAME')
        self._DB_HOST = os.getenv('DB_HOST')


def get_configs_instance():
    return Configs()
