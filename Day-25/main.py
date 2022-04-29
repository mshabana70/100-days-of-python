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
    temperatures = []
    for row in weather:
        #print(row) # print every row in csv data
        if row[1] != "temp":
            temp = int(row[1])
            temperatures.append(temp)
    print(temperatures)

# This is alot of work to get one column of data
# We can use 'pandas' library to avoid all this extra coding for simplicity
import pandas as pd

# Read csv data in one line of code
weather_data_pd = pd.read_csv("/Users/mahmoudshabana/Documents/Udemy/100-days-of-python/Day-25/weather_data.csv") 
print(weather_data_pd)

# Getting the temp column like we did with csv library (but using pandas)
print(weather_data_pd["temp"])

# Check the type of weather_data_pd
print(type(weather_data_pd)) # Pandas Dataframe data type

# Dataframe definition:
# It is the entire data file that is formatted like an excel sheet or a csv.

# Check the type of a column in the weather_data_pd Dataframe
print(type(weather_data_pd["temp"])) # Pandas Series data type

# Series definition:
# A 1 dimensional data structure that is used to make up the 
# 2 dimensional Dataframe. (Equivilent to a list)

# Convert Dataframe to dictionary
weather_data_dict = weather_data_pd.to_dict()
print(weather_data_dict)

# Convert series to list
temp_list = weather_data_pd["temp"].to_list()
print(temp_list)

# CHALLENGE: Find the average temp in our list of temp
avg_temp = sum(temp_list) / len(temp_list)
print(f"Average temperature: {round(avg_temp, 2)}")

# simpilar way:
avg_temp_series = weather_data_pd["temp"].mean()
print(f"Average temp using series functions: {avg_temp_series}")

# CHALLENGE: Find the maximum temp in our temp series using a series func
max_temp = weather_data_pd["temp"].max()
print(f"Maximum temperature: {max_temp}")

# We have seen how to access a column with bracket notation, but you can also use dot notation
condition_series = weather_data_pd.condition
print(condition_series)

# Get data from a row
print(weather_data_pd[weather_data_pd.day == "Monday"])

# CHALLENGE: Pull row of data where weather is maximum
print(weather_data_pd[weather_data_pd.temp == weather_data_pd.temp.max()])

monday = weather_data_pd[weather_data_pd.day == "Monday"]
fahrenheit = (int(monday.temp) * (9 / 5)) + 32 
print(fahrenheit)

# How to create a Dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

# create dataframe from dictionary
data = pd.DataFrame(data_dict)
#print(data)

# We can even convert our DataFrame to a csv file (just specify path)
data.to_csv("/Users/mahmoudshabana/Documents/Udemy/100-days-of-python/Day-25/new_data.csv")


