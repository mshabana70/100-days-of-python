# Day 19 Project - Turtle Race
#
# Create a turtle race game where you can bet on the winner
# prior to the race

from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make a bet", prompt="Which do you think will win the race? Enter a color: ")
print(user_bet)


leo = Turtle(shape="turtle")
leo.pu()
leo.goto(x=-230, y=-100) # Set start position of turtle

screen.exitonclick()