"""This script contains the class The911Bot and the interfaces needed to use it.
>>> class MessageDemo:
...     def output(self, text):
...         print text
>>>
>>> class ResponseImp (IResponse):
...     def __init__(self, messageObject):
...         self.myMessageObject = messageObject
...     def send(self,message):
...         self.myMessageObject.output(message)
>>>
>>> messageObject = MessageDemo()
>>> response = ResponseImp(messageObject)
>>> the911Bot = The911Bot()
>>> the911Bot.why(response)
This bot was created by Surge Consulting in response to the tragic events of 2016-08-24. In memory of Simon Hancock.
>>>
"""

from slackbot.bot import respond_to
import store

class IResponse:
    """Defines an interface for sending a response to the caller.
    >>> response = IResponse()
    >>> response.send("Test message")
    Test message
    """

    def send(self,message):
        """Method to override to provide a custom way of responding to the user.
        >>> response = IResponse()
        >>> response.send("Test message")
        Test message
        """
        print message

class IUser:
    """Interface for uniquely identifying the user making any given request.
    >>> user = IUser()
    >>> user.id()
    123
    """
    def id(self):
        """Method to override to provide a custom way to identify the user making a request.
        >>> user = IUser()
        >>> user.id()
        123
        """
        return 123

class The911Bot:
    """This class provides the core functionality of the 911Bot.  Custom implementations of its functionality
    should call its methods with custom objects of classes that are implementations of IResponse and IUser
    >>> response = IResponse()
    >>> bot = The911Bot()
    >>> bot.why(response)
    This bot was created by Surge Consulting in response to the tragic events of 2016-08-24. In memory of Simon Hancock.
    """
    def help(self, message):
        """ Display a help message outlining the different options provided by the 911Bot
        >>> response = IResponse()
        >>> bot = The911Bot()
        >>> bot.help(response)
        Commands: help, why, store-contact, emergency
        Example: why
        Example: store-contact Wife (Helen): 555-555-5555 Local PD: 555-555-5555
        Example: emergency @someuser
        Example: list-access
        Example: store-contact
        (The simple form of store-contact will display your current contact info)
        <BLANKLINE>
        """
        message.send("Commands: help, why, store-contact, emergency\n" + \
                     "Example: why\n" + \
                     "Example: store-contact Wife (Helen): 555-555-5555 Local PD: 555-555-5555\n" + \
                     "Example: emergency @someuser\n" + \
                     "Example: list-access\n" + \
                     "Example: store-contact\n" + \
                     "(The simple form of store-contact will display your current contact info)\n")

    def why(self,response):
        """ Send the given response object text to display.
        >>> response = IResponse()
        >>> bot = The911Bot()
        >>> bot.why(response)
        This bot was created by Surge Consulting in response to the tragic events of 2016-08-24. In memory of Simon Hancock.
        """
        response.send("This bot was created by Surge Consulting in response to " + \
                      "the tragic events of 2016-08-24. " + \
                      "In memory of Simon Hancock.")

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
