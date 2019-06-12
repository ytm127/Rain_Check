# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import requests


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC7f63b30dd407f399af7d53185d8a3b61'
auth_token = '52a6f851b2c35f9056142e164b803d81'
client = Client(account_sid, auth_token)

### Get weather info here 
response = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=72701,us&APPID=462542c82e839a074d9eed2a3e8408a8')
# weather description. Convert unicode to string.
weather_desc = (response.json()['weather'][0]["description"]).encode("utf-8")
# current temperature. Convert from flaot to string
temp_kelvin = response.json()['main']["temp"]
temp_f = str((temp_kelvin - 273.15)* 9/5 + 32 )
info = "Right now, it looks like " + weather_desc + " with a temperature of " + temp_f + " degrees fahrenheit."
# print(info)

# determine final message depending on forecast
if "rain" in weather_desc:
    message = info + '\n' + "It is raining right now. Bring an umbrella."
else:
    message = info + '\n' + "It is not raining right now. Enjoy the weather!"

print(message)


message = client.messages \
                .create(
                     body=info,
                     from_='+14792822715',
                     to='+14799258596'
                 )


print(message.sid)
