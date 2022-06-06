import requests
import os

SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")
SHEETY_AUTH = os.environ.get("SHEETY_AUTH")


class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.endpoint = SHEETY_ENDPOINT
        self.sheety_header = {
            "Authorization": f"Bearer {SHEETY_AUTH}"
        }
        self.response = ""
    
    def get_cities(self):
        self.response = requests.request('GET', url=self.endpoint, headers=self.sheety_header)
        return self.response.text


    pass

dm = DataManager()
print(dm.get_cities())