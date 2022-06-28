from twilio.rest import Client
import os
import smtplib

API_SID = os.environ.get("TWILIO_SID")
API_KEY = os.environ.get("TWILIO_KEY")
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")

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

    def send_email(self, emails, message, link):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(email=MY_EMAIL, password=MY_EMAIL_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )
