class Storage(object):
    """ Virtual base class, may have shared functionality.
    """
    def initialize(self):
        pass # does not need to be implemented
      
    def storeContact(self, userId, contactString, context):
        raise Exception("Storage Classes must override storeContact")
        
    def getContact(self, userid):
        raise Exception("Storage Classes must override getContact")
        
    def recordAccess(self, userid,requesting_user):
        raise Exception("Storage Classes must override recordAccess")
        
    def getAccess(self, userid):
        raise Exception("Storage Classes must override getAccess")