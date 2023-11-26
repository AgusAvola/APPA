import os
from dotenv import load_dotenv
from twilio.rest import Client
load_dotenv()
account_sid = "ACb900d4d9fe6d798bcb965438dcce8c16"
auth_token = "06dcbae469f09f541e6245116caef1d6"
client = Client(account_sid, auth_token)

client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+14704666180',
  body='quedan pocas pastillas',
  to='+5491155881876'
)

print(message.sid)