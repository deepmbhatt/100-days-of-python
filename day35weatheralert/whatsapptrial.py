from twilio.rest import Client

account_sid = 'YOUR ACCOUNT SID'
auth_token = 'YOUR AUTH TOKEN'
client = Client(account_sid, auth_token) # Create a Twilio client

message = client.messages.create( # Send a message
  from_='whatsapp:YOUR TWILIO NUMBER',
  body='Hello from the other side',
  to='whatsapp:YOUR NUMBER'
)