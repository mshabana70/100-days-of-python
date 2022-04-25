# Day 22 Project - Pong Game 
#
# Score board class file

from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.pu()
        self.hideturtle()
        self.goto(-100, 200)
        self.write(self.l_score, align = "center", font = ("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align = "center", font = ("Courier", 80, "normal"))
