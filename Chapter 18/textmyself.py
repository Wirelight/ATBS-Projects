#!  python3
#   textMyself.py - Defines the textmyself() function that texts a message
#   passed to it as a string.

# Preset values:
accountSID = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
authToken  = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
myNumber = '+44xxxxxxxxxx'
twilioNumber = '+1xxxxxxxxxx'

from twilio.rest import Client

def textmyself(message):
    twilioCli = Client(accountSID, authToken)
    twilioCli.messages.create(body=message, from_=twilioNumber, to=myNumber)
