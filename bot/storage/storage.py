import datetime
import logging

class Storage(object):
    """ Base Class for Storage Implementations. Requires child completion class. 
        
        Minimal implementation requires overriding the following:
            _getRecord(..)
            _storeRecord(..)
            initialize(..) (if nec)
            
        Sharing _getEmptyContact(..) ensures that all storage implementations
        share basic properties.
    """
    
    def _getRecord(self, userid):
        ''' Takes userid and returns record if it exists, otherwise and 
        blank contact record (see _getEmptyContact(..)). '''
        raise Exception("_getRecord must be implemented through child class")

    def _storeRecord(self, record):
        ''' Takes contact record and stores it. See _getEmptyContact for record format.'''
        raise Exception("_storeRecord must be implemented through child class")

    def _getEmptyContact(self, userid):
        return {
            'id': userid,
            'contact': "No contact information stored",
            'access':[],
            'context':{} # this is solely to allow for "grepping" in case of
            # emergency
        }
        
    def storeContact(self, userId, contactString, context):
        logging.info("Storing {0} for {1}".format(contactString,userId))
        record = self._getRecord(userId)

        record.update({
            'id':userId,
            'contact': contactString,
            'context': context
        })
        self._storeRecord(record)

    def getContact(self, userid):
        logging.info("Retreiving info for {}".format(userid))
        return self._getRecord(userid)['contact']

    def recordAccess(self, userid,requesting_user):
        logging.info("record Access")
        record = self._getRecord(userid)
        record['access'].append((str(datetime.datetime.now()),requesting_user))
        self._storeRecord(record)

    def getAccess(self, userid):
        record = self._getRecord(userid)
        return record['access']
