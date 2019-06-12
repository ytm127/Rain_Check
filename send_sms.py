# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC7f63b30dd407f399af7d53185d8a3b61'
auth_token = '52a6f851b2c35f9056142e164b803d81'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="RAIN CHECK - Hey, it looks like it's going to rain today. BRING YOUR UMBRELLA!",
                     from_='+14792822715',
                     to='+14799258596'
                 )

print(message.sid)
