# Day 26 Exercise - Dictionary Comprehension (bonus)
#
# You are going to use Dictionary Comprehsion to create a dictionary 
# called weather_f that takes each temperature in degrees Celcius and
# converts it into degrees Fahrenhiet
#
# To convert temp_c to temp_f:
# (temp_c * (9/5)) + 32 = temp_f 
#
#
# Example Output:
# {
#  'Monday': 53.6,
#  'Tuesday': 57.2,
#  'Wednesday': 59.0,
#  'Thursday': 57.2,
#  'Friday': 69.8,
#  'Saturday': 71.6,
#  'Sunday': 75.2,
# }

weather_c = {
    'Monday': 12,
    'Tuesday': 14,
    'Wednesday': 15,
    'Thursday': 14,
    'Friday': 21,
    'Saturday': 22,
    'Sunday': 24,
}

# Don't change code above 👆

# Write your code below:

result = {day:(round(((temp_c * (9/5)) + 32), 1)) for (day, temp_c) in weather_c.items()}

print(result)