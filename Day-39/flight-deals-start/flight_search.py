import requests
import os
from data_manager import DataManager

FLIGHT_URL = "https://tequila-api.kiwi.com"
FLIGHT_AUTH = os.environ.get("FLIGHT_AUTH")


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.departure_city_code = "NYC"
        self.departure_city = "New York City"
        self.currency = "USD"
        self.price = 600

    def get_IATA(self, city_name):
        '''Get IATA Code from Tequila Flight Search API'''
        #code = "TESTING"
        # We need to make a get call to the flight search api
        location_endpoint = f"{FLIGHT_URL}/locations/query"

        query_header = {
            "apiKey": FLIGHT_AUTH
        }

        query_params = {
            "term": city_name,
            "location-types": "city"
        }
        response = requests.get(url = location_endpoint, params = query_params, headers=query_header)
        code = response.json()["locations"][0]["code"]
        return code
    
    def get_flight_price(self, dest_city, date_from, date_to, return_date_from, return_date_to):
        '''Get Flight price for specified trip.'''
        # Set up request headers and body
        search_endpoint = f"{FLIGHT_URL}/v2/search"
        query_header = {
            "apiKey": FLIGHT_AUTH
        }
        query_params = {
            "fly_from": self.departure_city_code,
            "fly_to": dest_city,
            "date_from": date_from,
            "date_to": date_to,
            "return_from": return_date_from,
            "return_to": return_date_to,
            "flight_type": "round",
            "curr": self.currency,
            "price_to": self.price,
            "max_stopovers": 0
        }

        # Create Get request and grab response
        response = requests.get(url=search_endpoint, headers=query_header, params=query_params)

        # Get flight price from response
        flight_price = response.json()["data"]["price"]

        return flight_price




