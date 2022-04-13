# Day 10 Project - Calculator with functions
#
# Create a classic calculator program using functions
# with return keywords


# Calculator Functionality

# Add
def add(n1, n2):
    """Returns the sum of two integers"""
    return n1 + n2

# Subtract
def subtract(n1, n2):
    """Returns the difference of two integers"""
    return n1 - n2

# Multiply
def multiply(n1, n2):
    """Returns the product of two integers"""
    return n1 * n2

# Divide
def divide(n1, n2):
    """Returns the quotient of two integers"""
    return n1 / n2

# Dictionary of functions and their operators (key = operator, value = function name)
operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

#function = operations["*"]
#function(2, 3) # Same as calling multiply(2, 3)

# Ask for user input
