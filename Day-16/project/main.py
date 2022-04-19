# Day 16 Project - Coffee Machine using OOP (main code is already coded from yesterday)
#
# Build a program that uses external modules to recreate the coffee machine
# program from Day 15.

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Create objects
coffee_machine = CoffeeMaker()
coffee_menu = Menu()
money_processing = MoneyMachine()

# Prompt user for what they would like to drink
user_choice = input("What would you like? (espresso/latte/cappucino)").lower()

if user_choice == "off":
    is_continue = False
    print("Thank you for using our Coffee Machine! See you later!")
elif user_choice == "report":
    coffee_machine.report() # return report of current status
else:
    print("testing")

