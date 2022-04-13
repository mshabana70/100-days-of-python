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
num1 = int(input("What is the first number?: "))
num2 = int(input("What is the second number?: "))

# Loop through dictionary and show what symbols are available to the user
print("Here are the operations available to you.")
for operator in operations:
    print(operator, "\n") # +, -, *, /

operation_symbol = input("Pick an operation from the line above: ")

# Take operation_symbol and pick the value (function) associated to it
function = operations[operation_symbol]

print(f"{num1} {operation_symbol} {num2} = {function(num1, num2)}")
