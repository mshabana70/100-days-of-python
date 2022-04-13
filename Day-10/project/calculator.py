# Day 10 Project - Calculator with functions
#
# Create a classic calculator program using functions
# with return keywords

# Import Art
import art

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

# Exponent
def exp(n1, n2):
    """Returns the first num to the power of the second num"""
    return n1 ** n2

# Dictionary of functions and their operators (key = operator, value = function name)
operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
    "**": exp,
}

#function = operations["*"]
#function(2, 3) # Same as calling multiply(2, 3)

# Calculator function starts here (for recursion purposes)
def calculator():
    print(art.logo)
    # Ask for user input
    num1 = float(input("What is the first number?: "))

    # Loop through dictionary and show what symbols are available to the user
    print("Here are the operations available to you.")
    for operator in operations:
        print(operator, "\n") # +, -, *, /

    # Continue calculation from previous expression
    continue_calc = True
    while continue_calc:

        # Set up continuous calculation
        operation_symbol = input("Pick an operation: ")
        # Ask user for second num
        num2 = float(input("What is the next number?: "))
        # Take operation_symbol and pick the value (function) associated to it
        calculator_function = operations[operation_symbol]
        answer = calculator_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        check_user = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation (if you wish to terminate type 'q'): ")
        if check_user == 'y':
            num1 = answer
        elif check_user == 'q':
            quit()
        else:
            continue_cal = False
            calculator() # recursion to start from the beginning again
            #print("Calculator program has ended.")

# How can we restart from the beginning rather than continue from the previous answer?
# We would have to use recursion
calculator()