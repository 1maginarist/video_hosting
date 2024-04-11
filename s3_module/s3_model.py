import boto3


def get_s3_connection():
    resource = boto3.resource('s3')


def create_file_uuid():
    pass