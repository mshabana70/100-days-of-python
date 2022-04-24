from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.pu()
        self.goto(x = 0, y = 280)
        self.write(f"Scoreboard: 0", align = "center", font = 20)

        
    
    def add_score(self):
        self.score += 1
        self.clear()
        self.write(f"Scoreboard: {self.score}", align = "center", font = 20)
