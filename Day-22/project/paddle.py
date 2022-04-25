# Day 22 Project - Pong Game
#
# Create paddle object class
from turtle import Turtle

class Paddle(Turtle):

    def __init__(self):
        self.paddle = Turtle(shape = "square")
        self.paddle.pu()
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid = 5, stretch_len = 1)
        self.paddle.goto(x = 350, y = 0) 
    
    # Move paddle
    def go_up(self):
        new_y = self.paddle.ycor() + 20
        self.paddle.goto(self.paddle.xcor(), new_y)

    def go_down(self):
        new_y = self.paddle.ycor() - 20
        self.paddle.goto(self.paddle.xcor(), new_y)