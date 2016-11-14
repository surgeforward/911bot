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

def sendMessage(channel, message):
    latest = slackCall("im.history",channel=channel['channel']['id'],
                       count=1)['messages'][0]['ts']
    msg = slackCall("chat.postMessage",
                    channel=dm['channel']['id'],
                    text=message,
                    as_user=True
    )

    time.sleep(1)

    return slackCall("im.history",channel=channel['channel']['id'],
                     count=1)['messages'][0]['text']


slackCall("auth.test")
users = slackCall('users.list',presence=1)['members']
bot = None
for user in users:
    if user['name'] == '911bot':
        bot = user
        break

dm = slackCall('im.open',user=bot['id'])
print sendMessage(dm,"Hello, world")
print sendMessage(dm,"help")
dt = datetime.datetime.now()
print sendMessage(dm,"store-contact %s" % (dt))
contact = sendMessage(dm,"store-contact")
print contact
if contact.find(str(dt)) == -1:
    raise RuntimeError,"Could not successfully store or retreive contact info"
