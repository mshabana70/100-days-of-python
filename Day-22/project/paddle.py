# Day 22 Project - Pong Game
#
# Create paddle object class
from turtle import Turtle

# Constants
SHAPE = "square"
COLOR = "white"

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.paddle = Turtle(shape = SHAPE)
        self.paddle.pu()
        self.paddle.color(COLOR)
        self.paddle.shapesize(stretch_wid = 5, stretch_len = 1)
        self.paddle.goto(position) 
    
    # Move paddle
    def go_up(self):
        new_y = self.paddle.ycor() + 20
        self.paddle.goto(self.paddle.xcor(), new_y)

    def go_down(self):
        new_y = self.paddle.ycor() - 20
        self.paddle.goto(self.paddle.xcor(), new_y)