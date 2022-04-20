# Tasks:

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Question bank is a list of question objects
question_bank = []

for question in question_data:
    # question text = question["text"]
    # question answer = question["answer"]
    # question object = Question(question["text"], question["answer"])
    question_bank.append(Question(question["text"], question["answer"]))

# test question bank
# print(question_bank[0].text)

quiz = QuizBrain(question_bank)

# Check if quiz game still has questions left
# keep asking the next question if there are 
# questions left
while quiz.still_has_questions():
    quiz.next_question() # call for next question and prompt for user input

