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

# API Key from current weather service
API_KEY = "709ce3f5e5bb0c34dc2af53496ed79eb"
MY_LAT = 40.712776
MY_LONG = -74.005974

# API Parameters
parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
}

# Make request
response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)

# return HTTP status codes
response.raise_for_status()

# print response to console
json_data = response.json()
print(json_data)




