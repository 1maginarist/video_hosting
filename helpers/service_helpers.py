import os
import yaml
import uuid
import hashlib
import platform


def get_settings():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    settings_file_name = 'settings_dev.yaml' if get_os_name() == 'Windows' else 'settings_prod.yaml'
    yaml_path = os.path.join(current_dir, settings_file_name)
    with open(rf'{yaml_path}', 'r', encoding='UTF-8') as file:
        settings = yaml.safe_load(file)
        return settings


def generate_file_uuid():
    return str(uuid.uuid4())


def check_for_uuid_existence():
    pass


def make_hash_from_cred(string: str):
    return hashlib.sha256(string.encode()).hexdigest()


def get_os_name():
    return platform.system()
