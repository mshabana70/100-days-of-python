# Day 12 Project - Number Guessing Game
#
# Build a game where you are to guess a number between 1 and 100 inclusive.
# You can select a difficulty between easy, medium and hard.
#
# Easy, you have 10 attempts to guess the number correctly
# Medium, you have 7 attempts to guess the number correctly
# Hard, you have 5 attempts to guess the number correctly
#
# If you guess is above the target number, you will get a response of "Too High"
# If you guess is below the target number, you will get a response of "Too Low"
#
# Game will end once you are out of attempts

# Import random
import random

# Pick a target_num from 1 to 100
target_num = random.randint(1, 101)
print(f"Random num is {target_num}")
difficulty_dict = {
    "easy": 10,
    "medium": 7,
    "hard": 5,
}

# Ask user to select a difficulty
difficulty = input("Please pick a difficulty to play on. 'Easy', 'Medium', or 'Hard':").lower()
attempts = 0

# set attempts of game based on the difficulty the user picked
attempts = difficulty_dict[difficulty] # 10, 7, or 5
#print(f"You have {attempts} left to guess the number.")

# Run the guessing game as long as there are attempts left (loop)
player_won = False
while not player_won:
    # Let user know of the number of attempts left
    print(f"You have {attempts} left to guess the number.")

    # ask user to provide a guess
    guess_num = int(input("Guess a number: "))

    # If guess matches target, user wins break loop
    if guess_num == target_num:
        print(f"Congrats you win! The number was {target_num}")
        player_won = True
    # If guess is above target, return too high (decrease attempts by 1)
    elif guess_num > target_num:
        print("Too High.")
        attempts -= 1
    # If guess is below target, return too low (decrease attempts by 1)
    else:
        print("Too Low.")
        attempts -= 1

    # If user still has attempts and hasnt won, return 'Guess another number.'
    if attempts > 0 and not player_won:
        print("Guess another number.")
    # If user has 0 attempts and hasnt won, break loop and let user know.
    elif attempts == 0 and not player_won:
        player_won = True
        print(f"You are all out of attempts. The correct number was {target_num}.")

