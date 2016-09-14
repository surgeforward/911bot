from slackbot.bot import Bot
import logging
import os

def main():
    logging.basicConfig(level=logging.INFO)
    logging.info("Running")
    if not os.environ.has_key("SLACKBOT_API_TOKEN"):
        raise RuntimeError,"Missing env variable: SLACKBOT_API_TOKEN"

    bot = Bot()
    bot.run()

if __name__ == "__main__":
    main()
