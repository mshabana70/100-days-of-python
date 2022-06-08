#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager

# Get Data from our google spread sheets
dt = DataManager()
sheet_data = dt.get_data()

# Check if IATA codes exist in our data
for city in sheet_data:
    if city["iataCode"] is not None:
        print(city)
    else:
        sheet_data = sheet_data.update_data("iataCode", "TESTING")

print(sheet_data)