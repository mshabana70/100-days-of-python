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
word_length = len(target_word)

print(f"Psssst... The target word is {target_word}") # For testing

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
display = []
for _ in range(word_length):
    display.append("_")

end_game = False

while not end_game:
    # ask for a letter
    guess = input("Please guess a letter: ").lower()
    for index in range(word_length):
        if target_word[index] == guess:
            display[index] = guess
    print(display)

    if "_" not in display:
        end_game = True
        print("YAY! You win!")
