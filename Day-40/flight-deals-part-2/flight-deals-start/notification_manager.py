from twilio.rest import Client
import os

API_SID = os.environ.get("TWILIO_SID")
API_KEY = os.environ.get("TWILIO_KEY")

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.sender_num = "+12058582732"
        self.recepient_num = "+16464278840"

    def send_sms(self, messageBody):
        client = Client(API_SID, API_KEY)
        message = client.messages.create(
            body=messageBody,
            from_=self.sender_num,
            to=self.recepient_num
        )
        print(message.status)
