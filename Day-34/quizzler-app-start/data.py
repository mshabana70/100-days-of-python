# Challenge 1: Get 10 (True/False) questions using the Trivia API
# This will help us get 10 different questions each time

import requests

trivia_parameters = {
    "amount": 10,
    "type" : "boolean"
}

response = requests.get(url="https://opentdb.com/api.php", params=trivia_parameters)
response.raise_for_status # check for status error

data = response.json()

# Assign questions to question_data
question_data = data["results"]




