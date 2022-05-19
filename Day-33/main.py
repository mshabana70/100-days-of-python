# Making an API Request in python

# Response Codes
# 1XX: Hold On (still processing)
# 2XX: Here you go (successful)
# 3XX: Go Away (lack permissions)
# 4XX: You screwed up (Request does not exist)
# 5XX: I screwed up (Error on the server's side)

import requests

response = requests.get(url= "http://api.open-notify.org/iss-now.json")
print(response) # Response [200]