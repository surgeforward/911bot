import os
import json
import logging
import datetime

import storage

class DiskStorage(storage.Storage):
    def __init__(self):
        self.g_directory = None
        
    def _getFile(self, userid):
        return os.path.join(self.g_directory,userid+'.json')

    def _storeRecord(self, record):
        with open(self._getFile(record['id']),'w') as f:
            f.write(json.dumps(record))

  
    def _getRecord(self, userid):
        record = {
            'id': userid,
            'contact': "No contact information stored",
            'access':[],
            'context':{} # this is solely to allow for "grepping" in case of
            # emergency
        }
        if os.path.isfile(self._getFile(userid)):
            with open(self._getFile(userid),'r') as f:
                record.update(json.load(f))
        return record
  
    def initialize(self):
        super(DiskStorage, self).initialize()
        g_directory = self.g_directory = os.environ.get("CONTACTS_DIRECTORY","contacts")

        if not os.path.isdir(g_directory):
            os.makedirs(g_directory)
        
        os.system("ls {}".format(g_directory))

    def storeContact(self, userId, contactString, context):
        super(DiskStorage, self).storeContact(userId, contactString, context)
        logging.info("Storing {0} for {1}".format(contactString,userId))
        record = self._getRecord(userId)

        record.update({
            'id':userId,
            'contact': contactString,
            'context': context
        })
        self._storeRecord(record)

    def getContact(self, userid):
        super(DiskStorage, self).getContact(userid)
        
        logging.info("Retreiving info for {}".format(userid))
        return self._getRecord(userid)['contact']

    def recordAccess(self, userid,requesting_user):
        super(DiskStorage, self).recordAccess(userid, requesting_user)
        logging.info("record Access")
        record = self._getRecord(userid)
        record['access'].append((str(datetime.datetime.now()),requesting_user))
        self._storeRecord(record)

    def getAccess(self, userid):
        super(DiskStorage, self).getAccess(userid)
        record = self._getRecord(userid)
        return record['access']
