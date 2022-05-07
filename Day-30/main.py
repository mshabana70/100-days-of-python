# Day 30 - Exceptions and Error Handling
#
# Error Handling keywords
#
# try: Execute block of code that might cause an exception
# except: Execute block of code if there was an exception thrown
# else: Execute block of code if there was NO exception thrown
# finally: Execute block of code no matter what happens

# FileNotFound
# with open("a_file.txt") as file:
#     file.read()

#KeyError
# a_dictionary = {"Key": "Value"}
# value = a_dictionary["non_existent_key"]

#IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3] # out of range of list

#TypeError
# text = "abc"
# print(text + 5) # different types

# Lets try to make safe code for a FileNotFound Exception

try: 
    file = open("a_text_file.txt") # Should fail (file does not exist)
    a_dictionary = {"key":"value"}
    print(a_dictionary["ssnkdkn"]) # This will throw a TypeError
except FileNotFoundError():
    # Only run this block if it is a FileNotFoundError
    file = open("Day-30/a_text_file.txt", "w") # If file does not exist, create the file
    file.write("Something")
