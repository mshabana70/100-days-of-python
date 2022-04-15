# Exercise 3 - Debug FizzBuzz
#
# Read this the code
# Spot the problems 🐞.
# Modify the code to fix the program.
# No shortcuts - don't copy-paste to replace the code entirely with a working solution.

# for number in range(1, 101): # for every number between 1 - 101 (101 exclusive)
#   if number % 3 == 0 or number % 5 == 0: # if number is divisible by 3 OR 5
#     print("FizzBuzz")
#   if number % 3 == 0: # If number is divisible by 3
#     print("Fizz")
#   if number % 5 == 0: # If number is divisible by 5
#     print("Buzz")
#   else: # if not divisible by 5 or 3 than print number
#     print([number])

# debugged solution
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0: # divisible by 3 AND 5
        print("FizzBuzz")
    elif number % 3 == 0: # only execute when above expressions fails
        print("Fizz")
    elif number % 5 == 0: # only execute when above expressions fails
        print("Buzz")
    else:
        print([number])