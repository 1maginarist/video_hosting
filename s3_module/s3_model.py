import boto3
import sys
import os
import uuid
import botocore


class S3:

    def __init__(self):
        self.bucket_name = ''
        self.access_key = ''

        s3_client = boto3.client('s3')

    def upload_file(self):
        pass



def get_s3_connection():
    resource = boto3.resource('s3')


def create_file_uuid():
    pass