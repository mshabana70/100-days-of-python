from tkinter import *

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")

class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler App")

        # Create padding and bg color of window
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Create score label
        self.score = 0
        self.score_label = Label(text=f"Score: {self.score}", fg="white", bg=THEME_COLOR, highlightthickness=0)
        self.score_label.grid(row=0, column=1)

        # Create canvas
        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 175, text="SAMPLE QUESTION TEXT GOES HERE", width=270, font=FONT, fill=THEME_COLOR)





        self.window.mainloop()