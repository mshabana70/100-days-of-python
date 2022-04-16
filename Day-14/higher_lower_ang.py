# Day 14 Project - Angela implementation

from project import game_data
from project import art
import random


def format_data(account):
    """Format the account data into printable format."""
    # format the account data into printable format
    account_name = account['name']
    account_descr = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_descr} from {account_country}"

def check_answer(guess, a_followers, b_followers):
    """Take the user guess and follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"
        

# Display art
print(art.logo)
score = 0
game_should_continue = True
account_b = random.choice(game_data.data)

# Make code repeatable
while game_should_continue:

    # Generate a random account from the game data

    # making the accounts at position B become the next account at position A.
    account_a = account_b
    account_b = random.choice(game_data.data)

    while account_a == account_b:
        account_b = random.choice(game_data.data)

    print(f"Compare A: {format_data(account_a)}.")
    print(art.vs)
    print(f"Against B: {format_data(account_b)}.")

    # ask user for a guess.
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # check if user is correct
    ## get follower count of each account
    a_follower_count = account_a['follower_count']
    b_follower_count = account_b['follower_count']
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # give user feedback to their guess
    # Score keeping
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}")

