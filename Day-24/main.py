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