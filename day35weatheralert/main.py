import requests
from twilio.rest import Client

account_sid = 'YOUR ACCOUNT SID'
auth_token = 'YOUR AUTH TOKEN'
# Your Account SID from twilio.com/console
client = Client(account_sid, auth_token)


api_key = "[Your Open weather API Key]"
MY_LAT = 23.014509 # Your latitude
MY_LONG = 72.591759 # Your longitude
parameters = { 
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "cnt": 4
}
response = requests.get("https://api.openweathermap.org/data/2.5/weather", params=parameters) # Get the weather data
response.raise_for_status() # Raise an exception if the status code is not 200
weather_data = response.json() # Convert the data to JSON
print(weather_data["weather"][0]) # Print the weather data
will_rain = False # Initialize the will_rain variable


condition_code = weather_data["weather"][0]["id"] # Get the condition code
if int(condition_code) < 700: # Check if the condition code is less than 700
    will_rain = True # Set the will_rain variable to True
print(condition_code) 
if will_rain: # Check if it will rain
    message = client.messages.create( # Send a message
        from_='whatsapp:[From Whatsapp Number]',
        body='Bring an Umberalla☂️',
        to='whatsapp:[To Whatsapp Number]'
        )




