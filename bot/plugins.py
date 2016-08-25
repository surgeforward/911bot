from slackbot.bot import respond_to
import re
import store

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


@respond_to("emergency (.*)",re.IGNORECASE)
def emergency(message,username):
    username = username.replace('@','')
    userid = message._client.find_user_by_name(username)
    if userid:
        for user in message._client.users.iteritems():
            if user['name'] == username:
                message.reply(store.get(user))
                return
    message.reply("{0} not found".format(username))

