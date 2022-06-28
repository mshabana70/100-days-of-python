import requests
import os
import pprint
from data_manager import DataManager
from flight_data import FlightData

FLIGHT_URL = "https://tequila-api.kiwi.com"
FLIGHT_AUTH = os.environ.get("FLIGHT_AUTH")


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.departure_city_code = "NYC"
        self.departure_city = "New York City"
        self.currency = "USD"
        self.price = 1000
        self.flight_data = ""

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
    
    def get_flight_price(self, dest_city, date_from, date_to):
        '''Get Flight price for specified trip.'''
        # Set up request headers and body
        search_endpoint = f"{FLIGHT_URL}/v2/search"
        query_header = {
            "apiKey": FLIGHT_AUTH
        }
        # Not working for round trips????
        query_params = {
            "fly_from": self.departure_city_code,
            "fly_to": dest_city,
            "date_from": date_from,
            "date_to": date_to,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "curr": self.currency,
            "max_stopovers": 0,
            "one_for_city": 1
        }

        # Create Get request and grab response
        response = requests.get(url=search_endpoint, headers=query_header, params=query_params)

        # Get flight price from response
        try:
            data = response.json()["data"][0]
        except:
            print(f"No flights found for {dest_city}.")
            query_params["max_stopovers"] = 1
            response = requests.get(url=search_endpoint, headers=query_header, params=query_params)
            pprint.pprint(response.json()["all_stopover_airports"])
        else:
            # Append response to flight data object
            flight_data = FlightData(
                price=data["price"],
                origin_city=self.departure_city,
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )

            #return f"{self.flight_data.destination_city}: ${self.flight_data.price}"
            # Return FlightData object
            return flight_data




