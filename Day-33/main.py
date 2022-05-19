# Making an API Request in python
import requests

response = requests.get(url= "http://api.open-notify.org/iss-now.json")
print(response) # Response [200]