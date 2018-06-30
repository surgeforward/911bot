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
        record = self._getEmptyContact(userid)
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

