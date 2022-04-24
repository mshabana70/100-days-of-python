# Day 21 Project - Snake Game (Part 2)
#
# Create a class for the food drops that our snake will eat
from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.pu()
        self.shapesize(stretch_len = 0.5, stretch_wid = 0.5)
        self.color("blue")
        self.speed("fastest")
        
        # Random location for food drop
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(x = random_x, y = random_y)