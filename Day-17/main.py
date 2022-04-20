# Day 17 - Classes
#
# How do we create a class?

class User:

    # In order to set starting attributes for object, we need to
    # initialize these values using a constructor
    # We can create a constructor using the special __init__() function
    def __init__(self, user_id, username):
        # __init__ function will be called everytime you create a new 
        # object from this class (user_1 = User())
        self.id = user_id
        self.username = username
        self.followers = 0 # default value


    pass # just continuing



# Create an instance of our user class
user_1 = User("", "")

# Every word is capitalized (Pascal casing for classes)

# Lets add an attribute
user_1.id = "001"
user_1.username = "mahmoud"

# Accessing these attributes of our objects
print(user_1.id)
print(user_1.username)

# Instead of creating the attributes outside of the class,
# we will use the constructor to set values to our existing
# attributes for our User object
user_2 = User("002", "shabana")

# access these attributes
print(user_2.id)
print(user_2.username)
print(user_2.followers) # Output should be 0 by default