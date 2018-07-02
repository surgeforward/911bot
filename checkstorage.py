# tbh this is here b/c errors while loading plugins do not bubble up (see slackbot file manager.py)
# We want to check that this imports before running the bot.

def checkStorage():
    import bot.store
    # module throws exception if cannot initialize.
    # Note: could return storageObject if deemed useful.
    

