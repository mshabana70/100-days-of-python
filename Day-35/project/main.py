# Day 35 - Keys, Authentication and Environment Variables: Send sms
#
# The APIs used prior were free so there wasnt much of a need to 
# authenticate the user.
# For example: a weather api might charge users depending on the load 
# of calls that the weather provider recieves using their API.
#
# Think of these paid APIs as a way of selling computed data. A way 
# to keep users from gaining access to this data for free is by using
# a "API Key".

# Challenge 1 - Make an API call from python with the One Call API 
# https://openweathermap.org/api/one-call-3

import os
import requests
from twilio.rest import Client

# CONSTANTS
API_KEY = os.environ.get("OMW_API_KEY") # environment variables
OWM_URL = "https://api.openweathermap.org/data/2.5/onecall"
MY_LAT = 40.712776
MY_LONG = -74.005974

# TWILIO CONSTANTS
account_sid = "AC6b18ea2b02ea95a18ea6b6526b1cae5f"
auth_token = os.environ.get("TWILIO_AUTH_KEY")

# Test
TEST_LAT = 35.149532
TEST_LONG = -90.048981

# API Parameters
parameters = {
    "lat": TEST_LAT,
    "lon": TEST_LONG,
    "appid": API_KEY,
    "exclude": "current,minutely,daily",
}

# Make request
response = requests.get(url=OWM_URL, params=parameters)

# raise HTTP status codes
response.raise_for_status()

# print response to console
weather_data = response.json()
#print(json_data)

# Challenge 2 - Check if it will rain in the next 12 hours
#
# If weather id is less than 700, bring an umbrella (snow & rain)

# create list of weather data for next 12 hours
half_day_list = [weather_data["hourly"][i]["weather"] for i in range(12)]

# Check if it rains at any point at the half day report
need_umbrella = False

for i in range(len(half_day_list)):
    if half_day_list[i][0]["id"] < 700:
        need_umbrella = True

# if so, return that the user needs an umbrella
if need_umbrella:
    # Create twilio message 
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body="It's going to rain today. Remember to bring an umbrella ⛈☔️",
                     from_="+12058582732",
                     to="+16464278840"
                 )

    # Make sure message was set successfully
    print(message.status)
    







