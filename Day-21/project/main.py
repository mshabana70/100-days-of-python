# Day 21 Project - Snake Game (Part 2)
#
# 

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Welcome to Snake Game!")
screen.tracer(0) # turn animation off until told otherwise

snake = Snake() # Create snake body
food = Food() # Create a food object 
scoreboard = Scoreboard()

# Snake controls
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:

    # To clean up animation of moving snake
    screen.update()
    time.sleep(0.1)
    snake.move() # move snake

    # Detect collision of snake with food object
    if snake.head.distance(food) < 15:
        food.refresh() # if snake collides with food object, refresh its own location
        snake.grow() # add section to end of snake
        scoreboard.add_score()
    
    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        #game_is_on = False
        #scoreboard.game_over() # Game over title for when game is over
        scoreboard.reset()
        snake.reset()
    
    # Detect collision with tail
    for square in snake.snake_squares[1:]:
        if snake.head.distance(square) < 10:
            #game_is_on = False
            #scoreboard.game_over()
            scoreboard.reset()
            snake.reset()
    # if the head collides with any segment in the tail:
        # trigger end game sequence
    



    

    
        
        


    








screen.exitonclick()