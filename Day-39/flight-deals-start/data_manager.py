import requests
import os
from pprint import pprint

SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")
SHEETY_AUTH = os.environ.get("SHEETY_AUTH")
FLIGHT_AUTH = os.environ.get("FLIGHT_AUTH")


class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.endpoint = SHEETY_ENDPOINT
        self.sheety_header = {
            "Authorization": f"Bearer {SHEETY_AUTH}"
        }
        self.response = ""
    
    def get_data(self):
        '''Get all records in our Flight sheet'''
        self.response = requests.get(url=self.endpoint, headers=self.sheety_header)
        return self.response.json()["prices"]
    
    def update_data(self, column, value):

    
    # def get_IATA(self):
    #     '''Returns the IATA of each city in our sheets'''
    #     cities = self.get_data()["prices"]
    #     location_endpoint = "https://tequila-api.kiwi.com/locations/anything"
    #     for city in cities:
    #         name_of_city = city["city"]
    #         flight_parameters = {
    #             "apikey": FLIGHT_AUTH,
    #             "key": "name",
    #             "value": name_of_city
    #         }
        
    #     self.response = request.post(url=location_endpoint, params=flight_parameters)
    #     return self.response.json()
    



