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
import random

word_list = ["ardvark", "baboon", "camel"]

# Choose a random word for target_word
#randomInt = random.randint(0, len(word_list))
#target_word = word_list[randomInt]
target_word = random.choice(word_list)

# Ask for User input on a guess letter and assign it to guess
guess = input("Please guess a letter: ").lower()

# Check if guessed letter is in target_word (check each letter)
for letter in target_word:
    if guess == letter:
        print("Right")
    else:
        print("Wrong")







