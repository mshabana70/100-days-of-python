# Day 22 Project - Pong Game
#
# Create the Screen

from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor("black")
screen.title("Mahmoud's Pong Game")
screen.tracer(0)

# Create paddle bar 
paddle = Turtle()
paddle.shape("square")
paddle.pu()
paddle.color("white")
paddle.shapesize(stretch_wid = 5, stretch_len = 1)
paddle.goto(x = 350, y = 0)

# Move paddle
def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)

def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)

screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()