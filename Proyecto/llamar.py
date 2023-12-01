import os
import queries
from dotenv import load_dotenv
from twilio.rest import Client
nombre=queries.nombre
pariente=queries.pariente
load_dotenv()
# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

call = client.calls.create(
                       from_=queries.tel,
                       to='+54 9 11 5588 1876',
                     twiml='<Response><Say language="es-ES">Hola'+pariente+', usted ha sido contactado porque el señor '+ nombre +' de '+queries.edad+'se ha caído. La dirección es'+queries.ubicacion+' </Say></Response>'
                )

print(call.sid)