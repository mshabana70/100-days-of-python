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

# Main function to prompt user to play
def game():

    score = 0
    continue_game = True
    print(logo)
    celeb_a = random_celeb()
    while continue_game:
        
        celeb_b = random_celeb()
        if celeb_a['name'] != celeb_b['name']:
            compare_result = compare_celeb(celeb_a, celeb_b)
        else:
            game()

        # Show user what celebs to compare
        print(f"Compare One: {celeb_a['name']} is a {celeb_a['description']} from {celeb_a['country']}")
        print(vs)
        print(f"Compare Two: {celeb_b['name']} is a {celeb_b['description']} from {celeb_b['country']}")

        user_guess = int(input("Which Celebrity is more popular? Type '1' for One, '2' for Two: "))

        if user_guess == compare_result:
            celeb_a = celeb_b
            score += 1
            print(f"You're correct! Current score: {score}")
        else:
            if score > 5:
                print(f"You were on a roll! Your score is {score}. Better luck next time!")
            else:
                print(f"That is incorrect. You made the wrong guess, sorry!\nYour score is {score}.")
            continue_game = False


#start game
game()