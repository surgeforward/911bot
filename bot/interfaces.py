import store

class IResponse:
    def send(self,message):
        raise NotImplementedError("Called on base class!")

class IUser:
    def id(self):
        raiseNotImplemented()

class The911Bot:
    def why(self,response):
        response.send("Here is the why message")

    def storeContact(self,message,user,response):
        if message != "":
            self.store.saveInfo(user.id(),message)
            response.send("Stored, do some testing")
        else:
            response.send(self.store.getInfo(user.id()))

@respond_to("why")
def why(message):
    bot = get911BotInstance()# returns The911Bot
    response = SlackbotResponse(message)
    bot.why(response)

@respond_to("store-contact ....")
def storeContact(message,contactString):
    bot = get911BotInstance()
    response = SlackbotResponse(message)
    user = SlackbotUser(message._clients[message._body['user']])
    bot.storeContact(contactString,user,response)

@url("/why")
def why():
    response = HTTPResponse()
    thebot.why(response)

