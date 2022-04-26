from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.current_level = 1
        self.hideturtle()
        self.pu()
        self.color("black")
        self.update_scoreboard()
        
    
    def update_scoreboard(self):
        self.goto(x = -230, y = 260)
        self.write(f"Level: {self.current_level}", align = "center", font = FONT)
    
    def increase_level(self):
        self.current_level += 1
        self.clear()
        self.update_scoreboard()
    
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align = "center", font = FONT)

