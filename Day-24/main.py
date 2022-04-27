# Day 24 - Reading and writing files in python
# 
# 

# Opening a file
file = open("/Users/mahmoudshabana/Documents/Udemy/100-days-of-python/Day-24/my_file.txt") # has to be the full file path for mac i think

# Read contents of file to a variable
file_contents = file.read()

# Print that variable
print(file_contents)

# Close the file to free up resources
file.close()

## Method 2 for opening a file (no need for close() using the "with" keyword)

with open("/Users/mahmoudshabana/Documents/Udemy/100-days-of-python/Day-24/my_file.txt", mode = 'w') as file_2:
    # Read contents of file to a variable
    #file_contents_2 = file_2.read()
    # Print that variable
    #print(file_contents_2)

    # To write to a file, use write() (Make sure the mode in open() is set to 'w' for write permissions)
    file_2.write("\nNew Text from Python")


# If file in file path does not exist, it will create the file when writing to it
with open("/Users/mahmoudshabana/Documents/Udemy/100-days-of-python/Day-24/new_file.txt", mode = 'w') as file_3:

    # To write to a file, use write() (Make sure the mode in open() is set to 'w' for write permissions)
    file_3.write("\nNew Text from Python")

