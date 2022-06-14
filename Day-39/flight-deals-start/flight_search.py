import requests
import os
from data_manager import DataManager

FLIGHT_URL = "https://tequila-api.kiwi.com/locations/query"
FLIGHT_AUTH = os.environ.get("FLIGHT_AUTH")


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def get_IATA(self, city_name):
        '''Get IATA Code from Tequila Flight Search API'''
        #code = "TESTING"
        # We need to make a get call to the flight search api
        query_header = {
            "apiKey": FLIGHT_AUTH
        }

        query_params = {
            "term": city_name,
            "location-types": "city"
        }
        response = requests.get(url = FLIGHT_URL, params = query_params, headers=query_header)
        code = response.json()["locations"][0]["code"]
        return code

