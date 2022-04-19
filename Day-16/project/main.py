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

is_continue = True
while is_continue:
    # Prompt user for what they would like to drink
    user_choice = input(f"What would you like? ({coffee_menu.get_items()})").lower()

    if user_choice == "off":
        is_continue = False
        print("Thank you for using our Coffee Machine! See you later!")
    elif user_choice == "report":
        coffee_machine.report() # return report of current status of coffee machine
        money_processing.report() # returns report of current status of profits
    elif coffee_menu.find_drink(user_choice) != None:
        # Check if resources are sufficient
        order_ingredients = coffee_menu.find_drink(user_choice)
        if coffee_machine.is_resource_sufficient(order_ingredients):
            # Find the cost of the order
            cost_of_order = coffee_menu.find_drink(user_choice).cost

            # Process the coins for the order
            #money_processing.process_coins() # No need to call this, this is called in make_payment
            # Check if transaction was successful
            if money_processing.make_payment(cost_of_order):
                # Make coffee
                coffee_machine.make_coffee(order_ingredients)


