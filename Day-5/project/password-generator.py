# Day 5 Project: Create a Password Generator
#
# Write a program to takes in user input for the length of password,
# number of symbols in the password and number of numbers in the password.
#

# Values in lists
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
"n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C",
"D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
"T", "U", "V", "W", "X", "Y", "Z" ]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password? \n"))
nr_symbols = int(input("How many symbols would you like in your password? \n"))
nr_numbers = int(input("How many numbers would you like in your password? \n"))

# Easy version
# fghf^&23
final_password = ""
for i in letters:




