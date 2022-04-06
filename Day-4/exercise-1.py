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

# Generate random floating point
randomFloat = random.random()
print(randomFloat)
# returns random float 0.0 to 1.0

# Generate random float between 0 - 5
randomFloat *= 5 # [0.0 - 1.0] * 5 = [0.0 - 5.0]
print(randomFloat) 

# Lets solve the exercise here
#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
import random
	 
#Write the rest of your code below this line 👇
flipResult = random.randint(0, 1)

if (flipResult):
    print("Tails")
else:
    print("Heads")