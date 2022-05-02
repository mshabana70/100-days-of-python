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


# Unlimted Arguments

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