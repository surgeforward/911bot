''' store.py
    Application level interface to contact info storage.
'''
import logging
import json
import os
import sys
import datetime
import traceback

import storage

storageObject = None

def _raiseIfNoStorageObject():
    if not storageObject:
        raise Exception("Storage Object was not initialized.")

def createStorageObject():
    global storageObject
    try:
        storageObject = storage.createStorageObject()
    except:
        logging.error("Can Not Initialize Storage Method '{}'".format(storage.storageMethod))
        raise
    
    logging.info("created storage object {}".format(storageObject))
    
    return storageObject

def storeContact(userId, contactString, context):
    _raiseIfNoStorageObject();
    storageObject.storeContact(userId, contactString, context)

def getContact(userid):
    _raiseIfNoStorageObject();
    return storageObject.getContact(userid)

def recordAccess(userid,requesting_user):
    _raiseIfNoStorageObject();
    storageObject.recordAccess(userid, requesting_user)

def getAccess(userid):
    _raiseIfNoStorageObject();
    return storageObject.getAccess(userid)

    
