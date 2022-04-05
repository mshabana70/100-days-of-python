# Life in Weeks

# PEMDAS (Left to Right)
# 
# ()
# **
# * /
# + -

# Create a program using maths and f-Strings that 
# tells us how many days, weeks, months we have left 
# if we live until 90 years old.
#
# It will take your current age as the input and output 
# a message with our time left in this format:
#
# You have x days, y weeks, and z months left.
#
# Where x, y and z are replaced with the actual calculated 
# numbers.
#
#
# Example Input: How old are you in years?
#
# 56
#
#
# Example Output:
# 
# You have 12410 days, 1768 weeks, and 408 months left.


# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# Find how many years left with casted age value
yearsLeft = 90 - int(age)

# Convert yearsLeft to day, months and weeks
days = yearsLeft * 365
months = yearsLeft * 12
weeks = yearsLeft * 52

# Return values in a concated return string
print("You have ", days, " days, ", weeks, " weeks, ", months, " months left.")
