import requests
from datetime import datetime

PIXELA_USERNAME = "mshabana70"
PIXELA_TOKEN = "isjaogoy328o3896sgh"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
PIXELA_GRAPH_ID = "graph123"

user_params = {
    "token": PIXELA_TOKEN,
    "username": PIXELA_USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Passing in json data for user parameters 
# Comment out code below once user is created
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs"


graph_config = {
    "id": PIXELA_GRAPH_ID,
    "name": "Running Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

# Headers are more secure than parameters
# (how to authenticate using headers)
header = {
    "X-USER-TOKEN": PIXELA_TOKEN
}

# Comment out code once graph is created
# response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=header)
# print(response.text)

# POST a pixel on our graph

PIXEL_ENDPOINT = f"{GRAPH_ENDPOINT}/{PIXELA_GRAPH_ID}"

today = datetime.now()
# print(today.strftime("%Y%m%d"))


pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "4.5",
}

# response = requests.post(url=PIXEL_ENDPOINT, json=pixel_config, headers=header)
# print(response.text)

