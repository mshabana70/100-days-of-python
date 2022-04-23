# Day 20 - Building the Snake Game (Part 1)
#
# We will be using the turtle module to build the classic
# snake game.

from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Welcome to Snake Game!")

snake_squares = []

for i in range(0, 3):
    square = Turtle(shape = "square")
    square.pu()
    square.color("white")
    snake_squares.append(square)

# Starting Position for squares 
snake_squares[1].goto(x = -20, y = 0)
snake_squares[2].goto(x = -40, y = 0)






screen.exitonclick()