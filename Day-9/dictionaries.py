# Day 9 - Dictionaries

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again."
}

# Retrieving items using the Key
print(programming_dictionary["Bug"])
print(programming_dictionary["Function"])
print(programming_dictionary["Loop"])

# Printing whole dictionary
print(programming_dictionary)

# Add a new piece of data programmatically
programming_dictionary["Variable"] = "A name to assign and store data to for future retrieval (can be one of many data types)."
print(programming_dictionary["Variable"])

# Edit existing item in dictionary
programming_dictionary["Bug"] = "A pain in the butt."
print(programming_dictionary)

# Create an empty dictionary
empty_dictionary = {}

# Wipe existing dictionary
programming_dictionary = {}
print(programming_dictionary) # wiped dictionary