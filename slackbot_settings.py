import os

API_TOKEN=os.environ['SLACK_API_TOKEN']
DEFAULT_REPLY = "Sorry but I didn't understand you"
DEBUG=1

PLUGINS = [
    'slackbot.plugins',
    'bot.plugins'
]
