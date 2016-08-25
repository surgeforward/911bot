from slackbot.bot import respond_to
import re
import store
import logging

@respond_to("help",re.IGNORECASE)
def help(message):
    message.reply("""Commands: help, register, emergency

    Example: register Wife (Helen): 555-555-5555 Local PD (Toronto, Division 54): 555-555-5555
    Example: emergency @someuser
    """)

@respond_to("register (.*)",re.IGNORECASE)
def register(message,contactString):
    user = message._client.users[message._body['user']]
    store.register(user,contactString)
    contactString = store.get(user)
    message.reply("Stored '{0}' for {1}".format(contactString,user['name']))

def _get_user_by_id(message,userid):
    for _,user in message._client.users.iteritems():
        if user['id'] == userid:
            return user

@respond_to("emergency <@(.*)>",re.IGNORECASE)
def emergency(message,userid):
    logging.info("Emergency for {}".format(userid))
    target = _get_user_by_id(message,userid)
    req_user = _get_user_by_id(message,message._body['user'])
    if target:
        contact = store.get(target)
        response = "Emergency contact for @{}: {}".format(target['name'],contact)
        message.reply(response)
        message.reply("Access by {} recorded".format(req_user['name']))
    else:
        message.reply("{} not found".format(userid))
