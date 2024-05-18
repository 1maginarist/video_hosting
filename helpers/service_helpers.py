import os
import yaml
import uuid
import hashlib


def get_settings():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    yaml_path = os.path.join(current_dir, 'settings.yaml')
    with open(rf'{yaml_path}', 'r', encoding='UTF-8') as file:
        settings = yaml.safe_load(file)
        return settings


def generate_file_uuid():
    return str(uuid.uuid4())


def check_for_uuid_existence():
    pass


def make_hash_from_cred(str: str):
    return hashlib.sha256(str.encode()).hexdigest()
