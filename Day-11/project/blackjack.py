# Day 11 Project - Blackjack Game (Capstone)
#
# Create a black jack game in python, where you play against
# the dealer. You are given two cards at random, with the value of 
# of cards being what the number is (for number cards) and for face 
# cards it is a value of 10. The ace can count as 1 or 11.
#
# You place a bet, dealer deals the cards. You can call on your hand
# if you want or just fold and end the game. If you call and exceed 21, 
# you lose, if you are closer to 21 than the dealer, you win!
#
# Note: if dealer has less than 17, they must draw another card.

# Import random
import random

# Card values

# 11 will count as 11 until we exceed a hand total of 21.

def random_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def hand_total(hand_list):
    # Check for blackjack
    if sum(hand_list) == 21 and len(hand_list) == 2:
        return 0

    # check for aces, if greater than 21, set ace to 1 (remove 11)
    if 11 in hand_list and sum(hand_list) > 21:
        hand_list.remove(11)
        hand_list.append(1)
    return sum(hand_list)


def blackjack():
    user_hand = []
    computer_hand = []
    # START
    # User and computer get two random cards

    for _ in range(2):
        user_hand.append(random_card())
        computer_hand.append(random_card())

    current_user_score = 0
    current_computer_score = 0

    print(f"Computers hand: {computer_hand}")
    continue_game = True
    while continue_game:
        # Add up the scores of the user hand and the computer hand
        current_user_score = hand_total(user_hand)
        current_computer_score = hand_total(computer_hand)

        print(f"Your hand: {user_hand}")
        #check for blackjack
        if current_user_score == 0:
            print("Blackjack! user wins!")
            break

        if current_computer_score < 17:
            computer_hand.append(random_card())

        if current_user_score > 21:
            print("You went over 21, you lose!")
            if current_computer_score <= 21:
                print(f"Computer wins with {computer_hand} and a total of {current_computer_score}")
            continue_game = False
        else:
            draw_card = input("Would you like to draw another card? Type 'y' for yes, 'n' for no:").lower()
            if draw_card == "y":
                user_hand.append(random_card())
            elif draw_card == "n":
                if current_computer_score == current_user_score:
                    print(f"It is a draw! User: {user_hand}, Computer: {computer_hand}")
                elif current_computer_score > current_user_score and current_computer_score <= 21:
                    print(f"Computer wins with a total of {current_computer_score} and a hand of {computer_hand}.")
                else:
                    print(f"User wins with a total of {current_user_score} and a hand of {user_hand}.")
                    print(computer_hand)
                continue_game = False
                       

blackjack()