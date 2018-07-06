''' __init__.py
    * Exports storage object so that:
        * Takes responsibility for which storage method will be used.
        * A new storage method requires only implementing a Storage child class and adding it 
          to the `storageTypes` dictionary below. 
        * contains default storage method name.
          
'''
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
storageMethod = None
storageObject = None

def createStorageObject():
    global storageObject
    global storageMethod
    
    # no default in call, default is handled below to print warning
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
    return storageObject

