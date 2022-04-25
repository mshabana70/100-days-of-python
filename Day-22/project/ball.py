# Day 22 Project - Pong Game 
#
# Create the ball object file

from turtle import Turtle

# Constants 
SHAPE = "circle"
COLOR = "white"

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape(SHAPE)
        self.color(COLOR)
        self.pu()