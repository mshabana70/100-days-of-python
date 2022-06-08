#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager


dt = DataManager()

sheet_data = dt.get_data()
print(sheet_data)