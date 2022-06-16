#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch

# Get Data from our google spread sheets
sheet_data = DataManager()
fs = FlightSearch()
sheet_data.get_data()

# Check if IATA codes exist in our data
for city in sheet_data.data:
    if city["iataCode"] != "":
        # Parse through city codes to get flight pricing 
        print(city)
    else:
        iataCode = fs.get_IATA(city["city"])
        city["iataCode"] = iataCode

sheet_data.update_data_codes()
#print(sheet_data.data)


