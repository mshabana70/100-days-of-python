# Starting File for Part 2 of Flight deals project
import requests

SHEETY_ENDPOINT = "https://api.sheety.co/dfe6f6bfa0c16bea1d2f73e164d47a7c/flightDeals/users"

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
    print("You're in the club!")
  else:
    print("Sorry! the email does not match.")

post_params = {
    "user": {
        "firstName": first_name,
        "lastName": last_name,
        "email": email
    } 
}

response = requests.post(url=SHEETY_ENDPOINT, json=post_params)
response.raise_for_status()
