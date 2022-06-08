import requests
import os

FLIGHT_URL = "https://tequila-api.kiwi.com/v2/search"


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self, city):
        self.city = city
        self.endpoint = FLIGHT_URL
        

    pass