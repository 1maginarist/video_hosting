import boto3
import os
from botocore.config import Config

from helpers.service_helpers import get_settings
from helpers.service_helpers import generate_file_uuid


class S3:

    def __init__(self):
        self.base_download_path = 'src/'
        self.settings = get_settings()

        self.s3_config = Config(
            region_name=self.settings['s3']['REGION'],
            retries={
                "max_attempts": 5,
                "mode": "standard"
            }
        )

        self._bucket_name = self.settings['s3']['BUCKET_NAME']
        self._access_key = self.settings['s3']['ACCESS_KEY']
        self._secret_access_key = self.settings['s3']['SECRET_ACCESS_KEY']
        self._replication_bucket_name = self.settings['s3']['REPLICATION_BUCKET_NAME']
        self._replication_access_key = self.settings['s3']['REPLICATION_ACCESS_KEY']
        self._replication_secret_access_key = self.settings['s3']['REPLICATION_SECRET_ACCESS_KEY']
        self._region = self.settings['s3']['REGION']
        self._url = self.settings['s3']['URL']

        self.client = self.get_s3_connection()

    def get_all_buckets(self):
        """
        returns the list of all buckets under provided creds

        :return:
        """
        return self.client.list_buckets()

    def upload_file(self, fileobj):
        """
        Uploads file to the bucket

        :return:
        """
        with open("src/2.jpg", "rb") as f:
            file_uuid = generate_file_uuid()
            self.client.upload_fileobj(f, self._bucket_name, file_uuid)
            # блок записи в бд

    def check_for_success_upload(self):
        """
        checks if the  uploaded fileobj was successfully uploaded to s3

        :return:
        """
        pass

    def get_video_from_bucket(self, file_uuid):
        with open(f'{self.base_download_path}{file_uuid}', 'wb') as file:
            self.client.download_file(self._bucket_name, file_uuid, file)
            os.remove(f'{self.base_download_path}{file_uuid}')
            return file

    def get_bucket_replication(self, file_uuid):
        """
        method for replication data between buckets
        
        :param file_uuid: 
        :return: 
        """
        self.client.copy_object(Bucket=f"{self._replication_bucket_name}",
                                CopySource=f"/{self._bucket_name}/{file_uuid}",
                                Key=file_uuid)

    def get_s3_connection(self):
        """
        initializes connection to s3 service

        :return:
        """
        return boto3.client('s3',
                            aws_access_key_id=self._access_key,
                            aws_secret_access_key=self._secret_access_key,
                            endpoint_url=self._url,
                            config=self.s3_config)

    def get_fileobj_metadata(self, file_uuid):
        """
        gets metadata of fileobj

        :param file_uuid:
        :return:
        """
        return self.client.get_object(Bucket=self._bucket_name, Key=file_uuid)
