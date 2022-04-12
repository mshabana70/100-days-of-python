# Day 10 - Functions with outputs
#
# Test some functions with outputs

def format_name(f_name, l_name):
    full_name = ""
    full_name = f_name.title() + " " + l_name.title()
    return f"{full_name}"

# Call our function and see what the returned value is
print(format_name("MAHMOUD", "SHABANA")) # Output: Mahmoud Shabana
