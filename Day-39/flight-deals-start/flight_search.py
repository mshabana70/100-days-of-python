import requests
import os
from data_manager import DataManager

FLIGHT_URL = "https://tequila-api.kiwi.com/v2/search"


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.city = ""
        self.endpoint = FLIGHT_URL
    
    def get_IATA(self, city_name):
        '''Get IATA Code from Tequila Flight Search API'''
        return "Code from Flight Search"

