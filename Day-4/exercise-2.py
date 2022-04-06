# Exercise 2 - Bank Roulette
#
#
# You are going to write a program that will select a 
# random name from a list of names. The person selected 
# will have to pay for everybody's food bill.
# 
# Important: You are not allowed to use the choice() function.
# 
# Line 8 splits the string names_string into individual names 
# and puts them inside a List called names. For this to work, 
# you must enter all the names as names followed by comma then 
# space. e.g. name, name, name
# 
# When you run the code, just use a random number as the seed. 
# e.g. 67346 It doesn't matter what you chose, it's only for 
# our testing code to check your work.
#
# Example Input:
#
# Angela, Ben, Jenny, Michael, Chloe
#
# Example Output:
# 
# Michael is going to buy the meal today!

# Lets handle our imports first
import random

# Lets ask our user for input of a list
names_string = input("What are everyone's names, separated by a comma. ")

# We must split our string by using the comma as the delimiter
names = names_string.split(", ") # names will be a list of the names in names_string

# Now we must generate a random integer from 0 to the index of the last name in the list

randomInt = random.randint(0, (len(names) - 1))
# we must subract the length of the list by one 

# Now we search for a random name in the list
randomName = names[randomInt]

print(f"{randomName} is going to buy the meal today!")
