from twilio.rest import Client
import get_weather as weather
import shared 

client = Client(shared.TWILIO_ACCOUNT_SID, shared.TWILIO_AUTH_TOKEN)

for number in shared.USER_NUMBERS:
	client.messages.create(
    	to=number, 
    	from_=shared.TWILIO_NUMBER,
    	body=weather.getForecast())
	print number
