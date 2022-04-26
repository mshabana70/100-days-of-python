
from turtle import Turtle

STARTING_POSITION = (0, -280)
STARTING_DIRECTION = 90
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.pu()
        self.color("black")
        self.setheading(STARTING_DIRECTION)
        self.goto(STARTING_POSITION)
    
    def move_forward(self):
        self.forward(MOVE_DISTANCE)
    
    def reached_finish(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True
        return False 
        
