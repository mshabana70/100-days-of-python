# Day 21 Project - Snake Game (Part 2)

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
        for position in STARTING_POSITION:
            self.add_section(position)

            
    def add_section(self, position):
        # Make the visual for the square
        self.square = Turtle(shape = "square")
        self.square.pu()
        self.square.color("white")

        # Starting Position for squares 
        #square.goto(x = starting_position[i][0], y = starting_position[i][1])
        self.square.goto(position)

        # Add square to list of squares
        self.snake_squares.append(self.square)
    
    def grow(self):
        self.add_section(self.snake_squares[-1].position())

    def move(self):
        for sq_num in range(len(self.snake_squares) - 1, 0, -1):
            new_x = self.snake_squares[sq_num - 1].xcor()
            new_y = self.snake_squares[sq_num - 1].ycor()
            self.snake_squares[sq_num].goto(x = new_x, y = new_y)
        
        self.head.forward(MOVE_DISTANCE)
    
    def reset(self):
        for square in self.snake_squares:
            square.goto(1000, 1000) # put dead snakes offscreen
        self.snake_squares.clear()
        self.create_snake()
        self.head = self.snake_squares[0]

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
