# Day 22 Project - Pong Game
#
# Create the Screen

from turtle import Screen
from paddle import Paddle
import time

screen = Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor("black")
screen.title("Mahmoud's Pong Game")
screen.tracer(0)

# Create paddle bar 
paddle = Paddle()



screen.listen()
screen.onkey(paddle.go_up, "Up")
screen.onkey(paddle.go_down, "Down")

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()