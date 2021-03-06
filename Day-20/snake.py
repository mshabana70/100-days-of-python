# Day 20 Project - Snake Game
#
# Class to create the snake
from turtle import Turtle

# Constants
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.snake_squares = []
        self.create_snake()
        self.head = self.snake_squares[0]
    
    def create_snake(self):
        for i in range(0, 3):

            # Make the visual for the square
            self.square = Turtle(shape = "square")
            self.square.pu()
            self.square.color("white")

            # Starting Position for squares 
            #square.goto(x = starting_position[i][0], y = starting_position[i][1])
            self.square.goto(STARTING_POSITION[i])

            # Add square to list of squares
            self.snake_squares.append(self.square)

    def move(self):
        for sq_num in range(len(self.snake_squares) - 1, 0, -1):
            new_x = self.snake_squares[sq_num - 1].xcor()
            new_y = self.snake_squares[sq_num - 1].ycor()
            self.snake_squares[sq_num].goto(x = new_x, y = new_y)
        
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
