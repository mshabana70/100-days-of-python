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
        self.x_move = 10
        self.y_move = 10
    
    def move(self):
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(x = new_x, y = new_y)
    
    def bounce(self):
        self.y_move *= -1
