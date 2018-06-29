import logging
import json
import os
import sys
import datetime
import traceback

import storage

storageObject = storage.storageObject


def storeContact(userId, contactString, context):
    storageObject.storeContact(userId, contactString, context)

def getContact(userid):
    return storageObject.getContact(userid)

def recordAccess(userid,requesting_user):
    storageObject.recordAccess(userid, requesting_user)

def getAccess(userid):
    return storageObject.getAccess(userid)

try:
    storageObject.initialize()
except:
    logging.error("Can Not Initialize Storage Method '{}'".format(storage.storageMethod))
    raise
    