import logging
import json
import os

g_filename = "contacts.json"
g_contacts = {}
# map user id -> list of contact strings

def initialize():
    global g_contacts
    logging.info("Loading from {}".format(g_filename))
    if os.path.isfile(g_filename):
        with open(g_filename,'r') as f:
            g_contacts = json.load(f)
            logging.info("Loaded contacts for {} users".format(len(g_contacts)))

def register(user,contactString):
    logging.info("Storing {0} for {1}".format(contactString,user['id']))
    l = g_contacts.get(user['id'],[])
    l.insert(0,contactString)
    g_contacts[user['id']] = l
    with open(g_filename,'w') as f:
        f.write(json.dumps(g_contacts))

def get(user):
    return g_contacts.get(user['id'],["Nothing on file"])[0]

initialize()
