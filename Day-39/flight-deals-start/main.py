#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta

# Get Data from our google spread sheets
sheet_data = DataManager()
fs = FlightSearch()
sheet_data.get_data()

now_date = datetime.now()
six_months_date = now_date + timedelta(days=183)

# Departure dates
flight_date_from = now_date.strftime("%m/%d/%Y")
flight_date_to = six_months_date.strftime("%m/%d/%Y")


# Check if IATA codes exist in our data
for city in sheet_data.data:
    if city["iataCode"] != "":
        # Parse through city codes to get flight pricing
        flight_price = fs.get_flight_price(
            dest_city=city["city"], 
            date_from=flight_date_from, 
            date_to=flight_date_to, 
            return_date_from, 
            return_date_to
        ) 
        print(flight_price)
    else:
        iataCode = fs.get_IATA(city["city"])
        city["iataCode"] = iataCode

sheet_data.update_data_codes()
#print(sheet_data.data)


