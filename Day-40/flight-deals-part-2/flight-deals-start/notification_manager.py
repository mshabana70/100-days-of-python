from twilio.rest import Client
import os

API_SID = os.environ.get("TWILIO_SID")
API_KEY = os.environ.get("TWILIO_KEY")

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.sender_num = "+12058582732"
        self.recepient_num = "+16464278840"

    def send_sms(self, price, departure_city, departure_code, arrival_city, arrival_code, out_date, in_date):
        body = f"Low Price Alert! Only ${price} to fly from {departure_city}-{departure_code} to {arrival_city}-{arrival_code}, from {out_date} to {in_date}."
        client = Client(API_SID, API_KEY)
        message = client.messages.create(
            body=body,
            from_=self.sender_num,
            to=self.recepient_num
        )
        print(message.status)
