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


