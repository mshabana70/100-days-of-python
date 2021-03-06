# Day 19 Project - Turtle Race
#
# https://docs.python.org/3/library/turtle.html#turtle
#
# Create a turtle race game where you can bet on the winner
# prior to the race

from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make a bet", prompt="Which do you think will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-100, -60, -20, 20, 60, 100]
turtle_list = []
# racers = {}
# for color in colors:
#     racers[color] = Turtle(shape="turtle")
#     racers[color].color(color)
#     racers[color].pu()

# # Position turtle racers
# racers["red"].goto(x=-230, y=-100)
# racers["orange"].goto(x=-230, y=-60)
# racers["yellow"].goto(x=-230, y=-20)
# racers["green"].goto(x=-230, y=20)
# racers["blue"].goto(x=-230, y=60)
# racers["purple"].goto(x=-230, y=100)

# More efficient way of creating the turtle objects
for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.pu()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-230, y=y_positions[i]) # Set start position of turtle
    turtle_list.append(new_turtle)

is_race_on = False
if user_bet:
    is_race_on = True
while is_race_on:

    for turtle in turtle_list:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"Congratulations, you won the bet! The {winning_color} turtle won the race!")
            else:
                print(f"You lose! The {winning_color} turtle won the race and you bet the {user_bet} turtle to win.")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance) # move turtle forward by random distance

screen.exitonclick()