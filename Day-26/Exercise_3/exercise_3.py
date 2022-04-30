# Day 26 Exercise - Dictionary Comprehension
#
# Take a look inside file1.txt and file2.txt. They each contain a 
# bunch of numbers, each number on a new line.
#
# You are going to create a list called result which contains the 
# numbers that are common in both files.
#
# e.g if file1.txt contained:
#
# 1
# 2
# 3
#
# and file2.txt contained:
#
# 2
# 3
# 4
# 
# result = [2, 3]
#
#
# Example Output:
#
# [3, 6, 5, 33, 12, 7, 42, 13]

# Read file1 and put to a list
file_1 = open("/Users/mahmoudshabana/Documents/Udemy/100-days-of-python/Day-26/Exercise_3/file1.txt")
file_1_list = [int(num.strip()) for num in file_1.readlines()]

# Same for file2
file_2 = open("/Users/mahmoudshabana/Documents/Udemy/100-days-of-python/Day-26/Exercise_3/file2.txt")
file_2_list = [int(num.strip()) for num in file_2.readlines()]

result = [num for num in file_1_list if num in file_2_list]

print(result)
