# Exercise 2 - Debug Leap Year
#
# Read this the code
# Spot the problems 🐞.
# Modify the code to fix the program.
# No shortcuts - don't copy-paste to replace the code entirely with a working solution.

#year = input("Which year do you want to check?") # This returns a TypeError
# Trying to use modulo on a string will fail
# Must cast the user input as an integer for the following conditional expressions
year = int(input("Which year do you want to check?"))

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")
  