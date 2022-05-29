import requests

PIXELA_ENDPOINT = "https://pixe.la/v1/users"

user_params = {
    "token": "isjaogoy328o3896sgh",
    "username": "mahmoud",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# passing in json data for user parameters
requests.post(url=PIXELA_ENDPOINT, json=user_params)