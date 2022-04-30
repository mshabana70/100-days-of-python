# Day 26 Exercise - Dictionary Comprehension 2
#
# ou are going to use Dictionary Comprehension to create a 
# dictionary called result that takes each word in the given 
# sentence and calculates the number of letters in each word.
#
# Try Googling to find out how to convert a sentence into a list of words.
#
# Example Output:
#
# {
# 'What': 4, 
# 'is': 2, 
# 'the': 3, 
# 'Airspeed': 8, 
# 'Velocity': 8, 
# 'of': 2, 
# 'an': 2, 
# 'Unladen': 7, 
# 'Swallow?': 8
# }

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:

# Convert sentence to a list of words
word_list = sentence.split(" ")

result = {word:len(word) for word in word_list}


print(result)

