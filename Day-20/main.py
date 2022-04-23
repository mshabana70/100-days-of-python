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

    # To clean up animation of moving snake
    screen.update()
    time.sleep(0.1)

    for sq_num in range(len(snake_squares) - 1, 0, -1):
        new_x = snake_squares[sq_num - 1].xcor()
        new_y = snake_squares[sq_num - 1].ycor()
        snake_squares[sq_num].goto(x = new_x, y = new_y)
    
    snake_squares[0].forward(20)
    snake_squares[0].left(90)

    
        
        


    








screen.exitonclick()