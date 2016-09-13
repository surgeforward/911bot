import logging
import json
import os
import datetime

g_directory = "contacts"

def _getFile(userid):
    return os.path.join(g_directory,userid+'.json')

def _storeRecord(record):
    with open(_getFile(record['id']),'w') as f:
        f.write(json.dumps(record))

def _getRecord(userid):
    record = {
        'id': None,
        'contact': "",
        'access':[],
        'context':{} # this is solely to allow for "grepping" in case of
                     # emergency
    }
    with open(_getFile(userid),'r') as f:
        record.update(json.load(f))
    return record

def storeContact(userId,contactString,context):
    logging.info("Storing {0} for {1}".format(contactString,userId))
    record = {}
    try:
        record = _getRecord(userId)
    except:
        pass

    record.update({
        'id':userId,
        'contact': contactString,
        'context': context
    })

    _storeRecord(record)

def getContact(userid):
    logging.info("Retreiving info for {}".format(userid))
    return _getRecord(userid)['contact']

def recordAccess(userid,requesting_user):
    record = _getRecord(userid)
    record['access'].append((str(datetime.datetime.now()),requesting_user))
    _storeRecord(record)

def getAccess(userid):
    record = _getRecord(userid)
    return record['access']

if not os.path.isdir(g_directory):
    os.makedirs(g_directory)
