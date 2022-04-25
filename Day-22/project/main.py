# Day 22 Project - Pong Game
#
# Create the Screen

from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor("black")
screen.title("Mahmoud's Pong Game")
screen.tracer(0)

# Create paddle bar 
r_paddle = Paddle(position = (350, 0))
l_paddle = Paddle(position = (-350, 0))

# Create Ball
ball = Ball()

# Move Paddle bar
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

screen.exitonclick()