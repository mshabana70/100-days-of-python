# Day 9 Project - Silent Auction
#
# Design a program that takes in user input for a name and a bid
# The program will continue with as many bidders as you like.
# Once there are no more bidders to input, the program will return
# the name of the highest bidder.

bidders = {}

# Add bidders to bidder dictionary
def add_bidders(name, price):
    edit_existing = ""
    if name in bidders:
        edit_existing = input("This name already exists in our records, would you like to update your existing bid? (yes or no)")
        if edit_existing.lower() == "yes":
            bidders[name] = price
        else:
            pass
    else:
        bidders[name] = price

# Parse through bidder dictionary, search for highest bidder.
# Every time we come across a maximum, set that as max and insert 
# name and bid price to temp list to return once we parsed through
# the whole dictionary (could use 'sort' to optimize)
def highest_bidder(bidder_dict):
    winner = []
    max_bid = 0
    for name in bidder_dict:
        if bidder_dict[name] > max_bid:
            max_bid = bidder_dict[name]
            winner.insert(0, name)
            winner.insert(1, bidder_dict[name])
    print(f"The highest bidder is {winner[0]} with a bid of ${winner[1]}.")


continue_auction = True

print("Welcome to the secret auction program.")
# While user continues to add bidders, run program
while continue_auction:
    # Ask for user input
    bidder_name = input("What is your name?")
    bid = int(input("What is your bid?"))

    # Call add_bidder to add key/value to bidder dictionary
    add_bidders(name = bidder_name, price = bid)

    # Check if there is more bidders
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.").lower()

    # If no more bidders, set while loop condition to false
    # Call highest_bidder for the highest bidder
    if other_bidders == "no":
        continue_auction = False
        highest_bidder(bidders)



