import logging

g_contacts = {}
# map user id -> list of contact strings

def register(user,contactString):
    logging.info("Storing {0} for {1}",contactString,user)
    l = g_contacts.get(user['id'],[])
    l.insert(0,contactString)
    g_contacts[user['id']] = l

def get(user):
    return g_contacts.get(user['id'],["Nothing on file"])[0]

