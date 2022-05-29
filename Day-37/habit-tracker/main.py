import requests

PIXELA_USERNAME = "mshabana70"
PIXELA_TOKEN = "isjaogoy328o3896sgh"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"

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
    "id": "graph123",
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

response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=header)
print(response.text)



