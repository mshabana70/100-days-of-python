# Day 27 - Advanced Arguments in Python

# Arguments with Key words
def my_function_key(a, b, c):
    return a + b + c

# We would have to call the function like this
print(my_function_key(a = 1, b = 3, c = 6))

# Arguments with Default Values
def my_function_default(a = 1, b = 2, c = 3):
    return a + b + c

# We can call this function without passing any arguments
# This is because we set default values for the arguments
# That way we can change the arguments we need only
print(my_function_default())
print(my_function_default(a = 10))
print(my_function_default(c = 12))


# Unlimted Arguments: args

# What if we want our function to be flexible with the number of 
# arguments we can pass through
# The key part is the asterk (*)
def add(*args):
    result = 0
    for n in args:
        result += n
    return result

# We can call the function with any number of arguments now
print(add(1, 2, 3, 4, 5, 6)) # Result is 21

# With this method of unlimited arguments, we access the arguments by position
# What if we want to access arguments by name?

# Unlimited Arguments: kwargs (Many Keyworded arguments)

# We use two asterks here (**)
def calculate(n, **kwargs):
    #print(kwargs, type(kwargs)) # Dictionary data structure
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

#calculate(add = 3, multiply = 5) # kwargs = {'add': 3, 'multiply': 5}
calculate(2, add = 3, multiply = 5) # output = 25

# Create a class like Tk (using **kwargs)

class Car:

    def __init__(self, **kw):
        #self.make = kw["make"]
        #self.model = kw["model"]

        # .get() is better to use here because what if there is no
        # 'make' or 'model' arg passed? Then .get() will return None,
        # rather than crash the program.
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car = Car(make = "Toyota", model = "Camery")
print(my_car.make) # output = Toyota
print(my_car.model) # output = Camery

my_car_2 = Car(make = "Nissan")
print(my_car_2.make) # output = Nissan
print(my_car_2.model) # output = None