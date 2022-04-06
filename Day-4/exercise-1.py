# Exercise 1 - Heads or tails 
#
# You are going to write a virtual coin toss program. 
# It will randomly tell the user "Heads" or "Tails".
# 
# Important, the first letter should be capitalised 
# and spelt exactly like in the example e.g. Heads, not heads.
# 
# When you run the code, just use a random number as the seed. 
# e.g. 67346 It doesn't matter what you chose, it's only for 
# our testing code to check your work.
# 
# There are many ways of doing this. But to practice what we 
# learnt in the last lesson, you should generate a random number, 
# either 0 or 1. Then use that number to print out Heads or Tails.
# 
# e.g 1 means Heads 0 means Tails
#
# Example Output:
# 
# Heads
# Tails

# First, we much generate some randomness.
# To do that, we need to import the random module
import random

# Lets look at some examples before we solve the challenge
# Generating a randome integer
randomInt = random.randint(100, 200)
print(randomInt)
# returns a random between 100 and 200 (both inclusive)

# Lets solve the exercise here
