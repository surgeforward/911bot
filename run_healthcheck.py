# Use Web API to check health of 911bot

import datetime
import requests
import argparse
import json
import time
import os

parser = argparse.ArgumentParser()
parser.add_argument("--slack-token",
                    default=os.environ.get("HEALTHCHECK_SLACK_TOKEN",None),
                    help="Slack API token. Must be different " +\
                    "from the bot token. Generate here: https://api.slack.com/web")

args = parser.parse_args()

def slackCall(methodName,**params):
    url = "https://slack.com/api/" + methodName
    if params is None:
        params = {}
    params['token'] = args.slack_token
    result = requests.post(url,params=params).json()
    if result['ok']: return result
    else: raise RuntimeError,"Error calling %s: %s" % (methodName,result)

def sendMessage(channel, message,numMessages = 1):
    msg = slackCall("chat.postMessage",
                    channel=dm['channel']['id'],
                    text=message,
                    as_user=True
    )

    # Sleep so that the message has time to do the healthcheck -> slack ->
    # 911bot -> filesystem -> slack round trip. I mean, it should really be
    # more than 1 second to be safe. This is a hack.
    time.sleep(1)

    messages = slackCall("im.history",channel=channel['channel']['id'],
                         count=numMessages)['messages']
    if numMessages == 1:
        return messages[0]['text']
    else:
        return messages[:numMessages]


auth = slackCall("auth.test")
users = slackCall('users.list',presence=1)['members']
bot = None
for user in users:
    if user['name'] == '911bot':
        bot = user
        break

dm = slackCall('im.open',user=bot['id'])
print sendMessage(dm,"Hello, world")
print sendMessage(dm,"help")
dt = str(datetime.datetime.now())
print sendMessage(dm,"store-contact %s" % (dt))
verify = sendMessage(dm,"emergency {}".format(auth['user']))
if verify.find("verify") == -1:
    raise RuntimeError,"Unexpected response to emergency: {}".format(verify)
# Bot sends 3 messages in response, we need all of them and want the last
# message
info = sendMessage(dm,"YES",numMessages=3)[-1]['text']
print info
if info.find(dt) == -1:
    raise RuntimeError,"Contact info not retrieved correctly: {}".format(info)
