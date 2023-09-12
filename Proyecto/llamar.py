import os
from twilio.rest import Client
nombre="Carlos"

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'ACb900d4d9fe6d798bcb965438dcce8c16'
auth_token = '4602436c7a8a3641c8be915e9fc47840'
client = Client(account_sid, auth_token)

call = client.calls.create(
                        from_='+14704666180',
                         to='+5491155881876',
                        twiml='<Response><Say language="es-ES">Hola, usted ha sido contactado porque el señor '+ nombre +' se ha caído </Say></Response>'
                    )

print(call.sid)