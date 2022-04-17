# Day 15 Project - Coffee Machine Program
#
# Program a coffee machine with the following requirements:
#
# 1. Makes 3 hot flavors:
## Espresso
## Latte 
## Cappuccino
#
# Recipes for each flavor:
## Espresso: 50ml of Water, 18g of Coffee, zero milk
## Latte: 200ml of Water, 24g of Coffee, 150ml of milk
## Cappuccino: 250ml of Water, 24g of Coffee, 100ml of milk
#
# Price of each flavor:
## Espresso: $1.50
## Latte: $2.50
## Cappucino: $3.00
#
# Resources the coffee machine has:
## 300ml of Water
## 200ml of Milk
## 100g of Coffee
#
# 2. Coin Operated
## Penny: 1 cent
## Nickel: 5 cent
## Dime: 10 cent
## Quarter: 25 cent
#
# 3. Program Requirements:
# A. Print Report: Update on resources
# B. Check if resources are sufficent for what the user orders: Check resources against recipe of drink
# C. Process coins: Ask for quantity of each coin type. if not enough money refund user the money they put
# D. Check if transaction is successful: if enough coins, make coffee 
# C. Make coffee: deduct resources needed to make coffee from coffee machine resources

# Starting code
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def money_total(quarters, dimes, nickels, pennies):
    """Returns the total of all the coins the user inputted."""
    money_total = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
    return float(money_total)

def refill_machine():
    """Function to refill the resources of our coffee machine"""
    resources["coffee"] = 100
    resources["milk"] = 200
    resources["water"] = 300

def machine_report():
    """Returns a report of the current status of the coffee machine."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    if "money" in resources:
        print(f"Money: ${resources['money']}")

def make_coffee(flavor, coin):
    """Returns the remaining resources in the machine and the change to the user.
    If the ammount of coin is insufficent, return refund and make no changes to resources."""
    
    # Check if user coin ammount is sufficent
    cost = MENU[flavor]["cost"]
    if coin < cost:
        return f"Insuffient ammount of coins, please enter total cost. Money refunded: {coin}"
    else:
        # If amount of coins is sufficient, deduct amount of resources from machine to make flavor (resources - recipe):

        # Get all the values from our flavor object
        change = coin - cost
        water_needed = MENU[flavor]["ingredients"]["water"]
        coffee_needed = MENU[flavor]["ingredients"]["coffee"]
        if water_needed > resources["water"] or coffee_needed > resources["coffee"]:
            return "Issufficient resources. Type 'report' to see what resources are missing."
        else:
            resources["water"] -= water_needed
            resources["coffee"] -= coffee_needed
            if "milk" in MENU[flavor]["ingredients"]:
                milk_needed = MENU[flavor]["ingredients"]["milk"]
                if milk_needed > resources["milk"]:
                    return "Issufficient resources. Type 'report' to see what resources are missing."
                else:
                    resources["milk"] -= milk_needed
            
            # Return amount of money left over to user, update money in coffee machine (add amount of flavor to money property of machine)
            if "money" in resources:
                resources["money"] += cost
            else:
                resources["money"] = cost

            return f"Here is you change: ${str(round(change, 2))}"


# Loop program while input does not equal end
while user_flavor != "quit":
    # Ask User for what flavor of coffee they would like to drink
    user_flavor = input("What would you like? (espresso/latte/cappuccino)").lower()

    # If user inputs 'report', return current status of machine resources
    if user_flavor == 'report':
        machine_report()
    elif user_flavor == 'refill':
        refill_machine() 
    else:
        # Once flavor is picked, ask user for amount of coins they would like to pay with
        print("Please insert coins.")
        user_quarters = int(input("How many quarters?: "))
        user_dimes = int(input("How many dimes?: "))
        user_nickels = int(input("How many nickels?: "))
        user_pennies = int(input("How many pennies?: "))
        coin_ammount = money_total(user_quarters, user_dimes, user_nickels, user_pennies)


    if user_flavor in MENU:
        print(make_coffee(user_flavor, coin_ammount))
    else:
        print("Invalid flavor or command, try again.")
