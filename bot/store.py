import logging
import json
import os
import datetime

g_directory = "contacts"

def _get_file(userid):
    return os.path.join(g_directory,userid+'.json')

# TODO: Some of encryption would be nice
def _store_record(record):
    with open(_get_file(record['id']),'w') as f:
        f.write(json.dumps(record))

def _get_record(userid):
    record = {
        'id': None,
        'contact': "",
        'access':[]
    }
    with open(_get_file(userid),'r') as f:
        record.update(json.load(f))
    return record

def register(user,contactString):
    logging.info("Storing {0} for {1}".format(contactString,user['id']))
    _store_record({
        'id':user['id'],
        'contact': contactString,
        'access':[] # tuple of (datetime,user)
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
