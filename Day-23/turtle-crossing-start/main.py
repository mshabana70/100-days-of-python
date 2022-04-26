import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Create the player object
player_1 = Player()
scoreboard = Scoreboard()
cars = []

# Move the player
screen.listen()
screen.onkey(player_1.move_forward,"Up")

generate_car_counter = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    
    # Detect Collision with car object
    if player_1.distance(car) < 25:
        game_is_on = False
        scoreboard.game_over()
        
    if player_1.reached_finish():
        player_1.reset()
        car.increase_speed()
        scoreboard.increase_level()
        print("Passed Level!!")
    
    generate_car_counter += 1
