from slackbot.bot import Bot
import logging
import os

from bot.store import createStorageObject

def main():
    logging.basicConfig(level=logging.INFO)
    logging.info("Running")

    createStorageObject() # exception if no storage
    bot = Bot()
    bot.run()

if __name__ == "__main__":
    main()
