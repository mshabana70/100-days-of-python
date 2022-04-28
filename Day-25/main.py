# Day 25 - Working with CSV files

# Open CSV file

weather_list = []
with open("/Users/mahmoudshabana/Documents/Udemy/100-days-of-python/Day-25/weather_data.csv") as weather_data:

    # Read each line from csv file to a list
    weather_list = weather_data.readlines()

print(weather_list)