# Day 10 - Functions with outputs
#
# Test some functions with outputs

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You have entered an empty string" # terminate function early

    full_name = ""
    full_name = f_name.title() + " " + l_name.title()
    return full_name
    #print(full_name) # This will not run (return ends function execution)

# Call our function and see what the returned value is
print(format_name("MAHMOUD", "SHABANA")) # Output: Mahmoud Shabana

# Call our function with user inputs
print(format_name(input("What is your first name?"), input("What is your last name?")))

