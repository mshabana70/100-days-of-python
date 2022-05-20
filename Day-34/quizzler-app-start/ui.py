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
        self.score_label.grid(row=0, column=1, pady=20)

        # Create canvas
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, text="SAMPLE QUESTION TEXT GOES HERE", width=270, font=FONT, fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        # Create Buttons
        self.true_img = PhotoImage(file="/Users/mahmoudshabana/Documents/Udemy/100-days-of-python/Day-34/quizzler-app-start/images/true.png")
        self.false_img = PhotoImage(file="/Users/mahmoudshabana/Documents/Udemy/100-days-of-python/Day-34/quizzler-app-start/images/false.png")

        self.true_button = Button(image=self.true_img, highlightthickness=0)
        self.true_button.grid(row=2, column=0, pady=20)

        self.false_button = Button(image=self.false_img, highlightthickness=0)
        self.false_button.grid(row=2, column=1, pady=20)


        self.window.mainloop()