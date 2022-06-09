#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch

# Get Data from our google spread sheets
dt = DataManager()
fs = FlightSearch()
sheet_data = dt.get_data()

# Check if IATA codes exist in our data
for city in sheet_data:
    if city["iataCode"] != "":
        print(city)
    else:
        iataCode = fs.get_IATA(city["city"])
        city["iataCode"] = iataCode

for row in sheet_data:
    response = sheet