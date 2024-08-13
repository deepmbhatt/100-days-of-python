from twilio.rest import Client

account_sid = '[Your SID]'
auth_token = '[Your Toker]'
client = Client(account_sid, auth_token) # Create a Twilio client

message = client.messages.create( # Send a message
  from_='[From Number]',
  body='Hello from Python!',
  to='[To Number]'
)

print(message.sid)