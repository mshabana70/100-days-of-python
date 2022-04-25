# Day 22 Project - Pong Game 
#
# Create the ball object file

from turtle import Turtle
import random

# Constants 
SHAPE = "circle"
COLOR = "white"

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape(SHAPE)
        self.color(COLOR)
        self.pu()
    
    def move(self):
        new_y = self.ycor() + 10
        new_x = self.xcor() + 10
        self.goto(x = new_x, y = new_y)