#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager

# Get Data from our google spread sheets
sheet_data = DataManager()
fs = FlightSearch()
sheet_data.get_data()

now_date = datetime.now()
tomorrow_date = now_date + timedelta(days=1)
six_months_date = tomorrow_date + timedelta(days=183)
week_date = tomorrow_date + timedelta(weeks=1)
four_week_date = tomorrow_date + timedelta(weeks=4)

# Departure dates
flight_date_from = str(tomorrow_date.strftime("%d/%m/%Y"))
flight_date_to = str(six_months_date.strftime("%d/%m/%Y"))

# Return dates
flight_return_date_from = str(week_date.strftime("%d/%m/%Y"))
flight_return_date_to = str(four_week_date.strftime("%d/%m/%Y"))

# Check if IATA codes exist in our data
for city in sheet_data.data:
    if city["iataCode"] != "":
        # Parse through city codes to get flight pricing
        flight_data = fs.get_flight_price(
            dest_city=city["iataCode"], 
            date_from=flight_date_from, 
            date_to=flight_date_to
        )
        if (flight_data is not None) and (flight_data.price < city["lowestPrice"]):
            # Send sms message once flight data is retrieved
            messenger = NotificationManager()
            messenger.send_sms(
                price=flight_data.price, 
                departure_city=flight_data.origin_city, 
                departure_code=flight_data.origin_airport, 
                arrival_city=flight_data.destination_city, 
                arrival_code=flight_data.destination_airport, 
                out_date=flight_data.out_date, 
                in_date=flight_data.return_date
            )
    else:
        iataCode = fs.get_IATA(city["city"])
        city["iataCode"] = iataCode

sheet_data.update_data_codes()


