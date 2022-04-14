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
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# 11 will count as 11 until we exceed a hand total of 21.

def random_card(card_list):
    card = random.choice(card_list)
    return card

def hand_total(hand_list):
    return sum(hand_list)


def blackjack():
    user_hand = []
    computer_hand = []
    # START
    # User and computer get two random cards

    # user
    user_hand.append(random_card(cards))
    user_hand.append(random_card(cards))

    # computer
    computer_hand.append(random_card(cards))
    computer_hand.append(random_card(cards))

    current_user_score = 0
    current_computer_score = 0

    print(user_hand)
    print(computer_hand)
    draw_card = ""
    while draw_card != "n":

        print(f"User's current hand: {user_hand}")
        # Add up the scores of the user hand and the computer hand
        current_user_score = hand_total(user_hand)
        current_computer_score = hand_total(computer_hand)

        # Does either hand have an ace?
        if 11 in user_hand and 10 in user_hand and current_user_score == 21:
            print("Blackjack! User wins!")
        elif 11 in computer_hand and 10 in computer_hand and current_computer_score == 21:
            print("Blackjack! computer wins!")

        if current_user_score > 21:
            if 11 in user_hand:
                current_user_score -= 10
                if current_user_score > 21:
                    print("You went over 21, you lose!")
                    break
            else:
                print("You went over 21, you lose!")
                break
        else:
            draw_card = input("Would you like to draw another card? Type 'y' for yes, 'n' for no:").lower()
            if draw_card == "y":
                user_hand.append(random_card(cards))
                if current_computer_score < 17:
                    computer_hand.append(random_card(cards))
                continue
            else:
                current_computer_score = hand_total(computer_hand)
                current_user_score = hand_total(user_hand)
                if current_user_score == current_computer_score:
                    print("There is a draw")
                elif current_user_score > current_computer_score:
                    print(f"User has won with a hand of {user_hand} and total of {current_user_score}!")
                else:
                    print(f"Computer has won with a hand of {computer_hand} and total of {current_computer_score}!")
                           

blackjack()