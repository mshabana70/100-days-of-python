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
        with open("/Users/mahmoudshabana/Documents/Udemy/100-days-of-python/Day-21/project/data.txt") as data:
            self.highscore = int(data.read())
        self.color(COLOR)
        self.hideturtle()
        self.pu()
        self.goto(POSITION)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.highscore}", align = ALIGNMENT, font = FONT)
    
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("/Users/mahmoudshabana/Documents/Udemy/100-days-of-python/Day-21/project/data.txt", mode = 'w') as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update_score()
    
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", align = ALIGNMENT, font = FONT)
    
    def add_score(self):
        self.score += 1
        self.update_score()
    
    
