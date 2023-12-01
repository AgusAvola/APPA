import os
from dotenv import load_dotenv
from twilio.rest import Client
import queries
def sms(a:str):
  load_dotenv()
  account_sid = os.getenv('TWILIO_ACCOUNT_SID')
  auth_token = os.getenv('TWILIO_AUTH_TOKEN')
  client = Client(account_sid, auth_token)

  client = Client(account_sid, auth_token)

  message = client.messages.create(
    from_='+15074012437',
    body='quedan pocas pastillas en el tubo '+a+".",
    to='+5491155881876'
  )

  print(message.sid)