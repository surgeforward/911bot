from slackbot.bot import respond_to
import re
import store
import logging
from interfaces import IUser, IResponse, The911Bot

class SlackbotUser(IUser):
    def __init__(self,slackbotuser):
        self.user = slackbotuser

    def id(self):
        return self.user['id']

class SlackbotResponse(IResponse):
    def __init__(self,message):
        self.message = message

    def send(self,message):
        self.message.reply(message)

logger = logging.getLogger(__name__)
#logger.setLevel(logging.DEBUG)

@respond_to(r"^\s*help",re.IGNORECASE)
def help(message):
    message.reply("""Commands: help, why, store-contact, emergency

    Example: why
    Example: store-contact Wife (Helen): 555-555-5555 Local PD: 555-555-5555
    Example: emergency @someuser
    Example: list-access
    Example: store-contact
    (The simple form of store-contact will display your current contact info)
    """)

@respond_to(r"^\s*why",re.IGNORECASE)
def why(message):
    logger.debug(message);
    bot = The911Bot()
    response = SlackbotResponse(message)
    bot.why(response)

@respond_to(r"^\s*store-contact(.*)",re.IGNORECASE)
def storeContact(message,contactString):
    user = message._client.users[message._body['user']]
    contactString = contactString.strip()
    if contactString != "":
        store.storeContact(user['id'],contactString,user)
        contactString = store.getContact(user['id'])
        message.reply((u"Stored '{0}' for {1}. You may type " + \
                      u"`store-contact` at any time to update it or with " + \
                      u"no parameters to view your current information").
                      format(contactString,user['name']))
        message.reply("Please try the emergency command " + \
                      "to ensure everything works as expected")
    else:
        contactString = store.getContact(user['id'])
        message.reply("Current contact: " + contactString)

def _getUserById(message,userid):
    for _,user in message._client.users.iteritems():
        if user['id'] == userid:
            return user

# requesting user id -> target user id
g_emergencies = dict()
g_useridMatcher = re.compile("<@(.*)>")

@respond_to(r"^\s*emergency (.*)",re.IGNORECASE)
def emergency(message,targetUserNameOrId):
    logger.info(u"Emergency for {}".format(targetUserNameOrId))
    match = g_useridMatcher.match(targetUserNameOrId)
    if match:
        targetUserId = match.group(1)
    else:
        targetUserId = message._client.find_user_by_name(targetUserNameOrId)
    if targetUserId is None:
        message.reply("No such user found. Try emergency @username")
        return
    requestingUser = _getUserById(message,message._body['user'])
    requestingUserId = requestingUser['id']
    g_emergencies[requestingUserId] = targetUserId
    targetUser = _getUserById(message,targetUserId)
    logger.info(u"User Name is '{}.'".format(targetUser['name']))
    message.reply("TL;DR Is this an emergency? Type '@911bot YES' if so")
    message.reply((u"Note that you are trying to get emergency " +\
                   u"information for {0}. This service should not be " + \
                   u"used lightly and is strictly for true medical or " + \
                   u"other life-and-death emergencies. To verify this " + \
                   u"please respond by typing '@911bot YES'. Your access of " + \
                   u"the emergency information will be recorded.")
                  .format(targetUser['name']))

@respond_to(r"^\s*yes\s*$",re.IGNORECASE)
def isEmergency(message):
    requestingUser = _getUserById(message,message._body['user'])
    if requestingUser['id'] not in g_emergencies:
        message.reply(u"You have no pending emergency information requests. Try 'emergency @username' first.")
        return
    targetUserId = g_emergencies[requestingUser['id']]
    del g_emergencies[requestingUser['id']]
    contact = store.getContact(targetUserId)
    response = u"Emergency info: {}".format(contact)
    message.reply(response)
    store.recordAccess(targetUserId,requestingUser['name'])
    targetUser = _getUserById(message,targetUserId)
    message.reply(u"Access by {0} recorded. {1} has been notified"
                  .format(requestingUser['name'],targetUser['name']))
    message._client.send_message(u"@" + targetUser['name'],
                                 (u"{0} asked for your emergency contact info." +\
                                 u" Please let @{0} know if you're OK")
                                 .format(requestingUser['name']))

@respond_to(r"^\s*list-access")
def listAccess(message):
    userid = message._body['user']
    logger.info(u"Retreiving acess for {}".format(userid))
    accesses = store.getAccess(userid)
    if not accesses:
        message.reply("Your information has never been accessed")
    else:
        reply = "Your emergency info was accessed by\n"
        for (when,who) in accesses:
            reply += u"\t{} on {}\n".format(who,when)
        message.reply(reply)
