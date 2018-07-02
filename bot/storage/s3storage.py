import os
import boto3
from botocore.exceptions import ClientError
import json
import botocore
import logging
import storage

s3 = boto3.resource('s3')

class S3Storage(storage.Storage):
    def __init__(self):
        self.bucket_name = None
        
    def _getRecord(self, userid):
        contact = self._getEmptyContact(userid)
        storedContact = None
        
        try:
            contactStream = s3.Object(self.bucket_name, userid+".json").get()["Body"]
            storedContact = json.load(contactStream)
        except ClientError as ex:
            if ex.response['Error']['Code'] == 'NoSuchKey':
                storedContact = {}
            else:
                raise
        
        contact.update(storedContact)
        
        return contact
        
    def _storeRecord(self, record):
        userid = record["id"]
        contactObject = s3.Object(self.bucket_name, userid+".json")
        contactObject.put(Body = json.dumps(record))
        
    def initialize(self):
        super(S3Storage, self).initialize()
        # this is written on the belief that any access problems
        # and the non-existence of the given bucket will throw
        bucket_name = os.environ.get("BOT911_S3_BUCKET");
        self.bucket_name = bucket_name
        contacts_bucket = s3.Bucket(bucket_name)
        # will throw if bucket doesn't exist
        s3.meta.client.head_bucket(Bucket=bucket_name)
        
