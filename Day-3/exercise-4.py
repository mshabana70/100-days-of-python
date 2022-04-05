# Exercise 4 - Pizza Order Practice
# 
# Based on a user's order, work out their final bill.
# 
# Small Pizza: $15
# 
# Medium Pizza: $20
# 
# Large Pizza: $25
# 
# Pepperoni for Small Pizza: +$2
# 
# Pepperoni for Medium or Large Pizza: +$3
# 
# Extra cheese for any size pizza: + $1
# 
# Example Input:
# 
# size = "L"
# add_pepperoni = "Y"
# extra_cheese = "N"
# 
# Example Output:
# 
# Your final bill is: $28

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
total_price = 0

# Check pizza size and if they want pepperoni
if (size == "L"):
    # Add value for large pizza
    total_price += 25
    # Did they ask for pepperoni?
    if (add_pepperoni == "Y"):
        total_price += 3
elif (size == "M"):
    # Add value for medium pizza
    total_price += 20
    # Did they ask for pepperoni?
    if (add_pepperoni == "Y"):
        total_price += 3
else:
    # Add value for small pizza
    total_price += 15
    # Did they ask for pepperoni?
    if (add_pepperoni == "Y"):
        total_price += 2

# Add value of extra cheese (no need to check for size)
if (extra_cheese == "Y"):
    total_price += 1

# Return Total price of pizza order
print(f"Your final bill is: ${total_price}")

