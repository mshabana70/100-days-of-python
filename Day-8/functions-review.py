# Day 8 - Review
# 
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

# Create greet()
def greet():
    print("Hello from greet!")
    print("It is a pleasure to see you")
    print("Wish you a great day!")

greet()

# Wouldnt it be nice if we can add some customization 
# to our function?

# Function that allows for an input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How is your day {name}?")

greet_with_name("Mahmoud")