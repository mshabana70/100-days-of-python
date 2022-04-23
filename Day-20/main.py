# Day 20 - Building the Snake Game (Part 1)
#
# We will be using the turtle module to build the classic
# snake game.

from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Welcome to Snake Game!")
screen.tracer(0) # turn animation off until told otherwise

snake = Snake()

game_is_on = True
while game_is_on:

    # To clean up animation of moving snake
    screen.update()
    time.sleep(0.1)

    snake.move()
    

    
        
        


    








screen.exitonclick()