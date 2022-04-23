# Day 20 - Building the Snake Game (Part 1)
#
# We will be using the turtle module to build the classic
# snake game.

from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Welcome to Snake Game!")
screen.tracer(0) # turn animation off until told otherwise

snake_squares = []
starting_position = [(0, 0), (-20, 0), (-40, 0)]
for i in range(0, 3):

    # Make the visual for the square
    square = Turtle(shape = "square")
    square.pu()
    square.color("white")

    # Starting Position for squares 
    #square.goto(x = starting_position[i][0], y = starting_position[i][1])
    square.goto(starting_position[i])

    # Add square to list of squares
    snake_squares.append(square)

game_is_on = True
while game_is_on:
    for square in snake_squares:
        square.forward(20)
        screen.update()
        time.sleep(1)

        # To clean up animation of moving snake


    








screen.exitonclick()