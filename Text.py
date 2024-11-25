import logging
from twilio.rest import Client

# Enable debugging at the DEBUG level lowest level. Other options are CRITICAL 50 || ERROR 40 || WARNING 30 || INFO 20|| DEBUG 10 
logging.basicConfig(level=logging.DEBUG)

# Function which has an account 
def text(account_sid, auth_token, from_number, to_number, message_body):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=message_body,
        from_=from_number,
        to=to_number
    )
    return message.sid

from datetime import datetime

# Current date and time
current_datetime = datetime.now()

# Format the datetime as a string
timestamp = current_datetime.strftime("[%Y-%m-%d %H:%M:%S]")

# Timestamp
timestamp = f"{timestamp}" 

print(timestamp)


# Example Usage
if __name__ == "__main__":
    ACCOUNT_SID = "AC30cd08d8f54f6bd71e82510d3de45a72"
    AUTH_TOKEN = ""
    FROM_NUMBER = "+18339876850"  # Your Twilio phone number
    TO_NUMBER = "+13106660143"    # Recipient's phone number
    MESSAGE = f"{timestamp} Hello from Rahul Khanna.  The file name is Text.py 554331483951"

    message_sid = text(ACCOUNT_SID, AUTH_TOKEN, FROM_NUMBER, TO_NUMBER, MESSAGE)
    print(f"Message sent! SID: {message_sid}")



