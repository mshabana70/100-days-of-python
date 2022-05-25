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

import requests

# CONSTANTS
API_KEY = "709ce3f5e5bb0c34dc2af53496ed79eb"
OWM_URL = "https://api.openweathermap.org/data/2.5/onecall"
MY_LAT = 40.712776
MY_LONG = -74.005974

# Test
TEST_LAT = 35.149532
TEST_LONG = -90.048981

# API Parameters
parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
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





