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
while attempts > 0:
    print(f"You have {attempts} left to guess the number.")

    # ask user to provide a guess
    guess_num = int(input("Guess a number: "))

    if guess_num == target_num:
        print(f"Congrats you win! The number was {target_num}")
        attempts = 0
    elif guess_num > target_num:
        print("Too High.")
        print("Guess another number.")
        attempts -= 1
    else:
        print("Too Low.")
        print("Guess another number.")
        attempts -= 1

