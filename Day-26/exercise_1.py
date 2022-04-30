# Day 26 Exercise - Squaring Numbers
#
# You are going to write a List Comprehension to create a 
# new list called squared_numbers. This new list should 
# contain every number in the list numbers but each number 
# should be squared.
#
# Example Input:
#
# 4 * 4 = 16
#
# Example Output:
#
# [1, 1, 4, 9, 25, 64, 169, 441, 1156, 3025]

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above 👆

#Write your 1 line code 👇 below:

squared_numbers = [num ** 2 for num in numbers]

#Write your code 👆 above:

print(squared_numbers)