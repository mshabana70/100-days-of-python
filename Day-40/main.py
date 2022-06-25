# Starting File for Part 2 of Flight deals project
import requests

# Starting console print
print("Welcome to Mahmoud's Flight Club!\nWe find the best flight deals and email it to you.")

first_name = input("What is your first name?\n").capitalize()
last_name = input("What is your last name?\n").capitalize()

does_match = False
email = input("what is your email?\n")
while not (does_match):
  validate_email = input("Type your email again.\n")
  if validate_email == email:
    does_match = True
  else:
    print("Sorry! the email does not match.")

