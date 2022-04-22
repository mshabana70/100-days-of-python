# Day 19 - High Order Function, Event Listeners
# 
# Using turtle event listeners

from turtle import Turtle, Screen

leo = Turtle()
screen = Screen()

# Function for our turtle
def move_forward():
    leo.forward(10)


screen.listen()
# Here we place an event listener
screen.onkey(key="space", fun=move_forward) # listen for space key, when pressed, run move_forward function
# NOTE: when we pass a function as a parameter, we dont need its parenthesis
screen.exitonclick()

# Higher Order Function
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def calculator(n1, n2, func):
    return func(n1, n2)

# In this scenario, calculator is the high order function.
# This is because calculator() is taking a function as an input,
# and working with it in the body of the function.
result = calculator(2, 3, add)
print(result)
