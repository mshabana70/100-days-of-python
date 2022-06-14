import requests
import os
from data_manager import DataManager

FLIGHT_URL = "https://tequila-api.kiwi.com/v2/search"
FLIGHT_AUTH = os.environ.get("FLIGHT_AUTH")


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.city = ""
        self.endpoint = FLIGHT_URL
    
    def get_IATA(self, city_name):
        '''Get IATA Code from Tequila Flight Search API'''
        #code = "TESTING"
        # We need to make a get call to the flight search api
        query_params = {
            "apiKey": FLIGHT_AUTH,
            "term": city_name
        }
        response = requests.get(url = FLIGHT_URL, json = FLIGHT_AUTH)
        print(response.text)
        return code

