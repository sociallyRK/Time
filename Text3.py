from twilio.rest import Client

# Twilio credentials
ACCOUNT_SID = "AC30cd08d8f54f6bd71e82510d3de45a72"
AUTH_TOKEN = "02fa887cab4009b3957d8f679923bc10"

# Twilio client
client = Client(ACCOUNT_SID, AUTH_TOKEN)

# Send SMS
message = client.messages.create(
    body="Hello! This is Rahul Khanna.",  # Message content
    from_="+18339876850",                   # Your Twilio phone number
    to="+13106660143"                       # Recipient's phone number
)

print message.body