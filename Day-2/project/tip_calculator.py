# Tip Calculator Project

# Code a tip calulator that takes in user input of
# the total bill price, the percentage you wish to tip,
# and the number of people total splitting the bill.
#
#
# Example Input:
# What is the total bill?
# 124.56
# 
# What percentage tip would you like to give? 10, 12, or, 15?
# 12
# 
# How many people to split the bill?
# 7
#
# 
# Example Output:
# Each person should pay: $19.93
# Note we only want the return value to be rounded 
# to 2 decimal places

# Welcome Message
print("Welcome to the tip calculator.")

# Store user inputs to variables
total_bill = input("What was the total bill? $")
tip_percentage = input("What percentage tip would you like to give? 10, 12, or 15?")
total_people = input("How many people are splitting the bill?")

# Cast values to integers and floats
total_people = int(total_people)
tip_percentage = int(tip_percentage) / 100
total_bill = float(total_bill)

# Calculate tip per person (without bill added)
tip_per_person = (total_bill * tip_percentage) / total_people

# Calculate bill per person (without tip added)
bill_per_person = (total_bill / total_people)

# Add Bill and tip per person
total_per_person = bill_per_person + tip_per_person

# Lets clean up the calculation
#final_result = (total_bill / total_people) * (1 + tip_percentage)
final_result = "{:.2f}".format(total_per_person)
# Return value, rounded to nearest 2 decimal places
#print(f"Each person should pay: ${round(total_per_person, 2)}")
print(f"Each person should pay: ${final_result}")


