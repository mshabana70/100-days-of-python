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
    
    # Methods
    def next_question(self):
        """Method to get next question in list of questions. Also prompts user to answer the question."""
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text}. (True/False)?")
    
    def still_has_questions(self):
        """Method to check if there are questions left in list of questions."""
        if self.question_number < len(self.questions_list):
            return True
        return False
