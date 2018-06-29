# tbh this is here b/c errors in plugin loading do not bubble up (see slackbot manager.py)
# and so we want to check that this imports before running the bot.
# the module initialized on load.
def checkStorage():
    import bot.store
    # could do other checks but module throws exception if cannot initialize

