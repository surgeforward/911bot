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

defaultStorageMethod = "DiskStorage"

# no default, default handled below to print warning
storageMethod =  os.environ.get("BOT911_STORAGE_METHOD")

if not storageMethod:
  logging.warning("BOT911_STORAGE_METHOD not set in environment, Using default")
  storageMethod = defaultStorageMethod
  
logging.info("Storage method is '{}'".format(storageMethod))

if storageMethod not in storageTypes:
  raise EnvironmentError(
      "BOT911_STORAGE_METHOD is set to '{}' which is not supported".format(storageMethod))

storageObject = storageTypes[storageMethod]()
storageObject.storageMethod = storageMethod

