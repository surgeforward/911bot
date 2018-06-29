import os
import sys
import logging

### Specific Storage Classes
from diskstorage import DiskStorage
from s3storage import S3Storage

### supported storage types
storageTypes = {
  "DiskStorage": DiskStorage,
  "S3Storage": S3Storage,
}

defaultStorageMethod = "S3Storage"
storageMethod =  os.environ.get("BOT911_STORAGE_METHOD")

if not storageMethod:
  logging.warning("911BOT_STORAGE_METHOD not set in environment, Using default")
  storageMethod = defaultStorageMethod
  
logging.info("Storage method is '{}'".format(storageMethod))

if storageMethod not in storageTypes:
  raise EnvironmentError(
      "991BOT_STORAGE_METHOD is set to '{}' which is not supported".format(storageMethod))

storageObject = storageTypes[storageMethod]()
storageObject.storageMethod = storageMethod