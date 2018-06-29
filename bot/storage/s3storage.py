import boto3

import logging
import storage

s3 = boto3.resource('s3')

class S3Storage(storage.Storage):
    def initialize(self):
        bucket = s3.Bucket("911bot-contact-store")
        for o in bucket.objects.filter(Delimiter='/'):
            logging.info(o.key)
        raise Exception("ibidy")