# Day 7 Project - Hangman
#
# Build a program that works like the popular hangman game

# Step 1 of project

# TODO-1 - Randomly choose a word from the word_list and 
# assign it to the variable called target_word

# TODO-2 - Ask the user to guess a letter and assign their
# answer to a variable called guess. Make guess lowercase

# TODO-3 - Check if the letter the user guessed (guess) is 
# one of the letters in the target_word

# Import random module
# import random

# word_list = ["ardvark", "baboon", "camel"]

# # Choose a random word for target_word
# #randomInt = random.randint(0, len(word_list))
# #target_word = word_list[randomInt]
# target_word = random.choice(word_list)
# word_length = len(target_word)

# print(f"Psssst... The target word is {target_word}") # For testing

# Ask for User input on a guess letter and assign it to guess
#guess = input("Please guess a letter: ").lower()

# Check if guessed letter is in target_word (check each letter)
# for letter in target_word:
#     if guess == letter:
#         print("Right")
#     else:
#         print("Wrong")

# Step 2

# TODO-1 - Create an empty list called display.
# For each letter in the target_word, add an "_" to 
# 'display'.
# So if the target_word was "apple", display should be
# ["_", "_", "_", "_", "_"] with 5 "_" representing each 
# letter to guess.

# TODO-2 - Loop through each position in the target_word.
# If the letter at that position matches 'guess' then reveal
# that letter in the display at that position.
# e.g. if the the user guessed "p" and the target_word was "apple",
# then the display should be ["_", "p", "p", "_", "_"].

# TODO-3 - Print 'display' and you should see the guessed letter
# in the correct position and every other letter replace with "_".
# Hint - Dont worry about getting the user to guess the next letter.
# We'll tackle that in step 3.

# Create display list
# display = []
# display2 = []

# One solution with two loops

# Fill display list with underscore for each letter in target_word
# for i in range(word_length):
#     display.append("_")
#     display2.append("_")

# index and value is parsed with enumerate
# for index, letter in enumerate(target_word):
#     if letter == guess:
#         display[index] = guess

# another way without enumerate()
# for position in range(word_length):
#     if target_word[position] == guess:
#         display2[position] = guess
# print(display)
# print(display2)


# Step 3 

# TODO-1 - Use a while loop to let the user guess again. The loop 
# should only stop once the user has guessed all the letters in 
# the target_word and 'display' has no more blanks "_". Then you 
# can tell the user they've won.

# display
# display = []
# for _ in range(word_length):
#     display.append("_")

# end_game = False

# while not end_game:
#     # ask for a letter
#     guess = input("Please guess a letter: ").lower()
#     for index in range(word_length):
#         if target_word[index] == guess:
#             display[index] = guess
#     print(display)

#     if "_" not in display:
#         end_game = True
#         print("YAY! You win!")


# Step 4

# TODO-1 - Create a variable called 'lives' to keep track of the 
# number of lives left. Set 'lives' equal to 6

# TODO-2 - If guess is not a letter in the target_word, then reduce 
# 'lives' by 1. If lives goes down to 0 then the game should stop and
# it should print "You lose."

# TODO-3 - print the ASCII art from 'stages' that corresponds to the 
# current number of 'lives' the user has remaining.

# Stages
# stages = ['''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#       |
#       |
#       |
#       |
# =========
# ''']

# display
# display = []
# for _ in range(word_length):
#     display.append("_")

# lives = 6
# end_game = False

# while not end_game:
#     # Print Current progress
#     print(stages[lives])
#     print(display)

#     # ask for a letter
#     guess = input("Please guess a letter: ").lower()
#     for index in range(word_length):
#         if target_word[index] == guess:
#             display[index] = guess 

#     # If guess not in word at all, lose one life
#     if guess not in target_word:
#         lives -= 1   

#     # Check Current Progress
#     if "_" not in display:
#         end_game = True
#         print("YAY! You win!")
#     elif lives == 0:
#         end_game = True
#         print("You lose!")
#         print(stages[lives])

# Step 5 (Final)

# TODO-1 - Update the word_list to use the words from hangman_words.py

# TODO-2 - Import the logo from hangman_art.py and print it at the start 
# of game.

# TODO-3 - Import stages from hangman_art.py to clean up current code.

# Personal challenge - clean up code with functions

# imports
import random
import hangman_words
import hangman_art

# Set random word to guess
target_word = random.choice(hangman_words.word_list)
word_length = len(target_word)
display = []

def set_display(word_length):
    for _ in range(word_length):
        display.append("_")
    return display

def start_game():
    print(hangman_art.title)
    end_game = False
    lives = 6
    guesses = []

    while not end_game:
        # Print Current Progress
        print(hangman_art.stages[lives])
        print(display)

        # get user guess
        guess = input("Guess a letter: ").lower()

        # Check if the letter was guessed already
        if guess not in guesses:
            guesses.append(guess)
            for index in range(word_length):
                if target_word[index] == guess:
                    display[index] = guess
            
            # Check if guess is in word, if not they lose a life
            if guess not in target_word:
                print(f"You guessed the letter {guess}, that is not in the word. You lose a life.")
                lives -= 1
                
                # If the user reaches zero lives, they lose
                if lives == 0:
                    end_game = True
                    print("You lose!")
                    print(hangman_art.stages[lives])
                    print(f"The target word: {target_word}")
                    print(f"Your progress: {display}")
                    print(f"The letters you guessed: {guesses}")
                    
            
            # If there are no more blanks in display, user wins
            if "_" not in display:
                end_game = True
                print("Yay!! You win!")
        else:
            print(f"You have guessed {guess} already, try again.")
        

# Start game

# for testing
#print(f"Psssst... The target word is {target_word}")

display = set_display(word_length)
start_game()
    
    
