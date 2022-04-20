# Tasks:
#
# Asking the question
#
# Checking if the answer was correct
#
# Checking if we're at the end of the quiz


class QuizBrain:

    # Constructor
    def __init__(self, questions):
        self.question_number = 0
        self.questions_list = questions
        self.score = 0
    
    # Methods
    def next_question(self):
        """Method to get next question in list of questions. Also prompts user to answer the question."""
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text}. (True/False)?")
        self.check_answer(user_answer, current_question.answer) # users answer and the correct answer are passed to check_answer()
    
    def still_has_questions(self):
        """Method to check if there are questions left in list of questions."""
        return self.question_number < len(self.questions_list)

    def check_answer(self, u_answer, c_answer):
        """Method to check the answer of user. If correct increment score. Print correct answer and current score."""
        if u_answer.lower() == c_answer.lower():
            self.score += 1
            print("You got the answer right!")
        else:
            print("That was incorrect.")
        print(f"The correct answer was {c_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}.\n")