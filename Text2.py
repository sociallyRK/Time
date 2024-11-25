import os
from twilio.rest import Client

# Set environment variables for your credentials
# Read more at http://twil.io/secure

account_sid = "AC30cd08d8f54f6bd71e82510d3de45a72"
auth_token = ""
client = Client(account_sid, auth_token)

call = client.calls.create(
  url="http://demo.twilio.com/docs/voice.xml",
  to="+13106660143",
  from_="+18339876850"
)

print(call.sid)
