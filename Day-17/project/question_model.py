# Tasks:
#
# Create a model for our question object
#
# Attributes:
## text
## answer

class Question:

    # Constructor
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer


# Test objects
new_q = Question("2+4", "6")
print(new_q.text)
print(new_q.answer)