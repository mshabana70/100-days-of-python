from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler App")

        # Create padding and bg color of window
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Create score label
        self.score = 0
        self.score_label = Label(text=f"Score: {self.score}", fg="white", bg=THEME_COLOR, font= ("Arial", 16, "normal"), highlightthickness=0)
        self.score_label.grid(row=0, column=1, pady=20)

        # Create canvas
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150, 
            125, 
            text="SAMPLE QUESTION TEXT GOES HERE", 
            width=270, 
            font=FONT, 
            fill=THEME_COLOR
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        # Create Buttons
        true_img = PhotoImage(file="/Users/mahmoudshabana/Documents/Udemy/100-days-of-python/Day-34/quizzler-app-start/images/true.png")
        false_img = PhotoImage(file="/Users/mahmoudshabana/Documents/Udemy/100-days-of-python/Day-34/quizzler-app-start/images/false.png")

        self.true_button = Button(image=true_img, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0, pady=20)

        self.false_button = Button(image=false_img, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1, pady=20)

        # Display next_question
        self.get_next_question()

        self.window.mainloop()
    
    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)
    
    def true_pressed(self):
        self.quiz.check_answer("True")

    def false_pressed(self):
        self.quiz.check_answer("False")
