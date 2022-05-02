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
