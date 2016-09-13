import logging
import json
import os
import datetime

g_directory = "contacts"

def _get_file(userid):
    return os.path.join(g_directory,userid+'.json')

def _store_record(record):
    with open(_get_file(record['id']),'w') as f:
        f.write(json.dumps(record))

def _get_record(userid):
    record = {
        'id': None,
        'contact': "",
        'access':[],
        'context':{} # this is solely to allow for "grepping" in case of
                     # emergency
    }
    with open(_get_file(userid),'r') as f:
        record.update(json.load(f))
    return record

def storeContact(userId,contactString,context):
    logging.info("Storing {0} for {1}".format(contactString,userId))
    _store_record({
        'id':userId,
        'contact': contactString,
        'access':[], # tuple of (datetime,user)
        'context': context
        })

def get_info(userid):
    logging.info("Retreiving info for {}".format(userid))
    return _get_record(userid)['contact']

def record_access(userid,requesting_user):
    record = _get_record(userid)
    record['access'].append((str(datetime.datetime.now()),requesting_user))
    _store_record(record)

def get_access(userid):
    record = _get_record(userid)
    return record['access']

if not os.path.isdir(g_directory):
    os.makedirs(g_directory)
