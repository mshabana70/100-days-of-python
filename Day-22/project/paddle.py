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
        self.shape(SHAPE)
        self.pu()
        self.color(COLOR)
        self.shapesize(stretch_wid = 5, stretch_len = 1)
        self.goto(position) 
    
    # Move paddle
    def go_up(self):
        if self.ycor() < 240:
            new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        if self.ycor() > -240:
            new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)