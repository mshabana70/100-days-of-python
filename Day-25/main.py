# Day 25 - Working with CSV files

# Open CSV file

weather_list = []
clean_weather_list = []
with open("/Users/mahmoudshabana/Documents/Udemy/100-days-of-python/Day-25/weather_data.csv") as weather_data:

    # Read each line from csv file to a list
    weather_list = weather_data.readlines()\


for weather in weather_list:
    clean_weather = weather.strip()
    clean_weather_list.append(clean_weather)
print(clean_weather_list)

# Open file using csv library
import csv

with open("/Users/mahmoudshabana/Documents/Udemy/100-days-of-python/Day-25/weather_data.csv") as weather_data:
    weather = csv.reader(weather_data)
    for row in weather:
        print(row) # print every row in csv data
