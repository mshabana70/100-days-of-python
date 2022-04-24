from turtle import Turtle

# Constants
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")
POSITION = (0, 270)
COLOR = "white"

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color(COLOR)
        self.hideturtle()
        self.pu()
        self.goto(POSITION)
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", align = ALIGNMENT, font = FONT)
    
    def add_score(self):
        self.score += 1
        self.clear()
        self.update_score()
    
    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over.", align = ALIGNMENT, font = FONT)
