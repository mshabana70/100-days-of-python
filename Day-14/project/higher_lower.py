# Day 14 Project - Higher Lower Game
#
# Develop a game similar where you compare the popularity of 
# two people. You well be comparing two randomly picked celebraties 
# and guess which one has more followers or is more popular.
#
# Functionality:
#
# Have two randomly picked objects from an external data source (external file).
#
# Prompt user to pick between objects based on their popularity.
#
# If user is correct, continue game. If the user selects the wrong 
# Celebrity, than end the game and return a score to the user.


# Imports
import random
from art import logo, vs
from game_data import data

# Function to retrieve random objects
def random_celeb():
    celeb_list = data
    return random.choice(celeb_list)

# Compare celeb popularity (can be done before the user inputs anything)
def compare_celeb(celeb_one, celeb_two):
    if celeb_one["follower_count"] > celeb_two["follower_count"]:
        return 1
    elif celeb_one["follower_count"] < celeb_two["follower_count"]:
        return 2
    else:
        return 0

# Main function to prompt user to play
def game():

    score = 0
    continue_game = True
    print(logo)

    while continue_game:
        
        celeb_a = random_celeb()
        celeb_b = random_celeb()
        compare_result = compare_celeb(celeb_a, celeb_b)

        # Show user what celebs to compare
        

        user_guess = int(input("Which Celebrity is more popular? Type '1' for A, '2' for B: "))

        if user_guess == compare_result:
            score += 1
        else:
            print(f"That is incorrect. {")


