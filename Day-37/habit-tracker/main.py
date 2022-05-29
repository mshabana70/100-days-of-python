import requests

PIXELA_ENDPOINT = "https://pixe.la/v1/users"

user_params = {
    "token": "isjaogoy328o3896sgh",
    "username": "mshabana70",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Passing in json data for user parameters 
# Comment out code below once user is created
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)