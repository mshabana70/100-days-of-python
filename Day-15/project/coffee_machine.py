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
