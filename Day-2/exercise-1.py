# Data Types Exercise

# Write a program that adds the digits in a 2 digit number.
# e.g. if the input was 35, then the output should be 3 + 5 = 8
#
# Example input:
# 39
#
# Example Output:
# 3 + 9 = 12
# 12

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
stringNum = str(two_digit_number)

if (len(stringNum) > 1):
    firstDigit = int(stringNum[0])
    secondDigit = int(stringNum[1])
    sumVal = firstDigit + secondDigit
    print(firstDigit, "+", secondDigit,    "=", (sumVal))
    print(sumVal)
else: 
    print(two_digit_number)