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

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    # Detect collision with right_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or :
        ball.bounce_x()

    # Detect collision with left_paddle
    if ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    # Detect if ball hits wall behind paddles
    if ball.xcor() > 380 or ball.xcor() < -380:
        game_is_on = False
        print("GAME OVER")

screen.exitonclick()