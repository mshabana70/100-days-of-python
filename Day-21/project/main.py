# Day 21 Project - Snake Game (Part 2)
#
# 

from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Welcome to Snake Game!")
screen.tracer(0) # turn animation off until told otherwise

snake = Snake() # Create snake body

# Snake controls
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:

    # To clean up animation of moving snake
    screen.update()
    time.sleep(0.1)

    snake.move() # move snake
    

    
        
        


    








screen.exitonclick()