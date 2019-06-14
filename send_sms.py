# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import requests

# Fayetteville,AR code = 4110486


# Your Account Sid and Auth Token from twilio.com/console
# See http://twil.io/secure
account_sid = 'AC7f63b30dd407f399af7d53185d8a3b61'
auth_token = '52a6f851b2c35f9056142e164b803d81'
client = Client(account_sid, auth_token)

### Get weather info here 
# This GET request gets 6 timestamps at a 3 hour interval (18 hour span)
response = requests.get('http://api.openweathermap.org/data/2.5/forecast?id=4110486&cnt=6&APPID=462542c82e839a074d9eed2a3e8408a8')

rain = False
for i in range(6):
    weather_timestamp = response.json()['list'][i]['weather'][0]['description'] # parse through each of the 6 timestamps
    if 'rain' in str(weather_timestamp):
        rain = True

# final determination
if rain == True:
    notice = "There is rain in the forecast in Fayetteville, AR between now and 11pm! \n\nBRING YOUR UMBRELLA! \n"

    message = client.messages \
                .create(
                     body="\nGood Morning! \n" + notice + "- RainCheck :)",
                     from_='+14792822715',
                     to='+14799258596'
                 )


    print(message.sid)


# else:
#     notice = "No rain! woohoo!"
#     print('No rain! woohoo!')



