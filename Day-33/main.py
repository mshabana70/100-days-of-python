# Making an API Request in python

# Response Codes
# 1XX: Hold On (still processing)
# 2XX: Here you go (successful)
# 3XX: Go Away (lack permissions)
# 4XX: You screwed up (Request does not exist)
# 5XX: I screwed up (Error on the server's side)

import requests
import datetime

MY_LAT = 40.712776
MY_LONG = -74.005974

# response = requests.get(url= "http://api.open-notify.org/iss-now.json")
# print(response) # Response [200]
# print(response.status_code) # Returns status code

# # raise exception if we come across an error code
# response.raise_for_status()

# # get actual response
# data = response.json()

# # We can also use the json as a dictionary and access keys using bracket notation
# #data = response.json()['iss_position']['latitude']
# #print(data) # Returns latitude of ISS

# longitude = data['iss_position']['longitude']
# latitude = data['iss_position']['latitude']

# # create tuple
# iss_position = (longitude, latitude)

# print(iss_position)

# Create a set of parameters with a dict 
# (must match parameters in docs: https://sunrise-sunset.org/api)


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,

}

response = requests.get(url = "https://api.sunrise-sunset.org/json", params= parameters)
response.raise_for_status() # Bad request without api parameters

# Our response data 
data = response.json()

# Lets split our string into just hours
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise, sunset)

time_now = datetime.datetime.now()

print(time_now.hour)