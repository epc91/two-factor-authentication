import os 
from twilio.rest import Client

# Complete with your own credentials by Twilio

account_sid = ""
auth_token = ""
client = Client(account_sid, auth_token)

def send_sms(user_code, phone_number):
    message = client.messages.create(
        body="Hi! You user and verification code is {}".format(user_code),
        from_="",
        to="{}".format(phone_number) 

    )
    print(message)
