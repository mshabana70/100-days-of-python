# Day 17 - Classes
#
# How do we create a class?

class User:
    pass # just continuing

# Create an instance of our user class
user_1 = User()

# Every word is capitalized (Pascal casing for classes)

# Lets add an attribute
user_1.id = "001"
user_1.username = "mahmoud"

# Accessing these attributes of our objects
print(user_1.id)
print(user_1.username)