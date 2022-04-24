from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.pu()
        self.goto(x = 0, y = 270)
        self.write(f"Score: 0", align = "center", font = ("Arial", 24, "normal"))

        
    
    def add_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align = "center", font = ("Arial", 24, "normal"))