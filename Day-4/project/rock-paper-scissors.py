# Day 4 Project - Rock Paper Scissors Game
#
# Write a program where you compete with the computer
# with a game in rock paper scissors!
#

# We will need random integers for this project
import random

randomInteger = random.randint(1, 3)
userChoice = input("What will you draw? 1 for Rock, 2 for Paper, 3 for Scissors: ")

# Assign ascii art to rock, paper or scissors
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Return User decision
if (userChoice == "1"):
    print(rock)
elif (userChoice == "2"):
    print(paper)
elif (userChoice == "3"):
    print(scissors)
else:
    print("Please select one of the given integers.")

# Conditionals

dictionary = {
    1: "rock",
    2: "paper",
    3: "scissors"
}

# Return Computer Decision
if (dictionary[randomInteger] == "rock"):
    print(rock)
elif (dictionary[randomInteger] == "paper"):
    print(paper)
else:
    print(scissors)


# Determine a winner
if (userChoice == str(randomInteger)):
    print("It is a draw!")
elif (userChoice == "1"):
    if (dictionary[randomInteger] == "paper"):
        print(f"The computer has won by selecting {dictionary[randomInteger]}")
    else:
        print("You win! Rock beats scissors!")
elif (userChoice == "2"):
    if (dictionary[randomInteger] == "scissors"):
        print(f"The computer has won by selecting {dictionary[randomInteger]}")
    else:
        print("You win! Paper beats rock!")
elif (userChoice == "3"):
    if (dictionary[randomInteger] == "rock"):
        print(f"The computer has won by selecting {dictionary[randomInteger]}")
    else:
        print("You win! Scissors beats paper!")
else:
    print("something is not working???")
