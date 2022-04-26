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
car_manager = CarManager()

# Move the player
screen.listen()
screen.onkey(player_1.move_forward,"Up")

generate_car_counter = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if generate_car_counter % 100:
        car_manager.create_car()
    car_manager.move()
    
    # Detect Collision with car object
    for car in car_manager.all_cars:
        if player_1.distance(car) < 25:
            scoreboard.game_over()
        
    if player_1.reached_finish():
        player_1.reset()
        car_manager.increase_speed()
        scoreboard.increase_level()
        print("Passed Level!!")
    
    generate_car_counter += 1
