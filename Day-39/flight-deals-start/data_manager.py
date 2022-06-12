import requests
import os
from pprint import pprint

SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")
SHEETY_AUTH = os.environ.get("SHEETY_AUTH")
FLIGHT_AUTH = os.environ.get("FLIGHT_AUTH")


class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.sheety_header = {
            "Authorization": f"Bearer {SHEETY_AUTH}"
        }
        self.data = {}
    
    def get_data(self):
        '''Get all records in our Flight sheet'''
        response = requests.get(url=SHEETY_ENDPOINT, headers=self.sheety_header)
        self.data = response.json()["prices"]
        return self.data
    
    def update_data_codes(self):
        '''Update a record in our Flight sheet'''
        for city in self.data:
            put_params = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY_ENDPOINT}/{city['id']}", headers=self.sheety_header, json=put_params)
            print(response.text)

    


