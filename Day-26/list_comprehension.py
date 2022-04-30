# Day 26 - List Comprehension
#


# How we normally create a new list from an old one
numbers = [1, 2, 3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)
print(new_list)

# Using list comprehension
# Key word method: new_list = [new_item for item in list]
new_list_2 = [n + 1 for n in numbers]
print(new_list_2)

# You can also use strings with list comprehension
name = "Mahmoud"
name_list = [letter for letter in name] # Append letter to name_list for each letter in 'name' string
print(name_list)
