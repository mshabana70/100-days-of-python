# Exercise 2 - Prime Numbers
#
# Prime numbers are numbers that can only be cleanly divided 
# by themselves and 1.
# 
# https://en.wikipedia.org/wiki/Prime_number
# 
# You need to write a function that checks whether if the 
# number passed into it is a prime number or not.
# 
# e.g. 2 is a prime number because it's only divisible by 
# 1 and 2.
# 
# But 4 is not a prime number because you can divide it by 
# 1, 2 or 4.
#
# Example Input:
#
# 73
#
# Example Output:
#
# It is a prime number.

# How to calculate if a number is prime?

def is_prime(num):
    isPrime = True
    for i in range(2, 9):
        if num % i == 0 and num != i or num == 1:
            isPrime = False
    if not isPrime:
        print("It's not a prime number.")
    else:
        print("It's a prime number.")

for i in range(101):
    print(f"The number {i}: ")
    is_prime(i)


