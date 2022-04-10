# Day 8 - Exercise 1 - Paint Area Calculator
#
# You are painting a wall. The instructions on the paint can says 
# that 1 can of paint can cover 5 square meters of wall. Given a 
# random height and width of wall, calculate how many cans of paint 
# you'll need to buy.
# 
# number of cans = (wall height ✖️ wall width) ÷ coverage per can.
# 
# e.g. Height = 2, Width = 4, Coverage = 5
# 
# number of cans = (2 ✖️ 4) ÷ 5 = 1.6
# 
# But because you can't buy 0.6 of a can of paint, the result should 
# be rounded up to 2 cans.
# 
# IMPORTANT: Notice the name of the function and parameters must match 
# those on line 13 for the code to work.
# 
# Example Input:
# 
# test_h = 3
# test_w = 9
#
# Example Output:
#
# You'll need 6 cans of paint.

import math

# 1 can can cover 5 sq meters

def num_of_cans(height, width, cover):
    area = height * width
    num_of_cans_needed = area / cover

    return int(math.ceil(num_of_cans_needed))

height_in = float(input("Enter the height of the wall in meters: "))
width_in = float(input("Enter the width of the wall in meters: "))

print(f"You'll need {num_of_cans(height_in, width_in, 5)} cans to paint.")



