# Day 13 Notes - Debugging
#
# Describe the problem: 
# my_function is running a iterative for loop that goes through
# the range 1 (inclusive) and 20 (exclusive).
# The for loop has a condition that is check at each iteration. If 
# the value of i is equal to 20, then print "you got it". 
# The current issue is that nothing is being return by the function.
#
# This issue is because in the range() func, the upper bound is exclusive.
# This means the for loop will never reach 20 so the condition will therefore,
# never be true.

# def my_function():
#     #for i in range(1, 20): # 1 - 19
#     for i in range(1, 21): # bug fix
#         if i == 20:
#             print("You got it")
# my_function()

# Reproduce the Bug
# 
# This program is selecting an integer between 1-6 (inclusive) to 
# pick random faces of a dice from a list of dice images.
# The issue could be that the randint() function is picking from 
# a range of 1-6 inclusive, but the last index of the dice_imgs 
# list is 5. This will potentially lead to an "index out of range"
# error.

# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# #dice_num = randint(1, 6) # 1 - 6 (both inclusive)
# dice_num = randint(0, 5) # 0 - 5 (both inclusive)
# print(dice_imgs[dice_num])

# # Play Computer
#
# run through test cases and see how the computer will 
# execute such tests. For example: 1994 input returns nothing.
# This is because the computer if testing two expressions, when the
# year is between 1980 and 1994 exlusive, and when the year is 
# greater than 1994.
# This means there is no condition for when the year == 1994, there is 
# our bug.
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# #elif year > 1994:
# elif year >= 1994:
#   print("You are a Gen Z.")

# # Fix the Errors
#
# The program is return an indentation error and a TypeError. TypeError
# is due to us comparing age to integer when age is still a string.

# age = input("How old are you?")
age = int(input("How old are you?"))
if age > 18:
# print("You can drive at age {age}.")
    print(f"You can drive at age {age}.")

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])