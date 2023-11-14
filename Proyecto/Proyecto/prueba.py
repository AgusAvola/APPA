"""import vonage
response = client.voice.create_call({
    'to': [{'type': 'phone', 'number': +5491144770394}],
    'from': {'type': 'phone', 'number': +5491155881876},
    'ncco': [{'action': 'talk', 'text': 'This is a text to speech call from Nexmo'}]
})

pprint(response)"""
# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+14704666180',
                     to='+AGUS_NUMBER'
                 )

print(message.sid)
