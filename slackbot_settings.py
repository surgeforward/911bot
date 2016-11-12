import os

DEFAULT_REPLY = "Sorry but I didn't understand you. Try `help`"
DEBUG=1

PLUGINS = [
    'slackbot.plugins',
    'bot.plugins'
]

if not os.environ.has_key("SLACKBOT_API_TOKEN"):
   raise RuntimeError,"Missing env variable: SLACKBOT_API_TOKEN"
API_TOKEN=os.environ['SLACKBOT_API_TOKEN'].strip()
