from slackbot.bot import Bot
import logging
import os

def main():
    logging.basicConfig(level=logging.INFO)
    logging.info("Running")

    bot = Bot()
    bot.run()

if __name__ == "__main__":
    main()
