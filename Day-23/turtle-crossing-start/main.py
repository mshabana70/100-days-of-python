import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Create the player object
player_1 = Player()

# Move the player
screen.listen()
screen.onkey(player_1.move_forward,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if player_1.reached_finish():
        game_is_on = False
        print("Passed Level!!")
