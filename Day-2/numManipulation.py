# Number Manipulation and F String

# If you want to round a num to the nearest whole integer
expression = 8 / 3 # 2.666666665
print(round(expression))

# To round to a specific precision
print(round(expression, 2)) # rounds to 2 decimal places

# Floor Division
expressionFloor = 8 // 3 # returns an integer, rounds down
print(expressionFloor, type(expressionFloor))

# F Strings
#
# Allows for multiple different data types to be returned 
# in a string more easily
score = 87
print(f'Your score is {score}')
score2 = 93
print(f'Your score before studyin was {score}, after studying it was {score2}')

