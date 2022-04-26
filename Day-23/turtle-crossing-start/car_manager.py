from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    
    def __init__(self):
        super().__init__()
        self.move_speed = STARTING_MOVE_DISTANCE
        self.y_cor = random.randint(-280, 280)
        self.shape("square")
        self.pu()
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid = 1, stretch_len = random.randint(1, 4))
        self.goto(x = 300, y = self.y_cor)
        
    
    def move(self):
        new_x = self.xcor() - self.move_speed
        self.goto(x = new_x, y = self.y_cor)
    
    def increase_speed(self):
        self.move_speed += 10

    



