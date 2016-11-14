import os

DEFAULT_REPLY = "Sorry but I didn't understand you. Try `help`"
DEBUG=1

PLUGINS = [
    'slackbot.plugins',
    'bot.plugins'
]

API_TOKEN = os.environ['SLACKBOT_API_TOKEN'].strip()
