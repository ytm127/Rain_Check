# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import requests


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC7f63b30dd407f399af7d53185d8a3b61'
auth_token = '52a6f851b2c35f9056142e164b803d81'
client = Client(account_sid, auth_token)

# Get weather info here
response = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=72701,us&APPID=462542c82e839a074d9eed2a3e8408a8')
print(response.text)


message = client.messages \
                .create(
                     body=response.text,
                     from_='+14792822715',
                     to='+14799258596'
                 )


print(message.sid)
