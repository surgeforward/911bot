from slackbot.bot import Bot
import logging
import os

from checkstorage import checkStorage

def main():
    logging.basicConfig(level=logging.INFO)
    logging.info("Running")

    # checkStorage() # exception if no storage
    import bot.store
    # bot = Bot()
    # bot.run()

if __name__ == "__main__":
    main()
