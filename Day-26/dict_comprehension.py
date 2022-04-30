# Day 26 - Dictionary Comprehension overview

# Dictionary Comprehension
# Keyword method: new_dict = {new_key:new_value for item in list}

# You can also create a new dict from the values of existing dictionary
# new_dict = {new_key:new_value for (key, value) in dict.items()}

# Dictionary Comprehension with Conditional
# new_dict = {new_key:new_value for (key, value) in dict.items() if conditional}

# Examples
import random

names = ["Mahmoud", "Adam", "Summer", "Ahmed", "Abby", "Elsayed"]

# Task: generate a dictionary where the key is a name and the value is a random score
# assigned to each name
students_score = {student:(random.randint(1, 100)) for student in names}
print(students_score)

# Task: Take our new generated dict and create a new dictionary with all students with a passing grade
# (using dictionary comprehension)
passed_students = {student:grade for (student, grade) in students_score.items() if grade > 65}
print(passed_students)